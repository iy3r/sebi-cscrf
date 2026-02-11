# Mock Run Playbook

Run this to validate the full `/ciso` workflow end-to-end with deterministic checkpoints.

Prerequisites:
1. Claude Code is installed.
2. You are authenticated: `claude auth status` should show `"loggedIn": true`.
3. Run from repo root.

## Step 0: Clean Previous Run Artifacts (optional)

```bash
rm -f docs/.ciso-work/entity-profile.md \
      docs/.ciso-work/entity-profile.json \
      docs/.ciso-work/entity-tags.json \
      docs/.ciso-work/gap-analysis.md \
      docs/.ciso-work/gap-analysis.json \
      docs/.ciso-work/policy-plan.md \
      docs/.ciso-work/review-findings.md \
      docs/.ciso-work/roadmap.md
```

## Step 1: Full Orchestrator Flow

Prompt:

```bash
claude -p "/ciso start. We are Zenith Broking Pvt Ltd, stock broker, mid-size RE, cloud-first on AWS, 6 IT staff, using Market SOC, annual VAPT, no board-approved cyber policy yet. Create entity profile, gap analysis, and a 90-day roadmap."
```

Expected:
1. Produces profile summary + gap summary + roadmap direction.
2. Writes core artifacts in `docs/.ciso-work/`.
3. Uses Task-routed specialists during analysis and roadmap.

## Step 2: Targeted Policy Draft

Prompt:

```bash
claude -p "/ciso-policy access-control mid-size 'Zenith Broking Pvt Ltd'"
```

Expected:
1. Writes `docs/policies/access-control.md`.
2. Includes CSCRF IDs and mandatory/recommended language.
3. Runs reviewer QA cycle before final summary.

## Step 3: Policy Assessment

Prompt:

```bash
claude -p "/ciso-assess docs/policies/access-control.md mid-size"
```

Expected:
1. Produces coverage table and prioritized findings.
2. Flags missing mandatory controls if any.
3. Includes traceability checks.

## Step 4: Verify Artifacts

```bash
bash scripts/verify-ciso-artifacts.sh --strict
bash scripts/eval_skills.sh --with-artifacts
```

Expected:
1. Script reports all required artifacts present.
2. Mapping + resolver validation checks pass.
3. Key section checks pass.
4. Exit code `0`.

## Optional: Deterministic Fixture Validation (No Live Claude Run)

Use this when you want strict contract checks in CI or local validation without running the
interactive Claude prompts above.

```bash
bash scripts/eval_skills.sh --with-fixtures
```
