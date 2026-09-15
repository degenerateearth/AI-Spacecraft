"""Generate the complete proposed DEGENERATE-1 operating component set.

The output is a proposal and gap register. A row is not a Phase 1 selection
unless phase1_disposition is PHASE 1 BASELINE.
"""
from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "Proposed_Operating_Component_Set.csv"
CARD_DIR = HERE / "operating_set_cards"

BASE_FIELDS = [
    "set_id", "segment", "required_function", "quantity", "manufacturer",
    "proposed_component", "exact_identifier_or_project_part", "source_ids",
    "order_url", "phase1_disposition", "functional_basis",
    "evidence_or_design_gap", "blocked_release_or_analysis",
]
FIELDS = BASE_FIELDS + ["known_size_and_mass", "known_power_or_generation",
                        "cost_and_availability"]


def item(*values):
    assert len(values) == len(BASE_FIELDS)
    return dict(zip(BASE_FIELDS, values))


R = [
item("FLT-001","Flight","Primary 1U structure, rails and enclosure","1","ISISPACE","1-Unit CubeSat Structure","Storefront SKU 100000","S06; S01; S33","https://www.cubesatshop.com/product/1-unit-cubesat-structure/","CANDIDATE / EVIDENCE INCOMPLETE","Current 1U order route and provisional EXOpod-compatible allocation","Manufacturer part/configuration, controlled drawing, mass, tolerances, finish, fasteners and qualification evidence incomplete","Structure selection, mass properties, load path and deployer-fit release"),
item("FLT-002","Flight","Three independent separation/inhibit switches and RBF source isolation","1 configured set","ISISPACE + project integration","ICEPS2 three-switch/RBF option plus structure-mounted actuators","Exact actuator and EPS option identifiers unknown","S03; S01; S33","https://www.isispace.nl/product/compact-electrical-power-system/","CANDIDATE / EVIDENCE INCOMPLETE / NO DOCUMENTED COTS IMPLEMENTATION","Required to prevent powered hazards before separation","Exact actuator parts/travel, wiring truth table, independence, solar/test-source isolation and delivered option unavailable","Launch safety and RF/antenna-release authorization"),
item("FLT-003","Flight","Solar conversion, battery charge control and switched power distribution","1","ISISPACE","ICEPS2 Type A","Type A; exact sales/options code unknown","S02; S03","https://www.isispace.nl/product/compact-electrical-power-system/","CANDIDATE / EVIDENCE INCOMPLETE","Provides MPPT, battery, protected switched outputs and housekeeping in one compact assembly","Current page states 22.5 Wh while linked datasheet states 28.8 Wh; exact configuration, integrated transients and commands incomplete","Energy/life closure, rail compatibility and procurement release"),
item("FLT-004","Flight","Rechargeable eclipse/restart energy storage","1 integrated pack","ISISPACE","ICEPS2 Type A integrated battery","Exact cell/pack configuration unknown","S02; S03","https://www.isispace.nl/product/compact-electrical-power-system/","CANDIDATE / EVIDENCE INCOMPLETE","Integrated pack minimizes separate harness and volume","Cell identity, capacity conflict, lot, cycle/calendar life and installed thermal properties unavailable","Twelve-month capacity, battery safety and component-specific thermal analysis"),
item("FLT-005","Flight","Body-mounted generation on +Y, -Y and -X faces","3","ISISPACE","Customizable 1U two-cell fixed panel","Three exact face drawings/order codes unknown","S04; S22","https://www.isispace.nl/product/small-satellite-solar-panels/","CANDIDATE / EVIDENCE INCOMPLETE","Two-cell 1U family matches body-mounted concept","Signed planforms, guaranteed hot/cold/EOL IV curves, tolerances, pinout and mounting missing","Orbit/attitude energy closure and panel fit"),
item("FLT-006","Flight","Body-mounted generation on -Z face with separation-switch clearances","1","ISISPACE","Customizable 1U two-cell fixed panel","Exact -Z relieved configuration unknown","S04","https://www.isispace.nl/product/small-satellite-solar-panels/","CANDIDATE / EVIDENCE INCOMPLETE","Family can be customized around integration features","Relief drawing, mass, mounting, IV limits and harness data missing","Power and switch/rail interference release"),
item("FLT-007","Flight","Body-mounted generation on +Z face with antenna interface","1","ISISPACE","Customizable 1U two-cell fixed panel","Exact +Z AntS configuration unknown","S04; S05","https://www.isispace.nl/product/small-satellite-solar-panels/","CANDIDATE / EVIDENCE INCOMPLETE","Family is marketed with customizable cutouts/interfaces","AntS mounting drawing, exact mass, IV limits and harness data missing","Power and antenna mounting/deployment release"),
item("FLT-008","Flight","Body-mounted generation on +X camera face","1","ISISPACE","Customizable 1U two-cell panel with camera aperture","Exact aperture configuration unknown","S04; S49","https://www.isispace.nl/product/small-satellite-solar-panels/","CANDIDATE / EVIDENCE INCOMPLETE","A customized aperture could retain generation around piCAM","Aperture/cell layout, guaranteed >=1.8 W BOL, IV limits, mass and mounting absent","Imaging aperture feasibility and power closure"),
item("FLT-009","Flight","Command/data handling, 128 MB image storage, RTC, watchdog and rate sensing","1","GomSpace","NanoMind A3200","NanoMind A3200; exact delivered sales/revision code unknown","S07; S08","https://gomspace.com/product/nanomind-a3200/","CANDIDATE / EVIDENCE INCOMPLETE","Public datasheet provides processor, 128 MB NOR, FRAM, SDRAM, RTC, watchdog, CAN/I2C/UART and sensors","Delivered revision, BSP/SDK terms, errata, guaranteed recovery behavior and application-specific radiation assurance incomplete","Flight software release, fault containment and one-year reliability claim"),
item("FLT-010","Flight","Mechanical carrier and bus routing for OBC/radio","1","GomSpace","NanoDock DMC-3","Product 200232; OSF 1012964 configuration not completed","S44; S45; S46; S47","https://gomspace.com/product/nanodock-dmc-3/","CANDIDATE / EVIDENCE INCOMPLETE","Exact current carrier has public mechanics, pinouts, option sheet and qualification certificate","Stack connector, X/P connector population, supply matrix, AUX routing and CAN termination depend on unreleased D1-IF/harness pin map","Carrier configuration and procurement release"),
item("FLT-011","Flight","UHF command, health telemetry and image downlink","1","GomSpace","NanoCom AX100-U","Sales part 200315; Mode 5","S09; S10; S11","https://gomspace.com/product/nanocom-ax100/","CANDIDATE / EVIDENCE INCOMPLETE","Current U-band flight radio with public RF/electrical/mechanical data and Mode 5 lifecycle notice","Current firmware/API, exact acceptance evidence, approved operating frequency and application-specific radiation basis incomplete","Regulatory filing, software integration and one-year reliability claim"),
item("FLT-012","Flight","Deployable UHF turnstile and release electronics","1","ISISPACE","VHF/UHF Antenna System for 1U-3U","Turnstile, 5 V; exact order code/frequency/connector unknown","S05","https://isispace.nl/product/vhf-uhf-antenna-for-1u-3u/","CANDIDATE / EVIDENCE INCOMPLETE","Compact current family matches 1U and planned UHF link","Exact tuned variant, element layout/pattern, RF connector, pinout/commands, deployed envelope and test report absent","Integrated link margin, coax release and deployment clearance/reliability"),
item("FLT-013","Flight","Occasional recognizable Earth image capture","1","SkyFox Labs","piCAM Flight Model","piCAM/FM","S48; S49","https://www.skyfoxlabs.com/product/27-picam","CANDIDATE / EVIDENCE INCOMPLETE","Exact current product has VGA JPEG output, UART protocol, pinout, mechanics, optics guidance and listed price","95 mA datasheet versus 90 mA page; exact lens/MTF/exposure acceptance, qualification report and one-year radiation application evidence incomplete","Final image probability, power maximum and one-year survival claim"),
item("FLT-014","Flight","Independent 5 V to controlled 3.3 V avionics rails, switching and latchup protection","1","DEGENERATE-1 custom","Power/interface board","D1-IF-001","S03; S08; S10; S14; S49","","CUSTOM COMPONENT / DESIGN INCOMPLETE","Required because ICEPS2 direct 3.3 V maximum can exceed AX100 absolute maximum and piCAM recommends current limiting","No released schematic, IC/protection selection, BOM, layout, thermal/radiation/fault analysis or test specification","Safe avionics power, fault containment, carrier option selection and harness release"),
item("FLT-015","Flight","Power/data/RBF/separation-switch harness and strain relief","1 set","DEGENERATE-1 custom","Flight wire harness","D1-HAR-001","S03; S08; S10; S45; S46; S49","","CUSTOM COMPONENT / DESIGN INCOMPLETE","Connects all selected power, data, inhibit and service interfaces","Exact mating housings/contacts, wire types/gauges, lengths, shielding, pin map, derating and workmanship not released","Voltage drop, EMC, inhibit independence, CAD routing and assembly"),
item("FLT-016","Flight","50-ohm radio-to-antenna RF interconnect","1","DEGENERATE-1 custom","RF coax assembly","D1-RF-001","S05; S10","","CUSTOM COMPONENT / DESIGN INCOMPLETE","AX100 uses MCX and the integrated loss allocation is <=1 dB","AntS exact RF connector, cable type, connectors, length, bend radius, retention and measured loss absent","RF interface, link margin and mechanical routing"),
item("FLT-017","Flight","Camera mount, aperture baffle and light/thermal isolation","1","DEGENERATE-1 custom","piCAM bracket/baffle assembly","D1-CAM-MNT-001","S49","","CUSTOM COMPONENT / DESIGN INCOMPLETE","piCAM public drawing gives bracket envelope, four M2.5 holes and aperture-gap guidance","Material, finish, geometry, tolerances, fasteners, loads, stray-light and thermal analyses not released","Camera fit, optical clearance, structural margin and thermal interface"),
item("FLT-018","Flight","Battery/EPS thermal interface and electrical isolation","1","DEGENERATE-1 custom","Battery thermal-interface assembly","D1-THM-001","S02; S03; TMI-001","","CUSTOM COMPONENT / DESIGN INCOMPLETE","A defined measurable interface is required before component-specific thermal prediction","Material part numbers, thickness/area, conductance, insulation, fasteners, surface preparation and test method absent","Battery charging/survival thermal analysis"),
item("FLT-019","Flight","Mounting, locking, bonding and chassis-reference hardware","1 itemized set","DEGENERATE-1 custom","Integration hardware set","D1-MECH-HW-001","S01; S33; selected supplier drawings","","CUSTOM COMPONENT / DESIGN INCOMPLETE","Required to retain boards, bond conductive structure and survive launch","Fastener/washer/insert/bonding-jumper/locking-material part numbers, torque, interfaces and acceptance inspection absent","Load path, grounding, mass rollup and assembly release"),
item("GND-001","Ground","Mode 5 UHF receive and command modem","1","GomSpace","NanoCom AX100-U used as ground modem","Sales part 200315; Mode 5","S09; S10; S11","https://gomspace.com/product/nanocom-ax100/","CANDIDATE / EVIDENCE INCOMPLETE","Matching modem avoids an assumed third-party Mode 5 implementation","Ground firmware/API/license, host interface and authorized frequency/configuration not established","End-to-end waveform and command compatibility"),
item("GND-002","Ground","Carrier/USB interface for ground modem","1","GomSpace","NanoDock DMC-3","Product 200232; ground option set unknown","S44; S45; S46","https://gomspace.com/product/nanodock-dmc-3/","CANDIDATE / EVIDENCE INCOMPLETE","DMC-3 exposes USB-to-UART console and carries AX100","Exact ground configuration, power entry, connector population and required host control path not released","Ground modem electrical/host integration"),
item("GND-003","Ground","Current-limited regulated power for ground modem/carrier","1","Not selected","Bench or enclosed DC supply","NO COMPLIANT PART IDENTIFIED","S10; S45","","NO COMPLIANT PART IDENTIFIED","A stable protected source is required to operate the modem","Input connector and ground-carrier option are not frozen, so voltage/current/transient and mating requirements cannot be finalized","Ground modem operation and safety"),
item("GND-004","Ground","Circularly polarized 430-438 MHz directional antenna","1","M2 Antenna Systems","436CP42UG","436CP42UG","S28; S29","https://www.m2inc.com/M2FACTORYDIRECT?page=2","CANDIDATE / EVIDENCE INCOMPLETE","Manufacturer data support the planned high-gain 70 cm ground link","Authorized frequency, installed pattern/gain, site/mast/rotator loads and full feed loss are not established","Final link margin and site release"),
item("GND-005","Ground","Azimuth/elevation pointing and computer control","1 system","Not selected","Antenna rotator, controller and position feedback","NO COMPLIANT PART IDENTIFIED","S28; engineering/05","","NO COMPLIANT PART IDENTIFIED","The 5.7 m class antenna must track LEO passes","No exact rotator/controller has been selected or checked for antenna wind/torque, pointing, duty, interface and outdoor limits","Automated pass tracking and ground-site mechanical safety"),
item("GND-006","Ground","Low-loss outdoor RF feedline and connectors","1 installed run","Site-specific custom","Ground RF feedline assembly","D1-GND-RF-001","S28; engineering/05","","CUSTOM COMPONENT / SITE DESIGN INCOMPLETE","Budget permits <=1 dB receive feed loss","Cable/connector/lightning-protection types, run length, bend radius, weather sealing and measured loss absent","Final link margin and installation release"),
item("GND-007","Ground","Receive filtering/LNA and transmit/receive routing","1 chain","Not selected","70 cm filter, near-antenna LNA and duplex/T-R protection","NO COMPLIANT PART IDENTIFIED","engineering/05","","NO COMPLIANT PART IDENTIFIED","Needed if feed loss/noise and two-way switching cannot be met by modem placement","Authorized frequency, modem RF interface, gain/noise/P1dB, filtering and switching topology are not frozen","Receiver sensitivity, transmitter protection and lawful emissions"),
item("GND-008","Ground","Mast, foundation, bonding, lightning and weather protection","1 site","Site-specific custom","Ground antenna support/protection installation","D1-GND-SITE-001","S28; engineering/05","","CUSTOM COMPONENT / SITE DESIGN INCOMPLETE","Required for safe permanent operation of the selected antenna","Site, wind/ice/lightning criteria, structural design, grounding parts and permits unknown","Ground-station safety, reliability and cost"),
item("GND-009","Ground","Station computer, storage, network/time and control interfaces","1","Not selected","Ground station computer","NO COMPLIANT PART IDENTIFIED","engineering/05","","NO COMPLIANT PART IDENTIFIED","Runs pass prediction, modem control, packet archive and image reconstruction","Software/OS interfaces and storage/backup/time requirements are not released; no exact hardware selected","Ground software integration and operating cost"),
item("GND-010","Ground","Physical printing of reconstructed image","1","Not selected","Color or monochrome printer","NO COMPLIANT PART IDENTIFIED","Mission/Cornfield Criterion","","NO COMPLIANT PART IDENTIFIED","Required only for the final printed-image success criterion","Print size/media/interface/archival requirements and exact hardware are not selected","End-to-end mission demonstration"),
]

