<!-- contract_version: 1.2.0 | compatible_with: ciso>=1.2.0 -->

# CSCRF Reviewer Task Contract

Use this contract as the QA gate for `/ciso` outputs.

## Inputs
- `scope`: `gap-analysis`, `policy`, `roadmap`, or `all`
- `document_paths`
- `entity_category`
- Optional conditional tags (`cii`, `third-party-soc`, etc.)

## Required Reads
1. `SCHEMA.md` for applicability checks
2. `meta/compliance.md` for periodicity/reporting checks
3. Mapped framework files for reviewed scope

## Checklist
1. Every requirement maps to valid CSCRF IDs.
2. Mandatory requirements use binding language.
3. Applicable mandatory requirements are not omitted.
4. Periodicities align with Table 15.
5. Reporting authority aligns with Tables 16-23.
6. Output is implementation-ready for entity scale.

## Output
Return:
- `verdict`: `PASS` or `FAIL`
- `findings`: ordered by `high`, `medium`, `low`
- Each finding includes `location`, `issue`, `fix`
- `ready_for_user`: `yes` or `no`

## Constraints
- Flag concrete gaps first.
- Avoid style-only comments unless they weaken compliance evidence.
