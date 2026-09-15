# B08 — NanoDock DMC-3 carrier, top-side two modules

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B08 |
| Supplier | GomSpace |
| Quantity | 1 |
| Procurement type | Named COTS carrier with unconfirmed current availability |
| Project unit estimate, low/base/high | €900 / €1,500 / €2,500 |
| Public price evidence | No current public price; project planning allowance only |
| Order/quote URL | https://gomspace.com/product/nanomind-a3200/ |
| Ordering route | Contact GomSpace and request written confirmation that DMC-3 is orderable and supported with A3200 and AX100-U. The legacy direct datasheet URLs are not ordering routes. |
| Availability | UNCONFIRMED. Registered S12/S13 direct PDFs returned 404; no current DMC-3 product page was verified. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 51 g | PROVISIONAL project value from older indexed source; not verified against a current controlled document |
| Envelope | 88 × 88 × 1.6 mm used only as a CAD envelope assumption | ASSUMPTION; current A3200 page describes the broader NanoDock platform as standard PC/104 size 90 × 96 mm |
| Electrical power / generation | Unknown independently; project allocates 0.03 W nominal for interfaces/carrier/sensors combined and 0.02 W in recovery | PROJECT ALLOCATION, not vendor requirement |

## Supplier facts retained by the project

- Older project sources describe DMC-3 routing for daughter modules.
- No current controlled mechanical/electrical specification has been obtained.

## Exact project configuration

- Carrier for two top-side modules: B06 A3200 and B07 AX100-U.
- Do not assume cross-vendor PC/104 pin compatibility to B02; route approved power/data through B10/B11.
- CAN bus must provide two endpoints and about 60 Ω unpowered bus resistance.

## Mechanically/electrically relevant interfaces

- B06/B07 daughter-module connectors
- H04/H05 power routing
- H07 CAN routing
- Structure/standoff mounting

## Procurement-release blockers

- Whether DMC-3 can presently be purchased
- Exact order code, revision, supported module combination and top-side orientation
- Controlled outline, thickness, holes, connector heights and keep-outs
- Power and signal routing, CAN termination and current rating
- Mass, environmental evidence, price and lead time

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S07
- S12
- S13
- procurement/BOM.csv
- engineering/03_Interfaces.md
- drawings/freecad/CAD_SOURCE_TRACEABILITY.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
