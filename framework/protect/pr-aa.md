---
code: PR.AA
title: Identity Management, Authentication, and Access Control
goal: ANTICIPATE
function: PROTECT
version: "1.0"
source: CSCRF
objective: >
  Access to physical and logical assets and associated facilities is limited to
  authorized users, processes and devices, and is managed commensurate
  with the assessed risk of unauthorized access.
standards:
  - id: PR.AA.S1
    text: >
      Identities and credentials are issued, managed, verified, revoked, and
      audited for authorized devices, users and processes.
  - id: PR.AA.S2
    text: >
      Network integrity is protected (through measures such as network
      segregation, network segmentation, etc.).
  - id: PR.AA.S3
    text: >
      While granting access permissions and authorizations to resources (both
      on premise and cloud) of the organization, *Principle of Least Privilege*
      shall be followed along with segregation of duties.
  - id: PR.AA.S4
    text: >
      REs shall follow Zero Trust Model to allow individuals, devices, and
      resources to access organization's resources.
  - id: PR.AA.S5
    text: >
      Access rights shall be reviewed and documented on a periodic basis.
      Maker-Checker framework shall be implemented for granting, revoking,
      and modifying user rights in applications, databases, etc.
  - id: PR.AA.S6
    text: >
      A comprehensive authentication policy shall be documented and
      implemented. Identities shall be proofed and bound to credentials and
      asserted in interactions. Users, devices, and other assets are
      authenticated (single-factor or multifactor) commensurate with the risk of
      the transaction (e.g., individuals' security and privacy risks and other
      organizational risks).
  - id: PR.AA.S7
    text: >
      All *critical systems* shall have MFA implemented for all users accessing
      from untrusted network to trusted network.
  - id: PR.AA.S8
    text: >
      A comprehensive log management policy shall be documented and
      implemented.
  - id: PR.AA.S9
    text: >
      User logs shall be uniquely identified and stored for a specified period.
  - id: PR.AA.S10
    text: >
      Physical access to assets is managed, monitored, and protected. Physical
      access to the *critical systems* shall be monitored and recorded on a
      continuous basis. Individuals shall be screened before granting access to
      RE's organizational information and information systems.
  - id: PR.AA.S11
    text: >
      Privileged users' activities shall be reviewed periodically. Access
      restriction shall be there for employees as well as third-party service
      providers. If it is required to grant access, it shall be for the limited time-
      period, on need-to-know basis and shall be subject to stringent
      supervision and monitoring.
  - id: PR.AA.S12
    text: >
      Remote access to assets shall be strictly tracked and administered.
  - id: PR.AA.S13
    text: >
      A comprehensive data-disposal and data-retention policy shall be
      documented and implemented.
  - id: PR.AA.S14
    text: >
      Comprehensive SOPs shall be documented for handling storage media
      devices and their disposal.
  - id: PR.AA.S15
    text: >
      Access control for using systems such as endpoint devices, networks,
      APIs, removable media, laptops, mobiles, etc. shall be defined and
      implemented.
  - id: PR.AA.S16
    text: >
      Mobile applications shall be properly vetted against security requirements,
      and thoroughly tested before deployment.
  - id: PR.AA.S17
    text: >
      API security with proper authentication and authorization mechanisms
      shall be defined and implemented.
---

## Guidelines

### PR.AA.G1
- **standards:** [PR.AA.S1, PR.AA.S2, PR.AA.S3, PR.AA.S7, PR.AA.S9]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

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

### PR.AA.G2
- **standards:** [PR.AA.S1, PR.AA.S2, PR.AA.S3, PR.AA.S7, PR.AA.S9]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

3. Access Controls, Password Policy/ Authentication Mechanism
   a. PIM solution or PIM process shall be implemented to keep track of privileged access.
   b. REs shall implement an access policy which addresses strong password controls for users' access to systems, applications, networks and databases, etc. Illustrative examples for this are given in Annexure-G.
   c. REs shall formulate an Internet access policy to monitor and regulate the use of internet and internet based services such as social media sites, cloud-based internet storage sites, etc. within the critical IT infrastructure of REs.
   d. REs shall deploy controls and security measures to supervise staff with elevated system access entitlements (such as admin or privileged users). Such controls and measures shall inter-alia include restricting the number of privileged users, periodic²⁷ review of privileged users' activities, disallow privileged users from accessing systems logs in which their activities are being captured, strong controls over remote access by privileged users, etc.
