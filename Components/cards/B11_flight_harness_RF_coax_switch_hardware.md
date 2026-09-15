# B11 — Harness, RF coax, three-switch hardware allowance and strain relief

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B11 |
| Supplier | Integration vendor |
| Quantity | 1 |
| Procurement type | Custom integrated harness/hardware lot |
| Project unit estimate, low/base/high | €500 / €900 / €1,500 |
| Public price evidence | No product price; custom fabrication planning allowance |
| Order/quote URL | Not applicable—complete the harness drawing and issue an RFQ to a qualified space-harness/integration vendor. |
| Ordering route | Procure only from a released wire list, connector/contact schedule, routing drawing and workmanship/test specification. |
| Availability | NOT DESIGN RELEASED. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 65 g | PROJECT ALLOCATION |
| Envelope | Unknown; routing volume, lengths, bend radii and connector envelopes are not released | UNKNOWN |
| Electrical power / generation | No intentional load; must carry all H01–H13 currents with bounded voltage drop. RF path target ≤1 dB total loss. | PROJECT REQUIREMENT |

## Supplier facts retained by the project

- No supplier, part number, quote or manufactured article exists in the current record.

## Exact project configuration

- Implement documented H01–H13 without unreviewed stack-through mating.
- Use positively retained/keyed connections, strain relief and approved flight workmanship.
- Include 50 Ω radio coax and the allowed three separation-switch/RBF hardware scope; subtract overlaps after supplier quotes.

## Mechanically/electrically relevant interfaces

- H01–H13 in engineering/03_Interfaces.md
- Every powered/data subsystem
- Structure bonding and mechanical supports

## Procurement-release blockers

- Full pin map, mating connector part numbers, contact genders and cavity assignments
- Wire/coax types, gauges, shielding, lengths, derating, bend radii and voltage drops
- Switch part numbers, placement, travel, force and inhibit topology
- Grounding/bonding/shield termination and EMC behavior
- Mass roll-up, workmanship standard, continuity/hipot/insulation/RF acceptance tests

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- procurement/BOM.csv
- engineering/03_Interfaces.md
- engineering/04_Mechanical_Thermal_Radiation.md
- engineering/06_Integration_and_Verification.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
