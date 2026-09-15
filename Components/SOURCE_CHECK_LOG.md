# Component source and order-route check

Checked 2026-09-15. No supplier forms were submitted and no vendor was contacted.

| BOM lines | Source checked | Result for procurement |
|---|---|---|
| B01 | https://www.cubesatshop.com/product/1-unit-cubesat-structure/ | Current storefront listing shows €3,450, SKU 100000 and 4–6 weeks, with “Request more info.” Required configuration and mass are not published. Treat price/lead time as indicative. |
| B02 | https://www.isispace.nl/product/compact-electrical-power-system/ | Current Type A quote route. Page states 184 ±5 g, 96 × 92 × 26.45 mm and 22.5 Wh. Linked controlled-datasheet/configuration consistency must be resolved in the quote. |
| B03–B05, B14 | https://www.isispace.nl/product/small-satellite-solar-panels/ | Current configurable 1U product/quote route. No public price. Configuration-specific drawings and guaranteed performance are required. |
| B06 | https://gomspace.com/product/nanomind-a3200/ | Current product/contact page and downloadable older datasheet. No public price or lead time. |
| B07 | https://gomspace.com/product/nanocom-ax100/ | Current product/add-to-quote page. AX100-U and Mode 5 details must be tied to the delivered revision and S11 PCN. |
| B08 | https://gomspace.com/product/nanodock-dmc-3/ and S45–S47 | Current manufacturer page offers Add to quote and links DS 1012962 rev 1.12, OSF 1012964 rev 2.3 dated 2025-04-14 and qualification certificate 1028503 for product 200232. Exact option selection, price, lead time and delivered revision remain open. |
| B09 | https://www.isispace.nl/product/vhf-uhf-antenna-for-1u-3u/ | Current selectable Turnstile product/quote route. Exact 5 V UHF configuration, frequency and mechanical interface require quote. |
| B10 | https://www.ti.com/product/TPSM82823 | Candidate regulator is listed active/orderable by TI. B10 itself is an unreleased custom assembly and cannot be ordered from this link. |
| B11–B13, B16 | Project engineering record only | Custom integration lots have no supplier or order URL because drawings/specifications are not released. |
| B15 | https://crystalspace.eu/products/cs-101-kikas/ | Current product/contact page confirms 42 × 25 × 45 mm, 50 g and 5 MP. Detailed brief and quote require contact; public electrical data remain unavailable. It is unsuitable for Phase 1 while the better documented SkyFox piCAM/FM candidate exists. |
| C01 candidate | https://www.skyfoxlabs.com/product/27-picam and S49 | piCAM/FM exact variant, €4,950 single-unit price, 2–4 week lead time and a public 2025 datasheet with pinout, commands, mechanics, limits and integration guidance. Mission-relevant radiation, optical acceptance, peak/startup and configuration-specific environmental evidence remain incomplete, so it is not admitted to the baseline. |
| C02 alternative | S53–S57 | Pumpkin publishes exact Rev D 1U skeletonized structure component numbers and public assembly CAD, plus material/finish and interface guidance. Current store selectors are marked unavailable, and exact-set mass, selected switch/end-plate configuration and qualification evidence are incomplete. |
| C03 alternative | S58–S59 | Pumpkin's current fixed-panel family page gives 0.8 mm thickness, a USD 2,500–5,650 range and per-panel bakeout/irradiance claims. Current selections are marked unavailable and exact configuration, mass, IV curves, harness and environmental data are absent. |

## Registered detailed sources

The component cards refer to IDs in `review/Source_Register.md`. Component evidence added in this pass is S44–S59. This log records the procurement audit and does not duplicate or replace that controlled register.

## Price handling

Public prices are transcribed with their original currency and date. No foreign-exchange conversion is inferred. Vendor-quote items retain the low/base/high EUR planning allowances from `procurement/BOM.csv`. A future received quotation must record exact configuration, currency, validity, taxes, freight, duties, NRE, software/support, test scope and delivery terms before updating the controlled cost baseline.
