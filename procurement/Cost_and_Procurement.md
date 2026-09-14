# D1-CST-001 — Cost estimate and procurement strategy

Revision A | EUR planning allowances; 2026-09-14. No arbitrary spending ceiling is imposed.

## Cost result

Flight hardware has a EUR29,350 low scenario, EUR46,500 base and EUR70,100 high scenario. The **realistic minimum-cost planning case for spacecraft build is about EUR81,350**, including engineering hardware, assembly and engineering labor. Base spacecraft build is EUR152,500. These estimates assume an experienced small team and substantial reuse; they are not a promise that the lowest scenario can be purchased. Hardware-only price omits the work needed to make the satellite fly.

| Separate cost category | Low EUR | Base EUR | High EUR |
|---|---:|---:|---:|
| Spacecraft build: flight hardware | 29,350 | 46,500 | 70,100 |
| Spacecraft build: engineering hardware/spares | 8,000 | 18,000 | 30,000 |
| Spacecraft build: assembly/workmanship labor | 4,000 | 8,000 | 16,000 |
| Spacecraft build: nonrecurring engineering labor | 40,000 | 80,000 | 180,000 |
| Testing: external facilities and campaign support | 15,000 | 35,000 | 75,000 |
| Ground station: equipment and installation | 4,000 | 12,000 | 25,000 |
| Licensing/coordination: professional support and filing allowance | 5,000 | 15,000 | 40,000 |
| Launch: rideshare/deployer/integration service | 40,000 | 65,000 | 120,000 |
| Operations: 12 months recurring support | 5,000 | 12,000 | 30,000 |
| **Spacecraft build subtotal, first four rows only** | **81,350** | **152,500** | **296,100** |
| **All categories subtotal, do not add build subtotal again** | **150,350** | **291,500** | **586,100** |

Add 25% program contingency as a planning reserve: total authorization envelope about EUR187,938 / EUR364,375 / EUR732,625. Contingency is not a hidden markup on each BOM line. Taxes, duties, exchange-rate movement, major launch delay/reflight, insurance, extensive dedicated radiation qualification and new ground-site civil works are excluded. A targeted-imaging mission with ADCS is outside scope.

The NRE allowance can be read as roughly 800 hours at EUR50/h in the unusually lean case, 1000 hours at EUR80/h base, and 1800 hours at EUR100/h high; these are explicit project assumptions, not surveyed market rates. If this is a first-time team or the adapter/camera needs major qualification, those hours may be insufficient. No donated labor is silently assumed in the build subtotal.

## Price evidence versus estimates

Every selected flight item is presently budgeted using an engineering allowance. Vendors mostly require a quote. Published current comparison prices include EXA KRATOS EUR44,000–155,000 [S19], Crystalspace P1U EUR4,400 [S20], and M2 ground antenna USD910.95 [S29]. They are different configurations and currencies and are not inserted into the EUR BOM as firm quotes. No FX conversion is claimed. Competitive quotations should be normalized to delivery date, taxes, freight, software, support and acceptance-test scope.

## Hardware alternatives

| Candidate | Rationale | Decision / required evidence |
|---|---|---|
| Selected mixed COTS subsystem baseline | Small low-power avionics, six-face energy recovery, compact flight-oriented camera | Conditional; adapter/ICDs and DMC supply are key risks |
| Basic EXA KRATOS 1U plus camera | May eliminate inter-vendor integration and some test/NRE work | RFQ against same image, lifetime, orbit and compliance requirements; advertised entry price not assumed to include chosen camera |
| Alen 1U platform plus camera | Turnkey bus potentially reduces software and AIV | Quote with acceptance reports and image integration [S21] |
| CrystalSpace EPS substitution | Lower published entry EPS price | Do not substitute until battery/solar/inhibit/environment interfaces close |
| Consumer camera and custom MCU/radio stack | Cheapest raw parts | Substantial development/qualification; no twelve-month evidence or cost advantage established |
| Five-panel bus or active-pointing imager | Fewer panels saves parts / pointing improves targeting | Five-panel fixed-attitude recovery loses geometric guarantee; ADCS adds cost and qualification |

There is no proof of global minimum cost without actual comparable offers. The procurement rule is minimum **total cost of compliant delivery**, including one-time engineering, test gaps and expected retest exposure. All catalog availability claims require written lead-time and supported-revision confirmation. In particular DMC-3 has an older indexed primary datasheet with a dead direct URL; do not treat it as confirmed in-stock hardware.

## Request-for-quotation package (draft; not sent)

Provide these documents to candidate bus and subsystem suppliers and request:

1. Firm exact part/configuration numbers, current hardware and software revisions, obsolescence status, lead time, Incoterms, validity, payment terms, warranty and export classification.
2. As-ordered mass/STEP models, mechanical drawings, electrical pin maps, input/output tolerances, peak/idle currents, memory map and command protocols; include every adapter/harness and flight-software license needed.
3. Mission suitability evidence for one year at 450–500 km, delivered-lot radiation/SEE evidence, battery cycle/calendar evidence and environmental qualification/acceptance reports with actual profiles.
4. Three-inhibit/RBF configuration, isolation of solar/battery/debug power, cold battery restart and end-of-life source passivation. Request a system-level fault-tree review of inhibit independence.
5. Five >=2.3 W panels plus one >=1.8 W camera-aperture panel, cell string layout, hot/cold IV curves and AntS top mounting. Request guaranteed startup/MPPT compatibility.
6. CS-101 lens/FOV, supply, power, interface, shutter, JPEG/reduced-resolution support, Sun exposure and thermal focus data. Quote camera and aperture integration separately.
7. Ground modem/waveform compatibility and measured Mode 5 sensitivity; supported CAN settings and rate. Confirm operating band only after licensing review.
8. Separate flight hardware, engineering units, NRE, assembly, testing, ground support and launch services. Identify provided acceptance tests so facility costs are not double counted.

No purchases, external messages or license filings have been made. Firm supplier and launch quotes are the next evidence needed to convert this estimate into a purchasing baseline.
## AI and software cost boundary

The project baseline is ChatGPT Plus at $20/month, with Codex/Astra where available, and free/open-source engineering tools wherever practical. Enterprise AI, specialist AI platforms, large API usage and paid cloud compute are not assumed. The [Project Cost Ledger](Project_Cost_Ledger.csv) keeps AI/tooling separate from physical mission costs. External expert review and physical verification are separate human/test costs.
