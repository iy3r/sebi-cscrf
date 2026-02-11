#!/usr/bin/env python3
"""Validate CSCRF skill output contracts and generated artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / ".claude/skills/ciso/references/policy-area-map.json"

WORK_ARTIFACTS = [
    "docs/.ciso-work/entity-profile.md",
    "docs/.ciso-work/entity-profile.json",
    "docs/.ciso-work/entity-tags.json",
    "docs/.ciso-work/gap-analysis.md",
    "docs/.ciso-work/gap-analysis.json",
    "docs/.ciso-work/policy-plan.md",
    "docs/.ciso-work/review-findings.md",
    "docs/.ciso-work/roadmap.md",
]

REQUIRED_POLICY_KEYS = [
    "title",
    "entity",
    "category",
    "cscrf_version",
    "cscrf_standards",
    "cscrf_guidelines",
    "generated_date",
    "review_cycle",
]

VALID_CATEGORIES = {"mii", "qualified", "mid-size", "small-size", "self-certification"}
VALID_GAP_STATUSES = {"COMPLIANT", "GAP", "NEEDS_REVIEW"}
VALID_PRIORITIES = {"P1", "P2", "P3"}

STANDARD_ID_RE = re.compile(r"^[A-Z]{2}\.[A-Z]{2}\.S\d+$")
GUIDELINE_ID_RE = re.compile(r"^[A-Z]{2}\.[A-Z]{2}\.G\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[PASS] {message}")


def warn(message: str) -> None:
    print(f"[WARN] {message}")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> List[str]:
    content = value.strip()[1:-1].strip()
    if not content:
        return []
    return [strip_quotes(item.strip()) for item in content.split(",") if item.strip()]


def parse_frontmatter(markdown_text: str) -> Dict[str, Any] | None:
    match = re.match(r"^---\n(.*?)\n---\n?", markdown_text, re.DOTALL)
    if not match:
        return None

    block = match.group(1)
    lines = block.splitlines()
    data: Dict[str, Any] = {}
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            index += 1
            continue

        key, raw_value = key_match.groups()
        raw_value = raw_value.strip()

        if raw_value.startswith("[") and raw_value.endswith("]"):
            data[key] = parse_inline_list(raw_value)
            index += 1
            continue

        if raw_value == "":
            items: List[str] = []
            cursor = index + 1
            while cursor < len(lines):
                list_match = re.match(r"^\s*-\s*(.+)$", lines[cursor])
                if list_match:
                    items.append(strip_quotes(list_match.group(1).strip()))
                    cursor += 1
                    continue
                if not lines[cursor].strip():
                    cursor += 1
                    continue
                if re.match(r"^[A-Za-z0-9_-]+:\s*", lines[cursor]):
                    break
                break

            data[key] = items if items else ""
            index = cursor
            continue

        data[key] = strip_quotes(raw_value)
        index += 1

    return data


def extract_ids(text: str) -> Tuple[Set[str], Set[str]]:
    standards = set(re.findall(r"\b[A-Z]{2}\.[A-Z]{2}\.S\d+\b", text))
    guidelines = set(re.findall(r"\b[A-Z]{2}\.[A-Z]{2}\.G\d+\b", text))
    return standards, guidelines


def collect_global_framework_ids() -> Tuple[Set[str], Set[str]]:
    standards: Set[str] = set()
    guidelines: Set[str] = set()

    for path in sorted((ROOT / "framework").rglob("*.md")):
        std, gid = extract_ids(path.read_text(encoding="utf-8"))
        standards.update(std)
        guidelines.update(gid)

    return standards, guidelines


def load_area_allowed_ids() -> Dict[str, Tuple[Set[str], Set[str]]]:
    data = load_json(MAP_PATH)
    areas = data.get("areas")
    if not isinstance(areas, list):
        raise ValueError("policy-area-map.json must define an areas list")

    area_ids: Dict[str, Tuple[Set[str], Set[str]]] = {}
    for area in areas:
        slug = area.get("slug")
        files = area.get("framework_files")
        if not isinstance(slug, str) or not isinstance(files, list):
            continue

        standards: Set[str] = set()
        guidelines: Set[str] = set()
        for rel_path in files:
            if not isinstance(rel_path, str):
                continue
            path = ROOT / rel_path
            if not path.exists():
                continue
            std, gid = extract_ids(path.read_text(encoding="utf-8"))
            standards.update(std)
            guidelines.update(gid)

        area_ids[slug] = (standards, guidelines)

    return area_ids


def validate_entity_profile_json(path: Path, errors: List[str]) -> None:
    data = load_json(path)
    if not isinstance(data, dict):
        errors.append("entity-profile.json must be a JSON object")
        return
    for key in ("entity_type", "category"):
        if key not in data:
            errors.append(f"entity-profile.json missing key: {key}")


def validate_entity_tags_json(path: Path, errors: List[str]) -> None:
    data = load_json(path)
    if not isinstance(data, dict):
        errors.append("entity-tags.json must be a JSON object")
        return
    tags = data.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append("entity-tags.json must include non-empty tags list")
    category = data.get("category")
    if isinstance(category, str) and category not in VALID_CATEGORIES:
        errors.append(f"entity-tags.json has invalid category: {category}")


def validate_gap_analysis_json(path: Path, known_guidelines: Set[str], errors: List[str]) -> None:
    data = load_json(path)
    rows: Any = data
    if isinstance(data, dict):
        rows = data.get("items")
    if not isinstance(rows, list):
        errors.append("gap-analysis.json must be a list or object with 'items' list")
        return

    required = {
        "guideline_id",
        "function",
        "mandatory",
        "status",
        "reason",
        "owner_hint",
        "priority",
    }
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            errors.append(f"gap-analysis.json item {index} must be an object")
            continue
        missing = [field for field in required if field not in row]
        if missing:
            errors.append(f"gap-analysis.json item {index} missing fields: {', '.join(missing)}")
            continue

        guideline_id = row["guideline_id"]
        if not isinstance(guideline_id, str) or not GUIDELINE_ID_RE.match(guideline_id):
            errors.append(f"gap-analysis.json item {index} has invalid guideline_id: {guideline_id!r}")
        elif guideline_id not in known_guidelines:
            errors.append(f"gap-analysis.json item {index} references unknown guideline_id: {guideline_id}")

        status = row["status"]
        if not isinstance(status, str) or status not in VALID_GAP_STATUSES:
            errors.append(f"gap-analysis.json item {index} has invalid status: {status!r}")

        priority = row["priority"]
        if not isinstance(priority, str) or priority not in VALID_PRIORITIES:
            errors.append(f"gap-analysis.json item {index} has invalid priority: {priority!r}")


def validate_review_findings(path: Path, errors: List[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"\b(PASS|FAIL)\b", text):
        errors.append("review-findings.md must include PASS or FAIL verdict")

    lowered = text.lower()
    for token in ("location", "issue", "fix"):
        if token not in lowered:
            errors.append(f"review-findings.md missing '{token}' field in findings")


def validate_policy_file(
    path: Path,
    all_standards: Set[str],
    all_guidelines: Set[str],
    area_ids: Dict[str, Tuple[Set[str], Set[str]]],
    errors: List[str],
) -> None:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{path.relative_to(ROOT)} missing YAML frontmatter")
        return

    for key in REQUIRED_POLICY_KEYS:
        if key not in fm:
            errors.append(f"{path.relative_to(ROOT)} missing frontmatter key: {key}")

    category = fm.get("category")
    if isinstance(category, str) and category not in VALID_CATEGORIES:
        errors.append(f"{path.relative_to(ROOT)} has invalid category: {category}")

    generated_date = fm.get("generated_date")
    if isinstance(generated_date, str) and not DATE_RE.match(generated_date):
        errors.append(f"{path.relative_to(ROOT)} has invalid generated_date: {generated_date}")

    for list_key, pattern, known_ids in (
        ("cscrf_standards", STANDARD_ID_RE, all_standards),
        ("cscrf_guidelines", GUIDELINE_ID_RE, all_guidelines),
    ):
        values = fm.get(list_key)
        if not isinstance(values, list) or not values:
            errors.append(f"{path.relative_to(ROOT)} key '{list_key}' must be a non-empty list")
            continue
        for value in values:
            if not isinstance(value, str) or not pattern.match(value):
                errors.append(f"{path.relative_to(ROOT)} invalid ID in {list_key}: {value!r}")
                continue
            if value not in known_ids:
                errors.append(f"{path.relative_to(ROOT)} unknown ID in {list_key}: {value}")

    area = path.stem
    if area in area_ids:
        allowed_standards, allowed_guidelines = area_ids[area]
        standards = fm.get("cscrf_standards")
        guidelines = fm.get("cscrf_guidelines")
        if isinstance(standards, list):
            for standard in standards:
                if isinstance(standard, str) and standard not in allowed_standards:
                    errors.append(
                        f"{path.relative_to(ROOT)} references standard outside mapped area '{area}': {standard}"
                    )
        if isinstance(guidelines, list):
            for guideline in guidelines:
                if isinstance(guideline, str) and guideline not in allowed_guidelines:
                    errors.append(
                        f"{path.relative_to(ROOT)} references guideline outside mapped area '{area}': {guideline}"
                    )


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require all workflow artifacts from docs/.ciso-work to exist.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)

    errors: List[str] = []

    try:
        all_standards, all_guidelines = collect_global_framework_ids()
        area_ids = load_area_allowed_ids()
    except (ValueError, json.JSONDecodeError) as exc:
        fail(str(exc))
        return 1

    for rel_path in WORK_ARTIFACTS:
        path = ROOT / rel_path
        if not path.exists():
            if args.strict:
                errors.append(f"missing required artifact: {rel_path}")
            else:
                warn(f"artifact not present (skipped in non-strict mode): {rel_path}")
            continue

        if rel_path.endswith("entity-profile.json"):
            validate_entity_profile_json(path, errors)
        if rel_path.endswith("entity-tags.json"):
            validate_entity_tags_json(path, errors)
        if rel_path.endswith("gap-analysis.json"):
            validate_gap_analysis_json(path, all_guidelines, errors)
        if rel_path.endswith("review-findings.md"):
            validate_review_findings(path, errors)

    policy_dir = ROOT / "docs/policies"
    policy_files: List[Path] = []
    if policy_dir.exists():
        policy_files = sorted(
            path for path in policy_dir.glob("*.md") if path.name.lower() != "readme.md"
        )
    if not policy_files:
        warn("no policy files found in docs/policies; skipping policy contract checks")
    for path in policy_files:
        validate_policy_file(path, all_standards, all_guidelines, area_ids, errors)

    if errors:
        for error in errors:
            fail(error)
        return 1

    ok("Validated CISO output contracts")
    ok(f"Framework ID inventory: standards={len(all_standards)}, guidelines={len(all_guidelines)}")
    if policy_files:
        ok(f"Validated {len(policy_files)} policy file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
