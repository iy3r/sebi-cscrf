---
code: ID.AM
title: Asset Management
goal: ANTICIPATE
function: IDENTIFY
version: "1.0"
source: CSCRF
objective: >
  The data, personnel, devices, systems, and facilities that enable the RE to
  achieve its business purposes are identified and managed consistently in
  accordance with their relative importance to organizational objectives and
  the RE's risk strategy.
standards:
  - id: ID.AM.S1
    text: >
      Physical devices, digital assets (such as URLs, domain names,
      applications, APIs, etc.), shared resources (including cloud assets) and
      other interfacing systems within the organization are inventoried in a
      time bound manner.
  - id: ID.AM.S2
    text: >
      Organizational communication, data flows and encryption methods shall be
      mapped and inventoried with respect to all IT systems and network
      resources.
  - id: ID.AM.S3
    text: >
      REs shall ensure that no shadow IT assets are present in the
      organization.
  - id: ID.AM.S4
    text: >
      Board/ Partners/ Proprietor shall approve the list of *critical systems*.
  - id: ID.AM.S5
    text: >
      Inventories of data, and corresponding metadata for designated data
      types are maintained.
  - id: ID.AM.S6
    text: >
      All inventoried IT assets and data are managed throughout their
      lifecycles.
---

## Guidelines

### ID.AM.G1
- **standards:** [ID.AM.S1, ID.AM.S4]
- **applicability:** [mii, qualified, mid-size, small-size, self-certification]
- **mandatory:** true

1. All REs shall identify and classify *critical systems* as defined in this framework based on
   their sensitivity and criticality for business operations, services and data management.
   The Board/ Partners/ Proprietor of the REs shall approve the list of *critical systems*.
2. All REs shall maintain an up-to-date inventory of their (including but not limited to)
   hardware and systems, software, digital assets (such as URLs, domain names,
   application, APIs, etc.), shared resources (including cloud assets), interfacing systems
   (internal and external), details of its network resources, connections to its network and
   data flows.
3. Any additions/ deletions or changes in existing assets shall be reflected in the asset
   inventory within 3 working days.
4. For conducting criticality assessment of assets, REs shall take the following steps
   (including but not limited to):
   a. Maintain a comprehensive asset inventory
   b. Conduct threat modelling (based on risk assessment)
   c. Conduct vulnerability assessment
5. REs shall prepare and maintain an up-to-date network architecture diagram at the
   organisational level including wired and wireless networks.

### ID.AM.G2
- **standards:** [ID.AM.S1, ID.AM.S4]
- **applicability:** [mii]
- **mandatory:** true

6. REs shall put in place configuration management database approach to:
   a. Understand and inventorise their IT assets - both logical (e.g., data, software)
      and physical (e.g., hardware).
   b. Understand which data or systems are most critical for providing critical services
      as well as any associated interdependencies.

### ID.AM.G3
- **standards:** [ID.AM.S6]
- **applicability:** [mii, qualified, mid-size]
- **mandatory:** true

7. All IT assets shall be inventoried in ITSM tool.
8. REs shall integrate cybersecurity considerations into product life cycles.
