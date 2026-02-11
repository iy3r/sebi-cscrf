#!/usr/bin/env bash
set -euo pipefail

strict=0
if [[ "${1:-}" == "--strict" ]]; then
  strict=1
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required_files=(
  "docs/.ciso-work/entity-profile.md"
  "docs/.ciso-work/entity-profile.json"
  "docs/.ciso-work/entity-tags.json"
  "docs/.ciso-work/gap-analysis.md"
  "docs/.ciso-work/gap-analysis.json"
  "docs/.ciso-work/roadmap.md"
)

optional_files=(
  "docs/.ciso-work/policy-plan.md"
  "docs/.ciso-work/review-findings.md"
  "docs/policies/access-control.md"
)

missing_required=0
missing_optional=0
content_failures=0

echo "Verifying CSCRF workflow artifacts in: $repo_root"
echo

check_file() {
  local path="$1"
  if [[ -f "$path" ]]; then
    echo "[PASS] file exists: $path"
  else
    echo "[FAIL] missing file: $path"
    return 1
  fi
}

check_contains() {
  local path="$1"
  local pattern="$2"
  local label="$3"
  if [[ ! -f "$path" ]]; then
    return 0
  fi
  if rg -q "$pattern" "$path"; then
    echo "[PASS] $label in $path"
  else
    echo "[FAIL] $label missing in $path"
    return 1
  fi
}

echo "Required files:"
for f in "${required_files[@]}"; do
  if ! check_file "$f"; then
    missing_required=$((missing_required + 1))
  fi
done
echo

echo "Optional files:"
for f in "${optional_files[@]}"; do
  if [[ -f "$f" ]]; then
    echo "[PASS] file exists: $f"
  else
    echo "[WARN] missing optional file: $f"
    missing_optional=$((missing_optional + 1))
  fi
done
echo

echo "Content checks:"
if ! check_contains "docs/.ciso-work/entity-profile.md" "^## Entity Profile|Entity Profile" "entity profile heading"; then
  content_failures=$((content_failures + 1))
fi
if ! check_contains "docs/.ciso-work/entity-profile.json" "\"entity_type\"|\"category\"" "entity profile json core keys"; then
  content_failures=$((content_failures + 1))
fi
if ! check_contains "docs/.ciso-work/gap-analysis.md" "Mandatory Gaps|Priority 1|GAP" "gap analysis core section"; then
  content_failures=$((content_failures + 1))
fi
if ! check_contains "docs/.ciso-work/roadmap.md" "90-Day|Phase|Ongoing Compliance Calendar" "roadmap phase/calendar section"; then
  content_failures=$((content_failures + 1))
fi
if ! check_contains "docs/policies/access-control.md" "CSCRF Ref|PR.AA|Traceability Matrix" "policy traceability content"; then
  content_failures=$((content_failures + 1))
fi
echo

echo "Summary:"
echo "- missing required files: $missing_required"
echo "- missing optional files: $missing_optional"
echo "- content check failures: $content_failures"

if [[ $strict -eq 1 ]]; then
  if [[ $missing_required -gt 0 || $content_failures -gt 0 ]]; then
    echo
    echo "STRICT MODE: verification failed."
    exit 1
  fi
fi

echo
echo "Verification complete."