assert len(R) == 29
assert len({r["set_id"] for r in R}) == len(R)
assert not any(r["phase1_disposition"] == "PHASE 1 BASELINE" for r in R)

SUPPLEMENT = {
"FLT-001":("About 100 x 100 x 113.5 mm project envelope; 150 g project allocation; manufacturer values UNKNOWN","Passive","EUR 3,450 indicative storefront; 4-6 weeks stated; exact configuration not quoted"),
"FLT-002":("Integrated configuration; actuator geometry and added mass UNKNOWN","Passive switch paths; hazard-source isolation topology UNKNOWN","Included/option cost UNKNOWN"),
"FLT-003":("96 x 92 x 26.45 mm; 184 +/-5 g including battery","MPPT inputs; VD0 plus four 5 V and four 3.3 V outputs; exact integrated transient envelope incomplete","QUOTE REQUIRED; existing base planning allowance EUR 6,500 including battery"),
"FLT-004":("Included in FLT-003 mass/envelope","22.5 Wh current page versus 28.8 Wh datasheet conflict","Included in FLT-003; exact pack configuration unknown"),
"FLT-005":("50 g each family value; 1.2-2.0 mm typical thickness; exact planforms UNKNOWN","Approximately 1.23 W and 2.7 V per cell family values; not guaranteed for selected faces","QUOTE REQUIRED; existing base allowance EUR 1,800 each"),
"FLT-006":("50 g family value; exact planform/relief UNKNOWN","Approximate family cell values only; selected-face IV limits UNKNOWN","QUOTE REQUIRED; existing base allowance EUR 1,800"),
"FLT-007":("50 g family value; exact planform/interface UNKNOWN","Approximate family cell values only; selected-face IV limits UNKNOWN","QUOTE REQUIRED; existing base allowance EUR 1,800"),
"FLT-008":("50 g project allocation from family; aperture geometry UNKNOWN","Project target >=1.8 W BOL; no configuration guarantee","QUOTE REQUIRED; existing base allowance EUR 2,300"),
"FLT-009":("65 x 40 x 7.1 mm; 24 g including shield","3.2-3.4 V; datasheet current varies with clock/workload/peripherals","QUOTE REQUIRED; existing base planning allowance EUR 5,500"),
"FLT-010":("91.9 x 88.7 x 8.6 mm; 51 g without daughterboards","Passive in flight; USB-to-UART circuit powered only from USB","QUOTE REQUIRED; existing base planning allowance EUR 1,500"),
"FLT-011":("65 x 40 x 6.5 mm; 24.5 g","3.3 V; public RX/TX current tables; integrated rail transient compatibility open","QUOTE REQUIRED; existing base planning allowance EUR 6,500"),
"FLT-012":("98 x 98 x 7 mm stowed with cover; <90 g","5 V model <60 mW nominal; 2 W deployment; <=2 W RF input","QUOTE REQUIRED; existing base planning allowance EUR 2,500"),
"FLT-013":("33 x 33 x 19 mm body plus optics; 48 x 33 mm bracket; 40 g lens-dependent","2.7-3.6 V; 95 mA datasheet operating value versus 90 mA page","EUR 4,950 quantity one; 2-4 weeks plus shipping on current page"),
"FLT-014":("Target allocation 45 g is not a released part property","Two 5 V-to-3.3 V rails plus separately switched/current-limited camera branch; limits unreleased","Existing EUR 1,500 base allowance only; design/NRE/test cost UNKNOWN"),
"FLT-015":("Geometry and mass UNKNOWN; prior combined harness/coax/switch allocation cannot be assigned to this exact assembly","Carries EPS power, CAN, I2C, UART, switches and service lines; losses UNKNOWN","Custom fabrication/NRE cost UNKNOWN"),
"FLT-016":("Length and mass UNKNOWN","50 ohm; <=1 dB complete-assembly loss requirement","Custom fabrication/test cost UNKNOWN"),
"FLT-017":("Geometry and mass UNKNOWN; prior 20 g allocation is not a part property","Passive; installed thermal path and optical behavior UNKNOWN","Custom fabrication/NRE/test cost UNKNOWN"),
"FLT-018":("Geometry and mass UNKNOWN; prior 35 g allowance withdrawn as component evidence","Passive thermal/electrical interface; conductance UNKNOWN","Material, fabrication and test cost UNKNOWN"),
"FLT-019":("Itemized geometry and mass UNKNOWN; prior 25 g allowance is not a part property","Passive; bond resistance requirement not released","Hardware/fabrication/test cost UNKNOWN"),
"GND-001":("65 x 40 x 6.5 mm; 24.5 g before carrier/enclosure","3.3 V; TX/RX values per AX100 datasheet; ground configuration open","QUOTE REQUIRED; separate from flight-radio cost"),
"GND-002":("91.9 x 88.7 x 8.6 mm; 51 g before modem/enclosure","Passive carrier; USB circuit uses 5 V USB; modem supply routing open","QUOTE REQUIRED; separate from flight-carrier cost"),
"GND-003":("UNKNOWN","Required output cannot be frozen until GND-002 option and enclosure are defined","UNKNOWN"),
"GND-004":("Approximately 5.7 m boom; exact installed mass/load properties require datasheet/site extraction","Passive; 430-438 MHz, 18.9 dBic catalog gain","USD 910.95 storefront price on 2026-09-15"),
"GND-005":("UNKNOWN; must carry GND-004 wind/torque loads","Mains/control power UNKNOWN","UNKNOWN"),
"GND-006":("Site length and mass UNKNOWN","50 ohm; installed receive-feed loss requirement <=1 dB","UNKNOWN"),
"GND-007":("UNKNOWN","Gain/noise/P1dB/filter rejection/T-R limits UNKNOWN","UNKNOWN"),
"GND-008":("Site dependent","Passive except rotator/lightning auxiliaries","UNKNOWN; separate ground-station/site cost"),
"GND-009":("UNKNOWN","Mains power and storage/network requirements UNKNOWN","UNKNOWN; existing computer may be usable only after interface definition"),
"GND-010":("UNKNOWN","Mains/USB/network requirements UNKNOWN","UNKNOWN; ordinary printer selection deferred until print requirement is released"),
}
assert set(SUPPLEMENT) == {r["set_id"] for r in R}
for r in R:
    r.update(dict(zip(FIELDS[-3:], SUPPLEMENT[r["set_id"]])))
    if not r["order_url"]:
        r["order_url"] = "NOT APPLICABLE — custom item or no compliant part selected"

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(R)

