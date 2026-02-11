---
title: Access Control and Authentication Policy
entity: Zenith Broking Pvt Ltd
category: mid-size
cscrf_version: "1.0"
cscrf_standards: [PR.AA.S1, PR.AA.S2, PR.AA.S3]
cscrf_guidelines: [PR.AA.G1, PR.AA.G2, PR.AA.G3]
generated_date: "2026-01-15"
review_cycle: Quarterly
---

# Access Control and Authentication Policy

## 1. Purpose

This policy establishes access control and authentication requirements for Zenith Broking Pvt Ltd to protect information assets and critical systems in accordance with SEBI CSCRF PR.AA objectives. It ensures that access to systems, applications, and data is granted on a need-to-know basis with appropriate authentication controls.

## 2. Scope

This policy applies to all information systems operated by Zenith Broking Pvt Ltd, including:
- Trading platforms and order management systems
- Back-office and settlement applications
- Client data repositories and CRM systems
- Network infrastructure and remote access gateways
- Cloud-hosted services and third-party integrations

All employees, contractors, and third-party users with system access are subject to this policy.

## 3. Policy Statements

### 3.1 Access Governance (PR.AA.G1 — Mandatory)

1. All user access rights shall be granted based on the principle of least privilege and approved by the designated system owner for a defined duration (PR.AA.S1).
2. Access rights shall be reviewed quarterly by the CISO in coordination with department heads. Reviews shall verify that each user's access remains necessary for their current role.
3. User access shall be revoked or modified within 24 hours of role change, transfer, or termination. HR shall notify IT Security of all personnel changes via the established workflow.
4. A centralized access register shall be maintained documenting all active access grants, approval dates, and review dates.

### 3.2 Privileged Access Management (PR.AA.G2 — Mandatory)

1. Privileged accounts (system administrators, database administrators, network engineers) shall be governed under a separate elevated-access policy with enhanced monitoring (PR.AA.S2).
2. All privileged activities shall be logged with tamper-evident audit trails and reviewed weekly by the CISO or designated security officer.
3. Privileged access shall require multi-factor authentication (MFA) for all sessions. Shared privileged accounts are prohibited; each administrator shall use a named account.
4. Emergency or break-glass access procedures shall be documented, require post-incident review within 48 hours, and be reported to the IT Committee.

### 3.3 Authentication Standards (PR.AA.G3 — Mandatory)

1. All user-facing systems shall enforce MFA using at least two independent factors (PR.AA.S3).
2. Password complexity requirements: minimum 12 characters, mixed case, numeric, and special characters. Passwords shall be rotated every 90 days.
3. Failed login attempts shall trigger account lockout after 5 consecutive failures. Lockout duration shall be a minimum of 30 minutes or until manual reset by IT Security.
4. Session timeouts shall be enforced: 15 minutes for trading systems, 30 minutes for back-office applications.

## 4. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| CISO | Policy owner; quarterly access reviews; privileged access oversight |
| Head of IT | Technical implementation of access controls and MFA |
| Department Heads | Approve access requests for their teams; validate quarterly reviews |
| HR | Notify IT Security of all joiners, movers, and leavers within 24 hours |
| System Owners | Maintain access registers for their systems; approve access grants |
| All Users | Comply with authentication requirements; report unauthorized access |

## 5. Review and Update

- This policy shall be reviewed quarterly in accordance with Table 15 periodicity requirements for mid-size REs.
- Reviews shall be documented with findings, changes made, and approval by the CISO.
- Reporting authority: SEBI via designated compliance channel (Tables 16-23).

## 6. CSCRF Traceability Matrix

| Section | CSCRF Standard | CSCRF Guideline | Requirement Summary |
|---|---|---|---|
| 3.1 Access Governance | PR.AA.S1 | PR.AA.G1 | Least-privilege access lifecycle with periodic review |
| 3.2 Privileged Access | PR.AA.S2 | PR.AA.G2 | Elevated access governance, logging, and MFA |
| 3.3 Authentication | PR.AA.S3 | PR.AA.G3 | MFA enforcement, password policy, lockout controls |
