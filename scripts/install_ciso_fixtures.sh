#!/usr/bin/env bash
set -euo pipefail

force=0
if [[ "${1:-}" == "--force" ]]; then
  force=1
elif [[ "${1:-}" != "" ]]; then
  echo "[FAIL] unknown argument: ${1}"
  echo "Usage: bash scripts/install_ciso_fixtures.sh [--force]"
  exit 1
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_root="$repo_root/tests/fixtures"
work_src="$fixture_root/ciso-work"
policy_src="$fixture_root/policies"
work_dst="$repo_root/docs/.ciso-work"
policy_dst="$repo_root/docs/policies"

if [[ ! -d "$work_src" || ! -d "$policy_src" ]]; then
  echo "[FAIL] fixture source directories missing under tests/fixtures"
  exit 1
fi

mkdir -p "$work_dst" "$policy_dst"

if [[ "$force" -eq 0 ]]; then
  for path in "$work_dst/entity-profile.md" "$work_dst/entity-profile.json" "$work_dst/entity-tags.json" \
              "$work_dst/gap-analysis.md" "$work_dst/gap-analysis.json" "$work_dst/policy-plan.md" \
              "$work_dst/review-findings.md" "$work_dst/roadmap.md" "$policy_dst/access-control.md"; do
    if [[ -e "$path" ]]; then
      echo "[FAIL] destination file already exists: ${path#$repo_root/}"
      echo "Run with --force to overwrite fixture-target paths."
      exit 1
    fi
  done
fi

cp -f "$work_src"/* "$work_dst"/
cp -f "$policy_src"/*.md "$policy_dst"/

echo "[PASS] installed fixture artifacts into docs/.ciso-work and docs/policies"
