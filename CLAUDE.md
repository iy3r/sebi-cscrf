# CLAUDE.md

## Project

Structured extraction of SEBI's Cybersecurity and Cyber Resilience Framework (CSCRF) v1.0 for Indian securities market Regulated Entities (REs). Includes the full framework as structured Markdown, Claude Code skills for compliance workflows, specialist agents, and a validation suite.

## Repo Layout

```
.
├── CLAUDE.md
├── SCHEMA.md              # Canonical schema — read this first for all conventions
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml          # Python deps (pyyaml) + optional eval deps (anthropic)
├── uv.lock                 # Reproducible dependency lock
├── framework/
│   └── {function}/         # governance, identify, protect, detect, respond, recover, evolve
│       └── {code}.md       # One file per CSCRF sub-section (e.g. gv-oc.md, pr-aa.md)
├── meta/                   # Supplementary reference content
│   ├── definitions.md
│   ├── abbreviations.md
│   ├── it-committee.md
│   └── compliance.md
├── sources/                # Original SEBI-published PDFs (circulars + extracted refs)
│   ├── circulars/          # Unmodified SEBI circulars
│   └── refs/               # meta/ (topic-level) + framework/ (function-level) reference segments
├── docs/                   # User-authored documents (policies, memos)
├── .claude/
│   ├── skills/             # Claude Code skills (ciso, ciso-assess, ciso-policy)
│   └── agents/             # Specialist agents (analyst, gap-analyst, policy-drafter, reviewer, roadmap-planner)
├── scripts/                # Validation scripts and eval harness
├── tests/
│   ├── fixtures/           # Deterministic fixture data for validation
│   └── skills/functional/  # Functional contract manifests
```

Each framework `.md` file has YAML frontmatter (objective, standards) and a body (guidelines with applicability metadata, optional annexure).

## Key Conventions

- **SCHEMA.md is the source of truth** for frontmatter fields, applicability tags, ID patterns, and mapping rules. Always consult it before editing or generating files.
- **Verbatim text** — all standard and guideline text is reproduced exactly from CSCRF. Do not paraphrase, summarise, or reword.
- **Guideline IDs** are `{CODE}.G{n}`, assigned sequentially. Standards are `{CODE}.S{n}` from CSCRF.
- **Applicability tags**: 5 canonical (`mii`, `qualified`, `mid-size`, `small-size`, `self-certification`) + 6 conditional (`cii`, `third-party-soc`, `stock-brokers`, `depository-participants`, `qualified-stock-brokers-dps`, `mid-size-stock-brokers-dps`).
- **mandatory** is `true` only when CSCRF explicitly states "(Mandatory)". Never infer.
- New guideline ID when applicability or standards group changes; multiple numbered points under the same block stay as one guideline.

