---
code: PR.IP
title: Information Protection Processes and Procedures
goal: ANTICIPATE
function: PROTECT
version: "1.0"
source: CSCRF
objective: >
  Security policies (that address purpose, scope, roles, responsibilities,
  management commitment, and coordination among organizational
  entities), processes, and procedures are maintained and used to manage
  protection of information systems and assets.
standards:
  - id: PR.IP.S1
    text: >
      A baseline configuration of IT systems shall be created and maintained
      incorporating security principles (e.g. concept of least functionality).
  - id: PR.IP.S2
    text: >
      A System Development Life Cycle to manage systems shall be
      implemented.
  - id: PR.IP.S3
    text: >
      REs shall put in place processes for configuration change control as
      well as change management.
  - id: PR.IP.S4
    text: >
      REs shall thoroughly scan Critical software/ applications to ensure that
      no malicious code is present.
  - id: PR.IP.S5
    text: >
      If the source code of software/ application is not owned by the REs,
      then in such a case, the REs shall obtain an undertaking/ certificate
      from the third-party service providers stating that their software/
      application is free of known vulnerabilities, malwares, malicious/
      fraudulent code and any covert channels.
  - id: PR.IP.S6
    text: >
      Testing/ certification of software/ applications shall broadly address the
      objectives such as product/ version/ module(s) functions only in a
      manner that it is intended to do, it is developed as per the best secure
      design/ coding practices and standards, it addresses known flaws/
      threats due to insecure coding, etc.
  - id: PR.IP.S7
    text: >
      REs shall document backup and recovery plan of data to ensure that
      there is no data loss.
  - id: PR.IP.S8
    text: >
      REs shall implement, test, and maintain data backups. Further, drills
      for restoration of backup data shall be conducted on a periodic basis.
  - id: PR.IP.S9
    text: >
      Policies and regulations regarding the physical operating environment
      for REs' assets shall be defined and adhered to.
  - id: PR.IP.S10
    text: >
      Effectiveness of protective technologies shall be measured on a regular
      basis in line with the SLAs.
  - id: PR.IP.S11
    text: >
      Response plans (incident response and business continuity) and
      recovery plans (incident recovery and disaster recovery) shall be put in
      place and regularly tested and updated.
  - id: PR.IP.S12
    text: >
      A vulnerability management plan shall be developed and implemented.
  - id: PR.IP.S13
    text: >
      For applicable cloud instances of REs, SEBI circular 'Framework for
      Adoption of Cloud Services by SEBI Regulated Entities (REs)' shall be
      complied with.
  - id: PR.IP.S14
    text: >
      Only CERT-In empanelled IS auditing organizations shall be
      onboarded for external audit (including cyber audit) of REs to audit the
      implementation of standards and mandatory guidelines (as applicable)
      mentioned in this framework.
  - id: PR.IP.S15
    text: >
      All software services in the form of SaaS/ Hosted services, COTS,
      customized COTS, in-house developed software, etc. shall be certified
      for application security and functional audit. COTS products
      empanelled by stock exchanges/ depositories shall be certified for
      application security testing, and functional audit by STQC at the time of
      empanelment.
  - id: PR.IP.S16
    text: >
      MIIs and Qualified REs shall obtain ISO 27001 certification.
  - id: PR.IP.S17
    text: >
      MIIs and Qualified REs shall follow globally recognized standards such
      as CIS Critical Security Controls to enhance their cyber resilience.
---

## Guidelines

### PR.IP.G1
- **standards:** [PR.IP.S1]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** false

1. REs shall ensure that IT, OT and IS infrastructure is 'secure by design', 'secure by engineering/ implementation' and the infrastructure has appropriate elements to ensure 'secure IT operations'.
2. For implementation of principle of least functionality, measures such as configuring only essential capabilities by disabling unnecessary and/or unsecured functions, ports, protocols, services, etc. within an information systems shall be implemented.

### PR.IP.G2
- **standards:** [PR.IP.S1]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

3. REs shall use application directory whitelisting on all assets to ensure that only authorized software are run and all unauthorized software are blocked from installation/ execution.

