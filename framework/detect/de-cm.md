---
code: DE.CM
title: Security Continuous Monitoring
goal: ANTICIPATE
function: DETECT
version: "1.0"
source: CSCRF
objective: >
  The REs' information systems and assets are monitored to identify
  cybersecurity events and verify the effectiveness of protective measures.
standards:
  - id: DE.CM.S1
    text: >
      The SOC shall cover (including but not limited to) network, endpoints,
      physical environment, personnel activities, malicious code,
      unauthorized mobile code, activities of third-party service providers,
      monitoring of unauthorized personnel, devices, connections and
      software, etc. Security Operations Centre (SOC) shall be up and
      running 24×7×365 to monitor, prevent, predict, detect, investigate,
      and respond to cyber threats.
  - id: DE.CM.S2
    text: >
      Appropriate continuous security monitoring mechanisms shall be
      established in SOC for the timely detection of anomalous or malicious
      activities.
  - id: DE.CM.S3
    text: >
      All anomalies and alerts generated shall be properly monitored and
      investigated within stipulated time.
  - id: DE.CM.S4
    text: >
      Capacity utilization shall be monitored for all the *critical systems*
      in the organization.
  - id: DE.CM.S5
    text: >
      Cybersecurity audit, configuration audit, implementation audit, change
      management audit, and VAPT shall be conducted to detect
      vulnerabilities in IT environment.
---

## Guidelines

### DE.CM.G1
- **standards:** [DE.CM.S1, DE.CM.S2, DE.CM.S3]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Security Continuous Monitoring
   a. REs shall establish appropriate security monitoring systems and processes to facilitate continuous monitoring of security events/ alerts and timely detection of unauthorized or malicious activities, unauthorized changes, unauthorized access and unauthorized copying and transmission of data/ information held in contractual or fiduciary capacity, by internal and external parties. The security logs of systems, applications and network devices exposed to the internet shall also be monitored for anomalies.
   b. Suitable alerts shall be generated in the event of detection of unauthorized or abnormal system activities, transmission errors or unusual online transactions.
   c. To enhance the security monitoring, REs (except client-based stock brokers having less than 100 clients) are mandated to employ SOC services for their systems. REs may choose any of the following models to use SOC services:
      i. RE's own SOC/ group SOC
      ii. Market SOC implemented mandatorily by NSE, BSE and optionally by NSDL and/ or CDSL
      iii. Any other third party managed SOC
   d. Small-Size and Self-certification category REs are mandated to be on-boarded on above-mentioned Market SOC.

### DE.CM.G2
- **standards:** [DE.CM.S1, DE.CM.S2, DE.CM.S3]
- **applicability:** [mii, qualified]
- **mandatory:** true

2. Functional efficacy of SOC
   a. REs shall measure functional efficacy of their SOC using the quantifiable method given in **Annexure-N**.
   b. REs shall review the functional efficacy of SOC on a half-yearly basis.
   c. REs shall deploy solutions such as BAS, CART, decoy, vulnerability management, etc. to enhance their cybersecurity posture.

### DE.CM.G3
- **standards:** [DE.CM.S1, DE.CM.S2, DE.CM.S3]
- **applicability:** [third-party-soc]
- **mandatory:** true

   d. Those REs who are utilizing third-party managed SOC services or market SOC shall obtain SOC efficacy report (using the quantifiable method given in **Annexure-N**) from their SOC provider on a yearly basis.

> ⚠️ **Non-standard applicability:** "All REs having third-party managed SOC or market SOC" — this is a conditional tag based on SOC model, not RE size category.

### DE.CM.G4
- **standards:** [DE.CM.S1, DE.CM.S2, DE.CM.S3]
- **applicability:** [mii]
- **mandatory:** true

3. MIIs shall have a cybersecurity Operations Centre (C-SOC) that would be a 24×7×365 set-up manned by dedicated security analysts to identify, respond, recover and protect from cybersecurity incidents²⁸. The C-SOC for MIIs shall function in accordance with SEBI circular CIR/MRD/CSC/148/2018 dated December 07, 2018 which has been attached at **Annexure-M**.

> ²⁸ Refer SEBI circular CIR/MRD/CSC/148/2018 dated December 07, 2018.

### DE.CM.G5
- **standards:** [DE.CM.S4]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. The use of IT assets/ resources shall be monitored, tuned and projections shall be made for future capacity requirements to ensure the required system performance for meeting the business objectives.
2. To ensure high resilience, high availability and timely detection of attacks on systems and networks, REs shall implement suitable mechanisms to monitor capacity utilization of its *critical systems* and networks.
3. Capacity management shall comprise of three primary types; Data storage capacity – (e.g. in database systems, file storage areas, etc.); Processing power capacity – (e.g. adequate computational power to ensure timely processing operations); and Communications capacity – ("bandwidth" to ensure communications are made in a timely manner).
4. Capacity management shall be;
   a. Pro-active – for example, using capacity considerations as part of change management;
   b. Reactive – e.g. triggers and alerts for when capacity usage is reaching a critical threshold so that timely increments (temporary or permanent) can be made.

