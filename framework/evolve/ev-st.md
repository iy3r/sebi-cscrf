---
code: EV.ST
title: Strategies
goal: EVOLVE
function: EVOLVE
version: "1.0"
source: CSCRF
objective: >
  A major component of cyber resilience is the ability to adapt and improve
  the security posture to stay ahead of threats.
standards:
  - id: EV.ST.S1
    text: >
      REs shall formulate strategies to anticipate new attack vectors by
      removing or applying new controls to compensate for identified
      vulnerabilities or weaknesses, reducing or manipulating attack surfaces,
      and proactively orienting controls, practices, and capabilities to
      prospective, emerging, or potential threats.
  - id: EV.ST.S2
    text: >
      REs shall demonstrate heterogeneity to minimize common mode
      failures, particularly threat events exploiting common vulnerabilities.
  - id: EV.ST.S3
    text: >
      REs shall confirm post-incident modification of business functions and
      supporting processes to handle adversity and address environmental
      changes more effectively. In case of a cybersecurity incident, learning
      shall be incorporated to improve and evolve their cyber resilience
      posture.
  - id: EV.ST.S4
    text: >
      MIIs and Qualified REs shall continuously adapt and evolve to counter
      new cybersecurity threats and challenges.
  - id: EV.ST.S5
    text: >
      Mid-size and Small-size REs shall periodically evaluate their cyber
      resilience posture.
---

## Guidelines

### EV.ST.G1
- **standards:** [EV.ST.S1, EV.ST.S2, EV.ST.S3]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** false

1. REs shall anticipate new attack vectors through threat modelling (based on risk assessment) and work to defend them.
2. REs shall strive for reducing their attack surfaces.
3. RE shall proactively examine controls, practices, and capabilities for prospective, emerging or potential threats.
4. RE shall proactively assess and take necessary actions with respect to its system's requirements, architecture, design, configuration, acquisition processes, or operational processes as a strategy for adaptation to the identified and prospective threats and vulnerabilities.
5. RE shall continuously improve upon the ability to quickly deploy and integrate existing and new services, both on-premises and in the cloud.
6. RE shall strive to rapidly correlate data using mathematical models and machine learning in order to make data-driven decisions.
7. REs shall use auditing/logging systems on different OS to acquire and store audit/logging data.
8. In order to include heterogeneity, apply different audit/logging regimes at different architectural layers.
9. REs shall look for feasibility of deploying diverse operating systems. Attack or compromise on one type of OS may not affect other OS deployed.
10. RE shall maintain extra capacity of IT assets for information storage, processing, or communications.
