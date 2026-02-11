# Mandatory CSCRF Requirements for Small-Size Mutual Fund / AMC

| Field | Value |
|-------|-------|
| **Scope** | Small-size Regulated Entity — Mutual Fund / Asset Management Company |
| **CSCRF version** | 1.0 |
| **Applicability tag** | `small-size` |
| **Date of extraction** | 2026-02-11 |

This document lists every **mandatory** guideline from SEBI's Cybersecurity and Cyber Resilience Framework (CSCRF) v1.0 that applies to a small-size RE classified as a mutual fund / AMC. All guideline text is reproduced verbatim from the framework source files.

---

## Summary

| Function | Mandatory guidelines | IDs |
|----------|---------------------|-----|
| Governance | 5 | GV.OC.G2, GV.PO.G1, GV.RR.G2, GV.SC.G3, GV.SC.G4 |
| Identify | 2 | ID.AM.G1, ID.RA.G4 |
| Protect | 15 | PR.AA.G1, PR.AA.G5, PR.AA.G7, PR.AA.G8, PR.AA.G10, PR.AT.G1, PR.AT.G2, PR.DS.G2, PR.DS.G3, PR.DS.G4, PR.DS.G5, PR.IP.G3, PR.IP.G7, PR.IP.G9, PR.MA.G2 |
| Detect | 2 | DE.CM.G1, DE.CM.G6 |
| Respond | 7 | RS.AN.G1, RS.AN.G2, RS.CO.G1, RS.CO.G3, RS.IM.G1, RS.IM.G2, RS.MA.G1 |
| Recover | 4 | RC.RP.G1, RC.RP.G3, RC.RP.G5, RC.RP.G6 |
| Evolve | 0 | — |
| **Total** | **35** | |

---

## Notes Specific to Small-Size MF/AMC

1. **IT Committee for REs — not required (but see Note 6).** GV.PO.G4, which mandates constitution of a new IT Committee, applies only to MIIs, Qualified, and Mid-size REs. For small-size REs without a pre-existing committee, compliance review and approval is performed by the **MD / CEO / Board member / Partners / Proprietor** (or equivalent body). However, MF/AMCs already have a Technology Committee obligation — see Note 6.
2. **Reporting authority is SEBI.** Mutual funds / AMCs are not stock brokers or depository participants. Per Tables 17, 23, and 16 in CSCRF Section 4, the reporting authority for VAPT reports, cyber audit reports, and ISO certification evidence is **SEBI** directly (not stock exchanges / depositories).
3. **Cyber audit periodicity:** At least once per financial year (Table 21, "Rest of the REs"), unless the MF/AMC provides IBT or Algo trading (in which case, at least twice per year).
4. **VAPT periodicity:** At least once per financial year — activity shall commence in the first quarter (Table 18, "Rest of the REs").
5. **Market SOC:** Small-size REs are mandated to be on-boarded on Market SOC implemented by NSE/BSE (and optionally NSDL/CDSL).
6. **Existing Technology Committee for MFs/AMCs.** MFs/AMCs are required to have a Technology Committee per SEBI circular SEBI/HO/IMD/DF2/CIR/P/2019/058 (April 11, 2019). This is separate from the *IT Committee for REs* newly defined in CSCRF for Qualified and Mid-size REs. Per CSCRF Section 3.2, this existing Technology Committee must now also include **one (1) external independent expert on cybersecurity matters**. For common reference in CSCRF, the Technology Committee, SCOT, and IT Committee are collectively termed "*IT Committee for REs*". The ToRs in Section 3.5 of CSCRF apply as an addendum to the existing Technology Committee ToRs.

### Compliance Periodicities Applicable to Small-Size REs (from Table 15)

| # | Requirement | Periodicity |
|---|------------|-------------|
| 1 | Cybersecurity and cyber resilience policy review (GV.PO.S2) | Annually |
| 2 | Cybersecurity risk management policy (GV.PO.S4) | Annually |
| 3 | User access rights, delegated access and unused tokens review (PR.AA.S5) | Half-yearly |
| 4 | Review of privileged users' activities (PR.AA.S11) | Half-yearly |
| 5 | Cybersecurity training program (PR.AT.S1) | Annually |
| 6 | Review of systems managed by third-party service providers (GV.SC.S4) | Annually |
| 7 | Functional efficacy of SOC (for REs using third-party/Market SOC) | Annually |
| 8 | Cybersecurity scenario-based drill exercise (RC.RP.S3) | Annually |
| 9 | Review/update contingency plan, COOP (RS.MA.S3) | Annually |
| 10 | Evaluation of cyber resilience posture (EV.ST.S5) | Annually |

