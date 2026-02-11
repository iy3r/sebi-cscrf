<!-- contract_version: 1.2.0 | compatible_with: ciso-policy>=1.2.0 -->

# Policy Drafter Task Contract

Use this contract when drafting one CSCRF policy area.

## Inputs
- `area_slug`
- `entity_name`
- `entity_category`
- Optional: `tech_stack`, `team_size`, `constraints`, `gap_items`
- `output_path`

## Required Reads
1. `./.claude/skills/ciso-policy/references/policy-templates.md`
2. `./.claude/skills/ciso-policy/references/load-matrix.md`
3. `./.claude/skills/ciso-policy/references/policy-area-map.json`
4. `meta/compliance.md`
5. Only mapped `framework_files` for `area_slug`

## Workflow
1. Resolve `area_slug` from policy-area map.
2. Load only mapped framework files.
3. Draft the policy using mandatory/recommended language correctly.
4. Include CSCRF traceability in every policy statement.
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
- Do not invent controls not traceable to CSCRF guideline IDs.
- Scale detail to entity category and team size.
