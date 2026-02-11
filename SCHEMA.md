# CSCRF Schema Reference

Machine-readable structured extraction of SEBI's Cybersecurity and Cyber
Resilience Framework (CSCRF) v1.0 for Regulated Entities (REs) in the
Indian securities market.

## Purpose

This repository provides CSCRF objectives, standards, and guidelines as
structured markdown files with YAML frontmatter. Designed for:

- **RAG / LLM retrieval** — each file is a self-contained, searchable unit
- **Policy authoring** — reference from Typst, LaTeX, or any doc toolchain
- **Compliance tooling** — parse frontmatter to filter by RE type, mandatory status, or standard code
- **Audit preparation** — trace guidelines back to standards and vice versa

---

## Repository Structure

```
cscrf/
├── SCHEMA.md                  ← this file
├── framework/
│   ├── detect/
│   │   ├── de-cm.md           # Security Continuous Monitoring
│   │   └── de-dp.md           # Detection Process
│   ├── evolve/
│   │   └── ev-st.md           # Strategies
│   ├── governance/
│   │   ├── gv-oc.md           # Organizational Context
│   │   ├── gv-ov.md           # Oversight
│   │   ├── gv-po.md           # Policy
│   │   ├── gv-rm.md           # Risk Management
│   │   ├── gv-rr.md           # Roles, Responsibilities and Authorities
│   │   └── gv-sc.md           # Supply Chain Risk Management
│   ├── identify/
│   │   ├── id-am.md           # Asset Management
│   │   └── id-ra.md           # Risk Assessment
│   ├── protect/
│   │   ├── pr-aa.md           # Access Control and Authentication
│   │   ├── pr-at.md           # Awareness and Training
│   │   ├── pr-ds.md           # Data Security
│   │   ├── pr-ip.md           # Information Protection Processes and Procedures
│   │   └── pr-ma.md           # Maintenance
│   ├── recover/
│   │   ├── rc-co.md           # Communication
│   │   ├── rc-im.md           # Improvements
│   │   └── rc-rp.md           # Recovery Planning
│   └── respond/
│       ├── rs-an.md           # Analysis
│       ├── rs-co.md           # Communication
│       ├── rs-im.md           # Improvements
│       └── rs-ma.md           # Incident Management
├── meta/
│   ├── definitions.md         # Glossary (22 terms)
│   ├── abbreviations.md      # Abbreviations (126 entries)
│   ├── it-committee.md       # IT Committee requirements
│   └── compliance.md         # Compliance procedures & timelines
└── docs/
```

Folders map to cybersecurity functions (lowercase). Filenames are the
sub-section code (lowercase, hyphenated).

---

## Goal–Function–Folder Mapping

| Cyber Resilience Goal  | Cybersecurity Function | Folder                    |
|------------------------|----------------------|---------------------------|
| ANTICIPATE             | GOVERNANCE           | `framework/governance/`   |
| ANTICIPATE             | IDENTIFY             | `framework/identify/`     |
| ANTICIPATE             | PROTECT              | `framework/protect/`      |
| ANTICIPATE             | DETECT               | `framework/detect/`       |
| WITHSTAND & CONTAIN    | RESPOND              | `framework/respond/`      |
| RECOVER                | RECOVER              | `framework/recover/`      |
| EVOLVE                 | EVOLVE               | `framework/evolve/`       |

---

## File Schema

Each file has two parts: YAML frontmatter and a markdown body.

### Frontmatter

```yaml
---
code: GV.OC                    # Sub-section code (uppercase, dotted)
title: Organizational Context   # Human-readable title from CSCRF
goal: ANTICIPATE                # Cyber resilience goal (see enum below)
function: GOVERNANCE            # Cybersecurity function (see enum below)
version: "1.0"                 # CSCRF document version
source: CSCRF                  # Always "CSCRF"
objective: >                   # Verbatim objective text from Part I
  The essential concomitants...
standards:                     # Array of standards from Part I
  - id: GV.OC.S1              # Standard ID: {code}.S{n}
    text: >                    # Verbatim standard text
      Critical objectives...
---
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `code` | string | ✓ | Sub-section code, e.g. `GV.OC`, `PR.AA` |
| `title` | string | ✓ | Human-readable title |
| `goal` | enum | ✓ | One of: `ANTICIPATE`, `WITHSTAND & CONTAIN`, `RECOVER`, `EVOLVE` |
| `function` | enum | ✓ | One of: `GOVERNANCE`, `IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND`, `RECOVER`, `EVOLVE` |
| `version` | string | ✓ | CSCRF version (currently `"1.0"`) |
| `source` | string | ✓ | Always `CSCRF` |
| `objective` | string | ✓ | Verbatim from Part I |
| `standards` | array | ✓ | Standards from Part I |
| `standards[].id` | string | ✓ | Pattern: `{code}.S{n}` (sequential) |
| `standards[].text` | string | ✓ | Verbatim standard text |

### Body

The body contains two optional sections: `## Guidelines` and `## Annexure`.

