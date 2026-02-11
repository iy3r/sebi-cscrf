<!-- contract_version: 1.2.0 | compatible_with: ciso>=1.2.0 -->

# CSCRF Roadmap Planner Task Contract

Use this contract to build a prioritized remediation roadmap during `/ciso`.

## Inputs
- `entity_profile`
- `gap_analysis_summary`
- `gap_analysis_json`
- Optional: `horizon` (default `30-60-90`)
- `output_path`

## Required Reads
1. `meta/compliance.md`
2. `./.claude/skills/ciso/references/load-matrix.md`
3. Only framework files needed for top-priority gaps

## Workflow
1. Read profile and gap artifacts.
2. Sequence actions into phases:
   - Foundation controls
   - Core mandatory closure
   - Hardening and resilience
3. Add an ongoing compliance calendar.
4. Write roadmap to `output_path`.

## Output
Return:
- `top_actions`
- `sequencing_rationale`
- `dependencies`
- `coverage_summary`

## Constraints
- Prioritize mandatory and deadline-linked items first.
- Keep owner assignments realistic for team size.
