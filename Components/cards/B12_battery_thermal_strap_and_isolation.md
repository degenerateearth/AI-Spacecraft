# B12 — Battery thermal strap/isolation, approved films and mounting

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B12 |
| Supplier | Integration vendor |
| Quantity | 1 |
| Procurement type | Custom thermal/mechanical integration lot |
| Project unit estimate, low/base/high | €200 / €400 / €800 |
| Public price evidence | No product price; custom material/fabrication planning allowance |
| Order/quote URL | Not applicable—select materials after thermal analysis and issue an RFQ/purchase order from a released drawing and material list. |
| Ordering route | Procure characterized materials and fabricated strap/mount only after thermal-balance inputs close. |
| Availability | NOT DESIGN RELEASED. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 35 g | PROJECT ALLOCATION |
| Envelope | Unknown; represented within surrounding stack allocations only | UNKNOWN pending thermal design and vendor geometry |
| Electrical power / generation | No separate electrical load is allocated; EPS heater is budgeted at 0.10 W orbit average and 1 W instantaneous equivalent at 10% duty | PROJECT THERMAL/POWER ALLOCATION; heater is part of B02 |

## Supplier facts retained by the project

- No material, supplier or part number has been selected; ‘approved films’ is a requirement, not a component selection.

## Exact project configuration

- Provide a characterized conductive path and deliberate isolation for the B02 integrated battery.
- Retain battery mechanically independent of electrical terminals.
- Support project battery target +5 to +35 °C in normal operation and charge inhibit outside the approved range.

## Mechanically/electrically relevant interfaces

- B02 battery/EPS
- B01 structure
- Thermal coatings/films on available non-cell area

## Procurement-release blockers

- Thermal network and required conductance
- Strap material/cross-section/attachment and contact resistance
- Isolation film type, thickness, outgassing, dielectric and radiation evidence
- Heater actual power/control and stuck-on/off protection
- Fasteners, torque, workmanship, mass and acceptance test

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- procurement/BOM.csv
- engineering/02_Budgets_and_Analyses.md
- engineering/04_Mechanical_Thermal_Radiation.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
