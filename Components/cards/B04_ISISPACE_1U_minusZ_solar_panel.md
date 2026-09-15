# B04 — 1U -Z solar panel with separation-switch clearances

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**


## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B04 |
| Supplier | ISISPACE |
| Quantity | 1 |
| Procurement type | COTS-derived custom solar-panel configuration |
| Project unit estimate, low/base/high | €1,200 / €1,800 / €2,500 |
| Public price evidence | No public price; project planning allowance |
| Order/quote URL | https://www.isispace.nl/product/small-satellite-solar-panels/ |
| Ordering route | Select 1U and use the vendor's ‘I want to buy’ quote route. This is a configured item, not a stock checkout. |
| Availability | Catalog family is current; exact face configuration, lead time, and deliverable revision require written quotation. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 50 g | CURRENT VENDOR PAGE, configuration dependent |
| Envelope | Planform and relief geometry unknown; 1.2–2.0 mm typical thickness | CURRENT VENDOR PAGE for thickness |
| Electrical power / generation | Procurement target ≥2.3 W BOL; two series cells approximately 5.4 V BOL | PROJECT REQUIREMENT plus CURRENT VENDOR approximate per-cell values |

## Supplier facts retained by the project

- 1U panel catalog mass: 50 g, configuration dependent.
- Typical panel thickness: 1.2–2.0 mm; planform and mounting-hole drawing are not published on the current page.
- Approximate BOL output: 1.23 W and 2.7 V per GaAs cell; 30% BOL cell efficiency.
- Custom flat inline Omnetics interface, 2 mm height; included Raychem Spec 44 AWG26 harness.
- Integrated temperature sensor and photodiode.
- Operating range: -40 °C to +80 °C; catalog radiation statement: minimum two years in LEO.
- Shipped-unit acceptance includes functional test and thermal cycling; current page does not show acceptance TVAC, vibration, or shock.

## Exact project configuration

- Body-mounted -Z panel with supplier-designed clearances for the actual separation-switch/RBF hardware.
- Two cells in series and ≥2.3 W BOL under specified conditions.
- No cell cutting or ad-hoc field modification.

## Mechanically/electrically relevant interfaces

- H01–H03 to ICEPS2 MPPT
- Structure, rail and switch keep-outs
- Custom flat inline Omnetics and included AWG26 harness

## Procurement-release blockers

- Actual switch count, locations and travel
- Signed panel relief, cell routing and structural drawing
- Hot/cold IV curves, blocking path and MPPT compatibility
- As-ordered dimensions, mass, price, lead time and acceptance evidence

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S04
- S22
- procurement/BOM.csv
- engineering/01_Mission_and_Architecture.md
- engineering/02_Budgets_and_Analyses.md
- engineering/03_Interfaces.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