#### Guidelines

Each guideline is a heading with inline metadata and numbered content:

```markdown
## Guidelines

### GV.OC.G1
- **standards:** [GV.OC.S2, GV.OC.S3]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** false

1. First guideline point (verbatim from CSCRF)...
2. Second guideline point...
   a. Sub-point...
   b. Sub-point...
```

| Metadata field | Type | Description |
|----------------|------|-------------|
| `standards` | array of strings | Standard IDs this guideline implements |
| `applicability` | array of strings | RE categories this applies to (see tags below) |
| `mandatory` | boolean | `true` only when CSCRF explicitly states "(Mandatory)" |

**Guideline ID pattern:** `{code}.G{n}` — sequential within each file.

A new guideline ID is created when:
- The applicability changes, OR
- The referenced standards group changes

Multiple numbered points under the same applicability block belong to
one guideline.

#### Annexure

Box Items from the CSCRF appear after guidelines:

```markdown
## Annexure

### Box Item 5: Cyber risk management

Content here (verbatim, italicised where original uses italics)...
```

#### Footnotes

Rendered as blockquotes at the end of the guideline block that
references them:

```markdown
> ²³ Refer 'CSCRF Compliance, Audit Report Submission, and Timelines' section.
```

---

## Applicability Tags

### Canonical Tags (size-based RE classification)

These five tags map directly to the RE categorisation thresholds defined
in CSCRF Section 2.

| Tag | Description |
|-----|-------------|
| `mii` | Market Infrastructure Institutions (Stock Exchanges, Depositories, Clearing Corporations) |
| `qualified` | Qualified REs (meet threshold criteria per CSCRF Section 2) |
| `mid-size` | Mid-size REs |
| `small-size` | Small-size REs |
| `self-certification` | Self-certification REs |

### Conditional Tags

These tags represent applicability based on criteria other than RE size.
They appear infrequently and are flagged with a `⚠️` warning in the
source files.

| Tag | Condition | Used in |
|-----|-----------|---------|
| `cii` | REs identified as Critical Information Infrastructure by NCIIPC | GV.PO.G5 |
| `third-party-soc` | REs using third-party managed SOC or market SOC | DE.CM.G3 |
| `stock-brokers` | Stock Brokers specifically | PR.AA |
| `depository-participants` | Depository Participants specifically | PR.AA |
| `qualified-stock-brokers-dps` | Stock Brokers / DPs falling under Qualified REs | DE.CM.G7 |
| `mid-size-stock-brokers-dps` | Stock Brokers / DPs falling under Mid-size REs | DE.CM.G7 |

### Applicability Mapping from CSCRF Text

| CSCRF text | `applicability` | `mandatory` |
|------------|----------------|-------------|
| "All REs" | `[mii, qualified, mid-size, small-size, self-certification]` | `false` |
| "All REs (Mandatory)" | `[mii, qualified, mid-size, small-size, self-certification]` | `true` |
| "All REs except small-size, self-certification REs" | `[mii, qualified, mid-size]` | `false` |
| "All REs except small-size, Self-certification REs (Mandatory)" | `[mii, qualified, mid-size]` | `true` |
| "MIIs and Qualified REs" | `[mii, qualified]` | `false` |
| "MIIs, Qualified REs (Mandatory)" | `[mii, qualified]` | `true` |
| "MIIs (Mandatory)" | `[mii]` | `true` |
| "Mid-size, small-size, self-certification REs" | `[mid-size, small-size, self-certification]` | `false` |
| "Mid-size, small-size, self-certification REs (Mandatory)" | `[mid-size, small-size, self-certification]` | `true` |
| "All REs which have been identified as CII by NCIIPC" | `[cii]` | `true` |

---

## Querying for Applicability

To determine which guidelines apply to a specific RE, match the RE's
classification tag against the `applicability` array in each guideline.

**Example: Find all mandatory guidelines for a mid-size RE**

```python
# Pseudocode
for file in cscrf_files:
    for guideline in file.guidelines:
        if "mid-size" in guideline.applicability and guideline.mandatory:
            yield guideline
```

