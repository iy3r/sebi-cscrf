# CSCRF — Structured Extraction

A clean, machine-readable representation of SEBI's [Cybersecurity and Cyber Resilience Framework (CSCRF)](https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html) v1.0 for Regulated Entities (REs) in the Indian securities market.

Every objective, standard, and guideline from the framework is extracted verbatim into structured Markdown files with YAML frontmatter — making the entire framework parseable, queryable, and composable.

## Why

CSCRF is published as a PDF. That makes it hard to search, filter, or build tooling on top of. This repo fixes that by turning the framework into structured data you can work with programmatically:

- **Compliance-as-code** — filter guidelines by RE type, mandatory status, or standard code with a YAML parser
- **Policy authoring** — reference specific guidelines from Typst, LaTeX, or any document toolchain
- **RAG / LLM retrieval** — each file is a self-contained unit sized for embedding and retrieval
- **Audit preparation** — trace guidelines back to standards and vice versa

## Repository Structure

```
cscrf/
├── SCHEMA.md              # Canonical schema — start here for all conventions
├── pyproject.toml         # Python deps (pyyaml) + optional eval deps (anthropic)
├── framework/
│   ├── governance/        # GV.OC, GV.OV, GV.PO, GV.RM, GV.RR, GV.SC
│   ├── identify/          # ID.AM, ID.RA
│   ├── protect/           # PR.AA, PR.AT, PR.DS, PR.IP, PR.MA
│   ├── detect/            # DE.CM, DE.DP
│   ├── respond/           # RS.AN, RS.CO, RS.IM, RS.MA
│   ├── recover/           # RC.CO, RC.IM, RC.RP
│   └── evolve/            # EV.ST
├── sources/               # Original SEBI-published PDFs (circulars + extracted refs)
├── meta/                  # Definitions, abbreviations, IT committee, compliance timelines
├── docs/                  # User-authored documents (policies, memos)
├── .claude/
│   ├── skills/            # Claude Code skills (ciso, ciso-assess, ciso-policy)
│   └── agents/            # Specialist agents (5 task-routed agents)
├── scripts/               # Validation scripts and eval harness
└── tests/                 # Fixtures and functional contract manifests
```

**23 files** covering all CSCRF sub-sections across 7 cybersecurity functions. **128 standards**, **97 guidelines** (80 mandatory, 17 non-mandatory).

## How It Works

Each framework file has YAML frontmatter with the sub-section's metadata and standards, followed by a body containing guidelines with applicability and mandatory status:

```yaml
---
code: PR.AA
title: Access and Authentication
goal: WITHSTAND & CONTAIN
function: PROTECT
version: "1.0"
source: CSCRF
objective: >
  Verbatim objective text from CSCRF...
standards:
  - id: PR.AA.S1
    text: >
      Verbatim standard text...
---

## Guidelines

### PR.AA.G1
- **standards:** [PR.AA.S1, PR.AA.S2]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Verbatim guideline text from CSCRF...
```

### Applicability Tags

Five RE categories plus six conditional tags for specific entity types:

| Tag | Category |
|-----|----------|
| `mii` | Market Infrastructure Institutions |
| `qualified` | Qualified REs |
| `mid-size` | Mid-size REs |
| `small-size` | Small-size REs |
| `self-certification` | Self-certification REs |
| `cii` | Conditional — Critical Information Infrastructure |
| `stock-brokers` | Conditional — Stock Brokers |
| `depository-participants` | Conditional — Depository Participants |

See [SCHEMA.md](SCHEMA.md) for the full tag list and mapping rules.

### Querying

Parse the frontmatter with any YAML library and filter:

```python
import yaml, pathlib

for path in pathlib.Path("framework").rglob("*.md"):
    text = path.read_text()
    _, fm, body = text.split("---", 2)
    meta = yaml.safe_load(fm)
    # ... filter by applicability, mandatory status, standard code, etc.
```

See [SCHEMA.md](SCHEMA.md) for complete query examples.

## Claude Code Skills

Go from "we need to comply with CSCRF" to a complete gap analysis, policy set, and 90-day roadmap — in a single Claude Code session. Three skills cover the full compliance lifecycle across all 97 CSCRF guidelines.

### Quick Start

```bash
git clone https://github.com/iy3r/sebi-cscrf.git
cd sebi-cscrf
claude "/ciso start"
```

**What happens:**
- Structured interview determines your RE category and applicability tags
- All 97 CSCRF guidelines are mapped against your entity profile
- Gap analysis identifies missing controls with priority rankings
- Policies and a 90-day remediation roadmap are generated to `docs/`

**What you get** — real output from fixture data:

Entity profile (`docs/.ciso-work/entity-profile.md`):
```markdown
## Entity Profile

- Entity: Zenith Broking Pvt Ltd
- Entity type: stock-broker
- Category: mid-size
- Conditional flags: third-party-soc=true, cii=false
```

