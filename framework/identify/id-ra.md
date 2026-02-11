---
code: ID.RA
title: Risk Assessment
goal: ANTICIPATE
function: IDENTIFY
version: "1.0"
source: CSCRF
objective: >
  The cybersecurity risk to the organization, assets, and individuals is
  assessed and understood by the RE.
standards:
  - id: ID.RA.S1
    text: >
      Asset vulnerabilities shall be identified, validated and documented. Risk
      factors shall be assessed and managed for all IT assets of the REs.
  - id: ID.RA.S2
    text: >
      Risk assessment (including post-quantum risks¹⁸) of REs' IT environment
      shall be done on a periodic basis.
  - id: ID.RA.S3
    text: >
      REs shall receive CTI from reliable/ trusted information forums and
      sources. REs shall be on-boarded to CERT-In Intelligence platform to
      receive the advisories for necessary action and implementation.
      Advisories issued by CERT-In/ CSIRT-Fin shall be implemented in a
      timely manner¹⁹.
  - id: ID.RA.S4
    text: >
      Threats, vulnerabilities, their likelihoods, and impacts shall be used to
      understand inherent risk and develop risk response prioritization.
      Vulnerabilities and cyber threats, especially related to access and
      authentication, along with their likelihood and potential business
      impacts, shall be identified and documented.
  - id: ID.RA.S5
    text: >
      Risk responses shall be chosen, prioritized, planned, tracked, and
      communicated.
---

## Guidelines

### ID.RA.G1
- **standards:** [ID.RA.S1, ID.RA.S2]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. REs shall conduct a risk assessment (including post-quantum risks) of the IT
   environment of their organization on a half-yearly (for MIIs) and yearly (for qualified and
   mid-size REs) basis to acquire visibility and a reasonably accurate assessment of the
   overall cybersecurity risk posture. The above-mentioned risk assessment shall be
   utilized by the RE to develop a quantifiable cybersecurity risk score.
2. REs shall accordingly identify cyber risks²⁶ that they may face, along with the likelihood
   of associated threats and their impact on their business, and deploy controls
   commensurate to their criticality.
3. Risk Assessment shall include (but not limited to):
   a. Technology stack and solutions used
   b. Known vulnerabilities
   c. Dependence on third-party service providers
   d. Data storage, security and privacy protection
   e. Threats, likelihoods and associated risks

> ²⁶ Refer Definitions section for the Risk definition.

### ID.RA.G2
- **standards:** [ID.RA.S3]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall engage Dark web monitoring (for brand intelligence, customer protection,
   etc.), and takedown services as a cyber-defence strategy to check for any brand abuse,
   data/credentials leak, combating cyber abuse etc.
2. REs shall subscribe to anti-phishing/ anti-rogue app services to mitigate potential
   phishing or impersonation attacks.
3. REs shall devise SOPs to implement the advisories issued by CERT-In, NCIIPC or
   any other government agency in their IT environment within a defined timeframe.
4. REs shall have processes in place to manage and incorporate IOAs/ IOCs/ malware
   alerts/ vulnerability alerts (received from CERT-In or NCIIPC (as applicable) or any other
   government agencies) in their systems.
5. REs shall be onboarded to CERT-In intelligence platform to receive the advisories for
   necessary action and implementation.

### ID.RA.G3
- **standards:** [ID.RA.S3]
- **applicability:** [mii]
- **mandatory:** true

6. MIIs shall get onboarded to NCCC to generate necessary situational awareness of
   existing and potential cybersecurity threats, and enable timely information sharing for
   taking proactive, preventive, and protective actions by individual entities.

### ID.RA.G4
- **standards:** [ID.RA.S4]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Measures against Phishing websites and attacks
   a. REs need to proactively monitor the cyberspace to identify phishing websites w.r.t.
      REs' domains and report the same to CSIRT-Fin/CERT-In for taking appropriate
      action.

### ID.RA.G5
- **standards:** [ID.RA.S4]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** false

2. Risk assessment of authentication-based solutions shall be implemented to get insights
   about context behind every login. Further, when a user attempts to sign-in, risk-based
   authentication solution shall analyse factors such as device, location, network,
   sensitivity, etc.

## Annexure

### Box Item 7: Cybersecurity and Quantum Computing

*Quantum Computers can efficiently break the asymmetric cryptographic systems which may jeopardize the security of transactions and expose sensitive data. Further, the symmetric cryptography may also require larger key sizes to remain secure. In view of the above, this may potentially be a major cybersecurity risk in the coming decade for the financial sector and for the REs.*

*To mitigate these risks, REs shall focus on the following indicative measures:*

1. *REs shall maintain an inventory of cryptographic assets, prioritizing critical assets for Post Quantum Cryptography (PQC) migration, and assess their IT infrastructure capabilities.*
2. *REs shall develop strategies for the protection of assets which can and cannot be migrated to PQC.*
3. *REs shall upgrade employees' skills, periodically revise policies and conduct proof-of-concept trials in order to prepare themselves for cybersecurity challenges arising from quantum computing.*
4. *REs shall explore the feasibility to adopt PQC and technologies like Quantum Key Distribution (QKD).*
5. *REs shall monitor ongoing quantum computing developments for cybersecurity threats, and ensure that senior management and relevant third-party service providers are aware of the possible risks associated with this technology.*
6. *REs shall enhance their crypto-agility to ensure a seamless transition to quantum-resistant solutions without disrupting their current IT systems.*

> ¹⁸ Quantum computing is a rapidly emerging technology that exploits quantum mechanics' laws to solve complex problems. Post-quantum cryptography solutions can avert post-quantum risks and provide protection against quantum attacks.

> ¹⁹ Within 24 hours of receiving or as indicated by SEBI.
