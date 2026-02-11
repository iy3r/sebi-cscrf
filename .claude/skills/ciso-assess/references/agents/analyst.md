<!-- contract_version: 1.2.0 | compatible_with: ciso-assess>=1.2.0 -->

# Assessment Analyst Task Contract

Use this contract for spot-checks during policy assessment.

## Inputs
- `policy_path`
- `entity_category`
- Optional: `topic_scope` (one or more policy areas)
- Optional: list of disputed `guideline_ids`

## Required Reads
1. `./.claude/skills/ciso-assess/references/policy-area-map.json`
2. `./.claude/skills/ciso-assess/references/load-matrix.md`
3. `meta/compliance.md` when periodicity/reporting checks are needed
4. Only mapped framework files in scope

## Workflow
1. Resolve policy area(s) from map.
2. Filter applicable guidelines by entity category.
3. For disputed items, quote requirement evidence with IDs.
4. Return concise judgment for each disputed item.

## Output
Return:
- `spot_checks`: array with `guideline_id`, `status`, `evidence`, `reason`
- `notes`: concise caveats

## Constraints
- Never bulk-load framework files.
- Do not draft policy text; this is assessment support only.