4. Network Security Management
   a. REs shall apply appropriate network segmentation/ isolation techniques to restrict access to the sensitive information, hosts and services. Segment to segment access shall be based on strong access control policy and principle of least privilege.
   b. REs shall install network security devices, such as WAF, proxy servers, IPS, etc. to protect their IT infrastructure which is exposed to the internet, from security exposures originating from internal and external sources.
   c. REs shall deploy web and email filters on the network. These devices shall be configured to scan for known bad domains, sources, and addresses, block these before receiving and downloading message and filter out emails with known malicious indicators, such as known malicious subject lines, and block suspicious Internet Protocol (IP) addresses, malicious domains/URLs at the firewall. All emails, attachments, and downloads both on the host and at the mail gateway shall be scanned with a reputable antivirus solution.
   d. Network devices of REs shall be configured in line with whitelist approach of IPs, ports and services for inbound and outbound communication with proper ACL implementation.
   e. REs shall implement DNS filtering services to ensure clean DNS traffic is allowed in the environment. DNS security extension for secure communication shall be used.
   f. Management of critical servers/ applications/ services/ network elements shall be restricted through enterprise identified intranet systems.
   g. REs shall implement SPF, DMARC, and DKIM for email security.
   h. Email protection shall include (but not limited to) best practices like strong password protection, MFA, spam filtering, email encryption, secure email gateway, permissible attachments types, etc.
   i. REs shall block malicious domains/IPs after diligently verifying them without impacting the operations. CSIRT-Fin/ CERT-In advisories which are published periodically shall be referred for latest malicious domains/ IPs, C&C DNS and links.
   j. REs shall maintain an up-to-date and centralised inventory of authorised devices connected to REs' network (within/ outside RE's premises) and authorised devices enabling the REs' network. The REs may consider implementing solutions to automate network discovery and management.

> ²⁷ Refer Table 15 in 'CSCRF Compliance, Audit Report Submission, and Timelines' section.

### PR.AA.G3
- **standards:** [PR.AA.S1, PR.AA.S2, PR.AA.S3]
- **applicability:** [stock-brokers, depository-participants]
- **mandatory:** true

1. Stock Brokers who are providing algorithmic trading facilities shall take adequate measures to isolate and secure the perimeter and connectivity to the servers running algorithmic trading applications.

> ⚠️ **Non-standard applicability:** "Stock Brokers" and "Depository Participants" — these are conditional tags based on RE type, not RE size category.

