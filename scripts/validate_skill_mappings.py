#!/usr/bin/env python3
"""Validate canonical policy mapping and skill references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Sequence, Set

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / ".claude/skills/ciso/references/policy-area-map.json"
POLICY_SKILL_MAP_PATH = ROOT / ".claude/skills/ciso-policy/references/policy-area-map.json"
ASSESS_SKILL_MAP_PATH = ROOT / ".claude/skills/ciso-assess/references/policy-area-map.json"

REFERENCE_FILES = [
    ROOT / ".claude/skills/ciso/SKILL.md",
    ROOT / ".claude/skills/ciso-policy/SKILL.md",
    ROOT / ".claude/skills/ciso-assess/SKILL.md",
    ROOT / ".claude/skills/ciso/references/load-matrix.md",
    ROOT / ".claude/skills/ciso/references/smoke-tests.md",
    ROOT / ".claude/skills/ciso/references/trigger-tests.yaml",
    ROOT / ".claude/skills/ciso/references/policy-templates.md",
    ROOT / ".claude/skills/ciso/references/interview-flow.md",
    ROOT / ".claude/skills/ciso/scripts/resolve_entity_tags.py",
    ROOT / ".claude/skills/ciso-policy/references/load-matrix.md",
    ROOT / ".claude/skills/ciso-policy/references/smoke-tests.md",
    ROOT / ".claude/skills/ciso-policy/references/trigger-tests.yaml",
    ROOT / ".claude/skills/ciso-policy/references/policy-templates.md",
    ROOT / ".claude/skills/ciso-policy/references/agents/policy-drafter.md",
    ROOT / ".claude/skills/ciso-policy/references/agents/reviewer.md",
    ROOT / ".claude/skills/ciso-assess/references/load-matrix.md",
    ROOT / ".claude/skills/ciso-assess/references/smoke-tests.md",
    ROOT / ".claude/skills/ciso-assess/references/trigger-tests.yaml",
    ROOT / ".claude/skills/ciso-assess/references/assessment-template.md",
    ROOT / ".claude/skills/ciso-assess/references/agents/analyst.md",
    ROOT / ".claude/skills/ciso-assess/references/agents/reviewer.md",
]

PORTABILITY_RULES = [
    (
        ROOT / ".claude/skills/ciso-policy/SKILL.md",
        ".claude/skills/ciso-policy/references/",
    ),
    (
        ROOT / ".claude/skills/ciso-policy/references/load-matrix.md",
        ".claude/skills/ciso-policy/references/",
    ),
    (
        ROOT / ".claude/skills/ciso-policy/references/policy-templates.md",
        ".claude/skills/ciso-policy/references/",
    ),
    (
        ROOT / ".claude/skills/ciso-policy/references/smoke-tests.md",
        ".claude/skills/ciso-policy/references/",
    ),
    (
        ROOT / ".claude/skills/ciso-assess/SKILL.md",
        ".claude/skills/ciso-assess/references/",
    ),
    (
        ROOT / ".claude/skills/ciso-assess/references/load-matrix.md",
        ".claude/skills/ciso-assess/references/",
    ),
    (
        ROOT / ".claude/skills/ciso-assess/references/smoke-tests.md",
        ".claude/skills/ciso-assess/references/",
    ),
]

SKILL_FILES = [
    ROOT / ".claude/skills/ciso/SKILL.md",
    ROOT / ".claude/skills/ciso-policy/SKILL.md",
    ROOT / ".claude/skills/ciso-assess/SKILL.md",
]

REQUIRED_METADATA_FIELDS = {"version", "cscrf_version", "test_suite_version", "author"}
EXPECTED_ALLOWED_TOOLS = {
    "ciso": {"Read", "Grep", "Glob", "Write", "AskUserQuestion", "Task"},
    "ciso-policy": {"Read", "Grep", "Glob", "Write", "Edit", "AskUserQuestion", "Task"},
    "ciso-assess": {"Read", "Grep", "Glob", "Write", "AskUserQuestion", "Task"},
}

MIRROR_EXACT_FILES = (
    "policy-area-map.json",
    "trigger-tests.yaml",
)

MIRROR_PATH_AWARE_FILES = (
    "smoke-tests.md",
    "load-matrix.md",
)


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[PASS] {message}")


def load_map() -> Dict[str, object]:
    if not MAP_PATH.exists():
        raise ValueError(f"Missing map file: {MAP_PATH}")
    try:
        data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {MAP_PATH}: {exc}") from exc
    return data


def load_json(path: Path) -> Dict[str, object]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def parse_frontmatter(text: str) -> Dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not match:
        return {}
    data: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line.strip())
        if not m:
            continue
        key, value = m.groups()
        data[key] = value.strip()
    return data


def expected_mirror_text(name: str, mirror_skill: str) -> str:
    canonical = (
        ROOT / f".claude/skills/ciso/references/{name}"
    ).read_text(encoding="utf-8")
    if name in MIRROR_PATH_AWARE_FILES:
        return canonical.replace(
            ".claude/skills/ciso/references/",
            f".claude/skills/{mirror_skill}/references/",
        )
    return canonical


def validate_area_records(areas: Sequence[Dict[str, object]]) -> List[str]:
    errors: List[str] = []
    seen_slugs: Set[str] = set()

    for index, area in enumerate(areas, start=1):
        slug = area.get("slug")
        if not isinstance(slug, str) or not slug:
            errors.append(f"areas[{index}] missing string slug")
            continue
        if slug in seen_slugs:
            errors.append(f"Duplicate slug: {slug}")
        seen_slugs.add(slug)

        title = area.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{slug}: missing title")

        primary = area.get("primary_cscrf")
        if not isinstance(primary, list) or not primary:
            errors.append(f"{slug}: primary_cscrf must be a non-empty list")

        files = area.get("framework_files")
        if not isinstance(files, list) or not files:
            errors.append(f"{slug}: framework_files must be a non-empty list")
            continue

        for rel in files:
            if not isinstance(rel, str) or not rel:
                errors.append(f"{slug}: invalid framework file entry: {rel!r}")
                continue
            path = ROOT / rel
            if not path.exists():
                errors.append(f"{slug}: framework file missing: {rel}")

    expected_slugs = {
        "cybersecurity-policy",
        "risk-management",
        "roles-responsibilities",
        "access-control",
        "data-security",
        "information-protection",
        "maintenance",
        "training",
        "vendor-management",
        "security-monitoring",
        "detection-process",
        "incident-response",
        "recovery-planning",
        "resilience-evolution",
        "asset-management",
    }
    missing = sorted(expected_slugs - seen_slugs)
    extra = sorted(seen_slugs - expected_slugs)
    if missing:
        errors.append("Missing slugs: " + ", ".join(missing))
    if extra:
        errors.append("Unexpected slugs: " + ", ".join(extra))

    return errors


def validate_references(files: Sequence[Path]) -> List[str]:
    errors: List[str] = []
    table_row_pattern = re.compile(r"^\|\s*`[a-z0-9-]+`\s*\|", re.MULTILINE)

    for path in files:
        if not path.exists():
            errors.append(f"Missing required reference file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")

        if path.name == "SKILL.md" and path.parent.name == "ciso-policy":
            if "policy-area-map.json" not in text:
                errors.append(f"{path.relative_to(ROOT)} does not reference policy-area-map.json")
            if table_row_pattern.search(text):
                errors.append(
                    f"{path.relative_to(ROOT)} still contains inline policy-area table rows; use canonical map"
                )

        if path.name == "SKILL.md" and path.parent.name == "ciso-assess":
            if "policy-area-map.json" not in text:
                errors.append(f"{path.relative_to(ROOT)} does not reference policy-area-map.json")

        if path.name == "load-matrix.md":
            if "policy-area-map.json" not in text:
                errors.append(f"{path.relative_to(ROOT)} does not reference policy-area-map.json")
            if table_row_pattern.search(text):
                errors.append(
                    f"{path.relative_to(ROOT)} still contains inline area table rows; use canonical map"
                )

    return errors


def validate_map_mirrors() -> List[str]:
    errors: List[str] = []
    try:
        canonical = load_json(MAP_PATH)
    except ValueError as exc:
        return [str(exc)]

    for mirror in (POLICY_SKILL_MAP_PATH, ASSESS_SKILL_MAP_PATH):
        if not mirror.exists():
            errors.append(f"Missing map mirror: {mirror.relative_to(ROOT)}")
            continue
        try:
            mirrored = load_json(mirror)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if mirrored != canonical:
            errors.append(
                f"Map mirror differs from canonical map: {mirror.relative_to(ROOT)}"
            )

    return errors


def validate_portability_paths() -> List[str]:
    errors: List[str] = []
    for path, required_prefix in PORTABILITY_RULES:
        if not path.exists():
            errors.append(f"Missing portability-check file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if ".claude/skills/ciso/references/" in text:
            errors.append(
                f"{path.relative_to(ROOT)} references shared ciso references path; use local skill references"
            )
        if "policy-area-map.json" in text and required_prefix not in text:
            errors.append(
                f"{path.relative_to(ROOT)} must use local references path prefix: {required_prefix}"
            )
    return errors


def validate_skill_contracts() -> List[str]:
    errors: List[str] = []

    for skill_file in SKILL_FILES:
        if not skill_file.exists():
            errors.append(f"Missing skill file: {skill_file.relative_to(ROOT)}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        skill_name = skill_file.parent.name

        if "license: MIT" not in text:
            errors.append(f"{skill_file.relative_to(ROOT)} missing `license: MIT` frontmatter")

        metadata_match = re.search(r"\nmetadata:\n(.*?)(?:\n[A-Za-z0-9_-]+:|\n---)", text, re.DOTALL)
        if not metadata_match:
            errors.append(f"{skill_file.relative_to(ROOT)} missing metadata block")
        else:
            metadata_block = metadata_match.group(1)
            present_keys = {
                m.group(1)
                for m in re.finditer(r"^\s{2}([A-Za-z0-9_-]+):", metadata_block, re.MULTILINE)
            }
            missing = sorted(REQUIRED_METADATA_FIELDS - present_keys)
            if missing:
                errors.append(
                    f"{skill_file.relative_to(ROOT)} missing metadata keys: {', '.join(missing)}"
                )

        allowed = fm.get("allowed-tools")
        if not allowed:
            errors.append(f"{skill_file.relative_to(ROOT)} missing allowed-tools frontmatter")
        else:
            actual_tools = {token.strip() for token in allowed.split(",") if token.strip()}
            expected_tools = EXPECTED_ALLOWED_TOOLS.get(skill_name)
            if expected_tools and actual_tools != expected_tools:
                errors.append(
                    f"{skill_file.relative_to(ROOT)} has unexpected allowed-tools: "
                    f"{sorted(actual_tools)}; expected {sorted(expected_tools)}"
                )

    ciso_skill = ROOT / ".claude/skills/ciso/SKILL.md"
    if ciso_skill.exists():
        text = ciso_skill.read_text(encoding="utf-8")
        if ".claude/skills/ciso/scripts/resolve_entity_tags.py" not in text:
            errors.append("ciso SKILL.md must call the in-skill resolve_entity_tags.py path")

    return errors


def validate_tag_resolver() -> List[str]:
    errors: List[str] = []
    resolvers = [
        ROOT / "scripts/resolve_entity_tags.py",
        ROOT / ".claude/skills/ciso/scripts/resolve_entity_tags.py",
    ]
    for resolver in resolvers:
        if not resolver.exists():
            errors.append(f"Missing script: {resolver.relative_to(ROOT)}")
            continue
        if not resolver.read_text(encoding="utf-8").startswith("#!/usr/bin/env python3"):
            errors.append(f"{resolver.relative_to(ROOT)} missing python shebang")
    return errors


def validate_mirror_references() -> List[str]:
    errors: List[str] = []
    mirrors = ("ciso-policy", "ciso-assess")

    for filename in (*MIRROR_EXACT_FILES, *MIRROR_PATH_AWARE_FILES):
        canonical = ROOT / f".claude/skills/ciso/references/{filename}"
        if not canonical.exists():
            errors.append(f"Missing canonical mirror source: {canonical.relative_to(ROOT)}")
            continue

    for mirror_skill in mirrors:
        for filename in (*MIRROR_EXACT_FILES, *MIRROR_PATH_AWARE_FILES):
            mirror_path = ROOT / f".claude/skills/{mirror_skill}/references/{filename}"
            if not mirror_path.exists():
                errors.append(f"Missing mirror file: {mirror_path.relative_to(ROOT)}")
                continue
            expected = expected_mirror_text(filename, mirror_skill)
            actual = mirror_path.read_text(encoding="utf-8")
            if actual != expected:
                errors.append(
                    f"Mirror drift in {mirror_path.relative_to(ROOT)}; "
                    f"re-sync from .claude/skills/ciso/references/{filename}"
                )

    return errors


def main() -> int:
    errors: List[str] = []

    try:
        data = load_map()
        ok(f"Loaded {MAP_PATH.relative_to(ROOT)}")
    except ValueError as exc:
        fail(str(exc))
        return 1

    areas = data.get("areas")
    if not isinstance(areas, list):
        fail("policy-area-map.json must contain an 'areas' list")
        return 1

    errors.extend(validate_area_records(areas))
    errors.extend(validate_references(REFERENCE_FILES))
    errors.extend(validate_map_mirrors())
    errors.extend(validate_portability_paths())
    errors.extend(validate_skill_contracts())
    errors.extend(validate_tag_resolver())
    errors.extend(validate_mirror_references())

    if errors:
        for error in errors:
            fail(error)
        return 1

    ok(f"Validated {len(areas)} policy areas")
    ok("Validated skill references and deterministic helper scripts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