---

## 1. GOVERNANCE

### GV.OC.G2 — Organizational Context

- **Standards:** GV.OC.S2
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. All REs shall understand, manage and comply with relevant cybersecurity and data security/ protection requirements mentioned in government guidelines/ policies/ laws/ circulars/ regulations, etc. issued by SEBI/ GoI such as IT Act 2000, Digital Personal Data Protection Act (DPDP) 2023 or any other law/ circular/ regulation as and when issued.
2. Conduct audits and inspections of IT resources of REs (and its sub-contractors/ third-party service providers) or engage third-party auditor to conduct the same and check the adherence with SEBI and government guidelines/ policies/ laws/ circulars/ regulations, etc., and standard industry practices.
3. SEBI/ any other government agency shall at any time perform search and seizure of RE's IT resources storing/ processing data and other relevant IT resources (including but not limited to logs, user details, etc.) pertaining to the RE. In this process, SEBI or SEBI authorized personnel/ agency may access RE's IT infrastructure, applications, data, documents, including other necessary information given to, stored or processed by third-party service providers.
4. Engage a forensic auditor to identify the root cause of any incident (cybersecurity or other incidents) related to RE.
5. SEBI shall seek the audit reports of the audits conducted by RE.

---

### GV.PO.G1 — Policy

- **Standards:** GV.PO.S1, GV.PO.S2, GV.PO.S5
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. As part of the operational risk management framework to manage risks to systems, networks and databases from cyber-attacks and threats, REs shall formulate a comprehensive Cybersecurity and Cyber Resilience policy document encompassing CSCRF. In case of deviations from the CSCRF, reasons for such deviations, technical or otherwise, shall be provided in the policy document.
2. The policy document shall be approved by the Board/ Partners/ Proprietor of the REs. The policy document shall be reviewed by the aforementioned group periodically with a view to strengthen and improve cyber resilience posture.
3. REs shall have policies (including but not limited to) with respect to asset management, patch management, vulnerability management, VAPT policy, audit policy, monitoring of the networks and endpoints, configuration management, change management, secure software development life cycle management, authentication policies, authorization policies and processes, network segmentation/ isolation policies, commissioning internet facing assets, encryption policies, PII and privacy policies, cybersecurity control management policy, asset ownership documentation, etc., and chain of command for any approval process in the organization with respect to cybersecurity. The policies shall also contain do's and don'ts in the organization with respect to usage of information assets including desktops, laptops, BYOD, networks, internet, data, etc. The aforementioned policies may form a part of RE's cybersecurity policy or may be standalone policies.

---

### GV.RR.G2 — Roles, Responsibilities and Authorities

- **Standards:** GV.RR.S3
- **Applicability:** mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall designate a senior official or management personnel (henceforth, referred to as the "Designated Officer") whose function would be to assess, identify, and reduce cybersecurity risks, respond to incidents, establish appropriate standards and controls, and direct the establishment and implementation of processes and procedures as per the cybersecurity and cyber resilience policy approved by the Board/ Partners/ Proprietor. REs shall establish a reporting procedure to facilitate communication of cybersecurity incidents/ unusual activities to Designated Officer in a time-bound manner as defined by guidelines/ policies/ laws/ circulars/ regulations, etc. issued by SEBI or GoI.

---

### GV.SC.G3 — Supply Chain Risk Management

- **Standards:** GV.SC.S4
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

3. The responsibility, accountability and ownership of outsourced activities lies primarily with REs. Therefore, REs shall come up with appropriate monitoring mechanisms through a clearly defined framework to ensure that all the requirements as specified in CSCRF shall be complied with. The periodic reports submitted to SEBI shall highlight the critical activities handled by the third-party service providers and REs shall certify that the above-mentioned requirement is complied with.
4. REs shall conduct background checks and ensure signing of Non-Disclosure Agreement, and cybersecurity compliance for all third-party service providers.

**Compliance periodicity:** Review of third-party service providers — Annually (Table 15, row 10).

---

### GV.SC.G4 — Supply Chain Risk Management

- **Standards:** GV.SC.S5
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

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

---

## 2. IDENTIFY

### ID.AM.G1 — Asset Management

