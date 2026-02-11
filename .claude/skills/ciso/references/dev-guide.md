# Development Guide — /ciso

This file contains references for skill development, testing, and validation.
These resources are NOT loaded during normal user workflows.

## Smoke Tests

Run smoke tests to verify skill contract integrity:
- `./.claude/skills/ciso/references/smoke-tests.md`

## Trigger Tests

Trigger test suite with positive, negative, paraphrase, and boundary cases:
- `./.claude/skills/ciso/references/trigger-tests.yaml`

## Validation Scripts

- `uv run python3 scripts/validate_skill_mappings.py` — confirms policy-area-map consistency and agent contract mirror parity
- `uv run python3 scripts/validate_trigger_suite.py` — confirms trigger test coverage

## Validation

Run `bash scripts/eval_skills.sh` locally for full validation.

## Live Trigger Monitoring

Monitor skill trigger accuracy in production usage.

### Detecting Undertriggering
Users manually typing `/ciso` instead of natural language activating it indicates undertriggering.
Signs: users say "help us get CSCRF compliant" but the skill doesn't load automatically.
Fix: add the missed phrasing to `description` field and `trigger-tests.yaml` positive cases.

### Detecting Overtriggering
Skill loading for non-CSCRF queries (ISO 27001, RBI cyber framework, generic security questions).
Signs: skill loads when user asks about frameworks other than CSCRF, or asks general cybersecurity questions.
Fix: add the overtriggered phrase to `trigger-tests.yaml` negative cases and strengthen the negative exclusions in `description`.

### Feedback Loop
1. Log observed trigger misses or false activations in a scratch note.
2. Add new cases to `trigger-tests.yaml` in the appropriate bucket.
3. Run `uv run python3 scripts/validate_trigger_suite.py` to confirm coverage thresholds.
4. Update `description` field if wording changes are needed.

## Description QA Step

Ask Claude: "When would you use the ciso skill?" Verify it quotes the description accurately
and distinguishes ciso from ciso-policy and ciso-assess. If Claude conflates them, sharpen
the negative exclusions in the `description` field.

## Architecture Decision: Agent Contract Mirrors

Agent contracts are duplicated across `.claude/agents/` (canonical) and each skill's
`references/agents/` directory. This was a deliberate choice:

**Why mirrors instead of symlinks/references:**
- Skills are self-contained and portable — each skill folder can be extracted and
  distributed independently without breaking agent references.
- `validate_skill_mappings.py` includes mirror parity checks to ensure canonical
  copies and mirrors never drift.
- Trade-off accepted: 12 extra files and mirror-sync overhead vs. full portability.

**If maintaining mirrors becomes burdensome**, consider switching skill SKILL.md files
to reference canonical paths (`../../agents/cscrf-analyst.md`) instead. This would
break standalone distribution but eliminate sync overhead.
