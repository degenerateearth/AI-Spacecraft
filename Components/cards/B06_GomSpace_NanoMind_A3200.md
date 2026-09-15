# B06 — NanoMind A3200 flight computer

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B06 |
| Supplier | GomSpace |
| Quantity | 1 |
| Procurement type | COTS flight computer |
| Project unit estimate, low/base/high | €3,500 / €5,500 / €8,000 |
| Public price evidence | No public price; project planning allowance only |
| Order/quote URL | https://gomspace.com/product/nanomind-a3200/ |
| Ordering route | Use GomSpace quote request/contact; obtain exact sales code, hardware revision and software entitlement. |
| Availability | Current product page; stock, lead time, current revision, BSP and support terms are unconfirmed. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 24 g including shield | S08 VENDOR DATASHEET |
| Envelope | 65 × 40 × 7.1 mm | S08 VENDOR DATASHEET |
| Electrical power / generation | 3.2–3.4 V supply; vendor table gives 23–45 mA for listed clock/workload states, with additional sensor/flash loads; project allocates 0.18 W nominal, 0.08 W recovery and 0.9 W peak | S08 VENDOR DATASHEET plus PROJECT ALLOCATIONS; peak is not a measured mission value |

## Supplier facts retained by the project

- AVR32 MCU; 512 KB internal flash, 128 MB NOR flash, 32 kB FRAM and 32 MB SDRAM.
- I²C, UART, CAN, external SPI, ADC/GPIO, GSSB and PWM interfaces.
- Integrated magnetometer, gyroscope, RTC and temperature sensors.
- Operating temperature -30 °C to +85 °C; datasheet says environment tests were performed but directs users to GomSpace for details.

## Exact project configuration

- Top-side module on B08 DMC-3.
- Powered from D1-IF branch A at 3.30 V nominal; no direct ICEPS2 3.3 V connection.
- CAN/CSP to B07; separate I²C branches to EPS and AntS; camera serial interface subject to supplier option.

## Mechanically/electrically relevant interfaces

- Two 20-position hard-gold FSI connectors
- H04 power
- H07 CAN/CSP
- H08/H09 I²C
- H13 camera serial

## Procurement-release blockers

- Exact order code/current hardware revision and whether A3200 remains recommended for new designs
- BSP, bootloader, libraries, licenses, source access and support cost
- DMC-3 mechanical/electrical compatibility and connector stack height
- Mission-workload current and sleep/wake timing
- Radiation/SEE and delivered-unit acceptance evidence

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S07
- S08
- procurement/BOM.csv
- engineering/02_Budgets_and_Analyses.md
- engineering/03_Interfaces.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
