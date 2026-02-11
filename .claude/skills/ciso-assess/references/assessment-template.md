# Assessment Report Template

Use this template for the final output of `/ciso-assess`. Fill in every section;
remove rows that don't apply rather than leaving blanks.

```markdown
## CSCRF Policy Assessment Report

### Document Evaluated
- **File:** [path]
- **Policy Topic:** [identified topic]
- **Entity Category:** [category]
- **Assessment Date:** [today]

### Executive Summary
[2-3 sentences: overall coverage percentage, critical gaps, assessment verdict]

### Coverage Score
| Status | Count | % |
|--------|-------|---|
| COVERED | [n] | [%] |
| PARTIAL | [n] | [%] |
| MISSING | [n] | [%] |
| WEAK | [n] | [%] |
| **Total Applicable** | **[N]** | **100%** |

**Overall Rating:** [Strong / Adequate / Needs Improvement / Insufficient]

### Critical Gaps (Mandatory Guidelines Not Covered)

| # | Guideline | Requirement | Impact |
|---|-----------|-------------|--------|
| 1 | [ID] | [What's required] | [Why this matters — audit/compliance risk] |
...

### Partial Coverage (Needs Strengthening)

| # | Guideline | What's Present | What's Missing |
|---|-----------|----------------|----------------|
| 1 | [ID] | [What the policy says] | [What CSCRF requires but is absent] |
...

### Weak Statements (Too Vague for Compliance)

| # | Policy Statement | Issue | Suggested Revision |
|---|-----------------|-------|-------------------|
| 1 | "[quoted text]" | Too vague / aspirational | "[specific actionable version]" |
...

### Detailed Guideline-by-Guideline Assessment

#### [CSCRF Function: e.g., GOVERNANCE]

| Guideline | Mandatory | Status | Notes |
|-----------|-----------|--------|-------|
| GV.PO.G1 | Yes | COVERED | Sections 2.1, 2.3 address all points |
| GV.PO.G2 | No | PARTIAL | Mobile app policy missing (point 4) |
...

[Repeat for each function]

### Recommendations (Prioritized)

1. **[Priority 1 — Mandatory gaps]:** [Specific action]
2. **[Priority 2 — Partial coverage]:** [Specific action]
3. **[Priority 3 — Weak statements]:** [Specific action]

### Traceability Issues
[Flag any CSCRF references in the policy that are incorrect, outdated, or don't match
the actual guideline content]
```
