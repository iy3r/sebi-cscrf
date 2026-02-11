#!/usr/bin/env python3
"""Validate deterministic functional contracts for CSCRF skills."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST_GLOB = "tests/skills/functional/*.yaml"


def ok(message: str) -> None:
    print(f"[PASS] {message}")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def load_data(path: Path) -> Dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        try:
            import yaml  # type: ignore
        except ModuleNotFoundError as exc:
            raise ValueError(
                f"{path.relative_to(ROOT)} is not JSON-compatible YAML and PyYAML is unavailable"
            ) from exc
        data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a top-level object")
    return data


def parse_frontmatter(markdown_text: str) -> Dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---\n?", markdown_text, re.DOTALL)
    if not match:
        return None
    out: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def resolve_path(rel_path: str) -> Path:
    return ROOT / rel_path


def run_check(check: Dict[str, Any], errors: List[str], context: str) -> None:
    check_type = check.get("type")
    path_value = check.get("path")
    if not isinstance(check_type, str):
        errors.append(f"{context}: check missing string 'type'")
        return
    if not isinstance(path_value, str):
        errors.append(f"{context}: check missing string 'path'")
        return

    path = resolve_path(path_value)

    if check_type == "file_exists":
        if not path.exists():
            errors.append(f"{context}: file does not exist: {path_value}")
        return

    if not path.exists():
        errors.append(f"{context}: required file missing for {check_type}: {path_value}")
        return

    if check_type == "contains_all":
        patterns = check.get("patterns")
        regex = bool(check.get("regex", True))
        if not isinstance(patterns, list) or not all(isinstance(item, str) for item in patterns):
            errors.append(f"{context}: contains_all requires string list 'patterns'")
            return
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            if regex:
                if re.search(pattern, text, re.MULTILINE) is None:
                    errors.append(f"{context}: pattern not found in {path_value}: {pattern}")
            else:
                if pattern not in text:
                    errors.append(f"{context}: literal not found in {path_value}: {pattern}")
        return

    if check_type == "frontmatter_keys":
        keys = check.get("keys")
        if not isinstance(keys, list) or not all(isinstance(item, str) for item in keys):
            errors.append(f"{context}: frontmatter_keys requires string list 'keys'")
            return
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{context}: missing YAML frontmatter in {path_value}")
            return
        for key in keys:
            if key not in fm:
                errors.append(f"{context}: frontmatter key missing in {path_value}: {key}")
        return

    if check_type == "json_items_have_fields":
        required_fields = check.get("required_fields")
        min_items = check.get("min_items", 1)
        container_key = check.get("container_key")
        if not isinstance(required_fields, list) or not all(
            isinstance(item, str) for item in required_fields
        ):
            errors.append(f"{context}: json_items_have_fields requires string list 'required_fields'")
            return
        if not isinstance(min_items, int) or min_items < 0:
            errors.append(f"{context}: json_items_have_fields requires non-negative integer 'min_items'")
            return

        data = json.loads(path.read_text(encoding="utf-8"))
        rows: Any = data
        if isinstance(container_key, str):
            if not isinstance(data, dict):
                errors.append(f"{context}: expected object for container_key in {path_value}")
                return
            rows = data.get(container_key)

        if not isinstance(rows, list):
            errors.append(f"{context}: target JSON value is not a list in {path_value}")
            return
        if len(rows) < min_items:
            errors.append(f"{context}: expected at least {min_items} items in {path_value}")
            return

        for idx, row in enumerate(rows, start=1):
            if not isinstance(row, dict):
                errors.append(f"{context}: item {idx} in {path_value} is not an object")
                continue
            missing = [field for field in required_fields if field not in row]
            if missing:
                errors.append(
                    f"{context}: item {idx} in {path_value} missing fields: {', '.join(missing)}"
                )
        return

    errors.append(f"{context}: unsupported check type: {check_type}")


def validate_manifest(path: Path) -> List[str]:
    data = load_data(path)
    errors: List[str] = []

    suite = data.get("suite")
    cases = data.get("cases")

    if not isinstance(suite, str) or not suite.strip():
        return [f"{path.relative_to(ROOT)}: missing string 'suite'"]
    if not isinstance(cases, list):
        return [f"{path.relative_to(ROOT)}: missing list 'cases'"]

    for case_index, case in enumerate(cases, start=1):
        context = f"{path.relative_to(ROOT)} case[{case_index}]"
        if not isinstance(case, dict):
            errors.append(f"{context}: case must be an object")
            continue

        case_id = case.get("id")
        checks = case.get("checks")

        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{context}: missing string 'id'")
            continue
        if not isinstance(checks, list) or not checks:
            errors.append(f"{context} ({case_id}): missing non-empty list 'checks'")
            continue

        for check_index, check in enumerate(checks, start=1):
            if not isinstance(check, dict):
                errors.append(f"{context} ({case_id}) check[{check_index}]: check must be an object")
                continue
            run_check(check, errors, f"{context} ({case_id}) check[{check_index}]")

    return errors


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        action="append",
        default=[],
        help="Relative manifest path. Repeat flag to pass multiple manifests.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)

    manifests: List[Path] = []
    if args.manifest:
        manifests = [ROOT / rel for rel in args.manifest]
    else:
        manifests = sorted(ROOT.glob(DEFAULT_MANIFEST_GLOB))

    if not manifests:
        fail(f"No functional manifests found: {DEFAULT_MANIFEST_GLOB}")
        return 1

    errors: List[str] = []
    for manifest in manifests:
        if not manifest.exists():
            errors.append(f"Manifest does not exist: {manifest.relative_to(ROOT)}")
            continue
        try:
            manifest_errors = validate_manifest(manifest)
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
            continue
        if manifest_errors:
            errors.extend(manifest_errors)
        else:
            ok(f"Validated functional contract manifest: {manifest.relative_to(ROOT)}")

    if errors:
        for error in errors:
            fail(error)
        return 1

    ok(f"Validated {len(manifests)} functional contract manifest(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