- **Standards:** ID.AM.S1, ID.AM.S4
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. All REs shall identify and classify *critical systems* as defined in this framework based on their sensitivity and criticality for business operations, services and data management. The Board/ Partners/ Proprietor of the REs shall approve the list of *critical systems*.
2. All REs shall maintain an up-to-date inventory of their (including but not limited to) hardware and systems, software, digital assets (such as URLs, domain names, application, APIs, etc.), shared resources (including cloud assets), interfacing systems (internal and external), details of its network resources, connections to its network and data flows.
3. Any additions/ deletions or changes in existing assets shall be reflected in the asset inventory within 3 working days.
4. For conducting criticality assessment of assets, REs shall take the following steps (including but not limited to):
   a. Maintain a comprehensive asset inventory
   b. Conduct threat modelling (based on risk assessment)
   c. Conduct vulnerability assessment
5. REs shall prepare and maintain an up-to-date network architecture diagram at the organisational level including wired and wireless networks.

---

### ID.RA.G4 — Risk Assessment

- **Standards:** ID.RA.S4
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Measures against Phishing websites and attacks
   a. REs need to proactively monitor the cyberspace to identify phishing websites w.r.t. REs' domains and report the same to CSIRT-Fin/CERT-In for taking appropriate action.

---

## 3. PROTECT

### PR.AA.G1 — Access Control and Authentication

- **Standards:** PR.AA.S1, PR.AA.S2, PR.AA.S3, PR.AA.S7, PR.AA.S9
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Access Controls, Password Policy/ Authentication Mechanism
   a. No person by virtue of rank or position shall have any intrinsic right to access confidential data applications, system resources or facilities.
   b. Any access to REs' systems, applications, networks, databases, etc., shall be for a defined purpose and for a defined period. Access granted to IT systems, applications, databases and networks shall be on a need-to-use basis and based on the principle of least privilege. Such access shall be given for a specific duration and using effective authentication mechanisms.
   c. User access rights, delegated access and unused tokens, and privileged users' activities shall be reviewed on a periodic basis.
   d. Access to external cloud services such as Dropbox, google drive, iCloud, OneDrive, etc. shall be given as per RE's policy.
   e. REs shall ensure that records of user access to *critical systems*, wherever possible, are uniquely identified and logged for audit and review purposes. Such logs shall be maintained and stored in a secure location for a time period not less than two (2) years (atleast 6 months in online mode and rest in archival mode). REs also need to maintain records of users with access to shared accounts.
   f. Account access lock policies after failure attempts shall be implemented for all accounts.
   g. Existing user accounts and access rights shall be periodically reviewed by the owner of the system in order to detect dormant accounts, accounts with excessive privileges, unknown accounts or any type of discrepancy.
   h. Proper 'end of life' mechanisms shall be adopted for user management to deactivate access privileges of users who are leaving the organization or whose access privileges have been withdrawn. This includes named user IDs, default user IDs and generic email IDs.
   i. All *critical systems* accessible over the internet shall have multi-factor security (such as VPNs, Firewall controls, etc.) and MFA.
   j. MFA shall be enabled for all users and systems that connect using online/ internet facility and also particularly for VPNs, webmail, and accounts that access *critical systems* from non-trusted environments to trusted environments.
2. Network Security Management
   a. Adequate controls shall be deployed to address virus/ malware/ ransomware attacks on servers and other IT systems. These controls may include host/ network/ application based IPS, customized kernels for Linux, anti-virus and anti-malware software, etc. Anti-virus definition files updates and automatic anti-virus scanning shall be done on a regular basis.
   b. All REs shall establish baseline standards to facilitate consistent application of security configurations to OS, databases, network devices, enterprise mobile devices, etc. within the IT environment. REs shall also conduct regular enforcement checks to ensure that baseline standards are applied uniformly.
   c. The LAN and wireless networks within REs' premises shall be secured with proper access controls.
   d. REs shall keep total and maximum connections to SMTP server limited.

**Compliance periodicity:** User access rights review — Half-yearly; Privileged users' review — Half-yearly (Table 15, rows 7–8).

---

### PR.AA.G5 — Access Control and Authentication

- **Standards:** PR.AA.S6
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Effective authentication policy shall be implemented with the defined complexity of the password.
2. All generic user IDs and email IDs which are not in use shall be removed after the use.

---

### PR.AA.G7 — Access Control and Authentication

- **Standards:** PR.AA.S8
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs are advised to ensure that all logs sources are being identified and their respective logs are being collected. An indicative list of types of log data to be collected by REs is as follows: system logs, application logs, network logs, database logs, security logs, performance logs, audit trail logs, and event logs.
2. Strong log retention policy shall be implemented as per government guidelines/ policies/ laws/ circulars/ regulations, etc. issued by SEBI/ GoI such as IT Act 2000, Digital Personal Data Protection Act (DPDP) 2023, and as required by CERT-In, NCIIPC or any other government agency.
3. In order to identify unusual patterns and behaviours, monitoring of all logs of events and incidents shall be done.

