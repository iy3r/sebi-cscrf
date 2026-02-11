#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

run_artifact_checks=0
install_fixtures=0
for arg in "$@"; do
  case "$arg" in
    --with-artifacts)
      run_artifact_checks=1
      ;;
    --with-fixtures)
      run_artifact_checks=1
      install_fixtures=1
      ;;
    *)
      echo "[FAIL] unknown argument: $arg"
      echo "Usage: bash scripts/eval_skills.sh [--with-artifacts] [--with-fixtures]"
      exit 1
      ;;
  esac
done

if [[ "$install_fixtures" -eq 1 ]]; then
  echo "[0/7] Install deterministic fixture artifacts"
  bash scripts/install_ciso_fixtures.sh --force
  echo
fi

echo "[1/7] Validate skill description lengths (max 1024 chars)"
for skill_md in .claude/skills/*/SKILL.md; do
  skill_name="$(basename "$(dirname "$skill_md")")"
  desc_len="$(uv run python3 -c "
import yaml, sys
text = open('$skill_md').read()
_, fm, _ = text.split('---', 2)
meta = yaml.safe_load(fm)
print(len(meta.get('description', '')))
")"
  if [[ "$desc_len" -gt 1024 ]]; then
    echo "[FAIL] $skill_name description is $desc_len chars (max 1024)"
    exit 1
  fi
  echo "  $skill_name: ${desc_len} chars"
done
echo "[PASS] all skill descriptions under 1024 chars"

echo
echo "[2/7] Validate canonical policy-area mapping and mirror parity"
uv run python3 scripts/validate_skill_mappings.py

echo
echo "[3/7] Validate agent version compatibility"
uv run python3 scripts/validate_agent_versions.py

echo
echo "[4/7] Validate deterministic tag resolver behavior"
out_a="$(uv run python3 scripts/resolve_entity_tags.py --entity-type 'stock-broker' --category 'mid-size' --third-party-soc)"
out_b="$(uv run python3 scripts/resolve_entity_tags.py --entity-type 'Stock Broker' --category 'mid-size' --third-party-soc)"
if [[ "$out_a" != "$out_b" ]]; then
  echo "[FAIL] resolver produced different outputs for equivalent entity-type inputs"
  exit 1
fi
uv run python3 scripts/resolve_entity_tags.py --entity-type 'depository-participant' --category 'qualified' --cii >/tmp/cscrf-tags-check.json
if ! rg -q 'qualified-stock-brokers-dps' /tmp/cscrf-tags-check.json; then
  echo "[FAIL] expected qualified-stock-brokers-dps tag was not produced"
  exit 1
fi
echo "[PASS] resolver outputs are stable for equivalence and conditional tags"

echo
echo "[5/7] Validate semantic trigger suite"
uv run python3 scripts/validate_trigger_suite.py

echo
echo "[6/7] Validate functional contract manifests"
uv run python3 scripts/validate_skill_functional_contracts.py

echo
echo "[7/7] Validate output contracts for existing artifacts"
uv run python3 scripts/validate_ciso_outputs.py
if [[ "$run_artifact_checks" -eq 1 ]]; then
  uv run python3 scripts/validate_ciso_outputs.py --strict
  bash scripts/verify-ciso-artifacts.sh --strict
else
  echo "[INFO] skipping artifact strict checks (run with --with-artifacts or --with-fixtures to enable)"
fi

echo
echo "Skill evaluation checks complete."
