# CSCRF Selective Load Matrix

Use this guide to keep context scoped. Resolve policy-area routing from:
`./.claude/skills/ciso-assess/references/policy-area-map.json`

Claude Opus 4.6 supports a 200K input window and 128K output window, but this does not change
selective-loading strategy. Smaller, scoped reads improve consistency and reduce drift.

## Baseline

Always load:
- `SCHEMA.md` when resolving applicability tags or matching logic
- `meta/compliance.md` when frequencies, timelines, or reporting authorities are required

Load only on demand:
- `meta/definitions.md` for term definitions
- `meta/abbreviations.md` for abbreviation expansion
- `meta/it-committee.md` for governance composition details

## Policy Area Routing

1. Read `policy-area-map.json`.
2. Match the requested policy-area slug (or alias) to one `areas[]` record.
3. Load exactly the `framework_files` listed for that area.
4. For `all`, iterate one area at a time in map order.

Never hardcode area-to-file routing inside other skill files. The map is the single source of truth.

## Context Budget Guardrails

1. Never run `cat framework/**/*.md` or equivalent bulk loads.
2. Run each major phase as a Task with a compact input contract and compact output contract.
3. Persist intermediate artifacts in `docs/.ciso-work/` so downstream phases consume summaries, not raw transcripts.
4. Keep Task outputs concise:
- Profile summary: <= 300 words
- Gap summary: <= 600 words plus machine-readable table/JSON
- Policy draft summary: <= 200 words per policy file
- Review report: <= 20 findings, each one line issue + one line fix
5. For large user documents, read headings first, then targeted sections, then only missing sections.

## Handoff Artifacts

Write and reuse these files:
- `docs/.ciso-work/entity-profile.md`
- `docs/.ciso-work/entity-profile.json`
- `docs/.ciso-work/entity-tags.json`
- `docs/.ciso-work/gap-analysis.md`
- `docs/.ciso-work/gap-analysis.json`
- `docs/.ciso-work/policy-plan.md`
- `docs/.ciso-work/review-findings.md`
- `docs/.ciso-work/roadmap.md`

Each artifact should be incremental and append-safe so follow-up turns can continue without
reloading prior full outputs.
