#!/usr/bin/env python3
"""Resolve CSCRF applicability tags deterministically from entity profile inputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Set

VALID_CATEGORIES = {
    "mii",
    "qualified",
    "mid-size",
    "small-size",
    "self-certification",
}

ENTITY_TYPE_ALIASES = {
    "stock-broker": "stock-broker",
    "stock_broker": "stock-broker",
    "stock broker": "stock-broker",
    "broker": "stock-broker",
    "depository-participant": "depository-participant",
    "depository_participant": "depository-participant",
    "depository participant": "depository-participant",
    "dp": "depository-participant",
    "mutual-fund-amc": "mutual-fund-amc",
    "mutual_fund_amc": "mutual-fund-amc",
    "mutual fund": "mutual-fund-amc",
    "amc": "mutual-fund-amc",
    "clearing-corporation": "clearing-corporation",
    "clearing corporation": "clearing-corporation",
    "stock-exchange": "stock-exchange",
    "stock exchange": "stock-exchange",
    "depository": "depository",
    "other": "other",
}


class ResolverError(Exception):
    """Raised when input cannot be resolved safely."""


def _normalize_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "y", "on"}:
            return True
        if normalized in {"0", "false", "no", "n", "off", ""}:
            return False
    raise ResolverError(f"Invalid boolean value: {value!r}")


def _normalize_category(raw: Any) -> str:
    if not isinstance(raw, str):
        raise ResolverError("Category is required and must be a string")
    category = raw.strip().lower().replace("_", "-")
    if category not in VALID_CATEGORIES:
        raise ResolverError(
            "Invalid category. Expected one of: " + ", ".join(sorted(VALID_CATEGORIES))
        )
    return category


def _normalize_entity_type(raw: Any) -> str:
    if not isinstance(raw, str):
        raise ResolverError("Entity type is required and must be a string")
    key = raw.strip().lower().replace("_", " ").replace("-", " ")
    collapsed = " ".join(key.split())
    canonical = ENTITY_TYPE_ALIASES.get(collapsed)
    if canonical:
        return canonical
    raise ResolverError(
        "Unsupported entity type. Supported values include: stock-broker, "
        "depository-participant, mutual-fund-amc, clearing-corporation, "
        "stock-exchange, depository, other"
    )


def _load_profile(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ResolverError(f"Profile file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ResolverError(f"Invalid JSON in profile file: {path} ({exc})") from exc


def _first_value(data: Dict[str, Any], candidates: Iterable[str], default: Any = None) -> Any:
    for key in candidates:
        if key in data:
            return data[key]
    return default


def resolve_tags(profile: Dict[str, Any]) -> Dict[str, Any]:
    entity_type_raw = _first_value(profile, ["entity_type", "entityType", "type"])
    category_raw = _first_value(profile, ["category", "entity_category", "entityCategory"])

    cii_raw = _first_value(profile, ["cii", "is_cii", "isCii"], False)
    third_party_soc_raw = _first_value(
        profile, ["third_party_soc", "thirdPartySoc", "uses_market_soc", "usesMarketSoc"], False
    )

    entity_type = _normalize_entity_type(entity_type_raw)
    category = _normalize_category(category_raw)
    cii = _normalize_bool(cii_raw)
    third_party_soc = _normalize_bool(third_party_soc_raw)

    tags: Set[str] = {category}

    if cii:
        tags.add("cii")
    if third_party_soc:
        tags.add("third-party-soc")

    if entity_type == "stock-broker":
        tags.add("stock-brokers")
        if category == "qualified":
            tags.add("qualified-stock-brokers-dps")
        elif category == "mid-size":
            tags.add("mid-size-stock-brokers-dps")

    if entity_type == "depository-participant":
        tags.add("depository-participants")
        if category == "qualified":
            tags.add("qualified-stock-brokers-dps")
        elif category == "mid-size":
            tags.add("mid-size-stock-brokers-dps")

    return {
        "entity_type": entity_type,
        "category": category,
        "inputs": {
            "cii": cii,
            "third_party_soc": third_party_soc,
        },
        "tags": sorted(tags),
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve CSCRF applicability tags from profile JSON or CLI arguments."
    )
    parser.add_argument("--profile", type=Path, help="Path to profile JSON file")
    parser.add_argument("--entity-type", help="Entity type")
    parser.add_argument("--category", help="Entity category")
    parser.add_argument("--cii", action="store_true", help="Set CII true")
    parser.add_argument("--third-party-soc", action="store_true", help="Set third-party-soc true")
    parser.add_argument("--output", type=Path, help="Optional output JSON path")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()

    profile: Dict[str, Any] = {}
    if args.profile:
        profile = _load_profile(args.profile)

    if args.entity_type is not None:
        profile["entity_type"] = args.entity_type
    if args.category is not None:
        profile["category"] = args.category
    if args.cii:
        profile["cii"] = True
    if args.third_party_soc:
        profile["third_party_soc"] = True

    try:
        resolved = resolve_tags(profile)
    except ResolverError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    output = (
        json.dumps(resolved, indent=2, ensure_ascii=True)
        if args.pretty
        else json.dumps(resolved, separators=(",", ":"), ensure_ascii=True)
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output + "\n", encoding="utf-8")

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
