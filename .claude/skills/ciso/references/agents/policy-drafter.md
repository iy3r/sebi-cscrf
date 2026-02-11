<!-- contract_version: 1.2.0 | compatible_with: ciso>=1.2.0 -->

# CSCRF Policy Drafter Task Contract

Use this contract when drafting one policy area during `/ciso`.

## Inputs
- `area_slug`
- `entity_name`
- `entity_category`
- Optional: `tech_stack`, `team_size`, `constraints`, `gap_items`
- `output_path`

## Required Reads
1. `./.claude/skills/ciso/references/policy-templates.md`
2. `./.claude/skills/ciso/references/load-matrix.md`
3. `./.claude/skills/ciso/references/policy-area-map.json`
4. `meta/compliance.md`
5. Only mapped framework files for `area_slug`

## Workflow
1. Resolve `area_slug` using policy-area map.
2. Load only mapped framework files.
3. Draft the policy with correct mandatory/recommended language.
4. Include guideline traceability for each requirement statement.
5. Write only to `output_path`.

## Output
Return:
- `file_path`
- `guidelines_covered`
- `standards_covered`
- `word_count_approx`
- `open_assumptions`

## Constraints
- Do not draft multiple areas in one pass.
- Do not include controls that cannot be traced to CSCRF IDs.
