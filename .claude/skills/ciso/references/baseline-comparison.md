# Baseline Comparison: /ciso Skill vs. Manual Prompting

This document compares the skill-guided workflow against unstructured manual prompting
for SEBI CSCRF compliance tasks, as recommended by "The Complete Guide to Building Skills
for Claude" (January 2026, p.16).

## Methodology

Comparison based on observed behavior patterns across typical CSCRF compliance sessions.
Metrics are representative estimates, not formal benchmarks.

---

## Without Skill (Manual Prompting)

| Metric | Typical Value |
|---|---|
| User interactions to complete full assessment | 15-25 back-and-forth messages |
| Framework files loaded | Often bulk-loaded (`cat framework/**/*.md`), consuming 60-80% of context |
| Applicability tag accuracy | Inconsistent; tags inferred from conversation rather than deterministic script |
| Guideline coverage | Sampling-based; mandatory guidelines frequently missed |
| Periodicity verification | Rarely cross-referenced against Table 15 |
| Reporting authority checks | Often omitted entirely |
| Artifact persistence | None; results lost between sessions |
| Policy traceability | Generic statements without guideline ID references |
| Context budget management | No guardrails; context overflow on large entity scans |
| Estimated token usage (full journey) | 150K-200K+ tokens |

### Common failure modes (without skill)

1. Context exhaustion from loading entire framework at once
2. Applicability tags guessed incorrectly (e.g., conditional tags like `cii` missed)
3. Gap analysis limited to well-known areas; niche CSCRF requirements overlooked
4. No phase gating — errors compound across profiling, assessment, and policy steps
5. Policies contain generic boilerplate instead of CSCRF-traceable statements
6. No resumption capability; restarting requires full re-interview

---

## With Skill (/ciso)

| Metric | Typical Value |
|---|---|
| User interactions to complete full assessment | 3-5 (interview questions only) |
| Framework files loaded | Selective via policy-area-map; typically 3-8 files per area |
| Applicability tag accuracy | Deterministic via `resolve_entity_tags.py` script |
| Guideline coverage | Exhaustive; every mandatory guideline checked per quality gates |
| Periodicity verification | Mandatory cross-reference against Table 15 for every cycle |
| Reporting authority checks | Mandatory cross-reference against Tables 16-23 |
| Artifact persistence | Full artifact contract in `docs/.ciso-work/` |
| Policy traceability | Every statement traces to specific guideline ID |
| Context budget management | Load-matrix enforced; never exceeds budget |
| Estimated token usage (full journey) | 60K-90K tokens |

### Failure modes prevented by skill

1. **Context overflow** — load-matrix and policy-area-map enforce selective loading
2. **Tag inference errors** — deterministic Python script replaces LLM guessing
3. **Coverage gaps** — quality gates require exhaustive guideline checking
4. **Compounding errors** — phase gates (P1 -> P2 -> P3 -> P4) with explicit verification
5. **Boilerplate policies** — anti-boilerplate rules in policy-templates.md
6. **Session loss** — artifact contract enables cross-session resumption

---

## Improvement Summary

| Dimension | Without Skill | With Skill | Improvement |
|---|---|---|---|
| User interactions | 15-25 | 3-5 | ~80% reduction |
| Token usage | 150K-200K | 60K-90K | ~55% reduction |
| Tag accuracy | Variable | Deterministic | Eliminates inference errors |
| Guideline coverage | Partial | Exhaustive | Eliminates coverage gaps |
| Resumability | None | Full | Enables multi-session workflows |
| Quality assurance | None | Phase-gated + reviewer | Catches errors before delivery |
