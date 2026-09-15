# B09 — AntS 1U–3U UHF turnstile, 5 V model

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**


## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B09 |
| Supplier | ISISPACE |
| Quantity | 1 |
| Procurement type | COTS deployable antenna requiring frequency/mechanical configuration |
| Project unit estimate, low/base/high | €1,500 / €2,500 / €4,000 |
| Public price evidence | No public price; project planning allowance only |
| Order/quote URL | https://www.isispace.nl/product/vhf-uhf-antenna-for-1u-3u/ |
| Ordering route | Select Turnstile and use ‘I want to buy’; specify UHF tuning and 5 V electronics. |
| Availability | Current catalog product; exact turnstile frequency, element arrangement, connector and lead time require quote. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | <90 g | CURRENT VENDOR PAGE; project carries 90 g |
| Envelope | 98 × 98 × 7 mm stowed including supplied aluminum cover | CURRENT VENDOR PAGE |
| Electrical power / generation | <60 mW nominal for 5 V model; 2 W during deployment; maximum RF input 2 W | CURRENT VENDOR PAGE |

## Supplier facts retained by the project

- Up to four 55 cm tape-spring elements with redundant deployment system.
- Miniature 9-pin Omnetics electrical interface and I²C data.
- 145–868 MHz family range; UHF main-beam gain 0 dBi and >50 MHz -10 dB bandwidth are catalog values.
- Operating -20 °C to +60 °C; deployment -5 °C to +60 °C; deployment under 5 s.
- Shipped-unit acceptance shown: functional and thermal cycling; not TVAC, vibration or shock.

## Exact project configuration

- 5 V UHF turnstile; final tuning on the complete spacecraft.
- Project commands deployment only at +5 to +45 °C and never while transmitting.
- Top accommodates B05 without obstructing stow or deployment.
- Separate isolated I²C branch and three-inhibit release/RF safety architecture.

## Mechanically/electrically relevant interfaces

- H06 switched 5 V
- H09 isolated I²C
- H10 50 Ω RF
- B05 top-panel mount
- Structure and deployable keep-out

## Procurement-release blockers

- Authorized operating frequency and final tune requirement
- Exact RF connector/mating cable and full harness loss
- Signed B05/structure mounting arrangement and deployment envelope
- Release current/time trace and all-fault inhibit evidence
- Delivered-unit TVAC/vibration/shock scope, lead time and price

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S05
- procurement/BOM.csv
- engineering/01_Mission_and_Architecture.md
- engineering/03_Interfaces.md
- engineering/04_Mechanical_Thermal_Radiation.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