### PR.IP.G3
- **standards:** [PR.IP.S1]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Hardening of Hardware and Software
   a. REs shall deploy only hardened and vetted hardware/ software. During the hardening process, REs shall, inter-alia, ensure that default usernames and passwords are replaced with non-standard usernames and strong passwords and all unnecessary services are removed or disabled in software/ system.
   b. Hardening of OS shall be done to protect servers'/ endpoints' OS, and minimize attack surface and exposure to threats.
   c. For running services, non-default ports shall be used wherever applicable. Open ports on networks and systems, which are not in use or can be potentially used for exploitation of data, shall be blocked. All open ports shall be monitored and appropriate measures shall be taken to secure them.
   d. Practice of whitelisting of ports based (at firewall level) on business usage shall be implemented rather than blacklisting of certain ports. Traffic on all other ports which have not been whitelisted shall be blocked by default.
   e. REs shall restrict execution of "PowerShell" and "wscript" in their environment, if not required. Additionally, REs shall also ensure installation and use of latest version of PowerShell, with enhanced logging enabled, script block logging and transcription enabled. Send the associated logs to a centralized log repository for monitoring and analysis.
   f. REs shall utilize host based firewall to prevent Remote Procedure Call (RPC) and Server Message Block (SMB) communications among endpoints wherever possible to limit lateral movement as well as other attack activities.

### PR.IP.G4
- **standards:** [PR.IP.S3]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** false

1. The change management process shall be part of all agreements with third-party service providers to ensure that changes to the system are implemented in a controlled and coordinated manner.
2. Change Management process shall include (but not limited to) submission, planning (impact analysis, rollout plan), approval, and implementation, review (post-implementation), closure, etc.
3. REs shall have a clearly defined framework for change management including requirements justifying exception(s), duration of exception(s), process of granting exception(s), and authority for approving and for periodic review of exception(s) given.

### PR.IP.G5
- **standards:** [PR.IP.S4, PR.IP.S6]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

3. Secure Software Development Life Cycle (SSDLC)
   a. All REs shall ensure that regression testing is undertaken before new or modified systems are implemented. The scope of tests shall cover business logic, security controls and system performance under various stress-load scenarios, and recovery conditions.
   b. For any production release, vulnerability assessment shall be undertaken. For all *major release*, VAPT shall be conducted by the REs to assess the risk and vulnerabilities generated from recent additions/ modifications in applications/ software.

### PR.IP.G6
- **standards:** [PR.IP.S4, PR.IP.S6]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** false

4. Secure Software Development Cycle (SSDLC)
   a. REs shall prepare business requirement document with clear mentioning of security requirements, session management, audit trail, logging, data integrity, security event tracking, exception handling, etc.
   b. For secure rollout of software and applications, threat modelling and application security testing shall be conducted during development.
   c. REs shall refer to standards, security guidelines for application security and other protection measures given by OWASP (for e.g. OWASP-ASVS).
   d. REs shall adopt the principle of defence-in-depth to provide a layered security mechanism.
   e. Before introducing new technologies for *critical systems*, REs shall ensure that IT/ security team has assessed evolving security concerns and achieved fair level of maturity with such technologies before incorporating them into IT infrastructure.

### PR.IP.G7
- **standards:** [PR.IP.S14]
- **applicability:** [mii, qualified, mid-size, small-size]
- **mandatory:** true

1. Periodic Audit
   a. REs shall engage only CERT-In empanelled IS auditing organizations for conducting external audits including cyber audit to audit the implementation of all standards mentioned in this framework.
   b. A CERT-In empanelled IS auditing organisation can audit the RE for a maximum period of three consecutive years. Subsequently, the said IS auditing organisation shall be eligible for auditing the RE again only after a cooling off period of two years.
   c. The details of periodicity, timeline and report submission for cyber audit by REs have been provided in the *'CSCRF Compliance, Audit Report Submission, and Timelines'* section.
   d. Along with the cyber audit reports, henceforth, all REs shall also submit a declaration from the Managing Director (MD)/ Chief Executive Officer (CEO) as mentioned in Annexure-B.
   e. To ensure that all the open vulnerabilities in the IT assets of REs have been fixed, revalidation VAPT and cyber audit shall also be done in a time bound manner.
   f. Audit Management process of the REs shall include (but not limited to) audit program/ calendar, planning, preparation, delivery, evaluation, reporting, and follow-up, etc.
   g. For conducting audits, CERT-In *'IT Security Auditing Guidelines for Auditee Organizations'* may be followed by REs. Additionally, CERT-In *'Guidelines for CERT-In Empanelled IS Auditing Organizations'* (attached at Annexure-D) may be mandated for empanelled IS auditing organizations.
   h. Due diligence with respect to the audit process and the tools used for such audits shall be undertaken by REs to ensure competence and effectiveness of audits.