---

### PR.AA.G8 — Access Control and Authentication

- **Standards:** PR.AA.S10, PR.AA.S11, PR.AA.S12
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Physical Security
   a. Physical access to the *critical systems* shall be restricted to a minimum and shall be provided only to authorized officials. Physical access provided to third-party service providers shall be properly supervised by ensuring at the minimum that third-party service providers are accompanied at all times by authorized employees.
   b. Employees of REs shall be screened before granting access to organizational information and information systems. Physical access to the *critical systems* shall be revoked immediately if the same is no longer required.
   c. All REs shall ensure that the perimeter of the critical equipment's room, if any, are physically secured and monitored by employing physical, human and procedural controls such as the use of security guards, CCTVs, card access systems, mantraps, bollards, etc. wherever appropriate.
2. Remote Support Service Security
   a. As many OEMs and their service partners as well as System Integrators provide remote support services to organisations, REs shall ensure that these services are well-governed, controlled, logged and an oversight is maintained on all the activities done by remote support service providers. The above shall be complemented by regular monitoring and audit to ensure compliance of the defined policies for privileged users and remote access.
   b. REs shall ensure secure usage of RDP in IT systems. Further, it shall be implemented strictly on a need-to-use basis, and it must employ MFA. Remote access, if necessary, shall be given to authorised personnel from whitelisted IPs for a predefined time period, and with a provision to log all activities.
   c. Employees and third-party service providers who may be given authorized access to the *critical systems*, networks and other IT resources of REs shall be subject to stringent supervision, monitoring and access restrictions.

---

### PR.AA.G10 — Access Control and Authentication

- **Standards:** PR.AA.S13, PR.AA.S14
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall formulate a data-disposal and data-retention policy to identify the value and lifetime of various parcels of data.
2. REs shall frame suitable policies for disposal of storage media and systems. The critical data/ information on such devices and systems shall be removed by using methods such as wiping/ cleaning/ overwrite, degauss/ crypto shredding/ physical destruction as applicable.

---

### PR.AT.G1 — Awareness and Training

- **Standards:** PR.AT.S1, PR.AT.S2
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall work on building awareness of cybersecurity, cyber resilience, and system hygiene among employees (with a focus on employees from non-technical disciplines).
2. REs shall ensure that their employees are aware of potential risks including social engineering attacks, phishing, etc.
3. Majority of the infections are primarily introduced via phishing emails, malicious adverts on websites, and third-party apps and programs. Hence, thoughtfully designed security awareness campaigns that stress the avoidance of clicking on links and attachments in email, shall be established as an essential pillar of defence. Additionally, the advisories issues by CERT-In/ CSIRT-Fin may be referred for assistance in conducting exercises for public awareness.
4. REs shall conduct periodic training programs to enhance knowledge of IT/ cybersecurity policy and standards among the employees incorporating up-to-date cybersecurity threats. Wherever possible, this shall be extended to outsourced staff, third-party service providers, etc.
5. The training programs shall be reviewed and updated to ensure that the contents of the program remain current and relevant.

**Compliance periodicity:** Cybersecurity training program — Annually (Table 15, row 9).

---

### PR.AT.G2 — Awareness and Training

- **Standards:** PR.AT.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall mention/ incorporate a section on the mobile and web application clearly specifying the process and procedure (with forms/ contact information, etc.) to lodge customer/ investor grievances with respect to technology related issues and cybersecurity. A mechanism to keep this information periodically updated shall also be put in place. The reporting facility on the application shall provide an option for registering a grievance. Customers/ investors dispute handling, reporting and resolution procedures, including the expected timelines for the response should be clearly defined.
2. REs shall provide access to mobile and web applications to a customer only at her/ his option based on specific written or authenticated electronic requisition along with a positive acknowledgement of the terms and conditions.
3. REs shall provide a mechanism on their mobile and web application for their customers/ investors with necessary authentication to identify/ mark a transaction as fraudulent for seamless and immediate notification to his entities. On such notification by the customer/investor, they may endeavour to build the capability for seamless/ instant reporting of fraudulent transactions to the corresponding beneficiary/ counterparty's entities; vice-versa have mechanism to receive such fraudulent transactions reported from other entities.
4. Improve and maintain customer/ investor awareness and education with regard to cybersecurity risks.
5. Encourage customers/investors to report phishing mails/ phishing sites and on such reporting take effective remedial action.
6. Educate the customers/investors on the downside risk of sharing their login credentials/ passwords/ OTP etc. to any third-party and the consequences thereof.

---