Gap analysis (`docs/.ciso-work/gap-analysis.md`):
```markdown
## Mandatory Gaps

- Priority 1: PR.AA.G1 -> GAP (access review frequency undefined)
- Priority 2: PR.AA.G2 -> NEEDS_REVIEW (PIM process evidence pending)
```

Policy with traceability (`docs/policies/access-control.md`):
```markdown
## Traceability Matrix

| Section | CSCRF Ref | Control Summary |
|---|---|---|
| Access Governance | PR.AA.G1 | Access right lifecycle and periodic review |
| Privileged Access | PR.AA.G2 | Elevated access governance and monitoring |
```

### I Want To...

| I want to... | Command | Section |
|---|---|---|
| Run a full CSCRF compliance assessment | `/ciso start` | [Full Workflow](#ciso--full-compliance-workflow) |
| Generate a specific policy document | `/ciso-policy access-control qualified` | [Policy Generator](#ciso-policy--targeted-policy-generator) |
| Evaluate an existing policy | `/ciso-assess docs/policy.md qualified` | [Policy Evaluator](#ciso-assess--policy-evaluator) |
| Look up a CSCRF requirement | Ask naturally | [CSCRF Analyst](#cscrf-analyst-agent) |
| Generate all 15 policies at once | `/ciso-policy all mid-size 'Acme Ltd'` | [Policy Generator](#ciso-policy--targeted-policy-generator) |
| Resume a previous session | `/ciso assess` | [Full Workflow](#ciso--full-compliance-workflow) |

### Installation

Requires [Claude Code](https://claude.com/claude-code). Python 3.14+ and [uv](https://docs.astral.sh/uv/) for the entity tag resolver and validation.

**Option A — Clone the repo (recommended):**

```bash
git clone https://github.com/iy3r/sebi-cscrf.git
cd sebi-cscrf
```

**Option B — Upload to Claude.ai:**

```bash
bash scripts/package_skills.sh
# Upload dist/ciso.zip (or ciso-policy.zip, ciso-assess.zip) via:
# Claude.ai → Settings → Capabilities → Skills
```

**Option C — Copy into an existing project:**

```bash
cp -r .claude/skills/ciso .claude/skills/ciso-policy .claude/skills/ciso-assess /your-project/.claude/skills/
cp -r framework/ meta/ /your-project/
```

**Surface compatibility:**

| Surface | Support | Notes |
|---|---|---|
| Claude Code | Full | Task delegation, Bash for scripts |
| Claude.ai | Partial | Inline fallback — no Task delegation or script execution |
| API | Partial | Requires Code Execution Tool beta |

**Verify:** `bash scripts/eval_skills.sh`

### `/ciso` — Full Compliance Workflow

```bash
claude "/ciso start"        # Full interview → assess → generate flow
claude "/ciso assess"       # Jump to gap analysis (profiles first if needed)
claude "/ciso policy"       # Jump to policy generation
claude "/ciso roadmap"      # Generate remediation timeline
```

Four phases: entity profiling → gap analysis → policy generation → 90-day remediation roadmap. Each phase persists artifacts to disk, so you can resume across sessions.

**What you get:**

```
docs/.ciso-work/
├── entity-profile.md       # Interview results
├── entity-tags.json        # Deterministic applicability tags
├── gap-analysis.md         # Gap report with priority rankings
└── roadmap.md              # 90-day phased plan
docs/policies/
├── access-control.md       # Per-area policies with traceability
├── incident-response.md
└── ...
```

The skill checks for existing artifacts before starting each phase — pick up where you left off in a new session.

### `/ciso-policy` — Targeted Policy Generator

```bash
claude "/ciso-policy access-control qualified"                # Single policy
claude "/ciso-policy incident-response mid-size 'Acme Ltd'"   # With entity name
claude "/ciso-policy all qualified 'Example Securities'"      # All 15 policies
```

Each policy includes YAML frontmatter with CSCRF standard/guideline references and a traceability matrix linking every control statement to its source guideline.

<details>
<summary>Policy areas (15)</summary>

| Slug | Title | Key CSCRF Codes |
|---|---|---|
| `cybersecurity-policy` | Cybersecurity Policy | GV.PO, GV.OC, GV.OV |
| `risk-management` | Risk Management | GV.RM, ID.RA |
| `roles-responsibilities` | Roles and Responsibilities | GV.RR |
| `access-control` | Access Control | PR.AA |
| `data-security` | Data Security | PR.DS |
| `information-protection` | Information Protection | PR.IP |
| `maintenance` | Maintenance | PR.MA |
| `training` | Training and Awareness | PR.AT |
| `vendor-management` | Vendor Management | GV.SC |
| `security-monitoring` | Security Monitoring | DE.CM |
| `detection-process` | Detection Process | DE.DP |
| `incident-response` | Incident Response | RS.MA, RS.AN, RS.CO, RS.IM |
| `recovery-planning` | Recovery Planning | RC.RP, RC.CO, RC.IM |
| `resilience-evolution` | Resilience Evolution | EV.ST |
| `asset-management` | Asset Management | ID.AM |

Use slugs, titles, or aliases (defined in `policy-area-map.json`).

</details>

### `/ciso-assess` — Policy Evaluator

```bash
claude "/ciso-assess docs/policies/access-control.md qualified"
claude "/ciso-assess path/to/existing-security-policy.pdf mid-size"
```

Produces a coverage score, critical gaps, weak statements, and prioritized recommendations — all referenced to specific CSCRF guideline IDs.

### `cscrf-analyst` Agent

Lightweight read-only agent for quick CSCRF lookups. Used internally by the skills or directly via the Task tool.

```
"What guidelines apply to a qualified stock broker for access control?"
"What's the VAPT periodicity for mid-size REs?"
"List all mandatory guidelines for self-certification REs"
```

### How It Works

#### Skill Architecture

Three-level progressive disclosure: frontmatter (metadata, compatibility, allowed tools) → SKILL.md body (workflow steps, phase gates, examples) → `references/` (execution details, agent contracts, load matrices, templates).

#### Specialist Agents

Skills delegate analysis to five specialist agents via Task:

| Agent | Role | Used By |
|---|---|---|
| `cscrf-analyst` | CSCRF lookups and spot-checks | `/ciso`, `/ciso-assess` |
| `cscrf-gap-analyst` | Applicability filtering and gap classification | `/ciso` |
| `cscrf-policy-drafter` | Per-area policy drafting with traceability | `/ciso`, `/ciso-policy` |
| `cscrf-reviewer` | QA for mandatory coverage, periodicities | All skills |
| `cscrf-roadmap-planner` | Phased remediation planning | `/ciso` |

#### Context Budget

Skills use `policy-area-map.json` to load only the 3-8 framework files relevant to each policy area instead of bulk-loading all 23.

#### Skills vs. Manual Prompting

| Metric | Without Skill | With Skill |
|---|---|---|
| User interactions | 15-25 messages | 3-5 messages |
| Token usage | 150K-200K | 60K-90K |
| Guideline coverage | Sampling-based | Exhaustive |
| Resumability | None | Full |

See `.claude/skills/ciso/references/baseline-comparison.md` for methodology.

### Validation and Testing

```bash
bash scripts/eval_skills.sh --with-fixtures
```

Testing tiers:
1. `eval_skills.sh` — static consistency (7-step harness)
2. `eval_skills.sh --with-fixtures` — with fixture artifact checks
3. `eval_skills_api.py trigger` — offline trigger matching (53 cases)
4. `eval_skills_api.py functional` — API-based functional tests

<details>
<summary>All validation scripts</summary>

| Script | Purpose |
|--------|---------|
| `scripts/eval_skills.sh` | 7-step validation harness (`--with-artifacts` for strict checks, `--with-fixtures` to install fixtures + strict checks) |
| `scripts/validate_skill_mappings.py` | Canonical policy-area mapping and mirror parity validation |
| `scripts/validate_agent_versions.py` | Agent version compatibility |
| `scripts/resolve_entity_tags.py` | Deterministic entity tag resolver |
| `scripts/validate_trigger_suite.py` | Semantic trigger test suite validation |
| `scripts/validate_skill_functional_contracts.py` | Functional contract manifests |
| `scripts/validate_ciso_outputs.py` | Output contracts (`--strict` for required-artifact mode) |
| `scripts/eval_skills_api.py` | Skills API evaluation: `trigger`, `functional`, `full`, `report` |
| `scripts/verify-ciso-artifacts.sh` | Artifact verification (`--strict` for CI) |
| `scripts/install_ciso_fixtures.sh` | Install deterministic fixture artifacts (`--force` to overwrite) |
| `scripts/package_skills.sh` | Generate `.zip` files for Claude.ai skill upload |

</details>

## Development

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/). See [CLAUDE.md](CLAUDE.md) for full development conventions.

```bash
uv sync                                          # Install deps
bash scripts/eval_skills.sh --with-fixtures      # Run full validation suite
uv run python3 scripts/eval_skills_api.py trigger # Offline trigger tests
```

## Source

[SEBI Circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113](https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html) dated August 20, 2024.

All standard and guideline text is reproduced verbatim from the framework. Nothing is paraphrased or summarised.

## License

MIT — see [LICENSE](LICENSE).

The original CSCRF text is published by SEBI. This repository adds structure and metadata only.
