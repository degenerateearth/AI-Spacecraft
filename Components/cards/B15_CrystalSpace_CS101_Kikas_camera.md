# B15 — CS-101 Kikas 5 MP camera with infinity-focus wide-angle lens

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**
Phase 1 disposition: **UNSUITABLE while the better documented SkyFox piCAM/FM candidate is commercially available. CS-101 remains the controlled B15 entry until configuration control approves a replacement.**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B15 |
| Supplier | CrystalSpace |
| Quantity | 1 |
| Procurement type | COTS camera requiring optical/electrical configuration |
| Project unit estimate, low/base/high | €3,000 / €6,000 / €10,000 |
| Public price evidence | No public price; project planning allowance only |
| Order/quote URL | https://crystalspace.eu/products/cs-101-kikas/ |
| Ordering route | Use CrystalSpace contact/product-overview route and request a configured quotation; the detailed brief is gated. |
| Availability | Current product page; exact lens, electronics, protocol, revision, lead time and acceptance scope require quote. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 50 g | CURRENT VENDOR PAGE |
| Envelope | 42 × 25 × 45 mm | CURRENT VENDOR PAGE; orientation in spacecraft is a project decision pending CAD |
| Electrical power / generation | Unknown vendor supply/consumption; project caps camera at ≤2 W peak and ≤300 s powered/day, with 0.02 W average including OBC processing | PROJECT ALLOCATION only |

## Supplier facts retained by the project

- Current page states 5 MP, 50 g, 42 × 25 × 45 mm and TRL 9.
- Page describes multiple field-of-view lenses and communication protocols, Earth-observation use and ITAR-free status.
- No current public voltage, consumption, shutter, image-format or environmental table was obtained.

## Exact project configuration

- Visible, calibrated infinity-focus lens with roughly 60° horizontal FOV.
- Exposure control down to ≤1 ms; confirm shutter/readout behavior.
- JPEG or reduced-resolution output path and UART or RS485 supplier option compatible with B06.
- Mount with 25 mm dimension along Z in the documented 27 mm bay; optical axis toward +X.

## Mechanically/electrically relevant interfaces

- H13 switched payload power and serial
- B16 bracket/baffle/harness
- B14 aperture
- B06 storage/processing

## Procurement-release blockers

- Supply voltage, logic levels, peak/idle energy, cold-start and readout time
- Protocol, connector/pinout, image formats/resolutions, memory and command documentation
- Sensor model, spectral response, shutter type, exposure limits and exact lens/FOV
- Sun exposure tolerance, operating/storage temperature and thermal-vacuum focus behavior
- Radiation/qualification/acceptance evidence, price, lead time and export classification

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S23
- procurement/BOM.csv
- engineering/02_Budgets_and_Analyses.md
- engineering/03_Interfaces.md
- engineering/07_Imaging_Payload.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
