# B13 — Integration fasteners, bonding and small brackets

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B13 |
| Supplier | Integration vendor |
| Quantity | 1 |
| Procurement type | Custom integration hardware lot |
| Project unit estimate, low/base/high | €150 / €300 / €600 |
| Public price evidence | No product price; project allowance for a future itemized hardware lot |
| Order/quote URL | Not applicable—itemize only after mounting drawings and bonding plan are released, then order from qualified hardware suppliers/integrator. |
| Ordering route | No blanket hardware kit is selected. |
| Availability | NOT ITEMIZED OR DESIGN RELEASED. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 25 g | PROJECT ALLOCATION |
| Envelope | Unknown; no individual part geometry is released | UNKNOWN |
| Electrical power / generation | No electrical load; bonding path resistance/EMC requirements remain to be specified | FUNCTIONAL DESCRIPTION |

## Supplier facts retained by the project

- No supplier, material, finish, fastener size or bracket drawing has been selected.

## Exact project configuration

- Only hardware needed to mount and bond the already documented B01–B16 architecture.
- Do not use this allowance to hide ballast, blanket shielding or new subsystems.
- Use approved locking methods and installation/torque records.

## Mechanically/electrically relevant interfaces

- B01 structure
- All mounted boards/subassemblies
- Intentional chassis bond

## Procurement-release blockers

- Itemized fastener/bracket list and double-count check against B01/B11/B16
- Materials, coatings, galvanic compatibility and outgassing
- Thread engagement, torque, locking and preload analysis
- Bond locations, resistance acceptance and corrosion protection
- As-built mass and spare quantities

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
- engineering/06_Integration_and_Verification.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
