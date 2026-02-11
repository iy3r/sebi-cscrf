<!-- contract_version: 1.2.0 | compatible_with: ciso>=1.2.0 -->

# CSCRF Analyst Task Contract

Use this contract for targeted requirement lookups and spot-checks during `/ciso`.

## Inputs
- `question`
- Optional: `policy_area`, `entity_category`, `guideline_ids`

## Required Reads
1. `SCHEMA.md` for applicability logic
2. `./.claude/skills/ciso/references/load-matrix.md`
3. `./.claude/skills/ciso/references/policy-area-map.json`
4. Only mapped framework files in scope
5. `meta/compliance.md` when periodicity/reporting checks are needed

## Workflow
1. Resolve scope from `policy_area` and area map.
2. Load only required framework files for the question.
3. Return evidence-linked answers with CSCRF IDs.

## Output
Return:
- `answer`
- `evidence`: array of `{id, source_path, note}`
- `open_assumptions`

## Constraints
- Never bulk-load framework files.
- Do not draft policy text in this contract.
