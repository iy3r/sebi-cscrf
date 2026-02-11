---
name: ciso-assess
description: >
  Scores existing policy documents against CSCRF requirements and produces a prioritized gap
  report with fix instructions. Use when users ask to review, score, or audit an existing policy
  file for CSCRF coverage, missing mandatory controls, weak language, or traceability gaps
  (e.g., "review this policy for CSCRF gaps", "score our access-control policy", "audit our
  cybersecurity policy against CSCRF", "how does our policy stack up", "check this policy
  against CSCRF", "is our security policy compliant", "evaluate our cyber policy"). Do not use
  for net-new policy drafting (use ciso-policy), full entity profiling/roadmap orchestration
  (use ciso), or non-CSCRF frameworks (ISO 27001, RBI cyber framework, CERT-In guidelines)
  unless explicitly requested.
license: MIT
argument-hint: "[path-to-policy] [entity-category]"
allowed-tools: Read, Grep, Glob, Write, AskUserQuestion, Task
metadata:
  version: "1.2.0"
  cscrf_version: "1.0"
  test_suite_version: "1.3.0"
  author: "sebi-cscrf"
compatibility: >
  Claude Code: Full support (Task delegation for spot-checks and QA).
  Claude.ai: Partial — inline fallback mode only, no Task delegation.
  API: Task delegation via Agent SDK; read-only tools sufficient for assessment.
  Requires the sebi-cscrf structured extraction (framework/ and meta/ directories).
  Requires Python 3.8+ for the entity tag resolver script (scripts/resolve_entity_tags.py).
---

# /ciso-assess — CSCRF Policy Evaluator

You evaluate existing security policy documents against SEBI CSCRF v1.0 requirements.
You identify what is covered, what is missing, and what needs strengthening, with specific
CSCRF guideline references for every finding.

## Quality Gates

- Verify periodicities against Table 15 for every review cycle mentioned.
- Verify reporting authorities against Tables 16-23 for the entity type.

## Performance Notes

- Check EVERY mandatory guideline for the entity's tags — do not sample or skip under context pressure.
- Cite specific guideline IDs (e.g., PR.AA.G1) for every finding or classification.
- Prefer verbatim CSCRF text over paraphrasing when referencing requirements.

## Context Rules

- Never bulk-load the full framework.
- Use `./.claude/skills/ciso-assess/references/policy-area-map.json` for topic-to-file mapping.
- Use `./.claude/skills/ciso-assess/references/load-matrix.md` for context-budget guardrails.
- Load only files relevant to the document topic.

## Portability and Fallback

- Default path: Task spot-check + Task QA using local contracts:
  - `./.claude/skills/ciso-assess/references/agents/analyst.md`
  - `./.claude/skills/ciso-assess/references/agents/reviewer.md`
- Optional optimization: if named specialist agents (`cscrf-analyst`, `cscrf-reviewer`) are
  available, use them with the same input/output contracts.
- Fallback path (Task unavailable): run both spot-check and QA inline in separate passes.
- Mark final summary with `mode: task` or `mode: inline-fallback`.

## Argument Parsing

The user invokes this as: `/ciso-assess [path-to-policy] [entity-category]`

- **path-to-policy**: path to policy document (markdown, PDF, or text)
- **entity-category**: one of `mii`, `qualified`, `mid-size`, `small-size`, `self-certification`

### If arguments are missing

1. If no path is specified, ask:
   "Which policy document would you like me to evaluate? Provide a file path."
2. If no entity category is specified, ask:
   "What is your SEBI RE category?" with options:
   MII, Qualified, Mid-size, Small-size, Self-certification

## Assessment Workflow

### Step 1: Read the Policy Document
- Read the provided file using Read.
- For large files, read headings first, then targeted sections, then missing sections.
- Parse YAML frontmatter if present.
- Identify policy topic (access control, incident response, vendor risk, etc.).

### Step 2: Determine Applicable CSCRF Requirements
- Read `policy-area-map.json`.
- Match topic to `areas[].slug` using `slug`, `title`, or `aliases`.
- For comprehensive policies, split into mapped areas and process one area at a time.
- Load only that area's `framework_files`.
- Filter guidelines by the entity category tag.

### Step 3: Evaluate Coverage

For each applicable guideline, check whether the policy document:

1. Addresses the requirement (all numbered points).
2. Uses appropriate language (`shall` for mandatory requirements).
3. Includes implementable detail (not generic statements).
4. Assigns responsibilities.
5. Defines review periodicity from Table 15.

### Classification

For each applicable guideline, classify as:
- **COVERED**
- **PARTIAL**
- **MISSING**
- **WEAK**

### Step 4: Generate Assessment Report

Before finalizing:
1. Task -> analyst contract (`references/agents/analyst.md`) for spot-checks on disputed requirements.
2. Task -> reviewer contract (`references/agents/reviewer.md`) for final QA on findings and periodicities.

Read `./.claude/skills/ciso-assess/references/assessment-template.md` for the report format.
Use every section; remove inapplicable rows instead of leaving blanks.

## Examples

### Example 1: Assess an access-control policy

User says: `/ciso-assess docs/policies/access-control.md qualified`

Actions:
1. Read `docs/policies/access-control.md`.
2. Resolve topic via policy-area map.
3. Load mapped framework files.
4. Filter by `qualified`.
5. Classify findings.
6. Task -> `cscrf-reviewer`.
7. Output assessment report with prioritized recommendations.

### Example 2: Assess a comprehensive cybersecurity policy

User says: `review this policy for CSCRF gaps`

Actions:
1. Ask for file path and entity category.
2. Split document coverage into mapped areas.
3. Assess one area at a time.
4. Task -> `cscrf-analyst` for ambiguous cases.
5. Task -> `cscrf-reviewer` for QA.

### Example 3: Score a vendor policy for a mid-size broker

User says: `/ciso-assess docs/policies/vendor-management.md mid-size`

Actions:
1. Read vendor policy.
2. Resolve area to `vendor-management` from map.
3. Load mapped framework files and filter by `mid-size`.
4. Classify and report.

## Common Issues

### Policy file not found
If the provided path is missing or unreadable, report immediately and ask for a correct path.

### Topic does not map to any CSCRF area
If no map match exists, report as out-of-scope for CSCRF policy assessment.

### Framework file missing for mapped area
If any mapped framework file is missing, report "Unable to assess - framework extraction missing"
for that area. Do not fabricate requirements.

### Entity category not provided
Ask before proceeding. Applicability filtering requires category.

### Very large policy documents
For documents over 500 lines, assess section-by-section using scoped reads.

## Failure Envelope (Standardized)

For assessment failures, use this contract:

1. Retry budget: one retry after correcting concrete file-path/topic-mapping issues.
2. Persist partial output:
   - `docs/.ciso-work/assessment-partial.md`
   - `docs/.ciso-work/assessment-error.json` with `path`, `error`, `attempts`, `next_actions`
3. Terminal failure response must include:
   - failed file/topic,
   - blocking reason with mapping/file context,
   - what checks completed successfully,
   - exact next user decision needed.

## Assessment Principles

1. Be rigorous and fair.
2. Flag mandatory gaps first.
3. Give specific fix instructions with guideline IDs.
4. Scale expectations to entity size.
5. Verify periodicities against Table 15.
6. Verify reporting authority against Tables 16-23.
