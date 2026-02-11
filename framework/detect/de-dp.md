---
code: DE.DP
title: Detection Process
goal: ANTICIPATE
function: DETECT
version: "1.0"
source: CSCRF
objective: >
  Detection processes and procedures are maintained and tested to ensure
  awareness of anomalous events.
standards:
  - id: DE.DP.S1
    text: >
      Roles and responsibilities for detection are defined to ensure
      accountability.
  - id: DE.DP.S2
    text: >
      REs shall ensure that detection processes are tested by developing
      playbooks and use-cases.
  - id: DE.DP.S3
    text: >
      Event detection information shall be communicated as per the regulatory
      requirements and organizational policies.
  - id: DE.DP.S4
    text: >
      MIIs and Qualified REs shall conduct goal-based adversarial simulation
      red teaming exercise on a periodic basis to identify potential weaknesses
      within the organization's cyber defense.
  - id: DE.DP.S5
    text: >
      REs shall conduct threat hunting and compromise assessment on a
      regular basis.
---

## Guidelines

### DE.DP.G1
- **standards:** [DE.DP.S4]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall conduct red teaming exercises as part of their cybersecurity framework on a half-yearly basis through use of red/ blue teams.
2. CART solution shall be deployed for continuous, automated process of testing the security of the systems, and achieving greater visibility on attack surfaces.
3. For red teaming exercise, a red team may consist of REs employees and/ or outside experts. Additionally, the red team shall be independent of the function being tested.
4. The results of the red teaming exercise shall be placed before *IT Committee for REs* and Governing board. The lessons learned from conducting such red team exercises shall be shared with SEBI within 3 months after completion of the exercise. Status of the remediation of the observation found during the red team exercise shall be monitored by *IT Committee for REs*.

### DE.DP.G2
- **standards:** [DE.DP.S5]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall proactively search for hidden and undetected cyber threats in their network.
2. Threat hunting by leveraging threat intelligence, IOCs, IOAs, etc. shall be conducted on a quarterly basis.