### PR.AA.G4
- **standards:** [PR.AA.S4, PR.AA.S5]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall follow zero-trust security model in such a way that access (from within or outside REs' network) to their *critical systems* is by default denied by default and allowed only after proper authentication and authorization.
2. Delegated access and unused tokens shall be reviewed and cleaned at least on a quarterly basis.

### PR.AA.G5
- **standards:** [PR.AA.S6]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Effective authentication policy shall be implemented with the defined complexity of the password.
2. All generic user IDs and email IDs which are not in use shall be removed after the use.

### PR.AA.G6
- **standards:** [PR.AA.S6]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

3. REs shall implement strong password controls for users' access to systems, applications, networks, databases, etc. Password controls shall include (but not limited to) a change of password upon first login, minimum password length and history, password complexity as well as maximum validity period.
4. The user credential data shall be stored using strong hashing algorithms.

### PR.AA.G7
- **standards:** [PR.AA.S8]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. REs are advised to ensure that all logs sources are being identified and their respective logs are being collected. An indicative list of types of log data to be collected by REs is as follows: system logs, application logs, network logs, database logs, security logs, performance logs, audit trail logs, and event logs.
2. Strong log retention policy shall be implemented as per government guidelines/ policies/ laws/ circulars/ regulations, etc. issued by SEBI/ GoI such as IT Act 2000, Digital Personal Data Protection Act (DPDP) 2023, and as required by CERT-In, NCIIPC or any other government agency.
3. In order to identify unusual patterns and behaviours, monitoring of all logs of events and incidents shall be done.

### PR.AA.G8
- **standards:** [PR.AA.S10, PR.AA.S11, PR.AA.S12]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. Physical Security
   a. Physical access to the *critical systems* shall be restricted to a minimum and shall be provided only to authorized officials. Physical access provided to third-party service providers shall be properly supervised by ensuring at the minimum that third-party service providers are accompanied at all times by authorized employees.
   b. Employees of REs shall be screened before granting access to organizational information and information systems. Physical access to the *critical systems* shall be revoked immediately if the same is no longer required.
   c. All REs shall ensure that the perimeter of the critical equipment's room, if any, are physically secured and monitored by employing physical, human and procedural controls such as the use of security guards, CCTVs, card access systems, mantraps, bollards, etc. wherever appropriate.
2. Remote Support Service Security
   a. As many OEMs and their service partners as well as System Integrators provide remote support services to organisations, REs shall ensure that these services are well-governed, controlled, logged and an oversight is maintained on all the activities done by remote support service providers. The above shall be complemented by regular monitoring and audit to ensure compliance of the defined policies for privileged users and remote access.
   b. REs shall ensure secure usage of RDP in IT systems. Further, it shall be implemented strictly on a need-to-use basis, and it must employ MFA. Remote access, if necessary, shall be given to authorised personnel from whitelisted IPs for a predefined time period, and with a provision to log all activities.
   c. Employees and third-party service providers who may be given authorized access to the *critical systems*, networks and other IT resources of REs shall be subject to stringent supervision, monitoring and access restrictions.

### PR.AA.G9
- **standards:** [PR.AA.S10, PR.AA.S11, PR.AA.S12]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

   d. Environmental controls (temperature, water, smoke, etc.), service availability alerts (power supply, servers, etc.), access logs, etc. shall be monitored.

### PR.AA.G10
- **standards:** [PR.AA.S13, PR.AA.S14]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. REs shall formulate a data-disposal and data-retention policy to identify the value and lifetime of various parcels of data.
2. REs shall frame suitable policies for disposal of storage media and systems. The critical data/ information on such devices and systems shall be removed by using methods such as wiping/ cleaning/ overwrite, degauss/ crypto shredding/ physical destruction as applicable.

### PR.AA.G11
- **standards:** [PR.AA.S15]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. Endpoint security
   a. Solutions like EPP, EDR, XDR, anti-malware software etc. shall be implemented to detect threats and attacks on endpoint devices, and to enable immediate response to such threats and attacks. Further, REs shall ensure that signatures are updated on all IT systems.
   b. Solutions like IPS/ NG-IPS shall be used to continuously monitor the organizations' network for malicious activities.
   c. PowerShell and local admin rights shall be disabled by default on endpoint machines and shall be used only for a specific purpose and for a limited time.
2. Guidance on usage of Active Directory (AD) servers
   a. REs shall regularly review the AD to locate and close existing backdoors such as compromised service accounts, which often have administrative privileges and are a potential target of attacks.
   b. REs shall undertake the penetration testing activity for known AD Domain Controller abuse attacks. Weaknesses shall be remediated on topmost priority.
3. Restricted use of removable media and electronic devices
   a. REs shall define and implement policy for restriction and secure use of removable media (such as USB, external hard disks, etc.) and electronic devices (such as laptops, mobile devices, etc.). REs shall ensure secure erasure of data so that no data is in recoverable form on such media and electronic devices after use.

### PR.AA.G12
- **standards:** [PR.AA.S15]
- **applicability:** [mii]
- **mandatory:** true

4. Secure Domain Controllers (DCs)

   Threat actors often target and use DCs as a staging point to spread ransomware network-wide.
   a. REs shall ensure that DCs are patched as and when patch is released and it must be reviewed on a quarterly basis to ensure the implementation of the same.
   b. REs shall ensure that no unnecessary software is installed on DCs, as these can be leveraged to run arbitrary code on the system.
   c. REs shall ensure that access to DCs should be restricted to the Administrators group. Users within this group shall be limited and have separate accounts used for day-to-day operations with non-administrative permissions.
   d. REs shall ensure that DC host firewalls are configured to prevent direct internet access.

### PR.AA.G13
- **standards:** [PR.AA.S16, PR.AA.S17]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. API security
   a. API security protects against vulnerabilities and misconfigurations in the APIs and prevents their misuse. Thus, effective API security strategies like rate limiting, throttling, etc. shall be used while developing APIs to prevent overuse or abuse. If APIs have been provided by MIIs and consumed by REs then onus of ensuring API security shall be on MIIs. MIIs shall have API security solutions in place for securing services and data transmitted through APIs.
   b. Proper access management, and effective authentication and authorization shall be done to ensure that only the desired entities have access to the APIs.
   c. OWASP documentation for developing APIs shall be followed and OWASP top 10 API security risks shall be mitigated.
   d. Connecting to entities via APIs shall be strictly on a whitelist-based approach.
2. Mobile Application Security
   a. The mobile application shall perform root detection and root cloaking detection. The application shall not work on emulators or virtual devices.
   b. REs shall explore the feasibility of implementing a code that checks if the device is rooted/ jailbroken prior to the installation of the mobile application and disallow the mobile application to install/ function if the phone is rooted/ jailbroken.
   c. Device Policy enforcement such as detection of developer option, USB debugging, Mock Location, time settings manipulation, etc. shall be configured.
   d. Mobile application shall check new network connections or connections for unsecured networks like VPN connection, proxy and unsecured Wi-Fi connections.
   e. Mobile application shall have anti-malware capabilities covering application spoofing, RAT, screen mirroring, overlay malwares, key loggers, tap jacking, etc.
   f. Controls to prevent reverse engineering and application tampering shall be implemented in the mobile applications. These controls shall also validate the signature during runtime for authenticity of the application.
   g. Mobile application shall perform checksum validation and the checksum of applications shall be published in public domain.
   h. Mobile application shall identify the presence of active remote access, screen mirroring, active voice call, alert users, etc. to prevent online frauds.
   i. Mobile application shall require re-authentication whenever the device of the application remains unused for a designated period and also each time the investor/ user launches the application.
   j. Mobile application shall not store/ retain sensitive personal/ investor authentication information such as user IDs, passwords, keys, hashes, hard coded reference, etc. on the device and the application shall also securely wipe out any sensitive investor/ user information from memory when the investor/ user exits the application.
   k. Mobile application shall be secured against common vulnerabilities such as SQL injection, etc.
   l. REs shall ensure that the usage of raw SQL queries in mobile application to fetch or update data from databases is avoided. Additionally, sensitive information shall be written to the database in an encrypted form.

### PR.AA.G14
- **standards:** [PR.AA.S16, PR.AA.S17]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** false

   m. Mobile application shall implement device-binding solution to create a unique digital identity based on device, mobile number and SIM.
   n. OWASP – MASVS shall be referred for implementing mobile application security and other protection measures.
   o. REs shall consider implementing measures such as installing a "containerized" app on mobile/ smart phones for exclusive business use that is encrypted and separated from other smartphone data/ applications; implement measures to initiate a remote wipe on the containerized app, rendering the data unreadable, in case of requirement may also be considered.

### PR.AA.G15
- **standards:** [PR.AA.S16, PR.AA.S17]
- **applicability:** [mii, qualified]
- **mandatory:** false

3. Guidelines for Application Security and Emerging Technologies

   REs shall prepare SOPs for open source application security and concerns from emerging technologies like Generative AI security.

## Annexure

### Box Item 8: Application Programming Interface (API) security

*Application Programming Interface:* A system access point or library function that has a well-defined syntax and is accessible from application programs or user code to provide well-defined functionality.

Application Programming Interface (API) is an interface that allows software applications to interact and communicate with each other using a set of definitions and protocols.

Since APIs have become key component of modern software application development, the practice of preventing or mitigating attacks on APIs has also become critical. API security refers to processes and solutions to mitigate vulnerabilities and risks in APIs. OWASP has released API Top 10 security threats after a sharp increase in API-related security threats.

API security guidelines broadly include the following categories:

1. **API Discovery:** Knowing how many APIs are being exposed and what APIs are being used are critical steps in securing APIs.
2. **Access Management:** Enforcing strong authentication and authorization mechanisms enable secure verification of end-user client identity as well as limits the information access/ transfer to users/ systems. Implementing robust and reliable access management measures discourages use of open APIs, which increase the exposure and vulnerability of the data to potential breaches, fraud or misuse.
3. **Rate Limiting:** Rate limiting and throttling protects bandwidth of the systems by enforcing a limit on how often an API is called and also prevents API abuse.
4. **Secure API development:** Incorporating secure-by-design strategy safeguards APIs and prevents misconfigurations and flaws.
5. **Zero-trust approach:** With zero-trust approach, API security assumes no implicit trust for any entity. Further, it also mitigates potential OWASP Top 10 API security risks.
