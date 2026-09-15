# B16 — Camera bracket, baffle and harness

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B16 |
| Supplier | Integration vendor |
| Quantity | 1 |
| Procurement type | Custom payload integration assembly |
| Project unit estimate, low/base/high | €300 / €600 / €1,200 |
| Public price evidence | No product price; custom design/fabrication planning allowance |
| Order/quote URL | Not applicable—release camera CAD, bracket/baffle drawing and harness definition, then issue an RFQ to the integration/machining vendor. |
| Ordering route | Do not fabricate from the present envelope model. |
| Availability | NOT DESIGN RELEASED. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 20 g | PROJECT ALLOCATION |
| Envelope | Must fit the 27 mm camera bay around B15's 25 mm Z dimension; exact geometry unknown | PROJECT ALLOCATION and CURRENT CAMERA ENVELOPE; only about 1 mm nominal clearance per side remains before bracket/tolerance effects |
| Electrical power / generation | No separate electrical load; harness carries the unresolved B15 ≤2 W peak allocation | PROJECT ALLOCATION |

## Supplier facts retained by the project

- No supplier, material, coating, connector, drawing or manufactured article exists in the current record.

## Exact project configuration

- Hold B15 at infinity-focus alignment with optical axis toward +X.
- Provide short baffle/stray-light control without rail, panel-cell or AntS deployment obstruction.
- Maintain serviceability, contamination control and a positive mechanical load path.

## Mechanically/electrically relevant interfaces

- B15 camera
- B14 aperture panel
- B01 structure
- H13 payload harness

## Procurement-release blockers

- Vendor camera CAD, mounting holes, datum scheme and connector envelope
- Bracket material, thickness, attachment, tolerance and load analysis
- Baffle field stop/FOV, coating, contamination/outgassing and solar exposure
- Harness strain relief and connector access
- Post-vibration/TVAC optical alignment acceptance and final mass

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- procurement/BOM.csv
- engineering/04_Mechanical_Thermal_Radiation.md
- engineering/07_Imaging_Payload.md
- drawings/freecad/FINDINGS.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
