# Development Guide — /ciso-policy

This file contains references for skill development, testing, and validation.
These resources are NOT loaded during normal user workflows.

## Smoke Tests

Run smoke tests to verify skill contract integrity:
- `./.claude/skills/ciso-policy/references/smoke-tests.md`

## Trigger Tests

Trigger test suite with positive, negative, paraphrase, and boundary cases:
- `./.claude/skills/ciso-policy/references/trigger-tests.yaml`

## Validation Scripts

- `uv run python3 scripts/validate_skill_mappings.py` — confirms policy-area-map consistency and agent contract mirror parity
- `uv run python3 scripts/validate_trigger_suite.py` — confirms trigger test coverage

## Validation

Run `bash scripts/eval_skills.sh` locally for full validation.

## Live Trigger Monitoring

Monitor skill trigger accuracy in production usage.

### Detecting Undertriggering
Users manually typing `/ciso-policy` instead of natural language activating it indicates undertriggering.
Signs: users say "draft access-control policy for qualified RE" but the skill doesn't load automatically.
Fix: add the missed phrasing to `description` field and `trigger-tests.yaml` positive cases.

### Detecting Overtriggering
Skill loading for policy review/scoring tasks (should route to ciso-assess) or full orchestration (should route to ciso).
Signs: skill loads when user asks to "review my policy" or "run full CSCRF assessment".
Fix: add the overtriggered phrase to `trigger-tests.yaml` negative cases and strengthen negative exclusions in `description`.

### Feedback Loop
1. Log observed trigger misses or false activations in a scratch note.
2. Add new cases to `trigger-tests.yaml` in the appropriate bucket.
3. Run `uv run python3 scripts/validate_trigger_suite.py` to confirm coverage thresholds.
4. Update `description` field if wording changes are needed.

## Description QA Step

Ask Claude: "When would you use the ciso-policy skill?" Verify it quotes the description
accurately and distinguishes ciso-policy from ciso and ciso-assess. If Claude conflates them,
sharpen the negative exclusions in the `description` field.
