# B07 — NanoCom AX100-U, sales part 200315, Mode 5

Audit date: 2026-09-15  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | B07 |
| Supplier | GomSpace |
| Quantity | 1 |
| Procurement type | COTS UHF transceiver |
| Project unit estimate, low/base/high | €4,500 / €6,500 / €9,000 |
| Public price evidence | No public price; project planning allowance only |
| Order/quote URL | https://gomspace.com/product/nanocom-ax100/ |
| Ordering route | Add to GomSpace quote and specify AX100-U sales part 200315 plus supported Mode 5 configuration. |
| Availability | Current product page and 2024 PCN support U/UL sale, but exact delivery revision, lead time and firmware remain quote controlled. |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | 24.5 g | CURRENT VENDOR PAGE and S10 |
| Envelope | 65 × 40 × 6.5 mm | CURRENT VENDOR PAGE and S10 |
| Electrical power / generation | 3.3 V supply; RX 45/55/120 mA min/typ/max; TX 750/800/850 mA at +25 °C and up to 1 A across -30 to +85 °C; project allocates 0.20 W RX and 3.3 W TX | S10 VENDOR DATASHEET plus PROJECT ALLOCATIONS |

## Supplier facts retained by the project

- UHF option covers 430–440 MHz; project planning frequency 437 MHz is conditional on authorization.
- Adjustable 24–30 dBm output; 0.1–38.4 kbps family capability.
- I²C, UART and CAN/CSP; 20-position hard-gold FSI connector; current page identifies MCX antenna connector.
- Operating temperature -30 °C to +85 °C; PCB/assembly claims are catalog statements.

## Exact project configuration

- AX100-U sales part 200315; Mode 5 only per S11.
- Initial mission data rate 1200 bit/s with measured complete-modem threshold ≤-123 dBm at PER ≤1% for the selected frame.
- Powered from D1-IF branch B at 3.30 V nominal; signal pins high impedance when unpowered.
- Right-angle MCX implementation and 50 Ω coax to B09; final antenna tuned on assembled spacecraft.

## Mechanically/electrically relevant interfaces

- H05 power
- H07 CAN/CSP
- H10 50 Ω RF/MCX
- GOSH/UART service

## Procurement-release blockers

- Written acceptance of full 3.3 V supply tolerance/transients and D1-IF protection
- Exact Mode 5 waveform, licensing frequency, occupied bandwidth and ground modem compatibility
- Measured sensitivity and transmitter performance for delivered revision
- RF connector orientation/envelope and mating coax
- Radiation/SEE, qualification/acceptance, software license and lead time

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

- S09
- S10
- S11
- procurement/BOM.csv
- engineering/02_Budgets_and_Analyses.md
- engineering/03_Interfaces.md

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
