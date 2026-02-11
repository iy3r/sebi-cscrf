---
code: PR.DS
title: Data Security
goal: ANTICIPATE
function: PROTECT
version: "1.0"
source: CSCRF
objective: >
  Information and records (data) are managed consistent with the
  organization's risk strategy to protect the *Confidentiality*, *Integrity*, and
  *Availability* of information.
standards:
  - id: PR.DS.S1
    text: >
      Data-at-rest and Data-in-transit shall be protected. Strong data
      protection measures (for both at-rest and in-transit data), with industry
      standard encryption algorithms, shall be put in place by all REs. Along
      with data-at-rest and data-in-transit, MIIs shall also explore solutions for
      encrypting data while it is being used/ processed.
  - id: PR.DS.S2
    text: >
      REs shall classify their data into *Regulatory Data* and *IT and
      Cybersecurity Data* as defined in this framework. REs shall keep the
      *Regulatory Data* and *IT and Cybersecurity Data* available and easily
      accessible in legible and usable form, within the legal boundaries of
      India.
  - id: PR.DS.S3
    text: >
      Adequate capacity to ensure *Availability* of data shall be maintained.
  - id: PR.DS.S4
    text: >
      Measures against data leaks shall be implemented. Appropriate tools
      shall be put in place to prevent any data leakage.
  - id: PR.DS.S5
    text: >
      The development and testing environment(s) shall be separated from the
      production environment. For the development of critical software/
      applications development, there shall be atleast one non-production
      environment to perform rigorous testing before deploying them to the
      production environment.
  - id: PR.DS.S6
    text: >
      MIIs shall put in place integrity mechanisms to verify software, firmware,
      and information integrity of its *critical systems* and other systems
      connected to its *critical systems*.
---

## Guidelines

### PR.DS.G1
- **standards:** [PR.DS.S1, PR.DS.S2, PR.DS.S3]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. Data and Storage Devices security
   a. Data shall be encrypted in motion, at rest and in-use by using strong encryption methods. Data-in-use encryption shall be applicable for cloud deployment (refer Annexure-J). Layering of Full-disk Encryption (FDE) along with File-based Encryption (FBE) shall be used wherever possible. REs shall use industry standard, strong encryption algorithms (e.g., RSA, AES, etc.) wherever encryption is implemented. Illustrative measures in this regard are given in Annexure-H and Annexure-I.
   b. REs shall deploy Data Loss Prevention (DLP) solutions/ processes.
   c. REs shall implement measures to prevent unauthorized access, copying, transmission of data/ information held in contractual or fiduciary capacity. It shall be ensured that confidentiality of information is not compromised during the process of exchanging and transferring information with external parties. Illustrative measures to ensure security during transportation of data over the internet are given in Annexure-I.
   d. The information security policy shall also cover use of devices such as mobile phones, photocopiers, scanners, etc., which can be used for capturing and transmission of sensitive data within their IT infrastructure. For instance, defining access policies for personnel, network connectivity for such devices, etc.
   e. REs shall allow only authorized data storage device within their IT infrastructure through appropriate validation processes.

### PR.DS.G2
- **standards:** [PR.DS.S1, PR.DS.S2, PR.DS.S3]
- **applicability:** [mii, qualified, mid-size, small-size]
- **mandatory:** true

2. Application Security in Customer Facing Applications:
   a. Application security for Customer facing applications offered over the Internet such as IBTs (Internet Based Trading applications), portals containing sensitive or private information and Back office applications (repository of financial and personal information offered by REs to Customers) are paramount as they carry significant attack surfaces by virtue of being available publicly over the Internet for mass use. An illustrative list of measures for ensuring security in such applications is provided in Annexure-G.

### PR.DS.G3
- **standards:** [PR.DS.S1, PR.DS.S2, PR.DS.S3]
- **applicability:** [mii, qualified, mid-size, small-size]
- **mandatory:** true

1. REs shall implement suitable mechanisms, including generation of appropriate alerts, to monitor capacity utilisation on a real-time basis and shall proactively address issues pertaining to their capacity needs.
2. For capacity planning and monitoring, REs shall comply with circulars/ guidelines on capacity planning issued by SEBI (and updated from time to time).

