#!/usr/bin/env python3
"""Generate DEGENERATE-1 component audit cards and the summary CSV.

The data below contains exactly the 16 lines already present in procurement/BOM.csv.
Do not add a record here without first changing the controlled project BOM.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AUDIT_DATE = "2026-09-15"

COMMON_ISIS_SOLAR = {
    "vendor_facts": [
        "1U panel catalog mass: 50 g, configuration dependent.",
        "Typical panel thickness: 1.2–2.0 mm; planform and mounting-hole drawing are not published on the current page.",
        "Approximate BOL output: 1.23 W and 2.7 V per GaAs cell; 30% BOL cell efficiency.",
        "Custom flat inline Omnetics interface, 2 mm height; included Raychem Spec 44 AWG26 harness.",
        "Integrated temperature sensor and photodiode.",
        "Operating range: -40 °C to +80 °C; catalog radiation statement: minimum two years in LEO.",
        "Shipped-unit acceptance includes functional test and thermal cycling; current page does not show acceptance TVAC, vibration, or shock.",
    ],
    "order_url": "https://www.isispace.nl/product/small-satellite-solar-panels/",
    "order_route": "Select 1U and use the vendor's ‘I want to buy’ quote route. This is a configured item, not a stock checkout.",
    "price_evidence": "No public price. Project planning allowance only.",
    "availability": "Catalog family is current; exact face configuration, lead time, and deliverable revision require written quotation.",
    "sources": ["S04", "S22", "procurement/BOM.csv", "engineering/01_Mission_and_Architecture.md", "engineering/02_Budgets_and_Analyses.md", "engineering/03_Interfaces.md"],
}


COMPONENTS = [
    {
        "id": "B01", "slug": "ISISPACE_1U_structure", "vendor": "ISISPACE", "item": "1U structure, rails, fasteners, separation provisions", "qty": 1,
        "kind": "COTS structure with project-specific configuration", "mass": "150 g", "mass_basis": "PROJECT ALLOCATION; current storefront does not publish mass",
        "size": "Nominal spacecraft rail envelope about 100 × 100 × 113.5 mm", "size_basis": "PROJECT ALLOCATION from CubeSat form factor; controlled structure and deployer drawings remain required",
        "power": "No electrical load", "power_basis": "Physical structure",
        "cost": (2000, 3000, 4500), "published_price": "€3,450 shown by CubeSatShop on 2026-09-15; taxes, freight, options, and configuration scope unknown",
        "order_url": "https://www.cubesatshop.com/product/1-unit-cubesat-structure/", "order_route": "Request more information through CubeSatShop/ISISPACE; storefront SKU 100000.",
        "availability": "Storefront states 4–6 weeks, but this is not a supplier quotation or confirmation for the required flight configuration.",
        "vendor_facts": ["Generic modular 1U structure with load-carrying frames and detachable shear panels.", "Current storefront says flight heritage since 2012.", "One internal 1U PCB/module stack is described."],
        "configuration": ["Provide rails, frames, shear panels, secondary structure, approved board-mount hardware and fasteners.", "Accommodate the project-required three independent separation-switch/RBF architecture without rail or panel interference.", "Use the exact launch-provider/deployer ICD selected later."],
        "interfaces": ["Dispenser rails and envelope", "Internal board stack and standoffs", "Six body-mounted panel interfaces", "Separation switches/RBF"],
        "open": ["Exact order code and delivered kit content", "Controlled dimensions, tolerances, materials, coatings, fastener specifications, torque, venting and CAD", "Switch locations, travel and compatibility with B04", "As-ordered mass and center-of-mass contribution", "Whether the 4–6 week statement applies to this configuration"],
        "sources": ["S01", "S06", "procurement/BOM.csv", "engineering/02_Budgets_and_Analyses.md", "engineering/04_Mechanical_Thermal_Radiation.md", "drawings/freecad/FINDINGS.md"],
    },
    {
        "id": "B02", "slug": "ISISPACE_ICEPS2_Type_A", "vendor": "ISISPACE", "item": "ICEPS2 Type A with integrated battery and three-separation-switch/RBF option", "qty": 1,
        "kind": "COTS EPS/battery requiring configured safety option", "mass": "184 ± 5 g", "mass_basis": "CURRENT VENDOR PAGE; includes battery",
        "size": "96 × 92 × 26.45 mm, PCB and top battery", "size_basis": "CURRENT VENDOR PAGE; project CAD uses 26.5 mm from S03",
        "power": "Stores 22.5 Wh per current product page; VD0 unregulated, four VD1 5 V channels, four VD2 3.3 V channels; project peak delivered-load screen is 6.444 W and 1.26 A battery-side at 6 V", "power_basis": "VENDOR catalog plus PROJECT CALCULATION; per-channel transient closure is open",
        "cost": (4500, 6500, 9000), "published_price": "No public price; project planning allowance only",
        "order_url": "https://www.isispace.nl/product/compact-electrical-power-system/", "order_route": "Select Type A and use ‘I want to buy’/sales contact for a configured quotation.",
        "availability": "Current product family; exact switch/RBF option, electrical revision, lead time, battery lot, and acceptance scope require quote.",
        "vendor_facts": ["Type A has an integrated two-cell Li-ion pack.", "I²C control; hardware MPPT; emergency low-power behavior, supervisor/watchdog, housekeeping, overcurrent/thermal and reverse-current protection are listed.", "Operating range is -20 °C to +70 °C at product level.", "Shipped-unit acceptance shown: functional and thermal cycling; not TVAC, vibration, or shock."],
        "configuration": ["Type A only; do not add a separate battery BOM line.", "Request three-separation-switch/RBF implementation and evidence of source-to-hazard inhibit independence.", "Accept five unequal/intact two-cell faces plus one camera-aperture face across three MPPT inputs as defined by H01–H03.", "Use switched 5 V outputs for the two D1-IF branches and 5 V AntS branch."],
        "interfaces": ["H01–H03 solar/MPPT", "H04/H05 switched 5 V to D1-IF", "H06 switched 5 V to AntS", "H08 I²C", "H11 switches/RBF", "H12 service"],
        "open": ["Current product page says 22.5 Wh while the linked S03 revision shows a different Type-A energy/configuration value; obtain an as-ordered controlled datasheet", "Exact output current limits, startup/transients and 3.3 V high-side tolerance for delivered revision", "Battery charge/discharge temperature/current profile and ≥6000 shallow-cycle plus calendar-life evidence", "Complete inhibit topology including solar, battery, debug and backfeed paths", "Delivered-lot qualification/acceptance and radiation/SEE evidence"],
        "sources": ["S02", "S03", "procurement/BOM.csv", "engineering/02_Budgets_and_Analyses.md", "engineering/03_Interfaces.md", "engineering/04_Mechanical_Thermal_Radiation.md"],
    },
    {
        **COMMON_ISIS_SOLAR, "id": "B03", "slug": "ISISPACE_1U_side_solar_panels", "vendor": "ISISPACE", "item": "1U side solar panel, two cells in series", "qty": 3,
        "kind": "COTS-derived custom solar-panel configuration", "mass": "50 g each; 150 g line total", "mass_basis": "CURRENT VENDOR PAGE, configuration dependent",
        "size": "Planform unknown; 1.2–2.0 mm typical thickness", "size_basis": "CURRENT VENDOR PAGE for thickness; project CAD planform is an ASSUMPTION",
        "power": "Procurement target ≥2.3 W BOL per panel; two series cells approximately 5.4 V BOL using current catalog values", "power_basis": "PROJECT REQUIREMENT plus CURRENT VENDOR approximate per-cell values",
        "cost": (1200, 1800, 2500), "published_price": "No public price; project planning allowance per panel",
        "configuration": ["Three 1U body-mounted side panels for the documented side faces.", "Two cells in series per face; opposite faces parallel only through approved blocking paths into the assigned MPPT.", "Guaranteed ≥2.3 W BOL under supplier-stated conditions; no deployable panels."],
        "interfaces": ["H01–H03 to ICEPS2 MPPT", "Custom flat inline Omnetics and included AWG26 harness", "ISISPACE structure mounting"],
        "open": ["Exact face assignment for each ordered serial number", "Planform, hole pattern, cell layout, connector placement and cable length", "Hot/cold IV curves and startup/MPPT compatibility", "Reverse-current/blocking topology", "As-ordered mass, acceptance tests, lead time and price"],
    },
    {
        **COMMON_ISIS_SOLAR, "id": "B04", "slug": "ISISPACE_1U_minusZ_solar_panel", "vendor": "ISISPACE", "item": "1U -Z solar panel with separation-switch clearances", "qty": 1,
        "kind": "COTS-derived custom solar-panel configuration", "mass": "50 g", "mass_basis": "CURRENT VENDOR PAGE, configuration dependent",
        "size": "Planform and relief geometry unknown; 1.2–2.0 mm typical thickness", "size_basis": "CURRENT VENDOR PAGE for thickness",
        "power": "Procurement target ≥2.3 W BOL; two series cells approximately 5.4 V BOL", "power_basis": "PROJECT REQUIREMENT plus CURRENT VENDOR approximate per-cell values",
        "cost": (1200, 1800, 2500), "published_price": "No public price; project planning allowance",
        "configuration": ["Body-mounted -Z panel with supplier-designed clearances for the actual separation-switch/RBF hardware.", "Two cells in series and ≥2.3 W BOL under specified conditions.", "No cell cutting or ad-hoc field modification."],
        "interfaces": ["H01–H03 to ICEPS2 MPPT", "Structure, rail and switch keep-outs", "Custom flat inline Omnetics and included AWG26 harness"],
        "open": ["Actual switch count, locations and travel", "Signed panel relief, cell routing and structural drawing", "Hot/cold IV curves, blocking path and MPPT compatibility", "As-ordered dimensions, mass, price, lead time and acceptance evidence"],
    },
    {
        **COMMON_ISIS_SOLAR, "id": "B05", "slug": "ISISPACE_1U_plusZ_AntS_solar_panel", "vendor": "ISISPACE", "item": "1U +Z solar panel for AntS mounting", "qty": 1,
        "kind": "COTS-derived custom solar-panel configuration", "mass": "50 g", "mass_basis": "CURRENT VENDOR PAGE, configuration dependent; no AntS cover mass credit taken",
        "size": "Planform/interface unknown; 1.2–2.0 mm typical thickness", "size_basis": "CURRENT VENDOR PAGE for thickness",
        "power": "Procurement target ≥2.3 W BOL; two series cells approximately 5.4 V BOL", "power_basis": "PROJECT REQUIREMENT plus CURRENT VENDOR approximate per-cell values",
        "cost": (1200, 1800, 2500), "published_price": "No public price; project planning allowance",
        "configuration": ["Top panel mounted using the AntS-supported accommodation.", "UHF turnstile deployment must remain unobstructed.", "Two cells in series and ≥2.3 W BOL under specified conditions."],
        "interfaces": ["AntS top mounting interface", "H01–H03 to ICEPS2 MPPT", "Custom flat inline Omnetics and included AWG26 harness"],
        "open": ["Signed AntS/panel mechanical interface and whether supplied cover is retained or replaced", "Antenna-element stow/deployment clearances", "Cell/connector routing and RF interaction", "Hot/cold IV, MPPT compatibility, mass, price and acceptance evidence"],
    },
    {
        "id": "B06", "slug": "GomSpace_NanoMind_A3200", "vendor": "GomSpace", "item": "NanoMind A3200 flight computer", "qty": 1,
        "kind": "COTS flight computer", "mass": "24 g including shield", "mass_basis": "S08 VENDOR DATASHEET",
        "size": "65 × 40 × 7.1 mm", "size_basis": "S08 VENDOR DATASHEET",
        "power": "3.2–3.4 V supply; vendor table gives 23–45 mA for listed clock/workload states, with additional sensor/flash loads; project allocates 0.18 W nominal, 0.08 W recovery and 0.9 W peak", "power_basis": "S08 VENDOR DATASHEET plus PROJECT ALLOCATIONS; peak is not a measured mission value",
        "cost": (3500, 5500, 8000), "published_price": "No public price; project planning allowance only",
        "order_url": "https://gomspace.com/product/nanomind-a3200/", "order_route": "Use GomSpace quote request/contact; obtain exact sales code, hardware revision and software entitlement.",
        "availability": "Current product page; stock, lead time, current revision, BSP and support terms are unconfirmed.",
        "vendor_facts": ["AVR32 MCU; 512 KB internal flash, 128 MB NOR flash, 32 kB FRAM and 32 MB SDRAM.", "I²C, UART, CAN, external SPI, ADC/GPIO, GSSB and PWM interfaces.", "Integrated magnetometer, gyroscope, RTC and temperature sensors.", "Operating temperature -30 °C to +85 °C; datasheet says environment tests were performed but directs users to GomSpace for details."],
        "configuration": ["Top-side module on B08 DMC-3.", "Powered from D1-IF branch A at 3.30 V nominal; no direct ICEPS2 3.3 V connection.", "CAN/CSP to B07; separate I²C branches to EPS and AntS; camera serial interface subject to supplier option."],
        "interfaces": ["Two 20-position hard-gold FSI connectors", "H04 power", "H07 CAN/CSP", "H08/H09 I²C", "H13 camera serial"],
        "open": ["Exact order code/current hardware revision and whether A3200 remains recommended for new designs", "BSP, bootloader, libraries, licenses, source access and support cost", "DMC-3 mechanical/electrical compatibility and connector stack height", "Mission-workload current and sleep/wake timing", "Radiation/SEE and delivered-unit acceptance evidence"],
        "sources": ["S07", "S08", "procurement/BOM.csv", "engineering/02_Budgets_and_Analyses.md", "engineering/03_Interfaces.md"],
    },
    {
        "id": "B07", "slug": "GomSpace_NanoCom_AX100U", "vendor": "GomSpace", "item": "NanoCom AX100-U, sales part 200315, Mode 5", "qty": 1,
        "kind": "COTS UHF transceiver", "mass": "24.5 g", "mass_basis": "CURRENT VENDOR PAGE and S10",
        "size": "65 × 40 × 6.5 mm", "size_basis": "CURRENT VENDOR PAGE and S10",
        "power": "3.3 V supply; RX 45/55/120 mA min/typ/max; TX 750/800/850 mA at +25 °C and up to 1 A across -30 to +85 °C; project allocates 0.20 W RX and 3.3 W TX", "power_basis": "S10 VENDOR DATASHEET plus PROJECT ALLOCATIONS",
        "cost": (4500, 6500, 9000), "published_price": "No public price; project planning allowance only",
        "order_url": "https://gomspace.com/product/nanocom-ax100/", "order_route": "Add to GomSpace quote and specify AX100-U sales part 200315 plus supported Mode 5 configuration.",
        "availability": "Current product page and 2024 PCN support U/UL sale, but exact delivery revision, lead time and firmware remain quote controlled.",
        "vendor_facts": ["UHF option covers 430–440 MHz; project planning frequency 437 MHz is conditional on authorization.", "Adjustable 24–30 dBm output; 0.1–38.4 kbps family capability.", "I²C, UART and CAN/CSP; 20-position hard-gold FSI connector; current page identifies MCX antenna connector.", "Operating temperature -30 °C to +85 °C; PCB/assembly claims are catalog statements."],
        "configuration": ["AX100-U sales part 200315; Mode 5 only per S11.", "Initial mission data rate 1200 bit/s with measured complete-modem threshold ≤-123 dBm at PER ≤1% for the selected frame.", "Powered from D1-IF branch B at 3.30 V nominal; signal pins high impedance when unpowered.", "Right-angle MCX implementation and 50 Ω coax to B09; final antenna tuned on assembled spacecraft."],
        "interfaces": ["H05 power", "H07 CAN/CSP", "H10 50 Ω RF/MCX", "GOSH/UART service"],
        "open": ["Written acceptance of full 3.3 V supply tolerance/transients and D1-IF protection", "Exact Mode 5 waveform, licensing frequency, occupied bandwidth and ground modem compatibility", "Measured sensitivity and transmitter performance for delivered revision", "RF connector orientation/envelope and mating coax", "Radiation/SEE, qualification/acceptance, software license and lead time"],
        "sources": ["S09", "S10", "S11", "procurement/BOM.csv", "engineering/02_Budgets_and_Analyses.md", "engineering/03_Interfaces.md"],
    },
    {
        "id": "B08", "slug": "GomSpace_NanoDock_DMC3", "vendor": "GomSpace", "item": "NanoDock DMC-3 carrier, top-side two modules", "qty": 1,
        "kind": "Named COTS carrier with unconfirmed current availability", "mass": "51 g", "mass_basis": "PROVISIONAL project value from older indexed source; not verified against a current controlled document",
        "size": "88 × 88 × 1.6 mm used only as a CAD envelope assumption", "size_basis": "ASSUMPTION; current A3200 page describes the broader NanoDock platform as standard PC/104 size 90 × 96 mm",
        "power": "Unknown independently; project allocates 0.03 W nominal for interfaces/carrier/sensors combined and 0.02 W in recovery", "power_basis": "PROJECT ALLOCATION, not vendor requirement",
        "cost": (900, 1500, 2500), "published_price": "No current public price; project planning allowance only",
        "order_url": "https://gomspace.com/product/nanomind-a3200/", "order_route": "Contact GomSpace and request written confirmation that DMC-3 is orderable and supported with A3200 and AX100-U. The legacy direct datasheet URLs are not ordering routes.",
        "availability": "UNCONFIRMED. Registered S12/S13 direct PDFs returned 404; no current DMC-3 product page was verified.",
        "vendor_facts": ["Older project sources describe DMC-3 routing for daughter modules.", "No current controlled mechanical/electrical specification has been obtained."],
        "configuration": ["Carrier for two top-side modules: B06 A3200 and B07 AX100-U.", "Do not assume cross-vendor PC/104 pin compatibility to B02; route approved power/data through B10/B11.", "CAN bus must provide two endpoints and about 60 Ω unpowered bus resistance."],
        "interfaces": ["B06/B07 daughter-module connectors", "H04/H05 power routing", "H07 CAN routing", "Structure/standoff mounting"],
        "open": ["Whether DMC-3 can presently be purchased", "Exact order code, revision, supported module combination and top-side orientation", "Controlled outline, thickness, holes, connector heights and keep-outs", "Power and signal routing, CAN termination and current rating", "Mass, environmental evidence, price and lead time"],
        "sources": ["S07", "S12", "S13", "procurement/BOM.csv", "engineering/03_Interfaces.md", "drawings/freecad/CAD_SOURCE_TRACEABILITY.md"],
    },
    {
        "id": "B09", "slug": "ISISPACE_AntS_UHF_turnstile_5V", "vendor": "ISISPACE", "item": "AntS 1U–3U UHF turnstile, 5 V model", "qty": 1,
        "kind": "COTS deployable antenna requiring frequency/mechanical configuration", "mass": "<90 g", "mass_basis": "CURRENT VENDOR PAGE; project carries 90 g",
        "size": "98 × 98 × 7 mm stowed including supplied aluminum cover", "size_basis": "CURRENT VENDOR PAGE",
        "power": "<60 mW nominal for 5 V model; 2 W during deployment; maximum RF input 2 W", "power_basis": "CURRENT VENDOR PAGE",
        "cost": (1500, 2500, 4000), "published_price": "No public price; project planning allowance only",
        "order_url": "https://www.isispace.nl/product/vhf-uhf-antenna-for-1u-3u/", "order_route": "Select Turnstile and use ‘I want to buy’; specify UHF tuning and 5 V electronics.",
        "availability": "Current catalog product; exact turnstile frequency, element arrangement, connector and lead time require quote.",
        "vendor_facts": ["Up to four 55 cm tape-spring elements with redundant deployment system.", "Miniature 9-pin Omnetics electrical interface and I²C data.", "145–868 MHz family range; UHF main-beam gain 0 dBi and >50 MHz -10 dB bandwidth are catalog values.", "Operating -20 °C to +60 °C; deployment -5 °C to +60 °C; deployment under 5 s.", "Shipped-unit acceptance shown: functional and thermal cycling; not TVAC, vibration or shock."],
        "configuration": ["5 V UHF turnstile; final tuning on the complete spacecraft.", "Project commands deployment only at +5 to +45 °C and never while transmitting.", "Top accommodates B05 without obstructing stow or deployment.", "Separate isolated I²C branch and three-inhibit release/RF safety architecture."],
        "interfaces": ["H06 switched 5 V", "H09 isolated I²C", "H10 50 Ω RF", "B05 top-panel mount", "Structure and deployable keep-out"],
        "open": ["Authorized operating frequency and final tune requirement", "Exact RF connector/mating cable and full harness loss", "Signed B05/structure mounting arrangement and deployment envelope", "Release current/time trace and all-fault inhibit evidence", "Delivered-unit TVAC/vibration/shock scope, lead time and price"],
        "sources": ["S05", "procurement/BOM.csv", "engineering/01_Mission_and_Architecture.md", "engineering/03_Interfaces.md", "engineering/04_Mechanical_Thermal_Radiation.md"],
    },
    {
        "id": "B10", "slug": "D1IF_adapter", "vendor": "Integration vendor", "item": "D1-IF adapter: two 5 V to 3.3 V regulators, isolation and harness routing", "qty": 1,
        "kind": "Project-designed custom assembly using COTS candidate parts", "mass": "45 g", "mass_basis": "PROJECT ALLOCATION",
        "size": "88 × 88 × 6 mm CAD envelope", "size_basis": "ASSUMPTION; no schematic, layout or released PCB exists",
        "power": "Two independent 3.30 V branches: 1.0 A OBC design allocation and 1.2 A radio design allocation; project distribution efficiency 85% includes adapter losses", "power_basis": "PROJECT DESIGN ALLOCATION",
        "cost": (800, 1500, 3000), "published_price": "No product price; custom NRE/board/assembly/test planning allowance",
        "order_url": "Not applicable—release schematic/BOM/Gerbers and issue an RFQ to an integration/PCB assembly vendor. Candidate regulator reference: https://www.ti.com/product/TPSM82823", "order_route": "No purchase is authorized. First complete design and verification, then quote a flight assembly and engineering units.",
        "availability": "NOT DESIGN RELEASED. TI lists the candidate TPSM82823 as active, but that does not establish space suitability or adapter availability.",
        "vendor_facts": ["Candidate TPSM82823 is a catalog 3 A buck module, 2.4–5.5 V input, 0.6–4 V adjustable output, 2.0 × 2.5 × 1.1 mm package.", "TI lists output discharge, power-good, enable, soft start, short-circuit and overtemperature features.", "Candidate part is commercial catalog hardware; no radiation qualification is claimed."],
        "configuration": ["Two separate regulator channels supplied by separate ICEPS2 5 V outputs.", "Adjustable candidate starting point: 450 kΩ/100 kΩ 0.1% feedback, 10 µF input and 22 µF output X7R ≥10 V, subject to released analysis.", "Independent enables, output discharge, power-good telemetry and signal isolation against parasitic powering.", "Delivered radio rail target approximately 3.260–3.340 V DC, with ≤40 mV additional positive transient allocation."],
        "interfaces": ["H04 OBC branch", "H05 radio branch", "B02 switched 5 V inputs", "B08 carrier/harness routing", "Telemetry/control to B06"],
        "open": ["Schematic, complete component BOM, PCB stackup/layout, connectors and mechanical mounting", "Fault protection against feedback-open/switch-short overvoltage", "Stability/transient/EMI/thermal analysis and worst-case tolerance", "Radiation TID/SEE behavior and mission suitability", "Prototype, qualification and acceptance test plan; exact mass and cost"],
        "sources": ["S14", "procurement/BOM.csv", "engineering/03_Interfaces.md", "engineering/04_Mechanical_Thermal_Radiation.md", "drawings/freecad/FINDINGS.md"],
    },
    {
        "id": "B11", "slug": "flight_harness_RF_coax_switch_hardware", "vendor": "Integration vendor", "item": "Harness, RF coax, three-switch hardware allowance and strain relief", "qty": 1,
        "kind": "Custom integrated harness/hardware lot", "mass": "65 g", "mass_basis": "PROJECT ALLOCATION",
        "size": "Unknown; routing volume, lengths, bend radii and connector envelopes are not released", "size_basis": "UNKNOWN",
        "power": "No intentional load; must carry all H01–H13 currents with bounded voltage drop. RF path target ≤1 dB total loss.", "power_basis": "PROJECT REQUIREMENT",
        "cost": (500, 900, 1500), "published_price": "No product price; custom fabrication planning allowance",
        "order_url": "Not applicable—complete the harness drawing and issue an RFQ to a qualified space-harness/integration vendor.", "order_route": "Procure only from a released wire list, connector/contact schedule, routing drawing and workmanship/test specification.",
        "availability": "NOT DESIGN RELEASED.",
        "vendor_facts": ["No supplier, part number, quote or manufactured article exists in the current record."],
        "configuration": ["Implement documented H01–H13 without unreviewed stack-through mating.", "Use positively retained/keyed connections, strain relief and approved flight workmanship.", "Include 50 Ω radio coax and the allowed three separation-switch/RBF hardware scope; subtract overlaps after supplier quotes."],
        "interfaces": ["H01–H13 in engineering/03_Interfaces.md", "Every powered/data subsystem", "Structure bonding and mechanical supports"],
        "open": ["Full pin map, mating connector part numbers, contact genders and cavity assignments", "Wire/coax types, gauges, shielding, lengths, derating, bend radii and voltage drops", "Switch part numbers, placement, travel, force and inhibit topology", "Grounding/bonding/shield termination and EMC behavior", "Mass roll-up, workmanship standard, continuity/hipot/insulation/RF acceptance tests"],
        "sources": ["procurement/BOM.csv", "engineering/03_Interfaces.md", "engineering/04_Mechanical_Thermal_Radiation.md", "engineering/06_Integration_and_Verification.md"],
    },
    {
        "id": "B12", "slug": "battery_thermal_strap_and_isolation", "vendor": "Integration vendor", "item": "Battery thermal strap/isolation, approved films and mounting", "qty": 1,
        "kind": "Custom thermal/mechanical integration lot", "mass": "35 g", "mass_basis": "PROJECT ALLOCATION",
        "size": "Unknown; represented within surrounding stack allocations only", "size_basis": "UNKNOWN pending thermal design and vendor geometry",
        "power": "No separate electrical load is allocated; EPS heater is budgeted at 0.10 W orbit average and 1 W instantaneous equivalent at 10% duty", "power_basis": "PROJECT THERMAL/POWER ALLOCATION; heater is part of B02",
        "cost": (200, 400, 800), "published_price": "No product price; custom material/fabrication planning allowance",
        "order_url": "Not applicable—select materials after thermal analysis and issue an RFQ/purchase order from a released drawing and material list.", "order_route": "Procure characterized materials and fabricated strap/mount only after thermal-balance inputs close.",
        "availability": "NOT DESIGN RELEASED.",
        "vendor_facts": ["No material, supplier or part number has been selected; ‘approved films’ is a requirement, not a component selection."],
        "configuration": ["Provide a characterized conductive path and deliberate isolation for the B02 integrated battery.", "Retain battery mechanically independent of electrical terminals.", "Support project battery target +5 to +35 °C in normal operation and charge inhibit outside the approved range."],
        "interfaces": ["B02 battery/EPS", "B01 structure", "Thermal coatings/films on available non-cell area"],
        "open": ["Thermal network and required conductance", "Strap material/cross-section/attachment and contact resistance", "Isolation film type, thickness, outgassing, dielectric and radiation evidence", "Heater actual power/control and stuck-on/off protection", "Fasteners, torque, workmanship, mass and acceptance test"],
        "sources": ["procurement/BOM.csv", "engineering/02_Budgets_and_Analyses.md", "engineering/04_Mechanical_Thermal_Radiation.md"],
    },
    {
        "id": "B13", "slug": "integration_fasteners_bonding_brackets", "vendor": "Integration vendor", "item": "Integration fasteners, bonding and small brackets", "qty": 1,
        "kind": "Custom integration hardware lot", "mass": "25 g", "mass_basis": "PROJECT ALLOCATION",
        "size": "Unknown; no individual part geometry is released", "size_basis": "UNKNOWN",
        "power": "No electrical load; bonding path resistance/EMC requirements remain to be specified", "power_basis": "FUNCTIONAL DESCRIPTION",
        "cost": (150, 300, 600), "published_price": "No product price; project allowance for a future itemized hardware lot",
        "order_url": "Not applicable—itemize only after mounting drawings and bonding plan are released, then order from qualified hardware suppliers/integrator.", "order_route": "No blanket hardware kit is selected.",
        "availability": "NOT ITEMIZED OR DESIGN RELEASED.",
        "vendor_facts": ["No supplier, material, finish, fastener size or bracket drawing has been selected."],
        "configuration": ["Only hardware needed to mount and bond the already documented B01–B16 architecture.", "Do not use this allowance to hide ballast, blanket shielding or new subsystems.", "Use approved locking methods and installation/torque records."],
        "interfaces": ["B01 structure", "All mounted boards/subassemblies", "Intentional chassis bond"],
        "open": ["Itemized fastener/bracket list and double-count check against B01/B11/B16", "Materials, coatings, galvanic compatibility and outgassing", "Thread engagement, torque, locking and preload analysis", "Bond locations, resistance acceptance and corrosion protection", "As-built mass and spare quantities"],
        "sources": ["procurement/BOM.csv", "engineering/04_Mechanical_Thermal_Radiation.md", "engineering/06_Integration_and_Verification.md"],
    },
    {
        **COMMON_ISIS_SOLAR, "id": "B14", "slug": "ISISPACE_plusX_camera_aperture_solar_panel", "vendor": "ISISPACE", "item": "+X two-cell panel with camera aperture", "qty": 1,
        "kind": "COTS-derived custom solar/payload panel", "mass": "50 g", "mass_basis": "PROJECT ALLOCATION based on current 1U catalog mass; aperture configuration unquoted",
        "size": "Planform, aperture and cell layout unknown; 1.2–2.0 mm typical thickness", "size_basis": "CURRENT VENDOR PAGE for thickness; geometry UNKNOWN",
        "power": "Procurement target ≥1.8 W BOL after aperture/obstruction effects; nominal two-cell series voltage approximately 5.4 V BOL", "power_basis": "PROJECT REQUIREMENT plus CURRENT VENDOR approximate per-cell voltage",
        "cost": (1500, 2300, 3500), "published_price": "No public price; higher project allowance reflects custom aperture",
        "configuration": ["+X body-mounted panel with supplier-designed camera aperture and baffle interface.", "Guaranteed ≥1.8 W BOL for the delivered panel under supplier-stated conditions.", "No cell cutting by the project; supplier must sign cell routing and structural design."],
        "interfaces": ["B15/B16 optical aperture and baffle", "H01–H03 to ICEPS2 MPPT", "B01 structure/rails", "Custom flat inline Omnetics and included AWG26 harness"],
        "open": ["Aperture diameter/location and lens/baffle clearance", "Feasible two-cell string layout around aperture", "Hot/cold IV curves, shading behavior, blocking topology and MPPT startup", "Structural margin and panel mounting around aperture", "As-ordered mass, price, lead time and acceptance evidence"],
    },
    {
        "id": "B15", "slug": "CrystalSpace_CS101_Kikas_camera", "vendor": "CrystalSpace", "item": "CS-101 Kikas 5 MP camera with infinity-focus wide-angle lens", "qty": 1,
        "kind": "COTS camera requiring optical/electrical configuration", "mass": "50 g", "mass_basis": "CURRENT VENDOR PAGE",
        "size": "42 × 25 × 45 mm", "size_basis": "CURRENT VENDOR PAGE; orientation in spacecraft is a project decision pending CAD",
        "power": "Unknown vendor supply/consumption; project caps camera at ≤2 W peak and ≤300 s powered/day, with 0.02 W average including OBC processing", "power_basis": "PROJECT ALLOCATION only",
        "cost": (3000, 6000, 10000), "published_price": "No public price; project planning allowance only",
        "order_url": "https://crystalspace.eu/products/cs-101-kikas/", "order_route": "Use CrystalSpace contact/product-overview route and request a configured quotation; the detailed brief is gated.",
        "availability": "Current product page; exact lens, electronics, protocol, revision, lead time and acceptance scope require quote.",
        "vendor_facts": ["Current page states 5 MP, 50 g, 42 × 25 × 45 mm and TRL 9.", "Page describes multiple field-of-view lenses and communication protocols, Earth-observation use and ITAR-free status.", "No current public voltage, consumption, shutter, image-format or environmental table was obtained."],
        "configuration": ["Visible, calibrated infinity-focus lens with roughly 60° horizontal FOV.", "Exposure control down to ≤1 ms; confirm shutter/readout behavior.", "JPEG or reduced-resolution output path and UART or RS485 supplier option compatible with B06.", "Mount with 25 mm dimension along Z in the documented 27 mm bay; optical axis toward +X."],
        "interfaces": ["H13 switched payload power and serial", "B16 bracket/baffle/harness", "B14 aperture", "B06 storage/processing"],
        "open": ["Supply voltage, logic levels, peak/idle energy, cold-start and readout time", "Protocol, connector/pinout, image formats/resolutions, memory and command documentation", "Sensor model, spectral response, shutter type, exposure limits and exact lens/FOV", "Sun exposure tolerance, operating/storage temperature and thermal-vacuum focus behavior", "Radiation/qualification/acceptance evidence, price, lead time and export classification"],
        "sources": ["S23", "procurement/BOM.csv", "engineering/02_Budgets_and_Analyses.md", "engineering/03_Interfaces.md", "engineering/07_Imaging_Payload.md"],
    },
    {
        "id": "B16", "slug": "camera_bracket_baffle_harness", "vendor": "Integration vendor", "item": "Camera bracket, baffle and harness", "qty": 1,
        "kind": "Custom payload integration assembly", "mass": "20 g", "mass_basis": "PROJECT ALLOCATION",
        "size": "Must fit the 27 mm camera bay around B15's 25 mm Z dimension; exact geometry unknown", "size_basis": "PROJECT ALLOCATION and CURRENT CAMERA ENVELOPE; only about 1 mm nominal clearance per side remains before bracket/tolerance effects",
        "power": "No separate electrical load; harness carries the unresolved B15 ≤2 W peak allocation", "power_basis": "PROJECT ALLOCATION",
        "cost": (300, 600, 1200), "published_price": "No product price; custom design/fabrication planning allowance",
        "order_url": "Not applicable—release camera CAD, bracket/baffle drawing and harness definition, then issue an RFQ to the integration/machining vendor.", "order_route": "Do not fabricate from the present envelope model.",
        "availability": "NOT DESIGN RELEASED.",
        "vendor_facts": ["No supplier, material, coating, connector, drawing or manufactured article exists in the current record."],
        "configuration": ["Hold B15 at infinity-focus alignment with optical axis toward +X.", "Provide short baffle/stray-light control without rail, panel-cell or AntS deployment obstruction.", "Maintain serviceability, contamination control and a positive mechanical load path."],
        "interfaces": ["B15 camera", "B14 aperture panel", "B01 structure", "H13 payload harness"],
        "open": ["Vendor camera CAD, mounting holes, datum scheme and connector envelope", "Bracket material, thickness, attachment, tolerance and load analysis", "Baffle field stop/FOV, coating, contamination/outgassing and solar exposure", "Harness strain relief and connector access", "Post-vibration/TVAC optical alignment acceptance and final mass"],
        "sources": ["procurement/BOM.csv", "engineering/04_Mechanical_Thermal_Radiation.md", "engineering/07_Imaging_Payload.md", "drawings/freecad/FINDINGS.md"],
    },
]


def money(values: tuple[int, int, int]) -> str:
    return " / ".join(f"€{v:,}" for v in values)


def bullets(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values)


def make_card(c: dict) -> str:
    return f"""# {c['id']} — {c['item']}

