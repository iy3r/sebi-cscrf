<!-- contract_version: 1.2.0 | compatible_with: ciso>=1.2.0 -->

# CSCRF Gap Analyst Task Contract

Use this contract for entity-scoped CSCRF gap analysis during `/ciso`.

## Inputs
- `entity_profile`
- `entity_tags`
- Optional: `policy_area_scope` (`all` or one area slug)
- Optional: `existing_controls`

## Required Reads
1. `SCHEMA.md`
2. `./.claude/skills/ciso/references/load-matrix.md`
3. `./.claude/skills/ciso/references/policy-area-map.json`
4. `meta/compliance.md` when periodicity/reporting checks are needed
5. Only mapped framework files in scope

## Workflow
1. Resolve scope from policy-area map.
2. Filter guidelines by applicability tags.
3. Classify each applicable guideline as `COMPLIANT`, `GAP`, or `NEEDS_REVIEW`.
4. Prioritize mandatory gaps first.

## Output
Return both:
1. Compact markdown summary with counts and top mandatory gaps
2. JSON array items with:
   - `guideline_id`
   - `function`
   - `mandatory`
   - `status`
   - `reason`
   - `owner_hint`
   - `priority`

## Constraints
- Never process all framework files in one load.
- Be conservative when evidence is weak.
