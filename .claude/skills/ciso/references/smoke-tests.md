# Smoke Tests

Use these prompts to quickly validate triggering, routing, and context-efficient behavior.
For full end-to-end run sequencing and artifact checks, use `mock-run-playbook.md`.
Run `bash scripts/eval_skills.sh` for deterministic static checks.

Canonical trigger dataset:
- `./.claude/skills/ciso/references/trigger-tests.yaml`
- Validate with `uv run python3 scripts/validate_trigger_suite.py`

## /ciso Trigger Tests

Should trigger:
1. `Help us get CSCRF compliant before audit. We are a mid-size stock broker.`
2. `Run /ciso assess for a small-size DP with Market SOC and existing VAPT.`
3. `Create a 90-day CSCRF remediation roadmap for a qualified RE.`

Should not trigger:
1. `Explain zero trust architecture in simple terms.`
2. `Write a generic ISO 27001 policy template.`
3. `Summarize RBI cybersecurity directions for banks.`

Expected checks:
1. Asks profiling questions when required.
2. Uses Task-routed specialists for analysis and drafting steps.
3. Writes/reuses artifacts in `docs/.ciso-work/`.

## /ciso-policy Trigger Tests

Should trigger:
1. `/ciso-policy access-control qualified "Acme Securities"`
2. `Generate incident-response policy for self-certification RE "Delta PMS".`
3. `/ciso-policy all mid-size "Zenith Broking"`

Should not trigger:
1. `Assess this existing access-control policy file for gaps.` (belongs to `/ciso-assess`)
2. `Do a complete CSCRF interview and roadmap.` (belongs to `/ciso`)

Expected checks:
1. Drafts one area per cycle (or sequential cycles for `all`).
2. Runs reviewer QA before final summary.
3. No full-framework bulk load.

## /ciso-assess Trigger Tests

Should trigger:
1. `/ciso-assess docs/policies/access-control.md qualified`
2. `Review this IR policy against CSCRF for mid-size RE and list mandatory gaps.`

Should not trigger:
1. `Draft an access-control policy from scratch.` (belongs to `/ciso-policy`)
2. `Profile my entity and tell me what applies.` (belongs to `/ciso`)

Expected checks:
1. Reads target document in scoped passes for large files.
2. Maps findings to guideline IDs with severity.
3. Uses reviewer QA before final report.

## Subagent Path Tests (via /ciso)

Use `/ciso` and check delegation logs/output shape:
1. Gap path: verify `cscrf-gap-analyst` + `cscrf-reviewer` are used for assessment.
2. Policy path: verify `cscrf-policy-drafter` + `cscrf-reviewer` are used per area.
3. Roadmap path: verify `cscrf-roadmap-planner` + `cscrf-reviewer` are used.
4. Lookup path: verify `cscrf-analyst` is used for disputed requirement spot-checks.

## Quantitative Targets

Use these default thresholds for regression checks:
1. Trigger precision target: >= 0.90 on curated trigger/non-trigger set.
2. Trigger recall target: >= 0.90 on curated trigger set.
3. Functional success target: 100% pass for deterministic script checks (`eval_skills.sh`).
4. Artifact completeness target: 100% required artifacts present (`verify-ciso-artifacts.sh --strict`).