Audit date: {AUDIT_DATE}  
Evidence state: **DOCUMENTED/AUDITED; not purchased, tested, or procurement released**

## Identification and procurement

| Field | Audited value |
|---|---|
| BOM line | {c['id']} |
| Supplier | {c['vendor']} |
| Quantity | {c['qty']} |
| Procurement type | {c['kind']} |
| Project unit estimate, low/base/high | {money(c['cost'])} |
| Public price evidence | {c['published_price']} |
| Order/quote URL | {c['order_url']} |
| Ordering route | {c['order_route']} |
| Availability | {c['availability']} |

The cost range is an engineering allowance unless explicitly identified as a current published price. It excludes taxes, freight, duties, configuration NRE, spares, integration, testing and support unless a future quotation says otherwise.

## Size, mass and power

| Attribute | Value | Evidence basis |
|---|---|---|
| Unit mass | {c['mass']} | {c['mass_basis']} |
| Envelope | {c['size']} | {c['size_basis']} |
| Electrical power / generation | {c['power']} | {c['power_basis']} |

## Supplier facts retained by the project

{bullets(c['vendor_facts'])}

## Exact project configuration

{bullets(c['configuration'])}

## Mechanically/electrically relevant interfaces

{bullets(c['interfaces'])}

## Procurement-release blockers

