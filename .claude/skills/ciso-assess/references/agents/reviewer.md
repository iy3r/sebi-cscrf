<!-- contract_version: 1.2.0 | compatible_with: ciso-assess>=1.2.0 -->

# Assessment Reviewer Task Contract

Use this contract to QA final `/ciso-assess` findings before user delivery.

## Inputs
- Assessment report draft
- `policy_path`
- `entity_category`

## Required Reads
1. `./.claude/skills/ciso-assess/references/assessment-template.md`
2. `meta/compliance.md`
3. Mapped framework files for assessed areas

## Checklist
1. Findings map to valid CSCRF IDs.
2. Mandatory gaps are prioritized first.
3. Coverage labels (`COVERED`, `PARTIAL`, `MISSING`, `WEAK`) are used consistently.
4. Periodicity and reporting authority checks are accurate.
5. Recommendations are specific and implementable.

## Output
Return:
- `verdict`: `PASS` or `FAIL`
- `findings`: severity-ordered, each with `location`, `issue`, `fix`
- `ready_for_user`: `yes` or `no`

## Constraints
- Do not soften clear mandatory gaps.
- Do not add requirements that cannot be traced to CSCRF sources.
