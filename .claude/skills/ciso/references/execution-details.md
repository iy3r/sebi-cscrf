# Execution Details — /ciso

Read this file mid-execution for team setup, artifact paths, and failure handling.
This content is NOT needed when deciding whether to load the skill.

## Team Setup with Task Tool

Use Task as two logical teams.

### Assessment Team
- `references/agents/analyst.md` for targeted CSCRF lookups and requirement checks
- `references/agents/gap-analyst.md` for applicability filtering and gap classification
- `references/agents/reviewer.md` for QA of gap outputs

### Policy Team
- `references/agents/policy-drafter.md` for policy drafting by area
- `references/agents/reviewer.md` for traceability and periodicity QA
- `references/agents/roadmap-planner.md` for phased remediation roadmap

## Artifact Contract

Create and reuse:
- `docs/.ciso-work/entity-profile.md`
- `docs/.ciso-work/entity-profile.json`
- `docs/.ciso-work/entity-tags.json`
- `docs/.ciso-work/gap-analysis.md`
- `docs/.ciso-work/gap-analysis.json`
- `docs/.ciso-work/policy-plan.md`
- `docs/.ciso-work/review-findings.md`
- `docs/.ciso-work/roadmap.md`

## Iteration Policy

- Max iterations per phase: 2 (initial attempt + 1 retry after targeted fixes).
- Retry triggers: reviewer FAIL verdict, empty output, malformed JSON.
- Stopping criteria: second reviewer FAIL -> present draft with findings to user for decision.
- Never: silent retry loops, infinite iteration, suppressing failures.

## Failure Envelope (Standardized)

For any phase-level failure, use this contract:

1. Retry budget: one retry only after correcting concrete input errors.
2. Persist partial output:
   - `docs/.ciso-work/phase-partial.md`
   - `docs/.ciso-work/phase-error.json` with `phase`, `error`, `attempts`, `next_actions`
3. Terminal failure response must include:
   - phase that failed,
   - blocking reason with file/tool context,
   - what was completed successfully,
   - exact next user decision needed.