{bullets(c['open'])}

## Required quote/delivery evidence

- Exact part/configuration number and controlled hardware/software revision.
- Firm unit and nonrecurring prices, quote validity, lead time, Incoterms, payment terms, warranty and export classification.
- As-ordered mass, drawing and STEP model where applicable; connector/pin map and electrical limits where applicable.
- Included cables, mating connectors, fasteners, software/licenses, support and test reports; explicit exclusions.
- Delivered-unit acceptance tests and profiles, qualification heritage applicable to the delivered revision, material/workmanship certificates, and lot traceability as applicable.
- One-year 450–500 km LEO radiation/SEE and life evidence appropriate to the function, or a documented project verification plan where supplier evidence is absent.

## Traceability

{bullets(c['sources'])}

No supplier was contacted and no purchase was made during this audit. A catalog page, heritage statement, CAD envelope, or AI-generated record does not establish flightworthiness.
"""


def write_outputs() -> None:
    bom_path = ROOT.parent / "procurement" / "BOM.csv"
    with bom_path.open(encoding="utf-8-sig", newline="") as f:
        bom = list(csv.DictReader(f))
    assert [r["id"] for r in bom] == [c["id"] for c in COMPONENTS], "audit/BOM ID drift"
    for row, component in zip(bom, COMPONENTS):
        assert int(row["quantity"]) == component["qty"], f"quantity drift: {component['id']}"
        assert tuple(int(row[k]) for k in ("unit_low_EUR_estimate", "unit_base_EUR_estimate", "unit_high_EUR_estimate")) == component["cost"], f"cost drift: {component['id']}"

    cards = ROOT / "cards"
    cards.mkdir(exist_ok=True)
    rows = []
    for c in COMPONENTS:
        filename = f"{c['id']}_{c['slug']}.md"
        (cards / filename).write_text(make_card(c), encoding="utf-8", newline="\n")
        rows.append({
            "id": c["id"], "vendor": c["vendor"], "item": c["item"], "quantity": c["qty"],
            "unit_cost_low_EUR_estimate": c["cost"][0], "unit_cost_base_EUR_estimate": c["cost"][1], "unit_cost_high_EUR_estimate": c["cost"][2],
            "published_price": c["published_price"], "unit_mass": c["mass"], "mass_basis": c["mass_basis"],
            "dimensions": c["size"], "size_basis": c["size_basis"], "power": c["power"], "power_basis": c["power_basis"],
            "order_or_quote_url": c["order_url"], "availability": c["availability"], "audit_date": AUDIT_DATE,
            "card": f"cards/{filename}",
        })
    with (ROOT / "component_audit.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    assert len(COMPONENTS) == 16
    assert [c["id"] for c in COMPONENTS] == [f"B{i:02d}" for i in range(1, 17)]
    write_outputs()