### PR.DS.G2 — Data Security

- **Standards:** PR.DS.S1, PR.DS.S2, PR.DS.S3
- **Applicability:** mii, qualified, mid-size, small-size
- **Mandatory:** true

2. Application Security in Customer Facing Applications:
   a. Application security for Customer facing applications offered over the Internet such as IBTs (Internet Based Trading applications), portals containing sensitive or private information and Back office applications (repository of financial and personal information offered by REs to Customers) are paramount as they carry significant attack surfaces by virtue of being available publicly over the Internet for mass use. An illustrative list of measures for ensuring security in such applications is provided in Annexure-G.

---

### PR.DS.G3 — Data Security

- **Standards:** PR.DS.S1, PR.DS.S2, PR.DS.S3
- **Applicability:** mii, qualified, mid-size, small-size
- **Mandatory:** true

1. REs shall implement suitable mechanisms, including generation of appropriate alerts, to monitor capacity utilisation on a real-time basis and shall proactively address issues pertaining to their capacity needs.
2. For capacity planning and monitoring, REs shall comply with circulars/ guidelines on capacity planning issued by SEBI (and updated from time to time).

---

### PR.DS.G4 — Data Security

- **Standards:** PR.DS.S1, PR.DS.S2, PR.DS.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall keep the *Regulatory Data* available and easily accessible in legible and usable form, within the legal boundaries of India. However, for the investors whose country of incorporation is outside India, the REs shall keep the original data, available and easily accessible in legible and usable form, within the legal boundaries of India. Further, if the *Regulatory Data* retained within India is not in readable form, the REs must maintain an application/system to read/ analyse the retained data.
2. The *IT and Cybersecurity Data* which is sent to/ consumed by global/ international SOC of the REs and SaaS based cybersecurity solutions have been exempted from being maintained within the legal boundaries of India. For above mentioned SaaS based cybersecurity solutions and SOC offerings utilized by REs where the data is not processed/stored within the legal boundaries of India, such data shall be classified, assessed and periodically reviewed (at least once in a year) by the respective *IT Committee for REs* or equivalent body of the RE. Additionally, such *IT and Cybersecurity Data* shall be approved by the Board/ Partners/ Proprietor annually. Further, such data shall be made available to SEBI/ CERT-In/ any other government agency whenever required within a reasonable time not exceeding 48 hours from the time of request.
3. While doing data classification, REs shall adhere to data security standards and guidelines and other government guidelines/ policies/ laws/ circulars/ regulations, etc. issued by SEBI/ GoI such as IT Act 2000, Digital Personal Data Protection Act (DPDP) 2023 or any other law/ circular/ regulation as and when issued.

---

### PR.DS.G5 — Data Security

- **Standards:** PR.DS.S4
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall enforce effective data protection, backup, and recovery measures.
2. REs shall block administrative rights on end-user workstations/ PCs/ laptops by default and provide access rights on need basis as per the established process and approvals and for specific duration for which it is required.
3. Security controls for mobile and web applications shall focus on how these applications handle, store, and protect PII and other business related data.
4. Web and mobile applications shall not store sensitive information in HTML hidden fields, cookies, or any other client-side storage to avoid any compromise in the integrity of the data.
5. REs shall renew their digital certificates used in IT systems well in time.
6. REs shall implement measures to control usage of VBA/macros in office documents, control permissible attachment types in email systems.
7. REs shall have a documented data migration policy specifying SOPs and processes for data migration while ensuring data integrity, completeness and consistency.

---

### PR.IP.G3 — Information Protection Processes and Procedures

- **Standards:** PR.IP.S1
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Hardening of Hardware and Software
   a. REs shall deploy only hardened and vetted hardware/ software. During the hardening process, REs shall, inter-alia, ensure that default usernames and passwords are replaced with non-standard usernames and strong passwords and all unnecessary services are removed or disabled in software/ system.
   b. Hardening of OS shall be done to protect servers'/ endpoints' OS, and minimize attack surface and exposure to threats.
   c. For running services, non-default ports shall be used wherever applicable. Open ports on networks and systems, which are not in use or can be potentially used for exploitation of data, shall be blocked. All open ports shall be monitored and appropriate measures shall be taken to secure them.
   d. Practice of whitelisting of ports based (at firewall level) on business usage shall be implemented rather than blacklisting of certain ports. Traffic on all other ports which have not been whitelisted shall be blocked by default.
   e. REs shall restrict execution of "PowerShell" and "wscript" in their environment, if not required. Additionally, REs shall also ensure installation and use of latest version of PowerShell, with enhanced logging enabled, script block logging and transcription enabled. Send the associated logs to a centralized log repository for monitoring and analysis.
   f. REs shall utilize host based firewall to prevent Remote Procedure Call (RPC) and Server Message Block (SMB) communications among endpoints wherever possible to limit lateral movement as well as other attack activities.

