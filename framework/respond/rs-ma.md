---
code: RS.MA
title: Incident Management
goal: WITHSTAND & CONTAIN
function: RESPOND
version: "1.0"
source: CSCRF
objective: >
  Incident response plans and procedures are executed and maintained in
  order to ensure response to detected/ known cybersecurity incidents.
standards:
  - id: RS.MA.S1
    text: >
      A comprehensive CCMP shall be documented with scenario-based
      SOP. Further, incident response management plan shall also be a part
      of CCMP. Additionally, response plan and execution of required SOP
      shall be triggered as soon as an incident occurs.
  - id: RS.MA.S2
    text: >
      REs shall optimize their ability to respond in a timely and appropriate
      manner to adverse conditions, stresses, attacks, or indicators of these.
      This will maximize the REs' ability to maintain business operations, limit
      consequences, and avoid destabilization.
  - id: RS.MA.S3
    text: >
      REs shall prepare contingency plans, COOP, training, exercises, and
      incident response and recovery plans for their systems and infrastructure
      and get them approved from their respective Board/ Partners/ Proprietor.
  - id: RS.MA.S4
    text: >
      Cybersecurity incidents shall be contained and mitigated. Further, newly
      identified vulnerabilities shall be mitigated or documented as accepted
      risks.
  - id: RS.MA.S5
    text: >
      MIIs and Qualified REs shall get onboarded to CSK (Cyber Swachhta
      Kendra) and other CERT-In initiatives as notified from time to time.
---

## Guidelines

### RS.MA.G1
- **standards:** [RS.MA.S1]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. All REs shall formulate an up-to-date CCMP in line with national CCMP of CERT-In.
2. CCMP shall be approved by Board/ Partners/ Proprietor of REs.
3. Incident Response Management
   a. All REs shall develop an Incident Response Management Plan as part of their CCMP.
   b. The response plan shall define responsibilities and actions to be performed by its employees and support/ outsourced staff in the event of a cyber-attack or cybersecurity incident.
   c. REs shall have a SOP for handling cybersecurity incident response and recovery for the various cybersecurity attacks.
   d. MIIs shall have a SOP for cybersecurity incidents reported to them by the REs under their supervision.
   e. SOP for reporting of cybersecurity incidents to SEBI is attached at Annexure-O. The same shall be adhered to.

### RS.MA.G2
- **standards:** [RS.MA.S2]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** false

1. In order to optimize the REs' ability to respond in a timely and appropriate manner, REs shall:
   a. Create cybersecurity awareness,
   b. Provide cybersecurity training to the relevant teams,
   c. Develop/ hire people with appropriate skill-sets,
   d. Prepare cyber playbooks,
   e. Create knowledge database for all known adverse conditions and attacks

### RS.MA.G3
- **standards:** [RS.MA.S5]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall collaborate with Cyber Swachhta Kendra (CSK) operated by CERT-In to trace bots and vulnerable service(s) running on their public IP addresses, and receive alerts regarding the same. The alerts received from CSK shall be closed in a time-bound manner. Observations (from CSK) which require a longer time to close shall be put up to the *IT Committee for REs* for their guidance and appropriate mitigation/ closure.

## Annexure

### Box Item 12: Cybersecurity Incidents – Classification and Response

CSCRF has classified cybersecurity incidents into four categories:

1. Low severity
2. Medium severity
3. High severity
4. Critical severity

Cybersecurity incident response process can be divided into several phases. Cyber incident response handling can be divided into four broad phases:

1. **Preparation:** This phase covers not only establishment of incident response capabilities to ensure RE's readiness to respond to incidents but also prevention of incidents by having secure systems, networks, and applications. CSCRF has mandated REs to have an effective policy, response plan/strategy, communication, and documentation.
2. **Detection and Analysis:** Detection and analysis phase involves:
   i. Collection of data and logs
   ii. Identification of IOAs
   iii. Identifying a baseline for normal behavior, and
   iv. Correlating events to check deviation in behavior.
3. **Containment, Eradication & Recovery:** The objective of containment is to mitigate the incident before it overwhelms RE's resources and causes more damage. In eradication and recovery phase, all affected systems shall be isolated from the RE's network. Once the affected systems have been isolated, remediation steps should be taken to resume normal operations.
4. **Post-incident activity:** Lessons learned should be shared within the organization to improve the RE's security measures and incident handling process.

CSCRF covers aforementioned incident handling process through various standards and guidelines, and ensures that REs become more cyber resilient and provide a better response to cybersecurity incidents. Further, timelines for handling cyber incidents and report submission have also been provided in this framework.
