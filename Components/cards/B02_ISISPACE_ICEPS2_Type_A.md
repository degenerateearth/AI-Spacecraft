# B02 — ICEPS2 Type A with integrated battery and three-separation-switch/RBF option

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B02 |
| Supplier | ISISPACE |
| Quantity | 1 |
| Procurement type | COTS EPS/battery requiring configured safety option |
| Project unit estimate, low/base/high | €4,500 / €6,500 / €9,000 |
| Public price evidence | No public price; project planning allowance only |
| Order/quote URL | https://www.isispace.nl/product/compact-electrical-power-system/ |
| Ordering route | Select Type A and use ‘I want to buy’/sales contact for a configured quotation. |
| Availability | Current product family; exact switch/RBF option, electrical revision, lead time, battery lot, and acceptance scope require quote. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 184 ± 5 g | CURRENT VENDOR PAGE; includes battery |
| Envelope | 96 × 92 × 26.45 mm, PCB and top battery | CURRENT VENDOR PAGE; project CAD uses 26.5 mm from S03 |
| Electrical power / generation | Stores 22.5 Wh per current product page; VD0 unregulated, four VD1 5 V channels, four VD2 3.3 V channels; project peak delivered-load screen is 6.444 W and 1.26 A battery-side at 6 V | VENDOR catalog plus PROJECT CALCULATION; per-channel transient closure is open |

## Supplier facts retained by the project

- Type A has an integrated two-cell Li-ion pack.
- I²C control; hardware MPPT; emergency low-power behavior, supervisor/watchdog, housekeeping, overcurrent/thermal and reverse-current protection are listed.
- Operating range is -20 °C to +70 °C at product level.
- Shipped-unit acceptance shown: functional and thermal cycling; not TVAC, vibration, or shock.

## Exact project configuration

- Type A only; do not add a separate battery BOM line.
- Request three-separation-switch/RBF implementation and evidence of source-to-hazard inhibit independence.
- Accept five unequal/intact two-cell faces plus one camera-aperture face across three MPPT inputs as defined by H01–H03.
- Use switched 5 V outputs for the two D1-IF branches and 5 V AntS branch.

## Mechanically/electrically relevant interfaces

- H01–H03 solar/MPPT
- H04/H05 switched 5 V to D1-IF
- H06 switched 5 V to AntS
- H08 I²C
- H11 switches/RBF
- H12 service

## Procurement-release blockers

- Current product page says 22.5 Wh while the linked S03 revision shows a different Type-A energy/configuration value; obtain an as-ordered controlled datasheet
- Exact output current limits, startup/transients and 3.3 V high-side tolerance for delivered revision
- Battery charge/discharge temperature/current profile and ≥6000 shallow-cycle plus calendar-life evidence
- Complete inhibit topology including solar, battery, debug and backfeed paths
- Delivered-lot qualification/acceptance and radiation/SEE evidence

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S02
- S03
- procurement/BOM.csv
- engineering/02_Budgets_and_Analyses.md
- engineering/03_Interfaces.md
- engineering/04_Mechanical_Thermal_Radiation.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
