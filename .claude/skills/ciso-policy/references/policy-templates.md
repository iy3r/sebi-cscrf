# Policy Templates — Generation Rules & Anti-Boilerplate Guide

## Policy Document Format

Every generated policy MUST follow this exact structure:

```markdown
---
title: "[Policy Title]"
entity: "[Entity Name]"
category: "[mii | qualified | mid-size | small-size | self-certification]"
cscrf_version: "1.0"
cscrf_standards: [LIST OF STANDARD IDS]
cscrf_guidelines: [LIST OF GUIDELINE IDS]
generated_date: "[YYYY-MM-DD]"
review_cycle: "[From Table 15]"
---

# [Policy Title]

## 1. Purpose
[1-2 sentences. What this policy achieves. Reference CSCRF objective.]

## 2. Scope
[Specific to entity's tech stack and operations. Name actual systems/services.]

## 3. Policy Statements

### 3.1 [Topic from Guideline Group 1]
**CSCRF Ref:** [Guideline ID]
**Requirement:** [mandatory/recommended]

[Imperative, actionable statements. Use "shall" for mandatory, "should" for recommended.]

### 3.2 [Topic from Guideline Group 2]
...

## 4. Roles and Responsibilities

| Role | Responsibility | CSCRF Ref |
|------|---------------|-----------|
| [Role] | [Specific duty] | [Guideline ID] |
...

## 5. Implementation Procedures
[Only if the policy area requires specific technical steps. Skip for governance-only policies.]

## 6. Review and Update
- Review cycle: [From Table 15 in compliance.md]
- Approved by: [Board / IT Committee / CISO — per CSCRF requirements]
- Next review due: [Date based on cycle]

## 7. CSCRF Traceability Matrix

| CSCRF Standard | Requirement | Policy Section | Status |
|---------------|-------------|----------------|--------|
| [Standard ID] | [Brief text] | Section [n] | Addressed |
...
```

## Anti-Boilerplate Rules

These rules are MANDATORY. Violating them produces useless output.

### DO:
1. **Use the entity's actual tech stack.** If they said "AWS", write "AWS S3 buckets" not "storage systems". If they said "on-premise", reference "on-premise servers and network infrastructure".
2. **Name specific roles.** If entity has 1-3 people, the CISO might be the MD/CEO. Say so. Don't pretend they have a 50-person security team.
3. **Reference specific CSCRF guideline IDs** in every policy statement. The point is traceability.
4. **Scale appropriately.** A self-certification RE with 2 people doesn't need a 3-tier approval workflow.
5. **Use the numbered points from CSCRF guidelines** as the basis for policy statements. The framework already tells you what to require.
6. **Include actual periodicities from Table 15** — don't say "periodic review" when CSCRF says "annually" or "half-yearly".
7. **Be specific about reporting authority** — stock brokers report to exchanges, DPs to depositories, others to SEBI directly (Tables 16-23 in compliance.md).

### DO NOT:
1. **No "for the purposes of this policy" preamble paragraphs.** Get to the requirements.
2. **No redefining terms that are in meta/definitions.md.** Reference the glossary instead.
3. **No generic "information assets" when you know the entity's tech stack.**
4. **No aspirational language.** Not "strive to maintain" — either "shall maintain" (mandatory) or "should maintain" (recommended).
5. **No duplicating requirements across policies.** If access control is covered in the access control policy, don't repeat it in the cybersecurity policy. Cross-reference instead.
6. **No inventing requirements.** Every policy statement must trace to a CSCRF guideline. If CSCRF doesn't require it, don't add it.
7. **No "industry best practices" hand-waving.** Either cite the specific practice or skip it.
8. **No appendices full of templates/forms.** The policy is the deliverable, not a template library.

## Word Count Targets

| Entity Category | Per Policy | Total (all policies) |
|----------------|-----------|---------------------|
| Self-certification | 500-800 words | 3,000-5,000 |
| Small-size | 800-1,500 words | 5,000-10,000 |
| Mid-size | 1,500-2,500 words | 10,000-20,000 |
| Qualified | 2,500-4,000 words | 20,000-35,000 |
| MII | 4,000-8,000 words | 35,000-60,000 |

These are targets, not hard limits. A short, complete policy beats a long, padded one.

## Policy Area Routing Source

Use `./.claude/skills/ciso-policy/references/policy-area-map.json` as the canonical policy-area source.
Do not duplicate area-to-file or area-to-subsection mapping in this file.

Drafting flow for each requested area:
1. Resolve area slug/title/aliases from `policy-area-map.json`.
2. Load only `framework_files` for that area.
3. Build policy statements and traceability from the loaded framework files.

## Example: Minimal Access Control Policy (Small-size RE)

This is what good looks like for a small entity:

```markdown
---
title: "Access Control Policy"
entity: "Example Securities Ltd"
category: "small-size"
cscrf_version: "1.0"
cscrf_standards: [PR.AA.S1, PR.AA.S3, PR.AA.S5, PR.AA.S8, PR.AA.S9, PR.AA.S11, PR.AA.S15]
cscrf_guidelines: [PR.AA.G1, PR.AA.G5, PR.AA.G7, PR.AA.G8, PR.AA.G10]
generated_date: "2026-02-13"
review_cycle: "Half-yearly (Table 15, items 7-8)"
---

# Access Control Policy

## 1. Purpose
Establish access control requirements for all IT systems per SEBI CSCRF PR.AA standards,
ensuring least privilege and accountability for all user access.

## 2. Scope
All trading terminals, back-office systems, client-facing web applications, and cloud
services (AWS) used by Example Securities Ltd. Covers all employees (12 staff), vendor
accounts, and API integrations.

## 3. Policy Statements

### 3.1 Access Provisioning
**CSCRF Ref:** PR.AA.G1
**Requirement:** Mandatory

1. All user access shall be provisioned based on documented approval from the reporting
   manager and validated by the CISO (MD in our case).
2. Access rights shall follow the principle of least privilege — users get only the
   minimum access needed for their role.
3. A documented access control matrix shall be maintained mapping each role to permitted
   systems and access levels.

### 3.2 Privileged Access
**CSCRF Ref:** PR.AA.G5
**Requirement:** Mandatory

1. Administrative/root access shall be restricted to the designated system administrator
   and CISO only.
2. All privileged access usage shall be logged and reviewed half-yearly (per Table 15).
3. Privileged credentials shall not be shared. Each admin shall have individual named accounts.

...
```

Notice: specific entity name, actual team size, real tech stack, every statement has a CSCRF ref,
no filler. This is the standard.
