---
code: GV.SC
title: Cybersecurity Supply Chain Risk Management
goal: ANTICIPATE
function: GOVERNANCE
version: "1.0"
source: CSCRF
objective: >
  The RE's priorities, constraints, risk tolerance, and assumptions are
  established and used to support decisions associated with managing
  supply chain risks. The RE has established and implemented the
  processes to identify, assess and manage supply chain risks.
standards:
  - id: GV.SC.S1
    text: >
      Cybersecurity supply chain risk management strategy/ process shall
      be identified, established, assessed, managed, and agreed to by
      organizational stakeholders.
  - id: GV.SC.S2
    text: >
      Suppliers and third-party service providers of information
      systems, components, and services shall be identified, prioritized,
      and assessed using a cyber-supply chain risk assessment process.
  - id: GV.SC.S3
    text: >
      Contracts with suppliers and third-party service providers shall
      include appropriate measures to meet the objectives of the RE's
      cybersecurity program and cybersecurity supply chain risk
      management plan (including manpower adequacy in cybersecurity
      domain).
  - id: GV.SC.S4
    text: >
      REs shall monitor, review and ensure compliance of third-party
      service providers performing critical activities for their
      respective organization on a periodic basis.
  - id: GV.SC.S5
    text: >
      SBOM shall be obtained for all new software procurements of core
      and critical activities and kept updated with every upgrade or
      change. In case the SBOM cannot be obtained for the legacy or
      proprietary systems, the Board/ Partners/ Proprietor of the
      organization shall approve the same with proper limitation,
      rationale, and risk management approach.
  - id: GV.SC.S6
    text: >
      Response and recovery planning, and testing shall be conducted
      along with third-party service providers.
  - id: GV.SC.S7
    text: >
      Concentration risk on outsourced agencies shall be assessed and
      reviewed to achieve operational resiliency.
  - id: GV.SC.S8
    text: >
      Third-party service providers shall also be mandated to follow
      similar standards of information security.
---

## Guidelines

### GV.SC.G1
- **standards:** [GV.SC.S4]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. Where the systems (IBT, Back office and other customer facing applications, IT infrastructure, etc.) of a RE are managed by third-party service providers and in case the RE does not have direct control over the implementation of any of the guidelines, the RE shall instruct the third-party service providers to adhere to the applicable guidelines in the CSCRF and shall obtain the necessary cyber audit certifications from them to ensure compliance with the framework.

### GV.SC.G2
- **standards:** [GV.SC.S4]
- **applicability:** [mii]
- **mandatory:** true

2. Where applications (for e.g.: NSE's NEAT, BSE's BOLT etc.) are offered to users over the internet by MIIs, the responsibility of ensuring cyber resilience of such applications resides with the MIIs and not with the users who are using the applications.

### GV.SC.G3
- **standards:** [GV.SC.S4]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

3. The responsibility, accountability and ownership of outsourced activities lies primarily with REs. Therefore, REs shall come up with appropriate monitoring mechanisms through a clearly defined framework to ensure that all the requirements as specified in CSCRF shall be complied with. The periodic²⁵ reports submitted to SEBI shall highlight the critical activities handled by the third-party service providers and REs shall certify that the above-mentioned requirement is complied with.
4. REs shall conduct background checks and ensure signing of Non-Disclosure Agreement, and cybersecurity compliance for all third-party service providers.

> ²⁵ Refer 'CSCRF Compliance, Audit Report Submission, and Timelines' section.

### GV.SC.G4
- **standards:** [GV.SC.S5]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. REs shall obtain SBOM for existing their *critical systems* within 6 months (starting from the date of issuance of CSCRF).
2. REs shall obtain SBOMs for any new *critical systems* software products/ Software-as-a-Service applications (SaaS) at the time of procurement. SBOMs containing information such as all the open source and third-party components present in a codebase, versions of the components used in the codebase, and their patch status, etc. allow security teams to quickly identify any associated security or license risk.
3. MIIs shall include SBOM as part of their empanelment criteria for application software vendors.
4. SBOM shall include (but not limited to) the following:
   a. License information
   b. Name of the supplier
   c. All primary (top level) components with all their transitive dependencies (including third-party dependencies whether in-house or open-source components) and relationships
   d. Encryption used
   e. Cryptographic hash of the components
   f. Frequency of updates
   g. Known unknown (where a SBOM does not include a full dependency graph)
   h. Access control
   i. Methods for accommodating occasional incidental errors.

### GV.SC.G5
- **standards:** [GV.SC.S7]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. Any single third-party service provider, providing services to multiple REs, creates a concentration risk. When such third-party service providers encounter cybersecurity incidents/ attacks, it can led to systemic implications due to high concentration risk. Therefore, REs need to take into account concentration risk while outsourcing multiple critical services to the same third-party service provider.
2. REs shall identify their third-party service providers posing a concentration risk and shall prescribe specific cybersecurity controls, including audit of their systems and protocols from independent auditors, to mitigate such concentration risk. REs shall also validate that such third-party service providers are meeting their goals of operational resiliency.
3. Stock Exchanges/ Depositories shall take necessary steps to mitigate concentration risk of third-party service providers among Stock Brokers/ Depository Participants.
4. SEBI circulars on outsourcing of activities, currently mandated and updated from time to time, shall be complied with by the respective REs. List of currently mandated SEBI circulars on outsourcing of activities has been attached at Annexure-F.

## Annexure

### Box Item 6: Software Bill of Materials (SBOM)

*Recent security breaches at third-party vendors like Apache (Log4j), Solarwinds, etc. have led to the introduction of Software Bill of Materials (SBOM) that enables an organization to identify possible vulnerabilities in the applications/ software solutions.*

*With introduction of SBOM, the following benefits are envisaged for REs:*

1. ***Transparency:** REs will become more aware of components, versions, licenses, cryptographic hashes, etc. that they are using in their software applications. This will make the REs well-informed to make better security decisions.*
2. ***Tracking vulnerabilities:** REs will be able to track vulnerability status for each of the components as and when an update is made or a component is added/ deleted.*
3. ***Mitigate supply chain risks:** REs will be able to prevent and mitigate supply chain risks arising due to open-source or third-party dependencies (e.g. libraries, repositories, etc.) in software components.*
4. ***Audit:** REs will have the confidence that only authorized third-party dependencies have been used in their software applications and the same can be audited as and when required.*
