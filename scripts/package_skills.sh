#!/usr/bin/env bash
set -euo pipefail

# Package each Claude Code skill as an individual .zip for distribution.
# Output: dist/ciso.zip, dist/ciso-policy.zip, dist/ciso-assess.zip

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/.claude/skills"
dist_dir="$repo_root/dist"

mkdir -p "$dist_dir"

skills=(ciso ciso-policy ciso-assess)

for skill in "${skills[@]}"; do
  skill_path="$skills_dir/$skill"
  if [[ ! -d "$skill_path" ]]; then
    echo "[SKIP] $skill — directory not found at $skill_path"
    continue
  fi

  zip_path="$dist_dir/${skill}.zip"
  rm -f "$zip_path"

  (cd "$skills_dir" && zip -r "$zip_path" "$skill/" -x '*.DS_Store' '*__pycache__*')

  echo "[OK] $zip_path"
done

echo
echo "Done. Packaged ${#skills[@]} skills in $dist_dir/"
