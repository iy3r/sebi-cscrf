---
code: RS.AN
title: Incident Analysis
goal: WITHSTAND & CONTAIN
function: RESPOND
version: "1.0"
source: CSCRF
objective: >
  Incident analysis is conducted to ensure effective response and support
  recovery activities.
standards:
  - id: RS.AN.S1
    text: >
      Processes shall be established to receive, analyze and respond to
      vulnerabilities/ incidents disclosed to the RE from internal and external
      sources (e.g. internal testing, security bulletins, or security researchers).
  - id: RS.AN.S2
    text: >
      Cybersecurity incidents shall be categorized in-line with categorization
      given in RE's CCMP.
  - id: RS.AN.S3
    text: >
      Detailed investigation of cybersecurity incidents, and alerts as well as a
      forensic analysis (as appropriate) shall be done to identify the root-cause
      of the incident, the modus operandi of the threat actor, lateral movement
      of the threat actor (if any), and to prevent the reoccurrence of similar
      incidents.
  - id: RS.AN.S4
    text: >
      RCA shall be done to:
      a. Determine the gaps in terms of people, processes, and technology
      that led to the incident, and
      b. Further enhance the RE's security posture to prevent/ mitigate
      similar cybersecurity Incidents in the future.
  - id: RS.AN.S5
    text: >
      Impact analysis of the incident shall be mandatorily conducted by the
      REs. Further, RCA and forensics analysis (as appropriate) shall be
      performed as per 'Classification and Handling of Cybersecurity Incidents'
      SOP attached at Annexure-O.
---

## Guidelines

### RS.AN.G1
- **standards:** [RS.AN.S1, RS.AN.S2, RS.AN.S3]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Alerts generated from monitoring and detection systems shall be suitably investigated by the REs in order to determine activities that are to be performed to prevent spread of cybersecurity incidents/ attacks or breaches, mitigate their effects and resolve the incidents.
2. Data collection: REs shall collect and preserve data related to the incident, such as system logs, network traffic, and forensic images of affected systems.
3. Incident Analysis: REs shall analyse the data to understand the scope, cause, and impact of the incident, including how the incident occurred, what systems and data were affected, who was responsible, etc.
4. Evidence Preservation: REs shall preserve evidence related to the incident, including digital artefacts, network captures, and memory dumps, in a secure and forensically sound manner.

### RS.AN.G2
- **standards:** [RS.AN.S4, RS.AN.S5]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Root Cause Analysis: REs shall perform a root cause analysis (RCA) to identify the specific control that has failed, underlying cause of the incident and the potential areas of improvement.
2. Forensic: Forensic analysis (as appropriate) shall be undertaken by the REs.
3. Any incident of loss or destruction of data or systems shall be thoroughly analysed and lessons learned from such incidents shall be incorporated to strengthen the security mechanisms and improve the recovery planning and processes.
4. Reporting: REs shall create a detailed incident report that includes information on the scope, cause, and impact of the incident, as well as recommendations for improving incident response and recovery capabilities.
5. REs shall conduct a compromise assessment through CERT-In empanelled IS auditing organizations.