**Example: Check if a guideline applies to your organisation**

```python
my_tags = {"mid-size"}  # Set based on your RE classification

def applies_to_me(guideline) -> bool:
    return bool(my_tags & set(guideline.applicability))
```

For REs with conditional tags (e.g., CII designation, third-party SOC
usage), add those tags to `my_tags` as applicable.

---

## ID Conventions

| Entity | Pattern | Example |
|--------|---------|---------|
| Sub-section code | `{FN}.{SS}` | `GV.OC`, `PR.AA` |
| Standard | `{FN}.{SS}.S{n}` | `GV.OC.S1`, `PR.AA.S12` |
| Guideline | `{FN}.{SS}.G{n}` | `GV.OC.G1`, `PR.AA.G15` |

Where `FN` = function abbreviation (2 letters), `SS` = sub-section
abbreviation (2 letters), `n` = sequential integer starting at 1.

Standard IDs (`S{n}`) are assigned by CSCRF. Guideline IDs (`G{n}`)
are assigned during extraction (CSCRF does not number guidelines).

---

## Coverage Summary

| File | Code | Standards | Guidelines | Function |
|------|------|-----------|------------|----------|
| `framework/detect/de-cm.md` | DE.CM | 5 | 7 | DETECT |
| `framework/detect/de-dp.md` | DE.DP | 5 | 2 | DETECT |
| `framework/evolve/ev-st.md` | EV.ST | 5 | 1 | EVOLVE |
| `framework/governance/gv-oc.md` | GV.OC | 3 | 2 | GOVERNANCE |
| `framework/governance/gv-ov.md` | GV.OV | 4 | 1 | GOVERNANCE |
| `framework/governance/gv-po.md` | GV.PO | 5 | 6 | GOVERNANCE |
| `framework/governance/gv-rm.md` | GV.RM | 4 | 2 | GOVERNANCE |
| `framework/governance/gv-rr.md` | GV.RR | 6 | 4 | GOVERNANCE |
| `framework/governance/gv-sc.md` | GV.SC | 8 | 5 | GOVERNANCE |
| `framework/identify/id-am.md` | ID.AM | 6 | 3 | IDENTIFY |
| `framework/identify/id-ra.md` | ID.RA | 5 | 5 | IDENTIFY |
| `framework/protect/pr-aa.md` | PR.AA | 17 | 15 | PROTECT |
| `framework/protect/pr-at.md` | PR.AT | 5 | 2 | PROTECT |
| `framework/protect/pr-ds.md` | PR.DS | 6 | 7 | PROTECT |
| `framework/protect/pr-ip.md` | PR.IP | 17 | 11 | PROTECT |
| `framework/protect/pr-ma.md` | PR.MA | 3 | 3 | PROTECT |
| `framework/recover/rc-co.md` | RC.CO | 3 | 1 | RECOVER |
| `framework/recover/rc-im.md` | RC.IM | 2 | 2 | RECOVER |
| `framework/recover/rc-rp.md` | RC.RP | 4 | 7 | RECOVER |
| `framework/respond/rs-an.md` | RS.AN | 5 | 2 | RESPOND |
| `framework/respond/rs-co.md` | RS.CO | 3 | 3 | RESPOND |
| `framework/respond/rs-im.md` | RS.IM | 2 | 3 | RESPOND |
| `framework/respond/rs-ma.md` | RS.MA | 5 | 3 | RESPOND |
| **Total** | **23 files** | **128** | **97** | — |

Of the 97 guidelines: **80 mandatory**, **17 non-mandatory**.

---

## Text Fidelity Rules

- All standard and guideline text is **verbatim** from CSCRF v1.0
- OCR artifacts (broken words, stray line-break hyphens) are corrected
- Emphasis preserved where CSCRF uses italics (e.g., *critical systems*, *Regulatory Data*)
- Annexure references preserved as-is (e.g., "Annexure-K", "Annexure-E")
- Footnotes use Unicode superscript numerals (e.g., ²³) matching the original

---

## Contributing

When adding or updating extractions:

1. Follow the frontmatter schema exactly — parsers depend on field names and types
2. Use only canonical or documented conditional applicability tags
3. If a new conditional tag is needed, document it in this schema first
4. Preserve CSCRF wording verbatim — do not paraphrase
5. Assign guideline IDs sequentially within each file; do not reuse or skip numbers
6. Flag ambiguous applicability with a `⚠️` blockquote after the guideline
