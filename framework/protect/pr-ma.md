---
code: PR.MA
title: Maintenance
goal: ANTICIPATE
function: PROTECT
version: "1.0"
source: CSCRF
objective: >
  Maintenance and repairs of organizational control and information system
  components are performed consistent with policies and procedures.
standards:
  - id: PR.MA.S1
    text: >
      Maintenance and repair of REs' assets shall be performed and logged,
      with approved and controlled tools.
  - id: PR.MA.S2
    text: >
      Remote maintenance of REs' assets shall be approved, logged, and
      performed in a manner that prevents unauthorized access.
  - id: PR.MA.S3
    text: >
      Patches shall be identified and categorized based on their severity.
      Critical patches shall be implemented at the earliest. Patches shall be
      tested in non-production environment before applying to DC and DR.
---

## Guidelines

### PR.MA.G1
- **standards:** [PR.MA.S2]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

1. REs shall ensure proper remote access policy framework incorporating the specific requirements of accessing the enterprise resources (located in the data centre) securely from home using internet connection.
2. REs shall ensure that only trusted client machines shall be permitted to access enterprise IT resources remotely. REs shall put in place appropriate security control measures such as (including but not limited to) host integrity check, binding of MAC address of the device with the IP address, etc. for remote access and telecommuting.
3. REs shall ensure that appropriate risk mitigation mechanisms are put in place whenever remote access of data centre resources is permitted for third-party service providers.
4. REs shall ensure that remote access shall be monitored continuously for any abnormal/ unauthorized access, and appropriate alerts and alarms shall be generated to address this breach before any damage is done.

### PR.MA.G2
- **standards:** [PR.MA.S3]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. REs shall establish and ensure that the patch management procedures include the identification, categorization and prioritization of patches and updates. An implementation timeframe for each category of patches shall be established to apply them in a timely manner.
2. All operating systems and applications shall be updated with the latest patches on a regular basis. As an interim measure for zero-day vulnerabilities, and where patches are not available, virtual patching may be considered for protecting systems and networks. This measure hinders cybercriminals from gaining access to any system through vulnerabilities in end-of-support and end-of-life applications and software. Patches shall be sourced only from the authorized sites of the OEM.
3. REs shall perform comprehensive and rigorous testing of security patches and updates, wherever possible, before deployment into the production environment so as to ensure that application of patches does not impact other systems.
4. All patches shall be tested first in non-production environment which shall be identical to the production environment.
5. Hardware and software of *critical systems* shall be replaced before they reach End-of-Life/End-of-Support.
6. Compensatory controls like virtual patching shall be implemented for legacy systems for a maximum period of 6 months. Further, the constraints due to which virtual patching is done shall be legitimate and documented.
7. Procurement of hardware/software shall be aligned with technology refresh policy of the REs.

### PR.MA.G3
- **standards:** [PR.MA.S3]
- **applicability:** [mii, qualified]
- **mandatory:** true

8. REs shall establish a patch management policy to ensure that all applicable patches (at both PDC and DR Site are identified, assessed, tested and applied to all IT systems/applications in a timely manner. The policy shall be approved by *IT Committee for REs*. Additionally, the above-mentioned policy on patch management shall be reviewed by *IT Committee for REs* atleast on an annual basis.
9. REs shall ensure that post application of any patch/ update, the resources deployed are adequate enough to deliver the expected performance.
10. REs shall also establish processes for tracking patch compliance across all IT systems/ applications and reporting the same to their respective *IT Committee for REs* on a quarterly basis.
11. Based on the criticality of the patches, REs shall ensure that patches are implemented at both PDC and DR site within the upper/ maximum time limit as defined below. However, for emergency patching, patches shall be deployed within timelines as stipulated by the OEMs.

| S. No. | Criticality of Patch | Upper/ maximum Timeline |
|--------|---------------------|------------------------|
| 1 | High | 1 week |
| 2 | Moderate | 2 weeks |
| 3 | Low | 1 month |