### DE.CM.G6
- **standards:** [DE.CM.S5]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. The details of periodicity, timeline and report submission for cyber audit by REs have been provided in the *'CSCRF Compliance, Audit Report Submission, and Timelines'* section.
2. REs shall regularly conduct cybersecurity audit and VAPT with scope as mentioned in CSCRF in order to detect vulnerabilities in the IT environment. Further, REs shall conduct in-depth evaluation of the security posture of the system through simulations of actual attacks. An indicative (but not exhaustive and limited to) VAPT scope has been attached at **Annexure-L**.
3. The assets under these audits shall include (but not limited to) all *critical systems*, infrastructure components (like networking systems, security devices, load balancers, servers, databases, applications, remote access points, systems accessible through WAN, LAN as well as with Public IP's, websites, etc.), and other IT systems pertaining to the operations of REs.
4. REs shall perform VAPT prior to the commissioning of new systems, especially those which are part of *critical systems* or connected to *critical systems*.
5. Revalidation of VAPT post closure of observations shall be done in a time bound manner to ensure that all the open vulnerabilities have been fixed.

### DE.CM.G7
- **standards:** [DE.CM.S5]
- **applicability:** [qualified-stock-brokers-dps, mid-size-stock-brokers-dps]
- **mandatory:** true

6. In case of vulnerabilities being discovered in COTS (used for core business) or empanelled applications, REs shall report them to the vendors and the designated stock exchanges and/ or depositories in a timely manner.

> ⚠️ **Non-standard applicability:** "Stock Brokers/ Depository Participants falling under Qualified REs and Mid-size REs" — this is a conditional tag scoped to specific RE types within size categories.

## Annexure

### Box Item 11: Security Operations Centre (SOC) and Market SOC

*The key functions performed by SOC are as follows:*

1. **Continuous monitoring:** To monitor the end-points and network round the clock to immediately notify of abnormal or suspicious behavior.
2. **Log management:** To collect, maintain, and review logs of all end-points and network activities. Further, SOC aggregates and correlates data from various applications, firewalls, OS and endpoints to establish a baseline for normal behavior.
3. **Threat response:** To act as a first responder during a cybersecurity incident. Captive SOC is responsible to perform actions like isolating endpoints and limiting the damage with as little disruption of the business as possible. For all forms of managed SOC, the service provider shall alert the RE and guide them in incident management.
4. **Alert Management:** To monitor alerts issued by diverse tools and closely inspect each one of them in order to discard false positives (if any), and determine the potential impact of threats.
5. **Root Cause Investigation:** Post the occurrence of incident, SOC is responsible for investigating when, how and why an incident occurred. SOC analyzes all logs to identify the root cause of the incident and prevent its reoccurrence after incorporating learnings from the incident.

*While SOC serves twofold purpose, i.e., assessing and alerting security threats in real time thereby continuously improving organization's security posture, however, setting-up own SOC may be onerous for the small REs. Therefore, to improve the cybersecurity posture of such REs, CSCRF provides setting different types of SOC. CSCRF has mandated SOC for all REs (except client-based stock brokers having less than 100 clients). However, CSCRF allows REs to choose any one of the below models to utilize SOC services:*

1. *RE's own/ group SOC*
2. *Market SOC implemented mandatorily by NSE, BSE and optionally by NSDL and/ or CDSL*
3. *Any other third-party managed SOC*

*Small-Size and Self-certification category REs are mandated to be on-boarded on above-mentioned Market SOC.*

*SEBI's expectations from Market SOC are as follows:*

1. *To provide cyber hygiene for Indian securities market ecosystem by providing cost-effective solutions.*
2. *For small-size and mid-size REs, Market SOC shall also provide services of VAPT and cyber audit at an affordable cost. Further, the above-mentioned VAPT and cyber audit should be conducted by a CERT-In empanelled IS Auditing Organization.*

*The particulars of the Market SOC shall be as follows:*

1. *The Market SOC shall be setup:*
   a. *Mandatorily by NSE and BSE*
   b. *Optionally by NSDL and/ or CDSL*
2. *The Market SOC shall be set up in accordance with the CSCRF requirements and shall ensure that participating REs are in compliance with CSCRF as applicable to them.*
3. *The Market SOC shall bridge technological gap for small REs and provide them robust SOC services. However, the responsibility and accountability for compliance with CSCRF rests with the REs.*
4. *The Market SOC shall evolve continuously in order to incorporate new security controls and guidelines that may be issued by SEBI from time to time.*
5. *The Market SOC provider shall ensure that the REs participating in their SOC adhere to the minimum IT guidelines and security protocols all the time.*
6. *NSE and BSE (NSDL and CDSL, if applicable) shall carry out audit of their Market SOC activity annually and submit the report to SEBI.*

*Functional efficacy of market SOC shall be measured in accordance with **Annexure-N** of CSCRF and shall be reported along with market SOC providers' cyber audit report.*
