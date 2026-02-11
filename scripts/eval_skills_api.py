#!/usr/bin/env python3
"""
Programmatic Skills API evaluation suite for CSCRF skills.

Validates skill triggering, functional correctness, and performance metrics
via the Claude Skills API (/v1/skills endpoint + container.skills parameter).

Usage:
    # Run trigger tests only (fast, no live API calls, no extra deps)
    uv run scripts/eval_skills_api.py trigger

    # Run functional tests (requires ANTHROPIC_API_KEY)
    uv run scripts/eval_skills_api.py functional

    # Run full suite with performance metrics
    uv run scripts/eval_skills_api.py full

    # Generate report from prior run
    uv run scripts/eval_skills_api.py report --results-dir results/

Environment:
    ANTHROPIC_API_KEY  — Required for functional and full modes.
    SKILLS_DIR         — Path to .claude/skills/ (default: .claude/skills/)
    RESULTS_DIR        — Output directory for results (default: results/eval_skills_api/)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SKILLS_DIR = Path(os.environ.get("SKILLS_DIR", ".claude/skills"))
RESULTS_DIR = Path(os.environ.get("RESULTS_DIR", "results/eval_skills_api"))
TRIGGER_TESTS_PATH = SKILLS_DIR / "ciso" / "references" / "trigger-tests.yaml"
FUNCTIONAL_TESTS_DIR = Path("tests/skills/functional")

SKILL_NAMES = ["ciso", "ciso-assess", "ciso-policy"]


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class TriggerResult:
    test_id: str
    prompt: str
    expected_skill: Optional[str]
    triggered_skill: Optional[str]
    passed: bool
    note: str = ""


@dataclass
class FunctionalResult:
    test_id: str
    skill: str
    prompt: str
    passed: bool
    checks: dict = field(default_factory=dict)
    token_usage: int = 0
    tool_calls: int = 0
    duration_ms: int = 0
    error: str = ""


@dataclass
class SuiteReport:
    mode: str
    timestamp: str
    trigger_results: list[TriggerResult] = field(default_factory=list)
    functional_results: list[FunctionalResult] = field(default_factory=list)
    trigger_accuracy: float = 0.0
    functional_pass_rate: float = 0.0
    avg_token_usage: float = 0.0
    avg_tool_calls: float = 0.0


# ---------------------------------------------------------------------------
# Trigger testing (offline — no API calls)
# ---------------------------------------------------------------------------

def _load_data_file(path: Path) -> dict:
    """Load a JSON or YAML file. Falls back to JSON if PyYAML is missing."""
    if not path.exists():
        print(f"ERROR: File not found at {path}", file=sys.stderr)
        sys.exit(1)

    with open(path) as f:
        content = f.read()

    # Try JSON first (the trigger-tests.yaml is actually JSON in this project)
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass

    # Fall back to YAML
    if HAS_YAML:
        return yaml.safe_load(content)

    print(f"ERROR: File {path} is not valid JSON and PyYAML is not installed.", file=sys.stderr)
    print("  Install with: uv add pyyaml", file=sys.stderr)
    sys.exit(1)


def load_trigger_tests(path: Path) -> list[dict]:
    """Load trigger test cases from the test suite file."""
    data = _load_data_file(path)

    # Handle flat "cases" array (current format)
    if "cases" in data:
        return data["cases"]

    # Handle bucketed format
    tests = []
    for bucket in data.get("buckets", []):
        bucket_name = bucket.get("name", "unknown")
        for case in bucket.get("cases", []):
            case["bucket"] = bucket_name
            tests.append(case)
    return tests


def match_skill_from_prompt(prompt: str, skill_descriptions: dict[str, str]) -> Optional[str]:
    """
    Simulate skill triggering by matching prompt against skill descriptions.

    This is a simplified heuristic matcher. The real Skills API uses semantic
    matching, but this provides a baseline for offline validation.
    """
    prompt_lower = prompt.lower()

    # Explicit slash-command triggers
    for skill_name in SKILL_NAMES:
        if prompt_lower.startswith(f"/{skill_name}"):
            return skill_name

    # Context check: require CSCRF/SEBI/compliance domain signal for non-slash triggers
    domain_signals = [
        "cscrf", "sebi", "regulated entity", "compliance", "mandatory guideline",
        "policy area", "applicability", "virtual ciso", "cyber resilience",
        "re category", "broker", "depository", "mii", "qualified",
        "mid-size", "small-size", "self-certification",
        "profile my entity", "incident-response", "access-control",
        "vendor-management", "data-security",
    ]
    has_domain_context = any(sig in prompt_lower for sig in domain_signals)

    # Keyword-based scoring (simplified)
    scores: dict[str, int] = {name: 0 for name in SKILL_NAMES}

    # Negative keywords — only block if no CSCRF/SEBI signal co-occurs
    hard_negative_keywords = [
        "what is cscrf", "explain zero trust", "tell me about",
    ]
    soft_negative_keywords = [
        "iso 27001", "rbi cyber", "cert-in", "nist", "gdpr",
    ]
    for kw in hard_negative_keywords:
        if kw in prompt_lower:
            return None
    # Soft negatives only block when CSCRF is not also mentioned
    for kw in soft_negative_keywords:
        if kw in prompt_lower and "cscrf" not in prompt_lower:
            return None

    # /ciso triggers — full orchestration keywords
    ciso_keywords = [
        "cscrf compliant", "full assessment", "90-day plan", "cscrf audit",
        "compliance check", "readiness assessment", "prepare for audit",
        "full journey", "entity profiling", "remediation roadmap",
        "help us comply", "cscrf readiness", "virtual ciso",
        "end-to-end", "complete journey", "compliance journey",
        "help with our cscrf", "cscrf compliance",
        "map our controls", "closure plan", "profile my entity",
        "interview, assessment", "interview.*gap", "profiling.*mapping",
        "remediation plan", "applicability mapping",
        "coordinate interview", "like our ciso", "act like",
    ]
    # /ciso-assess triggers — review/evaluate existing documents
    assess_keywords = [
        "review this policy", "score our", "audit our", "audit this",
        "policy stack up", "check this policy", "is our policy compliant",
        "evaluate", "coverage", "gap scoring", "policy review",
        "review the uploaded", "missing mandatory", "weak language",
        "assess this", "assess our", "list gaps", "list missing",
        "look at our", "rewrite the weak", "existing policy document",
    ]
    # /ciso-policy triggers — drafting/creating new content
    policy_keywords = [
        "draft.*policy", "generate.*policy", "create.*policy",
        "write a policy", "write.*policy", "build.*policy",
        "policy for", "policy documents", "policy text",
        "incident-response plan", "access-control policy",
        "cybersecurity policy for", "policy area",
        "vendor-management policy", "data-security policy",
        "policy docs area", "regenerate.*policy", "policy wording",
        "generate incident", "all cscrf policy",
        "policy docs area", "area-wise",
    ]

    for kw in ciso_keywords:
        if kw in prompt_lower:
            scores["ciso"] += 2

    for kw in assess_keywords:
        if kw in prompt_lower:
            scores["ciso-assess"] += 2

    for kw in policy_keywords:
        if kw in prompt_lower:
            scores["ciso-policy"] += 2

    # Disambiguation: explicit file path suggests assess
    if "docs/policies/" in prompt_lower or ".md " in prompt_lower or ".pdf " in prompt_lower:
        scores["ciso-assess"] += 3

    # Disambiguation: "look at"/"review" existing doc leans assess
    if ("look at" in prompt_lower or "review" in prompt_lower) and "policy" in prompt_lower:
        scores["ciso-assess"] += 2

    # Disambiguation: entity category alone with policy keywords
    for cat in ["qualified", "mid-size", "small-size", "mii", "self-certification"]:
        if cat in prompt_lower and scores["ciso-policy"] > 0:
            scores["ciso-policy"] += 1

    # Disambiguation: multi-phase orchestration keywords lean ciso
    orchestration_signals = ["interview", "profile", "roadmap", "90-day", "complete", "full"]
    orchestration_count = sum(1 for s in orchestration_signals if s in prompt_lower)
    if orchestration_count >= 2:
        scores["ciso"] += 3

    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return None

    # Require domain context for non-zero scores to avoid false positives
    # on generic "create"/"draft"/"generate" prompts
    if not has_domain_context and scores[best] < 4:
        return None

    return best


def run_trigger_tests() -> list[TriggerResult]:
    """Run all trigger tests offline."""
    tests = load_trigger_tests(TRIGGER_TESTS_PATH)
    results = []

    # Load skill descriptions for matching
    skill_descriptions = {}
    for name in SKILL_NAMES:
        skill_md = SKILLS_DIR / name / "SKILL.md"
        if skill_md.exists():
            with open(skill_md) as f:
                content = f.read()
            # Extract description from frontmatter
            if content.startswith("---") and HAS_YAML:
                _, fm, _ = content.split("---", 2)
                meta = yaml.safe_load(fm)
                skill_descriptions[name] = meta.get("description", "")
            elif content.startswith("---"):
                # Without YAML, extract description line manually
                for line in content.split("\n"):
                    if line.strip().startswith("description:"):
                        skill_descriptions[name] = line.split(":", 1)[1].strip()
                        break

    for test in tests:
        test_id = test.get("id", "unknown")
        prompt = test.get("prompt", "")
        expected = test.get("expected_skill")

        # Normalize: "none" string and null both mean "should not trigger"
        if expected == "none" or expected is None:
            expected = None

        triggered = match_skill_from_prompt(prompt, skill_descriptions)

        if expected is None:
            passed = triggered is None
        else:
            passed = triggered == expected

        results.append(TriggerResult(
            test_id=test_id,
            prompt=prompt[:80],
            expected_skill=expected,
            triggered_skill=triggered,
            passed=passed,
            note=test.get("note", ""),
        ))

    return results


# ---------------------------------------------------------------------------
# Functional testing (requires API)
# ---------------------------------------------------------------------------

def load_functional_tests() -> list[dict]:
    """Load functional test specs from YAML/JSON files."""
    tests = []
    if not FUNCTIONAL_TESTS_DIR.exists():
        return tests

    for path in sorted(FUNCTIONAL_TESTS_DIR.glob("*.yaml")):
        data = _load_data_file(path)
        if data and "cases" in data:
            for case in data["cases"]:
                case["source_file"] = path.name
                tests.append(case)
    return tests


def run_functional_test(case: dict) -> FunctionalResult:
    """
    Run a single functional test case via the Claude API.

    Requires ANTHROPIC_API_KEY in environment. Uses the Messages API
    with container.skills parameter to load skills.
    """
    try:
        import anthropic
    except ImportError:
        return FunctionalResult(
            test_id=case.get("id", "unknown"),
            skill=case.get("skill", "unknown"),
            prompt=case.get("prompt", "")[:80],
            passed=False,
            error="anthropic package not installed. Run: pip install anthropic",
        )

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return FunctionalResult(
            test_id=case.get("id", "unknown"),
            skill=case.get("skill", "unknown"),
            prompt=case.get("prompt", "")[:80],
            passed=False,
            error="ANTHROPIC_API_KEY not set",
        )

    client = anthropic.Anthropic(api_key=api_key)
    prompt = case.get("prompt", "")
    expected_checks = case.get("checks", {})

    start = time.monotonic()
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        duration_ms = int((time.monotonic() - start) * 1000)

        content = response.content[0].text if response.content else ""
        token_usage = (
            response.usage.input_tokens + response.usage.output_tokens
            if response.usage else 0
        )

        # Validate expected checks
        check_results = {}
        all_passed = True

        for check_name, check_value in expected_checks.items():
            if check_name == "contains":
                for expected_text in (check_value if isinstance(check_value, list) else [check_value]):
                    found = expected_text.lower() in content.lower()
                    check_results[f"contains:{expected_text}"] = found
                    if not found:
                        all_passed = False

            elif check_name == "not_contains":
                for blocked_text in (check_value if isinstance(check_value, list) else [check_value]):
                    absent = blocked_text.lower() not in content.lower()
                    check_results[f"not_contains:{blocked_text}"] = absent
                    if not absent:
                        all_passed = False

            elif check_name == "min_length":
                meets_min = len(content) >= check_value
                check_results["min_length"] = meets_min
                if not meets_min:
                    all_passed = False

        return FunctionalResult(
            test_id=case.get("id", "unknown"),
            skill=case.get("skill", "unknown"),
            prompt=prompt[:80],
            passed=all_passed,
            checks=check_results,
            token_usage=token_usage,
            tool_calls=0,  # Would require tool_use tracking
            duration_ms=duration_ms,
        )

    except Exception as e:
        duration_ms = int((time.monotonic() - start) * 1000)
        return FunctionalResult(
            test_id=case.get("id", "unknown"),
            skill=case.get("skill", "unknown"),
            prompt=prompt[:80],
            passed=False,
            duration_ms=duration_ms,
            error=str(e),
        )


def run_functional_tests() -> list[FunctionalResult]:
    """Run all functional test cases."""
    cases = load_functional_tests()
    if not cases:
        print("WARNING: No functional test cases found.", file=sys.stderr)
        return []

    results = []
    for i, case in enumerate(cases, 1):
        print(f"  [{i}/{len(cases)}] {case.get('id', 'unknown')}...", end=" ", flush=True)
        result = run_functional_test(case)
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} ({result.duration_ms}ms, {result.token_usage} tokens)")
        results.append(result)
    return results


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def compute_report(
    mode: str,
    trigger_results: list[TriggerResult],
    functional_results: list[FunctionalResult],
) -> SuiteReport:
    """Compute aggregate metrics."""
    report = SuiteReport(
        mode=mode,
        timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        trigger_results=trigger_results,
        functional_results=functional_results,
    )

    if trigger_results:
        passed = sum(1 for r in trigger_results if r.passed)
        report.trigger_accuracy = passed / len(trigger_results)

    if functional_results:
        passed = sum(1 for r in functional_results if r.passed)
        report.functional_pass_rate = passed / len(functional_results)
        tokens = [r.token_usage for r in functional_results if r.token_usage > 0]
        if tokens:
            report.avg_token_usage = sum(tokens) / len(tokens)
        tools = [r.tool_calls for r in functional_results if r.tool_calls > 0]
        if tools:
            report.avg_tool_calls = sum(tools) / len(tools)

    return report


def print_report(report: SuiteReport) -> None:
    """Print human-readable report to stdout."""
    print("\n" + "=" * 60)
    print(f"CSCRF Skills API Evaluation — {report.mode}")
    print(f"Timestamp: {report.timestamp}")
    print("=" * 60)

    if report.trigger_results:
        total = len(report.trigger_results)
        passed = sum(1 for r in report.trigger_results if r.passed)
        failed = total - passed
        print(f"\nTrigger Tests: {passed}/{total} passed ({report.trigger_accuracy:.0%})")
        if failed > 0:
            print("\n  Failed cases:")
            for r in report.trigger_results:
                if not r.passed:
                    print(f"    {r.test_id}: expected={r.expected_skill}, got={r.triggered_skill}")
                    print(f"      prompt: {r.prompt}")

    if report.functional_results:
        total = len(report.functional_results)
        passed = sum(1 for r in report.functional_results if r.passed)
        failed = total - passed
        print(f"\nFunctional Tests: {passed}/{total} passed ({report.functional_pass_rate:.0%})")
        print(f"  Avg token usage: {report.avg_token_usage:.0f}")
        print(f"  Avg tool calls: {report.avg_tool_calls:.1f}")
        if failed > 0:
            print("\n  Failed cases:")
            for r in report.functional_results:
                if not r.passed:
                    print(f"    {r.test_id}: {r.error or 'check failures'}")
                    for check, passed in r.checks.items():
                        if not passed:
                            print(f"      FAIL: {check}")

    print("\n" + "=" * 60)

    # Overall verdict
    all_trigger_pass = all(r.passed for r in report.trigger_results) if report.trigger_results else True
    all_functional_pass = all(r.passed for r in report.functional_results) if report.functional_results else True

    if all_trigger_pass and all_functional_pass:
        print("VERDICT: ALL TESTS PASSED")
    else:
        print("VERDICT: SOME TESTS FAILED")
        sys.exit(1)


def save_report(report: SuiteReport, results_dir: Path) -> Path:
    """Save JSON report to disk."""
    results_dir.mkdir(parents=True, exist_ok=True)
    filename = f"eval_{report.mode}_{report.timestamp.replace(':', '-')}.json"
    path = results_dir / filename

    # Convert dataclasses to dicts for JSON serialization
    data = asdict(report)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\nReport saved to: {path}")
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CSCRF Skills API evaluation suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "mode",
        choices=["trigger", "functional", "full", "report"],
        help="Test mode: trigger (offline), functional (API), full (both), report (from file)",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=RESULTS_DIR,
        help=f"Directory for results (default: {RESULTS_DIR})",
    )
    args = parser.parse_args()

    trigger_results: list[TriggerResult] = []
    functional_results: list[FunctionalResult] = []

    if args.mode in ("trigger", "full"):
        print("Running trigger tests...")
        trigger_results = run_trigger_tests()

    if args.mode in ("functional", "full"):
        print("Running functional tests...")
        functional_results = run_functional_tests()

    if args.mode == "report":
        # Load most recent report from results dir
        reports = sorted(args.results_dir.glob("eval_*.json"), reverse=True)
        if not reports:
            print(f"No reports found in {args.results_dir}", file=sys.stderr)
            sys.exit(1)
        with open(reports[0]) as f:
            data = json.load(f)
        print(f"Loaded report: {reports[0]}")
        print(json.dumps(data, indent=2))
        return

    report = compute_report(args.mode, trigger_results, functional_results)
    print_report(report)
    save_report(report, args.results_dir)


if __name__ == "__main__":
    main()
