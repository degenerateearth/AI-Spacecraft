# B10 — D1-IF adapter: two 5 V to 3.3 V regulators, isolation and harness routing

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B10 |
| Supplier | Integration vendor |
| Quantity | 1 |
| Procurement type | Project-designed custom assembly using COTS candidate parts |
| Project unit estimate, low/base/high | €800 / €1,500 / €3,000 |
| Public price evidence | No product price; custom NRE/board/assembly/test planning allowance |
| Order/quote URL | Not applicable—release schematic/BOM/Gerbers and issue an RFQ to an integration/PCB assembly vendor. Candidate regulator reference: https://www.ti.com/product/TPSM82823 |
| Ordering route | No purchase is authorized. First complete design and verification, then quote a flight assembly and engineering units. |
| Availability | NOT DESIGN RELEASED. TI lists the candidate TPSM82823 as active, but that does not establish space suitability or adapter availability. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 45 g | PROJECT ALLOCATION |
| Envelope | 88 × 88 × 6 mm CAD envelope | ASSUMPTION; no schematic, layout or released PCB exists |
| Electrical power / generation | Two independent 3.30 V branches: 1.0 A OBC design allocation and 1.2 A radio design allocation; project distribution efficiency 85% includes adapter losses | PROJECT DESIGN ALLOCATION |

## Supplier facts retained by the project

- Candidate TPSM82823 is a catalog 3 A buck module, 2.4–5.5 V input, 0.6–4 V adjustable output, 2.0 × 2.5 × 1.1 mm package.
- TI lists output discharge, power-good, enable, soft start, short-circuit and overtemperature features.
- Candidate part is commercial catalog hardware; no radiation qualification is claimed.

## Exact project configuration

- Two separate regulator channels supplied by separate ICEPS2 5 V outputs.
- Adjustable candidate starting point: 450 kΩ/100 kΩ 0.1% feedback, 10 µF input and 22 µF output X7R ≥10 V, subject to released analysis.
- Independent enables, output discharge, power-good telemetry and signal isolation against parasitic powering.
- Delivered radio rail target approximately 3.260–3.340 V DC, with ≤40 mV additional positive transient allocation.

## Mechanically/electrically relevant interfaces

- H04 OBC branch
- H05 radio branch
- B02 switched 5 V inputs
- B08 carrier/harness routing
- Telemetry/control to B06

## Procurement-release blockers

- Schematic, complete component BOM, PCB stackup/layout, connectors and mechanical mounting
- Fault protection against feedback-open/switch-short overvoltage
- Stability/transient/EMI/thermal analysis and worst-case tolerance
- Radiation TID/SEE behavior and mission suitability
- Prototype, qualification and acceptance test plan; exact mass and cost

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S14
- procurement/BOM.csv
- engineering/03_Interfaces.md
- engineering/04_Mechanical_Thermal_Radiation.md
- drawings/freecad/FINDINGS.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