### PR.DS.G4
- **standards:** [PR.DS.S1, PR.DS.S2, PR.DS.S3]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. REs shall keep the *Regulatory Data* available and easily accessible in legible and usable form, within the legal boundaries of India. However, for the investors whose country of incorporation is outside India, the REs shall keep the original data, available and easily accessible in legible and usable form, within the legal boundaries of India. Further, if the *Regulatory Data* retained within India is not in readable form, the REs must maintain an application/system to read/ analyse the retained data.
2. The *IT and Cybersecurity Data* which is sent to/ consumed by global/ international SOC of the REs and SaaS based cybersecurity solutions have been exempted from being maintained within the legal boundaries of India. For above mentioned SaaS based cybersecurity solutions and SOC offerings utilized by REs where the data is not processed/stored within the legal boundaries of India, such data shall be classified, assessed and periodically reviewed (at least once in a year) by the respective *IT Committee for REs* or equivalent body of the RE. Additionally, such *IT and Cybersecurity Data* shall be approved by the Board/ Partners/ Proprietor annually. Further, such data shall be made available to SEBI/ CERT-In/ any other government agency whenever required within a reasonable time not exceeding 48 hours from the time of request.
3. While doing data classification, REs shall adhere to data security standards and guidelines and other government guidelines/ policies/ laws/ circulars/ regulations, etc. issued by SEBI/ GoI such as IT Act 2000, Digital Personal Data Protection Act (DPDP) 2023 or any other law/ circular/ regulation as and when issued.

### PR.DS.G5
- **standards:** [PR.DS.S4]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. REs shall enforce effective data protection, backup, and recovery measures.
2. REs shall block administrative rights on end-user workstations/ PCs/ laptops by default and provide access rights on need basis as per the established process and approvals and for specific duration for which it is required.
3. Security controls for mobile and web applications shall focus on how these applications handle, store, and protect PII and other business related data.
4. Web and mobile applications shall not store sensitive information in HTML hidden fields, cookies, or any other client-side storage to avoid any compromise in the integrity of the data.
5. REs shall renew their digital certificates used in IT systems well in time.
6. REs shall implement measures to control usage of VBA/macros in office documents, control permissible attachment types in email systems.
7. REs shall have a documented data migration policy specifying SOPs and processes for data migration while ensuring data integrity, completeness and consistency.

### PR.DS.G6
- **standards:** [PR.DS.S5]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. For the development of all software/ applications and feature enhancements, there shall be separate production and non-production environments.
2. After development and/ or feature enhancement, SIT shall be done to ensure that the complete software/ application is working as required.
3. During the development phase of any software/application to be used by the REs or customers of REs, it shall be ensured that vulnerabilities identified by best practices baselines such as OWASP, top 25 software security vulnerabilities identified by SANS, etc. are addressed. It is recommended that REs should adopt methodologies like DevSecOps for secure development of their applications/ software.

### PR.DS.G7
- **standards:** [PR.DS.S6]
- **applicability:** [mii, qualified]
- **mandatory:** true

1. REs shall obtain the source codes for all critical applications from their third-party service providers. Where obtaining of the source code is not possible, REs shall put in place a source code escrow arrangement or other equivalent arrangements to adequately mitigate the risk of default by the third-party service provider. REs shall ensure that all product updates and patches/ fixes are included in the source code escrow arrangement.
2. For all the software and applications, where vulnerabilities will be identified at a later date, REs shall ensure that the vulnerabilities shall be mitigated in a time bound manner. REs shall also stipulate timelines in their SLA with their third-party service providers for the timely compliance and closure of identified vulnerabilities.
3. REs shall put in place appropriate third-party service providers (including software vendors) risk assessment process and controls proportionate to their criticality/ risk in order to manage supply chain risks effectively.
4. REs shall ensure that maintenance and necessary support for applications/ software is provided by the third-party service providers (including software vendors) and the same is enforced through a formal agreement.

## Annexure

### Box Item 9: Data Classification

