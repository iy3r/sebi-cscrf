# Interview Flow — Entity Profiling Logic

This document defines the question bank, branching logic, and applicability tag resolution
for the `/ciso` entity profiling interview.

## Entity Type → Conditional Tag Mapping

| Entity Type | Possible Conditional Tags | Follow-up Questions |
|-------------|--------------------------|---------------------|
| Stock Broker | `stock-brokers`, `qualified-stock-brokers-dps`, `mid-size-stock-brokers-dps` | IBT/algo trading? |
| Depository Participant | `depository-participants`, `qualified-stock-brokers-dps`, `mid-size-stock-brokers-dps` | — |
| Mutual Fund / AMC | — | Existing Technology Committee? |
| Clearing Corporation | — (typically MII) | — |
| Stock Exchange | — (MII) | — |
| Depository | — (MII) | — |
| Other | Depends on classification | — |

## RE Category Determination

If the user selects "Not sure", help them determine their category using CSCRF Section 2 thresholds:

### MII Criteria
Entities that ARE MIIs (no threshold — by designation):
- Stock Exchanges (NSE, BSE, MSEI, etc.)
- Depositories (NSDL, CDSL)
- Clearing Corporations (NSCCL, ICCL, etc.)

### Qualified RE Criteria
An RE is "Qualified" if it meets ANY of these thresholds (varies by entity type):

**Stock Brokers:**
- Active clients >= 10 lakh, OR
- Trading volume >= Rs. 50,000 crore (across segments, per financial year)

**Depository Participants:**
- Active demat accounts >= 10 lakh

**Mutual Funds / AMCs:**
- AUM >= Rs. 1 lakh crore

**Other REs:**
- If unsure, ask the user to check with their SRO (Self-Regulatory Organization)

### Mid-size RE Criteria
Below Qualified thresholds but above Self-certification thresholds. Specific numbers
vary by entity type — refer user to SEBI circulars for their category.

### Small-size RE
Below Mid-size thresholds but not eligible for Self-certification.

### Self-certification RE
The smallest category — minimal thresholds, simplified compliance requirements.

## Applicability Tag Resolution

Do not re-implement tag logic inline. Use the deterministic resolver script:

```bash
uv run python3 scripts/resolve_entity_tags.py --profile docs/.ciso-work/entity-profile.json --pretty
```

Expected output shape:

```json
{
  "entity_type": "stock-broker",
  "category": "mid-size",
  "tags": ["mid-size", "mid-size-stock-brokers-dps", "stock-brokers", "third-party-soc"]
}
```

Write `tags` into `docs/.ciso-work/entity-tags.json` and use that output as the canonical input
for downstream gap analysis and policy generation.

## Guideline Count by Category

Quick reference for expected guideline counts (from SCHEMA.md coverage summary):

| Category | Total Applicable | Mandatory | Non-Mandatory |
|----------|-----------------|-----------|---------------|
| MII | 97 | 80 | 17 |
| Qualified | ~85 | ~70 | ~15 |
| Mid-size | ~70 | ~55 | ~15 |
| Small-size | ~55 | ~35 | ~20 |
| Self-certification | ~45 | ~30 | ~15 |

Note: Exact counts depend on conditional tags. These are approximate baselines.

## Existing Controls → Guideline Mapping

Map the user's stated existing controls to CSCRF guidelines for gap classification:

| Existing Control | Covers Guidelines |
|-----------------|-------------------|
| Board-approved cybersecurity policy | GV.PO.G1 (partially) |
| Designated CISO / security officer | GV.RR.G2 |
| SOC (in-house) | DE.CM.G1, DE.CM.G2 |
| SOC (third-party/Market SOC) | DE.CM.G1, DE.CM.G3 |
| ISO 27001 certification | PR.IP.G9 (partially) |
| Regular VAPT | DE.CM.G5, DE.CM.G6 |
| Incident response plan | RS.MA.G1 (partially) |
| IT asset inventory | ID.AM.G1 |
| DR/BCP plan tested | RC.RP.G1, RC.RP.G3 |
| Cybersecurity training program | PR.AT.G1 |
| Network segmentation | PR.IP.G3 (partially) |
| Privileged access management | PR.AA.G5 (partially) |

**Important:** A stated existing control marks the guideline as NEEDS REVIEW, not COMPLIANT.
Only classify as COMPLIANT if the control clearly addresses ALL numbered points in the
guideline. When in doubt, mark NEEDS REVIEW.

## Adapting Questions Based on Responses

### If entity is MII:
- Skip question about Market SOC (MIIs run it, not use it)
- Skip RE category question (always MII)
- Add question: "Do you operate a Market SOC for other REs?"

### If entity is Self-certification:
- Simplify existing controls checklist (remove SOC, ISO 27001 — not applicable)
- Skip CII question (extremely unlikely for self-cert)
- Add question: "Are you a newly registered entity or existing?"

### If entity is Mutual Fund / AMC:
- Ask about existing Technology Committee (per SEBI/HO/IMD/DF2/CIR/P/2019/058)
- Note that MF/AMCs report directly to SEBI, not through exchanges
- Reference the special IT Committee note from CSCRF Section 3.2

### If user mentions "not sure" about any control:
- Default to GAP for that area
- Add a note in the gap analysis suggesting verification