### PR.IP.G8
- **standards:** [PR.IP.S14]
- **applicability:** [mii, qualified]
- **mandatory:** true

   i. REs shall strive for building an automated tool and suitable dashboards (preferably integrated with log aggregator) for submitting compliance with CSCRF. A dashboard shall be available at the time of cyber audit, onsite inspection/ audit by SEBI or any agency appointed by SEBI.

### PR.IP.G9
- **standards:** [PR.IP.S15]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. All the categories of software solutions/ applications/ products for *critical systems* used by REs shall mandatorily pass-through the following tests/ audits and compliances:
   a. Application security testing:
      i. Dynamic Application Security Testing (DAST) for scanning software applications in real-time against leading vulnerability sources, such as OWASP Top 10, SANS Top 25 CWE, etc. to find security flaws or open vulnerabilities.
      ii. Static Application Security Testing (SAST) for analyzing program source code to identify security vulnerabilities such as SQL injection, buffer overflows, XML external entity (XXE) attacks, OWASP Top 10 security risks, etc.
   b. Functional audit
   c. VAPT after every *major release* of the application/software
   d. All *critical systems* logs shall be integrated with RE's SOC.
   e. Audit of firewall configuration, WAF configuration, token configuration and channel identification shall be done.
   f. Software bill of material (SBOM)
   g. Requirement Traceability Matrix
2. Tests/ audits stated above at point 1 (a-b) shall be limited to cybersecurity aspects. Application security testing shall also include API security and API discovery. Scope of functional audit shall cover data integrity, report integrity, and transaction integrity, etc.
3. With respect to empanelled COTS used by Stock Brokers and Depository Participants:
   a. Before empaneling any COTS solutions for supplying software/ products to their respective stock brokers and depository participants, Stock Exchanges and Depositories shall conduct tests/ audits stated above at point 1 (a-b) through STQC.
   b. The Stock Exchanges and Depositories shall prepare a SOP for inclusion of tests/ audits in their vendor empanelment process for COTS solutions.
   c. The empanelment shall be approved by the Stock Exchanges and Depositories only after receipt of compliance reports from STQC and VAPT report from the COTS vendor.
4. Customized COTS:
   a. REs shall ensure that the compliance with tests/ audits stated above at point 1 (a-d) by CERT-In empanelled IS auditing organization for any customized COTS.
5. Inhouse developed software:
   a. REs shall ensure compliance with aforementioned point 1 is submitted by CERT-In empanelled IS auditing organization.
6. Software services in form of SaaS/ hosted services used by REs:
   i. REs shall be required to submit compliance with the technical specification mentioned in hosted services definition for the SaaS/ hosted services used by them.
   ii. REs shall also submit compliance with adoption of hosted services and SaaS as per the various functions of CSCRF including Governance, Identify, Protect, Detect, Respond, and Recover.

### PR.IP.G10
- **standards:** [PR.IP.S16]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. ISO 27001 certification shall be mandatory for REs as it provides essential security standards with respect to ISMS. The scope for ISO 27001 certification shall include (but not limited to) PDC site, DR site, NDR site, SOC, and Colocation facility.

### PR.IP.G11
- **standards:** [PR.IP.S17]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall follow the latest version of CIS Controls or equivalent standards which are prioritized set of safeguards and actions for cyber defence and provide specific and actionable ways to mitigate prevalent cybersecurity incidents/ attacks.