*To ensure the smooth functioning of the securities market as well as sovereign control over data, SEBI has given high priority to security controls on the various kinds of data generated, managed, or processed by the REs. Taking this into consideration, CSCRF mandates REs to set up robust security controls for such data.*

*The data classification given below is technology agnostic, which will lead to a more enabled and strengthened environment for SEBI and REs.*

*CSCRF has defined the following categories of data:*

1. ***Regulatory Data:*** *Regulatory Data includes the following (but not limited to):*
   a. *Data related to core and critical activities of the RE, as well as any supporting/ ancillary data impacting core and critical activities*
   b. *Data with respect to communication between investors and REs through applications (eg. chat communication, messages, emails etc.).*
   c. *Data that is required by the laws/ regulations/ circulars, etc. issued by SEBI and Govt. of India from time to time.*
   d. *Data that is deemed necessary or sensitive by the RE/ SEBI/ central or state government.*
   e. *The Regulatory Data shall be stored in an easily accessible, legible and usable form, within the legal boundaries of India. However, for the investors whose country of incorporation is outside India, the REs shall keep the original data, available and easily accessible in legible and usable form, within the legal boundaries of India. Further, if the copy retained within India is not in readable format, the REs must maintain an application/system to read/ analyse the retained data.*

2. ***IT and Cybersecurity Data:*** *IT and Cybersecurity Data includes the following data (but not limited to):*
   a. *Logs and metadata related to IT systems and their operations. However, such data should not contain the following:*
      i. *Any Regulatory Data, and*
      ii. *Sensitive data such as internal network architecture, vulnerability details, details of admin/ privileged users of REs, password hashes, system configuration, etc.*
   b. *Further, it should not be ordinarily possible to generate regulatory Data from IT and Cybersecurity Data.*

### Box Item 10: Data Localization

*SEBI functions to safeguard the interests of investors and promote the development of the securities market. This includes protecting the REs from all such risks which arise due to threats like single-point of failure, concentration risk, etc. While performing business activities, REs utilise services from third-party service providers. These services include necessary software solutions hosted at the service providers' own and/ or third-party infrastructure. This could lead to business functions becoming more and more dependent on the service providers.*

*The hosted services/ software-as-a-service (SaaS)/ Cloud Service Providers (CSPs) usually store the data (business data, personal data etc.) where the processing of the data occurs. This results into data residing at the service providers' own and/ or third-party infrastructure.*

*While REs do not have a direct control on where their data is stored by the service providers, it is important to note that the REs' data may be stored on servers outside the legal boundaries of India.*

*If the REs' data resides outside the legal boundaries of India, SEBI and its REs may not have sovereign control on it which may cause governance issues and put limitations on the compliance of various laws related to data protection and cybersecurity in the country.*

*In order to protect interests of investors, and SEBI REs and their businesses, SEBI has envisaged data localization. Data localization means that all the data generated (including creation and storage) within the legal boundaries of India remains within the legal boundaries of India. Data localization ensures data sovereignty and data residency together. It will also lead to better governance and oversight.*

*SEBI REs shall ensure that processing and storage of data is done within legal boundaries of India. CSCRF has mandated REs to keep the original Regulatory Data available and easily accessible in legible and usable form, within the legal boundaries of India. However, for the investors whose country of incorporation is outside India, the REs shall keep the original Regulatory Data, available and easily accessible in legible and usable form, within the legal boundaries of India. Further, if the Regulatory Data retained within India is not in readable form, the REs must maintain an application/ system to read/ analyse the retained data. However, the IT and Cybersecurity Data which is to be sent to/ consumed by global/ international SOC of the REs, and SaaS based cybersecurity solutions, has been exempted from being maintained within the legal boundaries of India. For the above-mentioned SaaS based cybersecurity solutions and SOC offerings utilized by the REs (where the data is not processed/ stored within the legal boundaries of India), the IT and Cybersecurity Data sent to such solutions shall be classified, assessed and periodically reviewed (at least once in a year) by the respective IT Committee for REs or equivalent body of the RE. Additionally, such IT and Cybersecurity Data shall be approved by the Board/ Partners/ Proprietor annually.*
