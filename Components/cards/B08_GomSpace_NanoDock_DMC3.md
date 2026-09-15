# B08 — NanoDock DMC-3 carrier, top-side two modules

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**


## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B08 |
| Supplier | GomSpace |
| Quantity | 1 |
| Procurement type | Named current COTS carrier; exact option configuration not selected |
| Project unit estimate, low/base/high | €900 / €1,500 / €2,500 |
| Public price evidence | No current public price; project planning allowance only |
| Order/quote URL | https://gomspace.com/product/nanodock-dmc-3/ |
| Ordering route | Current manufacturer page offers Add to quote and links its datasheet, 2025 option sheet and qualification certificate. |
| Availability | Current public quote route verified 2026-09-15; stock, price and lead time remain unconfirmed. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 51 g without daughterboards | S45 DS 1012962 rev 1.12, p14 |
| Envelope | 91.9 × 88.7 × 8.6 mm | S45, pp4 and 14; replaces incorrect CAD envelope assumption |
| Electrical power / generation | Passive carrier in flight; the only active circuit is USB-to-serial and is powered from USB | S45, pp6 and 14; daughterboard loads remain separate |

## Supplier facts retained by the project

- Current product page describes support for four daughterboards and links the manufacturer documents.
- S45 identifies FSI, stack and breakout connectors and their pinouts.
- S46 is OSF 1012964 rev 2.3 dated 2025-04-14.
- S47 is qualification certificate 1028503 rev 1.0 and identifies product 200232.

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

- Exact option-sheet selection for connector population, supply routing and CAN termination
- Exact delivered revision, price, lead time and confirmation that certificate 1028503 applies
- Project mapping of A3200/AX100 positions and complete harness/stack pin review

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
- S44
- S45
- S46
- S47
- procurement/BOM.csv
- engineering/03_Interfaces.md
- drawings/freecad/CAD_SOURCE_TRACEABILITY.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