---

### PR.IP.G7 — Information Protection Processes and Procedures

- **Standards:** PR.IP.S14
- **Applicability:** mii, qualified, mid-size, small-size
- **Mandatory:** true

1. Periodic Audit
   a. REs shall engage only CERT-In empanelled IS auditing organizations for conducting external audits including cyber audit to audit the implementation of all standards mentioned in this framework.
   b. A CERT-In empanelled IS auditing organisation can audit the RE for a maximum period of three consecutive years. Subsequently, the said IS auditing organisation shall be eligible for auditing the RE again only after a cooling off period of two years.
   c. The details of periodicity, timeline and report submission for cyber audit by REs have been provided in the *'CSCRF Compliance, Audit Report Submission, and Timelines'* section.
   d. Along with the cyber audit reports, henceforth, all REs shall also submit a declaration from the Managing Director (MD)/ Chief Executive Officer (CEO) as mentioned in Annexure-B.
   e. To ensure that all the open vulnerabilities in the IT assets of REs have been fixed, revalidation VAPT and cyber audit shall also be done in a time bound manner.
   f. Audit Management process of the REs shall include (but not limited to) audit program/ calendar, planning, preparation, delivery, evaluation, reporting, and follow-up, etc.
   g. For conducting audits, CERT-In *'IT Security Auditing Guidelines for Auditee Organizations'* may be followed by REs. Additionally, CERT-In *'Guidelines for CERT-In Empanelled IS Auditing Organizations'* (attached at Annexure-D) may be mandated for empanelled IS auditing organizations.
   h. Due diligence with respect to the audit process and the tools used for such audits shall be undertaken by REs to ensure competence and effectiveness of audits.

**Compliance periodicity:** Cyber audit — At least once per year (Table 21); VAPT — At least once per year (Table 18).

---

### PR.IP.G9 — Information Protection Processes and Procedures

- **Standards:** PR.IP.S15
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

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

---

### PR.MA.G2 — Maintenance

- **Standards:** PR.MA.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. REs shall establish and ensure that the patch management procedures include the identification, categorization and prioritization of patches and updates. An implementation timeframe for each category of patches shall be established to apply them in a timely manner.
2. All operating systems and applications shall be updated with the latest patches on a regular basis. As an interim measure for zero-day vulnerabilities, and where patches are not available, virtual patching may be considered for protecting systems and networks. This measure hinders cybercriminals from gaining access to any system through vulnerabilities in end-of-support and end-of-life applications and software. Patches shall be sourced only from the authorized sites of the OEM.
3. REs shall perform comprehensive and rigorous testing of security patches and updates, wherever possible, before deployment into the production environment so as to ensure that application of patches does not impact other systems.
4. All patches shall be tested first in non-production environment which shall be identical to the production environment.
5. Hardware and software of *critical systems* shall be replaced before they reach End-of-Life/End-of-Support.
6. Compensatory controls like virtual patching shall be implemented for legacy systems for a maximum period of 6 months. Further, the constraints due to which virtual patching is done shall be legitimate and documented.
7. Procurement of hardware/software shall be aligned with technology refresh policy of the REs.

---

## 4. DETECT

### DE.CM.G1 — Security Continuous Monitoring

- **Standards:** DE.CM.S1, DE.CM.S2, DE.CM.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Security Continuous Monitoring
   a. REs shall establish appropriate security monitoring systems and processes to facilitate continuous monitoring of security events/ alerts and timely detection of unauthorized or malicious activities, unauthorized changes, unauthorized access and unauthorized copying and transmission of data/ information held in contractual or fiduciary capacity, by internal and external parties. The security logs of systems, applications and network devices exposed to the internet shall also be monitored for anomalies.
   b. Suitable alerts shall be generated in the event of detection of unauthorized or abnormal system activities, transmission errors or unusual online transactions.
   c. To enhance the security monitoring, REs (except client-based stock brokers having less than 100 clients) are mandated to employ SOC services for their systems. REs may choose any of the following models to use SOC services:
      i. RE's own SOC/ group SOC
      ii. Market SOC implemented mandatorily by NSE, BSE and optionally by NSDL and/ or CDSL
      iii. Any other third party managed SOC
   d. Small-Size and Self-certification category REs are mandated to be on-boarded on above-mentioned Market SOC.

