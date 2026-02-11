#!/usr/bin/env python3
"""Validate structured trigger/non-trigger suites for CSCRF skills."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Sequence

ROOT = Path(__file__).resolve().parent.parent
SUITE_PATHS = {
    "ciso": ROOT / ".claude/skills/ciso/references/trigger-tests.yaml",
    "ciso-policy": ROOT / ".claude/skills/ciso-policy/references/trigger-tests.yaml",
    "ciso-assess": ROOT / ".claude/skills/ciso-assess/references/trigger-tests.yaml",
}

VALID_SKILLS = {"ciso", "ciso-policy", "ciso-assess", "none"}
VALID_BUCKETS = {"positive", "negative", "paraphrase", "boundary"}
MIN_BUCKET_COUNTS = {"positive": 15, "negative": 15, "paraphrase": 10}
MIN_BOUNDARY_COUNT = 6
MIN_POSITIVE_PER_SKILL = 4
REQUIRED_SKILLS = ["ciso", "ciso-policy", "ciso-assess"]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[PASS] {message}")


def load_suite(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise ValueError(f"Missing trigger suite file: {path.relative_to(ROOT)}")

    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        try:
            import yaml  # type: ignore
        except ModuleNotFoundError as exc:
            raise ValueError(
                f"{path.relative_to(ROOT)} is not JSON-compatible YAML and PyYAML is unavailable"
            ) from exc
        data = yaml.safe_load(raw)
        if not isinstance(data, dict):
            raise ValueError(f"Top-level suite structure must be a mapping in {path.relative_to(ROOT)}")
        return data


def ensure_string(value: Any, field: str, errors: List[str], case_id: str) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{case_id}: '{field}' must be a non-empty string")
        return ""
    return value.strip()


def validate_cases(cases: Sequence[Dict[str, Any]], skills: Sequence[str]) -> List[str]:
    errors: List[str] = []
    id_pattern = re.compile(r"^[a-z0-9-]+$")

    ids: set[str] = set()
    prompts: set[str] = set()
    bucket_counts: Counter[str] = Counter()
    positive_by_skill: Counter[str] = Counter()
    boundary_by_skill: Counter[str] = Counter()

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"cases[{index}] must be an object")
            continue

        case_id = ensure_string(case.get("id"), "id", errors, f"cases[{index}]")
        if case_id:
            if not id_pattern.match(case_id):
                errors.append(f"{case_id}: id must match {id_pattern.pattern}")
            if case_id in ids:
                errors.append(f"{case_id}: duplicate case id")
            ids.add(case_id)

        prompt = ensure_string(case.get("prompt"), "prompt", errors, case_id or f"cases[{index}]")
        if prompt:
            normalized = " ".join(prompt.split()).lower()
            if normalized in prompts:
                errors.append(f"{case_id}: duplicate prompt")
            prompts.add(normalized)

        bucket = ensure_string(case.get("bucket"), "bucket", errors, case_id or f"cases[{index}]")
        if bucket and bucket not in VALID_BUCKETS:
            errors.append(f"{case_id}: invalid bucket '{bucket}'")

        expected_skill = ensure_string(
            case.get("expected_skill"), "expected_skill", errors, case_id or f"cases[{index}]"
        )
        if expected_skill and expected_skill not in VALID_SKILLS:
            errors.append(f"{case_id}: invalid expected_skill '{expected_skill}'")

        if bucket:
            bucket_counts[bucket] += 1
        if bucket == "negative" and expected_skill and expected_skill != "none":
            errors.append(f"{case_id}: negative cases must set expected_skill to 'none'")
        if bucket in {"positive", "paraphrase", "boundary"} and expected_skill == "none":
            errors.append(f"{case_id}: {bucket} cases must target a concrete skill")

        if bucket == "positive" and expected_skill in skills:
            positive_by_skill[expected_skill] += 1
        if bucket == "boundary" and expected_skill in skills:
            boundary_by_skill[expected_skill] += 1

    for bucket, minimum in MIN_BUCKET_COUNTS.items():
        count = bucket_counts.get(bucket, 0)
        if count < minimum:
            errors.append(f"bucket '{bucket}' has {count} cases; expected at least {minimum}")

    boundary_count = bucket_counts.get("boundary", 0)
    if boundary_count < MIN_BOUNDARY_COUNT:
        errors.append(
            f"bucket 'boundary' has {boundary_count} cases; expected at least {MIN_BOUNDARY_COUNT}"
        )

    for skill in skills:
        positive_count = positive_by_skill.get(skill, 0)
        if positive_count < MIN_POSITIVE_PER_SKILL:
            errors.append(
                f"skill '{skill}' has {positive_count} positive cases; expected at least "
                f"{MIN_POSITIVE_PER_SKILL}"
            )
        if boundary_by_skill.get(skill, 0) == 0:
            errors.append(f"skill '{skill}' must appear in at least one boundary case")

    return errors


def validate_suite_shape(name: str, suite: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    skills = suite.get("skills")
    cases = suite.get("cases")

    if not isinstance(skills, list) or not all(isinstance(item, str) for item in skills):
        errors.append(f"{name}: skills must be a list of skill names")
        return errors
    if set(skills) != set(REQUIRED_SKILLS):
        errors.append(f"{name}: skills must contain exactly: {', '.join(REQUIRED_SKILLS)}")

    if not isinstance(cases, list):
        errors.append(f"{name}: cases must be a list")
        return errors

    errors.extend(f"{name}: {error}" for error in validate_cases(cases, skills))
    return errors


def normalized_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def main() -> int:
    errors: List[str] = []
    suites: Dict[str, Dict[str, Any]] = {}

    for name, path in SUITE_PATHS.items():
        try:
            suite = load_suite(path)
        except ValueError as exc:
            fail(str(exc))
            return 1

        suites[name] = suite
        errors.extend(validate_suite_shape(name, suite))

    canonical_name = "ciso"
    canonical = suites[canonical_name]
    canonical_blob = normalized_json(canonical)

    for name, suite in suites.items():
        if name == canonical_name:
            continue
        if normalized_json(suite) != canonical_blob:
            errors.append(
                f"{name}: trigger suite differs from canonical {SUITE_PATHS[canonical_name].relative_to(ROOT)}"
            )

    if errors:
        for error in errors:
            fail(error)
        return 1

    counts = Counter(
        case.get("bucket")
        for case in canonical.get("cases", [])
        if isinstance(case, dict) and "bucket" in case
    )

    for name, path in SUITE_PATHS.items():
        ok(f"Loaded {path.relative_to(ROOT)}")
        ok(f"Validated semantic trigger suite for {name}")

    ok(
        "Validated canonical trigger suite counts: "
        f"positive={counts.get('positive', 0)}, "
        f"negative={counts.get('negative', 0)}, "
        f"paraphrase={counts.get('paraphrase', 0)}, "
        f"boundary={counts.get('boundary', 0)}"
    )
    ok(f"Validated {len(canonical.get('cases', []))} semantic trigger cases with mirror parity")
    return 0


if __name__ == "__main__":
    sys.exit(main())
