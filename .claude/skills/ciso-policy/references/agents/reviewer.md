<!-- contract_version: 1.2.0 | compatible_with: ciso-policy>=1.2.0 -->

# Policy Reviewer Task Contract

Use this contract to QA a drafted policy before finalizing.

## Inputs
- `policy_path`
- `entity_category`
- Optional conditional tags (`cii`, `third-party-soc`, etc.)

## Required Reads
1. `./.claude/skills/ciso-policy/references/policy-area-map.json`
2. `meta/compliance.md`
3. Mapped framework files for the policy area

## Checklist
1. Every requirement maps to valid CSCRF IDs.
2. Mandatory requirements use binding language.
3. Mandatory applicable controls are not missing.
4. Review cycles and periodicities align with Table 15.
5. Reporting authority aligns with Tables 16-23.
6. Policy is concise and implementable for entity scale.

## Output
Return:
- `verdict`: `PASS` or `FAIL`
- `findings`: ordered by `high`, `medium`, `low`
- Each finding includes `location`, `issue`, `fix`
- `ready_for_user`: `yes` or `no`

## Constraints
- Only flag concrete gaps with direct fix instructions.
- Avoid style-only comments unless they weaken compliance evidence.