**Compliance periodicity:** Functional efficacy of SOC (for third-party/Market SOC) — Annually (Table 15, row 11).

---

### DE.CM.G6 — Security Continuous Monitoring

- **Standards:** DE.CM.S5
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. The details of periodicity, timeline and report submission for cyber audit by REs have been provided in the *'CSCRF Compliance, Audit Report Submission, and Timelines'* section.
2. REs shall regularly conduct cybersecurity audit and VAPT with scope as mentioned in CSCRF in order to detect vulnerabilities in the IT environment. Further, REs shall conduct in-depth evaluation of the security posture of the system through simulations of actual attacks. An indicative (but not exhaustive and limited to) VAPT scope has been attached at **Annexure-L**.
3. The assets under these audits shall include (but not limited to) all *critical systems*, infrastructure components (like networking systems, security devices, load balancers, servers, databases, applications, remote access points, systems accessible through WAN, LAN as well as with Public IP's, websites, etc.), and other IT systems pertaining to the operations of REs.
4. REs shall perform VAPT prior to the commissioning of new systems, especially those which are part of *critical systems* or connected to *critical systems*.
5. Revalidation of VAPT post closure of observations shall be done in a time bound manner to ensure that all the open vulnerabilities have been fixed.

---

## 5. RESPOND

### RS.AN.G1 — Incident Analysis

- **Standards:** RS.AN.S1, RS.AN.S2, RS.AN.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Alerts generated from monitoring and detection systems shall be suitably investigated by the REs in order to determine activities that are to be performed to prevent spread of cybersecurity incidents/ attacks or breaches, mitigate their effects and resolve the incidents.
2. Data collection: REs shall collect and preserve data related to the incident, such as system logs, network traffic, and forensic images of affected systems.
3. Incident Analysis: REs shall analyse the data to understand the scope, cause, and impact of the incident, including how the incident occurred, what systems and data were affected, who was responsible, etc.
4. Evidence Preservation: REs shall preserve evidence related to the incident, including digital artefacts, network captures, and memory dumps, in a secure and forensically sound manner.

---

### RS.AN.G2 — Incident Analysis

- **Standards:** RS.AN.S4, RS.AN.S5
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Root Cause Analysis: REs shall perform a root cause analysis (RCA) to identify the specific control that has failed, underlying cause of the incident and the potential areas of improvement.
2. Forensic: Forensic analysis (as appropriate) shall be undertaken by the REs.
3. Any incident of loss or destruction of data or systems shall be thoroughly analysed and lessons learned from such incidents shall be incorporated to strengthen the security mechanisms and improve the recovery planning and processes.
4. Reporting: REs shall create a detailed incident report that includes information on the scope, cause, and impact of the incident, as well as recommendations for improving incident response and recovery capabilities.
5. REs shall conduct a compromise assessment through CERT-In empanelled IS auditing organizations.

---

### RS.CO.G1 — Communication

- **Standards:** RS.CO.S1, RS.CO.S2, RS.CO.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. Any cyber-attack, cybersecurity incident and/ or breach falling under CERT-In Cybersecurity directions shall be notified to SEBI and CERT-In within 6 hours of noticing/ detecting such incidents or being brought to notice about such incidents. This information shall be shared with SEBI through the *mkt_incidents@sebi.gov.in* within 6 hours. However, necessary details of the incidents shall be reported on SEBI Incident Reporting Portal within 24 hours. Stock Brokers/ Depository Participants shall also report the incidents to Stock Exchanges/ Depositories along with SEBI and CERT-In within 6 hours of noticing/ detecting such incidents or being brought to notice about such incidents. All other cybersecurity incident(s) shall be reported to SEBI, CERT-In and NCIIPC (as applicable) within 24 hours.
2. REs shall share Threat Intelligence data that is collected, processed, and analysed to gain insights into the motives and behaviour (of the threat actor), target, attack pattern, etc. on SEBI Incident Reporting portal.
3. The incident shall also be reported to CERT-In in accordance with the guidelines/ directions issued by CERT-In from time to time. Additionally, the REs, whose systems have been identified as "Protected system" by NCIIPC shall also report the incident to NCIIPC.
4. The quarterly reports containing information on cyber-attacks, threats, cybersecurity incidents and breaches experienced by REs and measures taken to mitigate vulnerabilities, threats and attacks including information on bugs/ vulnerabilities, threats that may be useful for other REs and SEBI, shall be submitted to SEBI within 15 days from the quarter ended June, September, December and March of every year.
5. Such details, which are deemed useful for sharing with other REs, in a masked manner, shall be shared using mechanism to be specified by SEBI from time to time. While sharing the above-mentioned sensitive information, TLP may be followed with four levels of sensitivity: white, green, amber, or red.
6. During the processing of reported incidents by SEBI, REs shall provide regular reports (such as RCA, forensic analysis report, etc.) on the progress of the incident analysis.

---

### RS.CO.G3 — Communication

- **Standards:** RS.CO.S2
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

5. REs shall notify the customer/ investor, through alternate communication channels, of all transactions including buy/ sell, payment or fund transfer above a specified value determined by the customer/ investor.

---

### RS.IM.G1 — Improvements

- **Standards:** RS.IM.S1
- **Applicability:** mii, qualified, mid-size, small-size
- **Mandatory:** true

1. REs shall periodically review and update their contingency plan, COOP, training exercises, and incident response and recovery plans (including CCMP) to incorporate lessons learned, and strengthen their response capabilities in the event of a future incident/ attack.

> Half-yearly for MIIs and Qualified REs. Once in two years for Mid-size and small-size REs.

**Compliance periodicity:** Review/update contingency plan, COOP — Annually (Table 15, row 15).

---

### RS.IM.G2 — Improvements

- **Standards:** RS.IM.S1
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

2. Post occurrence of cybersecurity incident (if any), REs shall update their response and recovery plan (including CCMP) to improve their cyber resilience and incorporate the learnings from the cybersecurity incident.

---

### RS.MA.G1 — Incident Management

- **Standards:** RS.MA.S1
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. All REs shall formulate an up-to-date CCMP in line with national CCMP of CERT-In.
2. CCMP shall be approved by Board/ Partners/ Proprietor of REs.
3. Incident Response Management
   a. All REs shall develop an Incident Response Management Plan as part of their CCMP.
   b. The response plan shall define responsibilities and actions to be performed by its employees and support/ outsourced staff in the event of a cyber-attack or cybersecurity incident.
   c. REs shall have a SOP for handling cybersecurity incident response and recovery for the various cybersecurity attacks.
   d. MIIs shall have a SOP for cybersecurity incidents reported to them by the REs under their supervision.
   e. SOP for reporting of cybersecurity incidents to SEBI is attached at Annexure-O. The same shall be adhered to.

---

## 6. RECOVER

### RC.RP.G1 — Recovery Planning

- **Standards:** RC.RP.S1
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. The response and recovery plans of the REs shall include scenario-based classifications. REs shall build their own response and recovery plan as per their business model and include the same in their CCMP.
2. The response and recovery plan of the REs shall have plans for the timely restoration of systems affected by incidents of cybersecurity incidents/ attacks or breaches (for instance, offering alternate services or systems to customers). Tests shall be designed to challenge the assumptions of response, resumption and recovery practices, including governance arrangements and communication plans. These tests shall include all stakeholders such as critical service providers, vendors, other linked REs, etc.
3. An indicative (but not exhaustive and limited to) recovery plan to be followed by the REs has been attached at Annexure-C.

---

### RC.RP.G3 — Recovery Planning

- **Standards:** RC.RP.S2
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. In the event of disruption of any one or more of the *critical systems*, the RE shall, within 30 minutes of the incident, declare that incident as 'Disaster' based on the business impact analysis. Accordingly, the RTO shall be two (2) hours as recommended by IOSCO for the resumption of critical operations. The RPO shall be 15 minutes for all REs. The recovery plan shall be scenario-based and in line with the RTO and RPO specified.

---

### RC.RP.G5 — Recovery Planning

- **Standards:** RC.RP.S3
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. All REs shall conduct suitable periodic drills to test the adequacy and effectiveness of the response and recovery plan.

**Compliance periodicity:** Cybersecurity scenario-based drill exercise — Annually (Table 15, row 14).

---

### RC.RP.G6 — Recovery Planning

- **Standards:** RC.RP.S4
- **Applicability:** mii, qualified, mid-size, small-size, self-certification
- **Mandatory:** true

1. A backup and recovery plan shall be formulated by the REs and approved by their respective *IT Committee for REs*. The backup and recovery plan shall include policies and software solutions that work together to maintain business continuity in the event of a security incident. Such plan shall include guidance on restoration of data with the backup software used by the RE.
2. The backup and recovery policy shall include backup of data as well as backup of server images.
3. The backup of data and server images shall be maintained at off-site locations to keep backup copies intact and unbroken.
4. RTO and RPO, as prescribed by SEBI from time to time, shall be included in the recovery plan for the restoration of systems after cybersecurity incidents.

---

## 7. EVOLVE

No mandatory guidelines from the EVOLVE function apply to small-size REs.