CARD_DIR.mkdir(exist_ok=True)
for r in R:
    title = r["proposed_component"]
    lines = [
        f'# {r["set_id"]} — {title}', "",
        f'**Phase 1 disposition:** {r["phase1_disposition"]}  ',
        f'**Segment:** {r["segment"]}  ',
        f'**Required function:** {r["required_function"]}', "",
        "## Identity and procurement", "",
        "| Field | Record |", "|---|---|",
        f'| Manufacturer | {r["manufacturer"]} |',
        f'| Exact identifier/project part | {r["exact_identifier_or_project_part"]} |',
        f'| Quantity | {r["quantity"]} |',
        f'| Order URL | {r["order_url"]} |',
        f'| Cost and availability | {r["cost_and_availability"]} |',
        f'| Primary source IDs | {r["source_ids"]} |', "",
        "## Engineering properties", "",
        "| Property | Record |", "|---|---|",
        f'| Size and mass | {r["known_size_and_mass"]} |',
        f'| Power or generation | {r["known_power_or_generation"]} |',
        f'| Functional basis | {r["functional_basis"]} |', "",
        "## Evidence decision", "",
        f'**Gap:** {r["evidence_or_design_gap"]}', "",
        f'**Blocked release or analysis:** {r["blocked_release_or_analysis"]}', "",
        "This card proposes a required item; it is not procurement authority, an",
        "as-built record, qualification evidence or proof of compatibility.", "",
    ]
    (CARD_DIR / f'{r["set_id"]}.md').write_text("\n".join(lines), encoding="utf-8")

print(f"wrote {len(R)} rows to {OUT} and {len(R)} component cards to {CARD_DIR}")
