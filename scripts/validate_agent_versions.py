#!/usr/bin/env python3
"""Validate agent metadata versions are compatible with skill versions."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / ".claude" / "agents"
SKILLS_DIR = ROOT / ".claude" / "skills"

AGENT_FILES = [
    "cscrf-analyst.md",
    "cscrf-gap-analyst.md",
    "cscrf-reviewer.md",
    "cscrf-policy-drafter.md",
    "cscrf-roadmap-planner.md",
]

SKILL_DIRS = ["ciso", "ciso-policy", "ciso-assess"]

VERSION_RE = re.compile(r'version:\s*"([^"]+)"')
COMPAT_RE = re.compile(r'compatible_skill_versions:\s*"([^"]+)"')


def extract_version(text: str) -> str | None:
    match = VERSION_RE.search(text)
    return match.group(1) if match else None


def extract_compat(text: str) -> str | None:
    match = COMPAT_RE.search(text)
    return match.group(1) if match else None


def parse_semver(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def check_compat(skill_version: str, compat_spec: str) -> bool:
    """Check if skill_version satisfies compat_spec (e.g., '>=1.2.0')."""
    if compat_spec.startswith(">="):
        min_ver = compat_spec[2:]
        return parse_semver(skill_version) >= parse_semver(min_ver)
    return skill_version == compat_spec


def main() -> int:
    errors: List[str] = []

    skill_versions: dict[str, str] = {}
    for skill in SKILL_DIRS:
        skill_md = SKILLS_DIR / skill / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"missing skill file: {skill_md.relative_to(ROOT)}")
            continue
        text = skill_md.read_text(encoding="utf-8")
        version = extract_version(text)
        if version:
            skill_versions[skill] = version
        else:
            errors.append(f"no version metadata in {skill_md.relative_to(ROOT)}")

    for agent_file in AGENT_FILES:
        path = AGENTS_DIR / agent_file
        if not path.exists():
            errors.append(f"missing agent file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        agent_version = extract_version(text)
        compat = extract_compat(text)

        if not agent_version:
            errors.append(f"no version metadata in {path.relative_to(ROOT)}")
            continue
        if not compat:
            errors.append(f"no compatible_skill_versions in {path.relative_to(ROOT)}")
            continue

        for skill, skill_ver in skill_versions.items():
            if not check_compat(skill_ver, compat):
                errors.append(
                    f"{agent_file} (compat {compat}) incompatible with "
                    f"{skill} v{skill_ver}"
                )

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    print(f"[PASS] all {len(AGENT_FILES)} agent versions compatible with {len(skill_versions)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