## Development Setup

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                    # Install pyyaml into .venv/
uv sync --extra eval       # Also install anthropic (for eval_skills_api.py functional/full modes)
```

All scripts are invoked via `uv run python3`:

```bash
uv run python3 scripts/resolve_entity_tags.py --entity-type 'stock-broker' --category 'mid-size'
bash scripts/eval_skills.sh --with-fixtures
```

## Scripts and Validation

| Script | Purpose |
|--------|---------|
| `eval_skills.sh` | 7-step validation harness — runs all checks below (`--with-artifacts` for strict checks, `--with-fixtures` to install fixtures + strict checks) |
| `validate_skill_mappings.py` | Validates canonical policy-area mapping, skill references, and mirror parity |
| `validate_agent_versions.py` | Ensures agent version compatibility with skills |
| `resolve_entity_tags.py` | Deterministic entity tag resolver (entity-type + category → tags) |
| `validate_trigger_suite.py` | Validates semantic trigger test suites for all 3 skills |
| `validate_skill_functional_contracts.py` | Validates functional contract manifests against skill files |
| `validate_ciso_outputs.py` | Validates output contracts for CISO artifacts (`--strict` for required-artifact mode) |
| `eval_skills_api.py` | Skills API evaluation: `trigger` (offline), `functional` (API), `full`, `report` |
| `verify-ciso-artifacts.sh` | Artifact verification helper (`--strict` for CI) |
| `install_ciso_fixtures.sh` | Install deterministic fixture artifacts (`--force` to overwrite) |
| `package_skills.sh` | Generate `.zip` files for Claude.ai skill upload |

## Agents and Skills

### Skills (3)

| Skill | Type | Purpose |
|-------|------|---------|
| `/ciso` | Full compliance workflow | Entity profiling → gap analysis → policy generation → 90-day roadmap |
| `/ciso-policy` | Targeted policy drafting | Generate CSCRF-compliant policy documents per area |
| `/ciso-assess` | Policy evaluation | Score existing policies against CSCRF requirements |

### Agents (5)

| Agent | File | Purpose |
|-------|------|---------|
| `cscrf-analyst` | `.claude/agents/cscrf-analyst.md` | Read-only CSCRF lookups (guidelines, applicability, periodicities) |
| `cscrf-gap-analyst` | `.claude/agents/cscrf-gap-analyst.md` | Applicability filtering and gap classification |
| `cscrf-policy-drafter` | `.claude/agents/cscrf-policy-drafter.md` | One-policy-at-a-time drafting with CSCRF traceability |
| `cscrf-reviewer` | `.claude/agents/cscrf-reviewer.md` | QA for missing mandatory items, language strength, periodicities |
| `cscrf-roadmap-planner` | `.claude/agents/cscrf-roadmap-planner.md` | Phased remediation planning and compliance calendar |

## Common Tasks

**Adding a new sub-section extraction:** Follow the exact frontmatter schema. Assign guideline IDs sequentially. Flag non-standard applicability with `⚠️` blockquote.

**Querying applicability:** Match RE's tag(s) against `applicability` arrays. See SCHEMA.md for the Python pseudocode pattern.

**Validating extractions:** Every file should have a 1:1 match between standards referenced in guidelines and standards defined in frontmatter. No orphan standards, no phantom references.

**Running validation locally:**

```bash
bash scripts/eval_skills.sh                    # Quick check (skips strict artifact checks)
bash scripts/eval_skills.sh --with-fixtures    # Full check with fixture installation
```

**Adding a new agent:** Create `.claude/agents/{name}.md` with the agent description. Update `validate_agent_versions.py` if the agent has version constraints.

**Adding a new script:** Add the script to `scripts/`. If it needs validation, add a step in `eval_skills.sh`. If it needs Python deps, add them to `pyproject.toml` and run `uv sync`.

**Packaging skills for Claude.ai upload:**

```bash
bash scripts/package_skills.sh          # Generates dist/*.zip files
```

**Running API-level skill evaluation:**

```bash
uv run python3 scripts/eval_skills_api.py trigger      # Offline trigger matching
uv run python3 scripts/eval_skills_api.py functional    # API-based functional tests
uv run python3 scripts/eval_skills_api.py full          # Full end-to-end evaluation
uv run python3 scripts/eval_skills_api.py report        # Generate evaluation report
```

**Installing deterministic fixture artifacts:**

```bash
bash scripts/install_ciso_fixtures.sh          # Install fixtures (skip existing)
bash scripts/install_ciso_fixtures.sh --force  # Overwrite existing fixtures
```

## Quality Expectations (All Skills)

- Quality is more important than speed — take the time to cross-reference every mandatory guideline.
- Do not skip validation steps even under context pressure.
- Check EVERY mandatory guideline for the entity's tags — do not skip or sample.
- Every policy statement or finding must trace to a specific CSCRF guideline ID.

## Do Not

- Rewrite or paraphrase CSCRF text
- Invent applicability tags not documented in SCHEMA.md
- Merge guidelines with different applicability into one block
- Skip guideline sequence numbers within a file
- Call `python3` directly — always use `uv run python3`
- Add Python dependencies without updating `pyproject.toml` and running `uv sync`
