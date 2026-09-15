# Component source and order-route check

Checked 2026-09-15. No supplier forms were submitted and no vendor was contacted.

| BOM lines | Source checked | Result for procurement |
|---|---|---|
| B01 | https://www.cubesatshop.com/product/1-unit-cubesat-structure/ | Current storefront listing shows €3,450, SKU 100000 and 4–6 weeks, with “Request more info.” Required configuration and mass are not published. Treat price/lead time as indicative. |
| B02 | https://www.isispace.nl/product/compact-electrical-power-system/ | Current Type A quote route. Page states 184 ±5 g, 96 × 92 × 26.45 mm and 22.5 Wh. Linked controlled-datasheet/configuration consistency must be resolved in the quote. |
| B03–B05, B14 | https://www.isispace.nl/product/small-satellite-solar-panels/ | Current configurable 1U product/quote route. No public price. Configuration-specific drawings and guaranteed performance are required. |
| B06 | https://gomspace.com/product/nanomind-a3200/ | Current product/contact page and downloadable older datasheet. No public price or lead time. |
| B07 | https://gomspace.com/product/nanocom-ax100/ | Current product/add-to-quote page. AX100-U and Mode 5 details must be tied to the delivered revision and S11 PCN. |
| B08 | Registered S12/S13 legacy DMC-3 PDF URLs and current GomSpace product catalog | Legacy direct PDFs returned 404 and no current DMC-3 product page was verified. Contact GomSpace before retaining this line as orderable. |
| B09 | https://www.isispace.nl/product/vhf-uhf-antenna-for-1u-3u/ | Current selectable Turnstile product/quote route. Exact 5 V UHF configuration, frequency and mechanical interface require quote. |
| B10 | https://www.ti.com/product/TPSM82823 | Candidate regulator is listed active/orderable by TI. B10 itself is an unreleased custom assembly and cannot be ordered from this link. |
| B11–B13, B16 | Project engineering record only | Custom integration lots have no supplier or order URL because drawings/specifications are not released. |
| B15 | https://crystalspace.eu/products/cs-101-kikas/ | Current product/contact page confirms 42 × 25 × 45 mm, 50 g and 5 MP. Detailed brief and quote require contact; public electrical data remain unavailable. |

## Registered detailed sources

The component cards refer to IDs in `review/Source_Register.md`. Source IDs S01–S29 remain the project-wide register. This log records the procurement audit and does not duplicate or replace that controlled register.

## Price handling

Public prices are transcribed with their original currency and date. No foreign-exchange conversion is inferred. Vendor-quote items retain the low/base/high EUR planning allowances from `procurement/BOM.csv`. A future received quotation must record exact configuration, currency, validity, taxes, freight, duties, NRE, software/support, test scope and delivery terms before updating the controlled cost baseline.
