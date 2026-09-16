# Phase 1 consolidated proposed component register

Revision A — 2026-09-15. **GATE NOT CLOSED. No complete spacecraft baseline is admitted.**

52 records: 22 CANDIDATE / EVIDENCE INCOMPLETE; 25 CUSTOM/TO BE VERIFIED; 5 SUPPORTED.

**SUPPORTED** means the specific component has adequate primary data for its stated bounded use; it does not establish the integrated installation, launch suitability or 12-month survival. **CUSTOM/TO BE VERIFIED** means a genuine custom work package, not fabricated design evidence. **CANDIDATE / EVIDENCE INCOMPLETE** is an explicit failed closure exception: the requested two-state end condition has not been reached. Removing this third state would conceal missing evidence.

This register supersedes the 29-line operating proposal for the current review. It does not modify the controlled procurement BOM or authorize purchase. Alternative-only and included constituents are marked to avoid double counting. Unknown quantity, dimensions, mass, cost or current means unknown, never zero. No complete mass, power or cost total is defensible.

Canonical data: `component_register.json`. Source IDs E01–E50 resolve in `source_index.md`; S identifiers resolve in `review/Source_Register.md` and `review/sources.json`. Archived manufacturer files stay local pending redistribution permission.

| ID | Function | Exact proposed part | State |
|---|---|---|---|
| FLT-001 | Primary 1U structure, rails and enclosure | Storefront SKU 100000 | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-002 | Three independent separation/inhibit switches and RBF source isolation | Exact actuator and EPS option identifiers unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-003 | Solar conversion, battery charge control and switched power distribution | Type A; exact sales/options code unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-004 | Rechargeable eclipse/restart energy storage | Exact cell/pack configuration unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-005 | Body-mounted generation on +Y, -Y and -X faces | Three exact face drawings/order codes unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-006 | Body-mounted generation on -Z face with separation-switch clearances | Exact -Z relieved configuration unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-007 | Body-mounted generation on +Z face with antenna interface | Exact +Z AntS configuration unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-008 | Body-mounted generation on +X camera face | Exact aperture configuration unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-009 | Command/data handling, 128 MB image storage, RTC, watchdog and rate sensing | NanoMind A3200; exact delivered sales/revision code unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-010 | Mechanical carrier and bus routing for OBC/radio | Product 200232; OSF 1012964 configuration not completed | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-011 | UHF command, health telemetry and image downlink | Sales part 200315; Mode 5 | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-012 | Deployable UHF turnstile and release electronics | SAM-S, 5 V UHF configuration; exact tuned/order configuration unreleased | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-013 | Occasional recognizable Earth image capture | piCAM/FM | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-014 | Independent 5 V to controlled 3.3 V avionics rails, switching and latchup protection | D1-IF-001 | CUSTOM/TO BE VERIFIED |
| FLT-015 | Power/data/RBF/separation-switch harness and strain relief | D1-HAR-001 | CUSTOM/TO BE VERIFIED |
| FLT-016 | 50-ohm radio-to-antenna RF interconnect | D1-RF-001 | CUSTOM/TO BE VERIFIED |
| FLT-017 | Camera mount, aperture baffle and light/thermal isolation | D1-CAM-MNT-001 | CUSTOM/TO BE VERIFIED |
| FLT-018 | Battery/EPS thermal interface and electrical isolation | D1-THM-001 | CUSTOM/TO BE VERIFIED |
| FLT-019 | Mounting, locking, bonding and chassis-reference hardware | D1-MECH-HW-001 | CUSTOM/TO BE VERIFIED |
| GND-001 | Mode 5 UHF receive and command modem | Sales part 200315; Mode 5 | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-002 | Carrier/USB interface for ground modem | Product 200232; ground option set unknown | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-003 | Current-limited regulated power for ground modem/carrier | DP711 | SUPPORTED |
| GND-004 | Circularly polarized 430-438 MHz directional antenna | 436CP42UG | SUPPORTED |
| GND-005 | Azimuth/elevation pointing and computer control | G-5500DC, 110–120 V AC controller configuration | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-006 | Low-loss outdoor RF feedline and connectors | D1-GND-RF-001 | CUSTOM/TO BE VERIFIED |
| GND-007 | Receive filtering/LNA and transmit/receive routing | D1-GND-TR-001 | CUSTOM/TO BE VERIFIED |
| GND-008 | Mast, foundation, bonding, lightning and weather protection | D1-GND-SITE-001 | CUSTOM/TO BE VERIFIED |
| GND-009 | Station computer, storage, network/time and control interfaces | Raspberry Pi 400 US Personal Computer Kit, 4 GB | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-010 | Physical printing of reconstructed image | SELPHY CP1500 US kit with CA-CP300B adapter and PCPL-CP400 paper cassette | SUPPORTED |
| GND-011 | Protected modem DC conversion and supply leads | D1-GND-PWR-001 | CUSTOM/TO BE VERIFIED |
| GND-012 | Computer-to-rotator control, safe stop and feedback | D1-GND-CTRL-001 | CUSTOM/TO BE VERIFIED |
| GND-013 | Rotator field wiring and weatherproof strain relief | D1-GND-ROT-HAR-001 | CUSTOM/TO BE VERIFIED |
| GND-014 | Nonconductive antenna crossboom and conductor exclusion | D1-GND-BOOM-001 | CUSTOM/TO BE VERIFIED |
| GND-015 | Receive low-noise gain | ZX60-P103LN+ | SUPPORTED |
| GND-016 | RF surge suppression at bonded entry | IS-50NX-C0 | SUPPORTED |
| GND-017 | Ground receive band selection and rejection | D1-GND-FILT-001 | CUSTOM/TO BE VERIFIED |
| GND-018 | Station display | VA24EHF | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-019 | Removable image transfer and archival media | SDCIT2/32GB | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-020 | Host-to-removable-card interface | SDMSDRWU3AC | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-021 | Printer ink and physical photo paper | RP-108 | CANDIDATE / EVIDENCE INCOMPLETE |
| GND-022 | Ground RF/weather enclosure and DC distribution | D1-GND-ENC-001 | CUSTOM/TO BE VERIFIED |
| GND-023 | Mains distribution, protective earth and shutdown | D1-GND-AC-001 | CUSTOM/TO BE VERIFIED |
| GND-024 | Host data and network cabling | D1-GND-DATA-HAR-001 | CUSTOM/TO BE VERIFIED |
| GND-025 | RF switching hardware alternate under evaluation | RC-2SPDT-A18 | CANDIDATE / EVIDENCE INCOMPLETE |
| FLT-020 | Independent launch/handling hazard isolation | D1-SAFE-001 | CUSTOM/TO BE VERIFIED |
| FLT-021 | External cell/panel structural and electrical integration | D1-SOL-INTEG-001 | CUSTOM/TO BE VERIFIED |
| FLT-022 | Wire/hardware retention, insulation and contamination control | D1-MAT-001 | CUSTOM/TO BE VERIFIED |
| FLT-023 | Venting, service access and closeout identification | D1-CLOSEOUT-001 | CUSTOM/TO BE VERIFIED |
| SUP-001 | Ground handling, charging and programming access | D1-EGSE-001 | CUSTOM/TO BE VERIFIED |
| SUP-002 | Assembly support, transport and ESD protection | D1-HANDLING-001 | CUSTOM/TO BE VERIFIED |
| SUP-003 | Conducted RF commissioning hardware | D1-RF-TEST-001 | CUSTOM/TO BE VERIFIED |
| SUP-004 | Electrical/functional acceptance instrumentation and fixtures | D1-VERIFY-001 | CUSTOM/TO BE VERIFIED |

## FLT-001 — Primary 1U structure, rails and enclosure

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Storefront SKU 100000
- **Quantity:** 1
- **Description:** 1-Unit CubeSat Structure
- **Dimensions/mass:** About 100 x 100 x 113.5 mm project envelope; 150 g project allocation; manufacturer values UNKNOWN
- **Power:** Passive
- **Interfaces:** Current 1U order route and provisional EXOpod-compatible allocation
- **Cost/availability:** EUR 3,450 indicative storefront; 4-6 weeks stated; exact configuration not quoted
- **Order/reference route:** https://www.cubesatshop.com/product/1-unit-cubesat-structure/
- **Selection rationale:** Current 1U order route and provisional EXOpod-compatible allocation
- **Remaining uncertainty:** Manufacturer part/configuration, controlled drawing, mass, tolerances, finish, fasteners and qualification evidence incomplete
- **Blocked work:** Structure selection, mass properties, load path and deployer-fit release
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S06, S01, S33

## FLT-002 — Three independent separation/inhibit switches and RBF source isolation

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE + project integration
- **Part/configuration:** Exact actuator and EPS option identifiers unknown
- **Quantity:** 1 configured set
- **Description:** ICEPS2 three-switch/RBF option plus structure-mounted actuators
- **Included/alternative relationship:** FLT-020; unresolved COTS actuator constituent, not an additional assembly
- **Dimensions/mass:** Integrated configuration; actuator geometry and added mass UNKNOWN
- **Power:** Passive switch paths; hazard-source isolation topology UNKNOWN
- **Interfaces:** Required to prevent powered hazards before separation
- **Cost/availability:** Included/option cost UNKNOWN
- **Order/reference route:** https://www.isispace.nl/product/compact-electrical-power-system/
- **Selection rationale:** Required to prevent powered hazards before separation
- **Remaining uncertainty:** Exact actuator parts/travel, wiring truth table, independence, solar/test-source isolation and delivered option unavailable
- **Blocked work:** Launch safety and RF/antenna-release authorization
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S03, S01, S33

## FLT-003 — Solar conversion, battery charge control and switched power distribution

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Type A; exact sales/options code unknown
- **Quantity:** 1
- **Description:** ICEPS2 Type A
- **Dimensions/mass:** 96 x 92 x 26.45 mm; 184 +/-5 g including battery
- **Power:** MPPT inputs; VD0 plus four 5 V and four 3.3 V outputs; exact integrated transient envelope incomplete
- **Interfaces:** Provides MPPT, battery, protected switched outputs and housekeeping in one compact assembly
- **Cost/availability:** QUOTE REQUIRED; existing base planning allowance EUR 6,500 including battery
- **Order/reference route:** https://www.isispace.nl/product/compact-electrical-power-system/
- **Selection rationale:** Provides MPPT, battery, protected switched outputs and housekeeping in one compact assembly
- **Remaining uncertainty:** Current page states 22.5 Wh while linked datasheet states 28.8 Wh; exact configuration, integrated transients and commands incomplete
- **Blocked work:** Energy/life closure, rail compatibility and procurement release
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S02, S03

## FLT-004 — Rechargeable eclipse/restart energy storage

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Exact cell/pack configuration unknown
- **Quantity:** 1 integrated pack
- **Description:** ICEPS2 Type A integrated battery
- **Dimensions/mass:** Included in FLT-003 mass/envelope
- **Power:** 22.5 Wh current page versus 28.8 Wh datasheet conflict
- **Interfaces:** Integrated pack minimizes separate harness and volume
- **Cost/availability:** Included in FLT-003; exact pack configuration unknown
- **Order/reference route:** https://www.isispace.nl/product/compact-electrical-power-system/
- **Selection rationale:** Integrated pack minimizes separate harness and volume
- **Remaining uncertainty:** Cell identity, capacity conflict, lot, cycle/calendar life and installed thermal properties unavailable
- **Blocked work:** Twelve-month capacity, battery safety and component-specific thermal analysis
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S02, S03

## FLT-005 — Body-mounted generation on +Y, -Y and -X faces

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Three exact face drawings/order codes unknown
- **Quantity:** 3
- **Description:** Customizable 1U two-cell fixed panel
- **Dimensions/mass:** 50 g each family value; 1.2-2.0 mm typical thickness; exact planforms UNKNOWN
- **Power:** Approximately 1.23 W and 2.7 V per cell family values; not guaranteed for selected faces
- **Interfaces:** Two-cell 1U family matches body-mounted concept
- **Cost/availability:** QUOTE REQUIRED; existing base allowance EUR 1,800 each
- **Order/reference route:** https://www.isispace.nl/product/small-satellite-solar-panels/
- **Selection rationale:** Two-cell 1U family matches body-mounted concept
- **Remaining uncertainty:** Signed planforms, guaranteed hot/cold/EOL IV curves, tolerances, pinout and mounting missing
- **Blocked work:** Orbit/attitude energy closure and panel fit
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S04, S22

## FLT-006 — Body-mounted generation on -Z face with separation-switch clearances

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Exact -Z relieved configuration unknown
- **Quantity:** 1
- **Description:** Customizable 1U two-cell fixed panel
- **Dimensions/mass:** 50 g family value; exact planform/relief UNKNOWN
- **Power:** Approximate family cell values only; selected-face IV limits UNKNOWN
- **Interfaces:** Family can be customized around integration features
- **Cost/availability:** QUOTE REQUIRED; existing base allowance EUR 1,800
- **Order/reference route:** https://www.isispace.nl/product/small-satellite-solar-panels/
- **Selection rationale:** Family can be customized around integration features
- **Remaining uncertainty:** Relief drawing, mass, mounting, IV limits and harness data missing
- **Blocked work:** Power and switch/rail interference release
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S04

## FLT-007 — Body-mounted generation on +Z face with antenna interface

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Exact +Z AntS configuration unknown
- **Quantity:** 1
- **Description:** Customizable 1U two-cell fixed panel
- **Dimensions/mass:** 50 g family value; exact planform/interface UNKNOWN
- **Power:** Approximate family cell values only; selected-face IV limits UNKNOWN
- **Interfaces:** Family is marketed with customizable cutouts/interfaces
- **Cost/availability:** QUOTE REQUIRED; existing base allowance EUR 1,800
- **Order/reference route:** https://www.isispace.nl/product/small-satellite-solar-panels/
- **Selection rationale:** Generation on the antenna face remains a project requirement; the old configured panel is not assumed compatible with the replacement antenna.
- **Remaining uncertainty:** Existing AntS-specific panel concept no longer matches proposed SAM-S. Exact panel/antenna interface, mounting, mass and IV limits must be redesigned and documented.
- **Blocked work:** Power and antenna mounting/deployment release
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S04, S05

## FLT-008 — Body-mounted generation on +X camera face

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ISISPACE
- **Part/configuration:** Exact aperture configuration unknown
- **Quantity:** 1
- **Description:** Customizable 1U two-cell panel with camera aperture
- **Dimensions/mass:** 50 g project allocation from family; aperture geometry UNKNOWN
- **Power:** Project target >=1.8 W BOL; no configuration guarantee
- **Interfaces:** A customized aperture could retain generation around piCAM
- **Cost/availability:** QUOTE REQUIRED; existing base allowance EUR 2,300
- **Order/reference route:** https://www.isispace.nl/product/small-satellite-solar-panels/
- **Selection rationale:** A customized aperture could retain generation around piCAM
- **Remaining uncertainty:** Aperture/cell layout, guaranteed >=1.8 W BOL, IV limits, mass and mounting absent
- **Blocked work:** Imaging aperture feasibility and power closure
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S04, S49

## FLT-009 — Command/data handling, 128 MB image storage, RTC, watchdog and rate sensing

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** GomSpace
- **Part/configuration:** NanoMind A3200; exact delivered sales/revision code unknown
- **Quantity:** 1
- **Description:** NanoMind A3200
- **Dimensions/mass:** 65 x 40 x 7.1 mm; 24 g including shield
- **Power:** 3.2-3.4 V; datasheet current varies with clock/workload/peripherals
- **Interfaces:** Public datasheet provides processor, 128 MB NOR, FRAM, SDRAM, RTC, watchdog, CAN/I2C/UART and sensors
- **Cost/availability:** QUOTE REQUIRED; existing base planning allowance EUR 5,500
- **Order/reference route:** https://gomspace.com/product/nanomind-a3200/
- **Selection rationale:** Public datasheet provides processor, 128 MB NOR, FRAM, SDRAM, RTC, watchdog, CAN/I2C/UART and sensors
- **Remaining uncertainty:** Delivered revision, BSP/SDK terms, errata, guaranteed recovery behavior and application-specific radiation assurance incomplete
- **Blocked work:** Flight software release, fault containment and one-year reliability claim
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S07, S08

## FLT-010 — Mechanical carrier and bus routing for OBC/radio

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** GomSpace
- **Part/configuration:** Product 200232; OSF 1012964 configuration not completed
- **Quantity:** 1
- **Description:** NanoDock DMC-3
- **Dimensions/mass:** 91.9 x 88.7 x 8.6 mm; 51 g without daughterboards
- **Power:** Passive in flight; USB-to-UART circuit powered only from USB
- **Interfaces:** Exact current carrier has public mechanics, pinouts, option sheet and qualification certificate
- **Cost/availability:** QUOTE REQUIRED; existing base planning allowance EUR 1,500
- **Order/reference route:** https://gomspace.com/product/nanodock-dmc-3/
- **Selection rationale:** Exact current carrier has public mechanics, pinouts, option sheet and qualification certificate
- **Remaining uncertainty:** Stack connector, X/P connector population, supply matrix, AUX routing and CAN termination depend on unreleased D1-IF/harness pin map
- **Blocked work:** Carrier configuration and procurement release
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S44, S45, S46, S47

## FLT-011 — UHF command, health telemetry and image downlink

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** GomSpace
- **Part/configuration:** Sales part 200315; Mode 5
- **Quantity:** 1
- **Description:** NanoCom AX100-U
- **Dimensions/mass:** 65 x 40 x 6.5 mm; 24.5 g
- **Power:** 3.3 V; public RX/TX current tables; integrated rail transient compatibility open
- **Interfaces:** Current U-band flight radio with public RF/electrical/mechanical data and Mode 5 lifecycle notice
- **Cost/availability:** QUOTE REQUIRED; existing base planning allowance EUR 6,500
- **Order/reference route:** https://gomspace.com/product/nanocom-ax100/
- **Selection rationale:** Current U-band flight radio with public RF/electrical/mechanical data and Mode 5 lifecycle notice
- **Remaining uncertainty:** Current firmware/API, exact acceptance evidence, approved operating frequency and application-specific radiation basis incomplete
- **Blocked work:** Regulatory filing, software integration and one-year reliability claim
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S09, S10, S11

## FLT-012 — Deployable UHF turnstile and release electronics

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** Spacemanic
- **Part/configuration:** SAM-S, 5 V UHF configuration; exact tuned/order configuration unreleased
- **Quantity:** 1
- **Description:** Proposed replacement for ISISPACE AntS family
- **Dimensions/mass:** 98 x 98 x 6.2 mm bare; 10.1 mm including components; approximately 55 g
- **Power:** 5 V; 0.075 W average, 1.5 W deployment per reviewed revision
- **Interfaces:** I2C/RS485 CSP v1; Molex 53261-0971 with mating housing 51021-0900; MMCX 73415-1000 RF port, example mate 73415-0950
- **Cost/availability:** EUR 6,200 public page indication; not quoted as configured
- **Order/reference route:** https://spacemanic.com/products/sam-antenna/
- **Selection rationale:** Public SAM-S revision 4.2 supplies connector/pinout and mechanical detail missing from the earlier AntS family evidence. Better documented does not mean fully supported.
- **Remaining uncertainty:** Exact tuned frequency/order configuration, command dictionary, deployed swept geometry/pattern and application environmental evidence remain incomplete. Original PDF download failed; public web text reviewed. Not admitted.
- **Blocked work:** Antenna release/control, link and clearance closure
- **Verification/release path:** Acquire exact current document bytes, check tuned variant and full command definitions, derive deployment envelope from controlled drawing and verify inhibited/redundant release. Integration with panel and cable requires new drawings, not silent CAD edits.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E26, E37

## FLT-013 — Occasional recognizable Earth image capture

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** SkyFox Labs
- **Part/configuration:** piCAM/FM
- **Quantity:** 1
- **Description:** piCAM Flight Model
- **Dimensions/mass:** 33 x 33 x 19 mm body plus optics; 48 x 33 mm bracket; 40 g lens-dependent
- **Power:** 2.7-3.6 V; 95 mA datasheet operating value versus 90 mA page
- **Interfaces:** Exact current product has VGA JPEG output, UART protocol, pinout, mechanics, optics guidance and listed price
- **Cost/availability:** EUR 4,950 quantity one; 2-4 weeks plus shipping on current page
- **Order/reference route:** https://www.skyfoxlabs.com/product/27-picam
- **Selection rationale:** Exact current product has VGA JPEG output, UART protocol, pinout, mechanics, optics guidance and listed price
- **Remaining uncertainty:** 95 mA datasheet versus 90 mA page; exact lens/MTF/exposure acceptance, qualification report and one-year radiation application evidence incomplete
- **Blocked work:** Final image probability, power maximum and one-year survival claim
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S48, S49

## FLT-014 — Independent 5 V to controlled 3.3 V avionics rails, switching and latchup protection

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1 custom
- **Part/configuration:** D1-IF-001
- **Quantity:** 1
- **Description:** Power/interface board
- **Dimensions/mass:** Target allocation 45 g is not a released part property
- **Power:** Two 5 V-to-3.3 V rails plus separately switched/current-limited camera branch; limits unreleased
- **Interfaces:** Required because ICEPS2 direct 3.3 V maximum can exceed AX100 absolute maximum and piCAM recommends current limiting
- **Cost/availability:** Existing EUR 1,500 base allowance only; design/NRE/test cost UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** Required because ICEPS2 direct 3.3 V maximum can exceed AX100 absolute maximum and piCAM recommends current limiting
- **Remaining uncertainty:** No released schematic, IC/protection selection, BOM, layout, thermal/radiation/fault analysis or test specification
- **Blocked work:** Safe avionics power, fault containment, carrier option selection and harness release
- **Verification/release path:** Release schematic, regulator/protection IC BOM, layout and logic-level/backfeed analysis. Separate 5 V-derived regulated branches for OBC/radio and switched camera; prove voltage extrema below connected absolute maxima, current limit/retry behavior, thermal dissipation and single-fault containment with actual parts.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S03, S08, S10, S14, S49
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-015 — Power/data/RBF/separation-switch harness and strain relief

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1 custom
- **Part/configuration:** D1-HAR-001
- **Quantity:** 1 set
- **Description:** Flight wire harness
- **Dimensions/mass:** Geometry and mass UNKNOWN; prior combined harness/coax/switch allocation cannot be assigned to this exact assembly
- **Power:** Carries EPS power, CAN, I2C, UART, switches and service lines; losses UNKNOWN
- **Interfaces:** Connects all selected power, data, inhibit and service interfaces
- **Cost/availability:** Custom fabrication/NRE cost UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** Connects all selected power, data, inhibit and service interfaces
- **Remaining uncertainty:** Exact mating housings/contacts, wire types/gauges, lengths, shielding, pin map, derating and workmanship not released
- **Blocked work:** Voltage drop, EMC, inhibit independence, CAD routing and assembly
- **Verification/release path:** Partition power, CAN/I2C/UART, switch/RBF and service harness branches; list every mating housing/contact/backshell and wire specification, gauge, length and termination. Require pin-to-pin drawing, continuity/insulation/voltage-drop tests, pull/strain-relief inspection and routing/bend/access review.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S03, S08, S10, S45, S46, S49
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-016 — 50-ohm radio-to-antenna RF interconnect

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1 custom
- **Part/configuration:** D1-RF-001
- **Quantity:** 1
- **Description:** RF coax assembly
- **Dimensions/mass:** Length and mass UNKNOWN
- **Power:** 50 ohm; <=1 dB complete-assembly loss requirement
- **Interfaces:** AX100 uses MCX and the integrated loss allocation is <=1 dB
- **Cost/availability:** Custom fabrication/test cost UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** AX100 uses MCX and the integrated loss allocation is <=1 dB
- **Remaining uncertainty:** AX100 MCX to SAM-S MMCX endpoints now identified at interface-family level; exact cable, connector configurations, length, bend radius, retention and measured loss absent.
- **Blocked work:** RF interface, link margin and mechanical routing
- **Verification/release path:** AX100 MCX and proposed SAM-S MMCX endpoints are identified. Release exact 50-ohm cable, two connector part numbers and gender, length, bend/retention and workmanship; measure insertion/return loss at the authorized band against the existing <=1 dB assembly allocation.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E26, S10
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-017 — Camera mount, aperture baffle and light/thermal isolation

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1 custom
- **Part/configuration:** D1-CAM-MNT-001
- **Quantity:** 1
- **Description:** piCAM bracket/baffle assembly
- **Dimensions/mass:** Geometry and mass UNKNOWN; prior 20 g allocation is not a part property
- **Power:** Passive; installed thermal path and optical behavior UNKNOWN
- **Interfaces:** piCAM public drawing gives bracket envelope, four M2.5 holes and aperture-gap guidance
- **Cost/availability:** Custom fabrication/NRE/test cost UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** piCAM public drawing gives bracket envelope, four M2.5 holes and aperture-gap guidance
- **Remaining uncertainty:** Material, finish, geometry, tolerances, fasteners, loads, stray-light and thermal analyses not released
- **Blocked work:** Camera fit, optical clearance, structural margin and thermal interface
- **Verification/release path:** Design to piCAM/FM drawing and actual lens; release material/alloy/finish, M2.5 mating hardware, tolerances and baffle aperture. Verify retention, optical obstruction over field, fastener access, contamination and measured installed thermal path.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S49
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-018 — Battery/EPS thermal interface and electrical isolation

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1 custom
- **Part/configuration:** D1-THM-001
- **Quantity:** 1
- **Description:** Battery thermal-interface assembly
- **Dimensions/mass:** Geometry and mass UNKNOWN; prior 35 g allowance withdrawn as component evidence
- **Power:** Passive thermal/electrical interface; conductance UNKNOWN
- **Interfaces:** A defined measurable interface is required before component-specific thermal prediction
- **Cost/availability:** Material, fabrication and test cost UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** A defined measurable interface is required before component-specific thermal prediction
- **Remaining uncertainty:** Material part numbers, thickness/area, conductance, insulation, fasteners, surface preparation and test method absent
- **Blocked work:** Battery charging/survival thermal analysis
- **Verification/release path:** Determine actual battery permitted temperature/charge conditions first. Release exact insulating/thermal material, thickness/area, compression/fasteners and surface preparation. Measure installed conductance and isolation across temperature; no generic conductance/density substituted.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S02, S03, TMI-001
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-019 — Mounting, locking, bonding and chassis-reference hardware

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1 custom
- **Part/configuration:** D1-MECH-HW-001
- **Quantity:** 1 itemized set
- **Description:** Integration hardware set
- **Dimensions/mass:** Itemized geometry and mass UNKNOWN; prior 25 g allowance is not a part property
- **Power:** Passive; bond resistance requirement not released
- **Interfaces:** Required to retain boards, bond conductive structure and survive launch
- **Cost/availability:** Hardware/fabrication/test cost UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** Required to retain boards, bond conductive structure and survive launch
- **Remaining uncertainty:** Fastener/washer/insert/bonding-jumper/locking-material part numbers, torque, interfaces and acceptance inspection absent
- **Blocked work:** Load path, grounding, mass rollup and assembly release
- **Verification/release path:** Create joint-by-joint fastener/standoff/washer/insert and bond-jumper schedule including manufacturer or drawing, alloy, length, thread engagement, locking method, torque and procurement quantity. Analyze joint loads and verify preload retention, bond continuity and access.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S01, S33
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-001 — Mode 5 UHF receive and command modem

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** GomSpace
- **Part/configuration:** Sales part 200315; Mode 5
- **Quantity:** 1
- **Description:** NanoCom AX100-U used as ground modem
- **Dimensions/mass:** 65 x 40 x 6.5 mm; 24.5 g before carrier/enclosure
- **Power:** 3.3 V; TX/RX values per AX100 datasheet; ground configuration open
- **Interfaces:** Matching modem avoids an assumed third-party Mode 5 implementation
- **Cost/availability:** QUOTE REQUIRED; separate from flight-radio cost
- **Order/reference route:** https://gomspace.com/product/nanocom-ax100/
- **Selection rationale:** Matching modem avoids an assumed third-party Mode 5 implementation
- **Remaining uncertainty:** Ground firmware/API/license, host interface and authorized frequency/configuration not established
- **Blocked work:** End-to-end waveform and command compatibility
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S09, S10, S11

## GND-002 — Carrier/USB interface for ground modem

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** GomSpace
- **Part/configuration:** Product 200232; ground option set unknown
- **Quantity:** 1
- **Description:** NanoDock DMC-3
- **Dimensions/mass:** 91.9 x 88.7 x 8.6 mm; 51 g before modem/enclosure
- **Power:** Passive carrier; USB circuit uses 5 V USB; modem supply routing open
- **Interfaces:** DMC-3 exposes USB-to-UART console and carries AX100
- **Cost/availability:** QUOTE REQUIRED; separate from flight-carrier cost
- **Order/reference route:** https://gomspace.com/product/nanodock-dmc-3/
- **Selection rationale:** DMC-3 exposes USB-to-UART console and carries AX100
- **Remaining uncertainty:** Exact ground configuration, power entry, connector population and required host control path not released
- **Blocked work:** Ground modem electrical/host integration
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** S44, S45, S46

## GND-003 — Current-limited regulated power for ground modem/carrier

- **State:** SUPPORTED
- **Manufacturer/design authority:** RIGOL
- **Part/configuration:** DP711
- **Quantity:** 1
- **Description:** DP700-series programmable bench supply, US mains configuration
- **Dimensions/mass:** 140 x 202 x 332 mm; 6.9 kg
- **Power:** 0–30 V, 0–5 A DC output; 150 W rated output. Selectable 100/120/220/240 V AC, 50–60 Hz; maximum input 400 VA.
- **Interfaces:** Front output terminals; RS-232. Use at 5 V upstream of GND-011, never as a direct AX100 3.3 V protection device.
- **Cost/availability:** Current manufacturer product route; price not established
- **Order/reference route:** https://www.rigol.com/europe/products/dc-power-supply/DP700.html
- **Selection rationale:** Replaces unnamed supply with an exact documented model; separate regulation avoids reliance on slow/coarse bench OVP.
- **Remaining uncertainty:** US line setting/fuse must be inspected. Leads are a separate custom assembly. System protection belongs to GND-011.
- **Blocked work:** No independent site or modem integration verification yet
- **Verification/release path:** Manufacturer ratings establish the supply component, not the protected modem installation. Check line selector/fuse, polarity, calibration and load behavior before connection.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E13, E14, E40

## GND-004 — Circularly polarized 430-438 MHz directional antenna

- **State:** SUPPORTED
- **Manufacturer/design authority:** M2 Antenna Systems
- **Part/configuration:** 436CP42UG
- **Quantity:** 1
- **Description:** 436CP42UG
- **Dimensions/mass:** Boom 18 ft 10 in; maximum element 13.25 in; antenna 7.5 lb (shipping 10 lb); mast interface 1.5–2 in
- **Power:** Passive 50-ohm antenna, 430–438 MHz; manufacturer catalog gain 18.9 dBic; not installed link evidence
- **Interfaces:** N-female feed. Manufacturer phasing lines and assembly hardware included; nonconductive mast/crossboom and clearance mandatory.
- **Cost/availability:** USD 910.95 storefront price on 2026-09-15
- **Order/reference route:** https://www.m2inc.com/
- **Selection rationale:** Exact existing antenna has a full assembly manual and parts list. No gain or mission performance upgraded.
- **Remaining uncertainty:** Authorized frequency, installed feed loss/pattern, site loads and tracking remain unverified integration properties.
- **Blocked work:** Installed link and site acceptance
- **Verification/release path:** Assemble to E27; inspect phasing/handedness; measure return loss and installed feed loss; verify site loads and pointing independently.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E27

## GND-005 — Azimuth/elevation pointing and computer control

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** Yaesu
- **Part/configuration:** G-5500DC, 110–120 V AC controller configuration
- **Quantity:** 1 system
- **Description:** Azimuth/elevation rotators and manual controller kit
- **Dimensions/mass:** Rotators 8 kg; controller 3 kg. Mast diameter 38–63 mm; boom 32–43 mm; installation drawings in E32.
- **Power:** 110–120 V AC selected regional controller; motors 22 V DC. Maximum continuous rotation 3 minutes; input current not established here.
- **Interfaces:** Two field control cables needed; supplied 7-pin connectors and 8-pin DIN interface. Computer interface is GND-012, not included.
- **Cost/availability:** UNKNOWN
- **Order/reference route:** https://www.yaesu.com/product-detail.aspx?CatName=Rotators&Model=G-5500DC
- **Selection rationale:** Replaces unnamed rotator with a documented kit. Component support is conditional on published mechanical/duty limits; the selected antenna installation is not yet demonstrated.
- **Remaining uncertainty:** Site loads, current/protection sizing and tracking duty remain installation acceptance items. Accuracy specification is ±4 percent, not ±4 degrees.
- **Blocked work:** Automatic tracking and installed load acceptance
- **Verification/release path:** Use E32 wiring and drawings; measure input demand for site protection; prove commanded limits, feedback calibration, duty and safe stop before mounting antenna.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E32

## GND-006 — Low-loss outdoor RF feedline and connectors

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** Site-specific custom
- **Part/configuration:** D1-GND-RF-001
- **Quantity:** 1 installed run
- **Description:** Ground RF feedline assembly
- **Dimensions/mass:** Site length and mass UNKNOWN
- **Power:** 50 ohm; installed receive-feed loss requirement <=1 dB
- **Interfaces:** Budget permits <=1 dB receive feed loss
- **Cost/availability:** UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** Budget permits <=1 dB receive feed loss
- **Remaining uncertainty:** Cable/connector/lightning-protection types, run length, bend radius, weather sealing and measured loss absent
- **Blocked work:** Final link margin and installation release
- **Verification/release path:** Separate static feedline, motion-rated flex loop, patch leads, adapters and weather seals. LMR-400 is only a static-run candidate; do not assume continuous-flex suitability. Freeze site lengths and endpoints, release exact cable/connector BOM, test installed loss/return loss, weather seals and full rotator travel.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S28, engineering/05
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-007 — Receive filtering/LNA and transmit/receive routing

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-TR-001
- **Quantity:** 1 chain
- **Description:** Custom interlocked ground receive/transmit chain
- **Dimensions/mass:** UNKNOWN
- **Power:** Gain/noise/P1dB/filter rejection/T-R limits UNKNOWN
- **Interfaces:** AX100 RF port → fail-safe routing → filter/feedline/antenna; receive branch has documented LNA. Switching must precede and inhibit transmitter operation.
- **Cost/availability:** UNKNOWN
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** A genuine site-specific interlocked assembly is required; an LNA alone cannot provide two-way operation.
- **Remaining uncertainty:** Schematic, exact switching/filter constituents, control logic and protection release absent; RC-2SPDT-A18 is a researched candidate, not approved.
- **Blocked work:** Receiver sensitivity, transmitter protection and lawful emissions
- **Verification/release path:** Create RF/control schematic and loss/noise/power budget, prove no transmit path into LNA under reset/power loss/single-control fault; measure isolation, sequencing, insertion loss and conducted emissions.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E31, E42, E43, S10
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-008 — Mast, foundation, bonding, lightning and weather protection

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** Site-specific custom
- **Part/configuration:** D1-GND-SITE-001
- **Quantity:** 1 site
- **Description:** Ground antenna support/protection installation
- **Dimensions/mass:** Site dependent
- **Power:** Passive except rotator/lightning auxiliaries
- **Interfaces:** Required for safe permanent operation of the selected antenna
- **Cost/availability:** UNKNOWN; separate ground-station/site cost
- **Order/reference route:** NOT APPLICABLE — custom item or no compliant part selected
- **Selection rationale:** Required for safe permanent operation of the selected antenna
- **Remaining uncertainty:** Site, wind/ice/lightning criteria, structural design, grounding parts and permits unknown
- **Blocked work:** Ground-station safety, reliability and cost
- **Verification/release path:** Specify site, wind/ice/soil requirements, mast/foundation, nonconductive crossboom, anchors, bonds, entry surge protection and weather housing. Release drawings and exact hardware; independent structural/electrical review and installation inspection before use.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S28, engineering/05
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-009 — Station computer, storage, network/time and control interfaces

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** Raspberry Pi
- **Part/configuration:** Raspberry Pi 400 US Personal Computer Kit, 4 GB
- **Quantity:** 1
- **Description:** Ground host, integrated keyboard; kit PSU/mouse/micro-HDMI cable and supplied card
- **Dimensions/mass:** 286 x 122 x 23 mm; manufacturer mass absent from reviewed brief
- **Power:** USB-C 5 V; kit regional PSU included; exact PSU SKU and host maximum input/current not closed by reviewed brief
- **Interfaces:** USB 3.0 x2, USB 2.0 x1, Gigabit Ethernet, micro-HDMI. Raspberry Pi OS; actual modem/control software must be ported and demonstrated.
- **Cost/availability:** Manufacturer brief lists US kit USD 80 excluding tax; current delivered price/stock not guaranteed
- **Order/reference route:** https://www.raspberrypi.com/products/raspberry-pi-400/specifications/
- **Selection rationale:** Exact inexpensive free-software host proposal replaces unnamed PC; no claim that vendor modem software runs on it.
- **Remaining uncertainty:** Mass, PSU exact identity/rating, deterministic recovery, storage endurance and modem software support incomplete.
- **Blocked work:** Ground software, power and configuration release
- **Verification/release path:** Not procurement released. See linked earlier property matrix and custom work packages.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E20, E41

## GND-010 — Physical printing of reconstructed image

- **State:** SUPPORTED
- **Manufacturer/design authority:** Canon
- **Part/configuration:** SELPHY CP1500 US kit with CA-CP300B adapter and PCPL-CP400 paper cassette
- **Quantity:** 1
- **Description:** Print reconstructed image from SD card; exact retail color/SKU not material to electrical function
- **Dimensions/mass:** 182.2 x 57.6 x 133 mm; approximately 850 g printer body. Paper travel clearance must follow manual.
- **Power:** Maximum printing 60 W; standby 4 W or less. Included adapter input 100–240 V AC 50/60 Hz; output 24 V DC, 1.8 A.
- **Interfaces:** SD/SDHC/SDXC card printing of supported JPEG/Exif images; USB-C is data, not charging. No Linux USB driver compatibility assumed.
- **Cost/availability:** Current US manufacturer order page; final delivered price not captured
- **Order/reference route:** https://www.usa.canon.com/shop/p/selphy-cp1500
- **Selection rationale:** Direct SD printing avoids dependence on an unverified Linux print driver; exact manufacturer documentation covers the intended use.
- **Remaining uncertainty:** Confirm regional kit contents at ordering; integrated image-format/read/print demonstration remains outstanding. Adapter rating and printer maximum are separate published statements.
- **Blocked work:** End-to-end printed mission artifact not demonstrated
- **Verification/release path:** Test a reconstructed image and retain original bytes plus documented print derivative. Use included power supply and compatible paper/ink.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E17, E18, E39, E48, E49

## GND-011 — Protected modem DC conversion and supply leads

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-PWR-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom 5 V input to regulated/protected avionics rail enclosure
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** DP711 output terminals to DMC-3 selected inputs; separate logic/USB power paths
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release regulator/eFuse/fuse exact ICs, schematic, wire/terminal BOM, enclosure, limits and test points. Prove all tolerance/load/transient/startup/fault states stay within AX100 voltage limits; demonstrate no USB backfeed. Bench OVP is not an adequate replacement.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release regulator/eFuse/fuse exact ICs, schematic, wire/terminal BOM, enclosure, limits and test points. Prove all tolerance/load/transient/startup/fault states stay within AX100 voltage limits; demonstrate no USB backfeed. Bench OVP is not an adequate replacement.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E13, E14, S10, S45
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-012 — Computer-to-rotator control, safe stop and feedback

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-CTRL-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom controller/interface assembly
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** G-5500DC 8-pin DIN signals to isolated host interface
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release controller schematic, ADC/driver/isolator part numbers, connector pin map and enclosure. Demonstrate limits, watchdog, disconnected feedback, stalled motion, calibration and power-loss stop; verify manual override. GS-232B researched as COTS alternate but English documentation/configuration incomplete.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release controller schematic, ADC/driver/isolator part numbers, connector pin map and enclosure. Demonstrate limits, watchdog, disconnected feedback, stalled motion, calibration and power-loss stop; verify manual override. GS-232B researched as COTS alternate but English documentation/configuration incomplete.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E32, E16
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-013 — Rotator field wiring and weatherproof strain relief

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-ROT-HAR-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Two field cables with supplied rotator connector kits
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Six conductors per azimuth/elevation circuit per E32; length/site dependent
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release exact cable gauge/jacket, cores, shields if needed, terminal assignments, gland and support parts; calculate voltage drop from motor data and actual length, verify continuity/insulation/motion without snagging.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release exact cable gauge/jacket, cores, shields if needed, terminal assignments, gland and support parts; calculate voltage drop from motor data and actual length, verify continuity/insulation/motion without snagging.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E32
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-014 — Nonconductive antenna crossboom and conductor exclusion

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-BOOM-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom glass-fiber or other justified nonconductive boom and clamps
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** M2 mast 1.5–2 in; Yaesu boom 32–43 mm: compatible clamp geometry must be designed, not assumed
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Specify exact stock material and supplier, section, length and clamp hardware; no carbon-fiber substitution assumed nonconductive. Verify bending/torsion/fatigue/weathering, swept envelope and conductor exclusion. E27 requires at least 12 in element-tip clearance; rear coax loop approximately 60 in, reattach beyond clearance.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Specify exact stock material and supplier, section, length and clamp hardware; no carbon-fiber substitution assumed nonconductive. Verify bending/torsion/fatigue/weathering, swept envelope and conductor exclusion. E27 requires at least 12 in element-tip clearance; rear coax loop approximately 60 in, reattach beyond clearance.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E27, E32
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-015 — Receive low-noise gain

- **State:** SUPPORTED
- **Manufacturer/design authority:** Mini-Circuits
- **Part/configuration:** ZX60-P103LN+
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Documented coaxial LNA; constituent of GND-007
- **Included/alternative relationship:** GND-007
- **Dimensions/mass:** 23 g; body approximately 18.80 x 19.1 x 11.68 mm; connector envelope per E31 drawing
- **Power:** 5 V DC; 95 mA typical, 120 mA maximum; maximum no-damage RF input 21 dBm in 50–2000 MHz range
- **Interfaces:** SMA female 50 ohm RF ports; DC connector per manufacturer outline
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** https://www.minicircuits.com/pdfs/ZX60-P103LN%2B.pdf
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** No system sensitivity established; preserve case temperature and input limits. Transmit must never enter this branch. Verify actual frequency gain/noise and installed bias filtering.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** No system sensitivity established; preserve case temperature and input limits. Transmit must never enter this branch. Verify actual frequency gain/noise and installed bias filtering.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E31

## GND-016 — RF surge suppression at bonded entry

- **State:** SUPPORTED
- **Manufacturer/design authority:** PolyPhaser
- **Part/configuration:** IS-50NX-C0
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** DC-blocking coax surge protector
- **Included/alternative relationship:** GND-008
- **Dimensions/mass:** 62.23 x 44.45 x 38.1 mm; 158.76 g
- **Power:** Passive; 125 W rating for 220–700 MHz; DC blocked
- **Interfaces:** 50 ohm N-female both ends; 1.5–700 MHz
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** https://www.polyphaser.com/
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Verify installed bonding/entry enclosure and local code; no outdoor IP rating established. Not proof of lightning-safe installation.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Verify installed bonding/entry enclosure and local code; no outdoor IP rating established. Not proof of lightning-safe installation.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E28

## GND-017 — Ground receive band selection and rejection

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-FILT-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom filter assembly, frequency-dependent design
- **Included/alternative relationship:** GND-007
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** 50 ohm RF chain; connector gender and location in GND-007 to be released
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Specify licensed frequency and occupied bandwidth first; derive loss/rejection/power requirements from chosen waveform and local interferers. Release topology, exact resonator/LC parts, tuning instructions and enclosure; measure S parameters and power behavior. Not a fictional filter part.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Specify licensed frequency and occupied bandwidth first; derive loss/rejection/power requirements from chosen waveform and local interferers. Release topology, exact resonator/LC parts, tuning instructions and enclosure; measure S parameters and power behavior. Not a fictional filter part.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S10, E31
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-018 — Station display

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** ASUS
- **Part/configuration:** VA24EHF
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Candidate 23.8-inch monitor with stand
- **Dimensions/mass:** 539.5 x 417.2 x 205.9 mm with stand; 2.84 kg
- **Power:** 100–240 V AC 50/60 Hz; listed 12.02 W consumption; maximum demand not verified
- **Interfaces:** HDMI 1.4 from Pi kit micro-HDMI cable
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** https://www.asus.com/id/displays-desktops/monitors/eye-care/va24ehf/techspec/
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Regional power cord/configuration and operating environment not fully captured; confirm before admission.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Regional power cord/configuration and operating environment not fully captured; confirm before admission.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E44

## GND-019 — Removable image transfer and archival media

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** Kingston
- **Part/configuration:** SDCIT2/32GB
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Two Kingston industrial microSD cards with SD adapters proposed: transfer and backup
- **Dimensions/mass:** Card 11 x 15 x 1 mm; adapter 24 x 32 x 2.1 mm; mass unknown
- **Power:** 3.3 V; maximum current not provided in reviewed source
- **Interfaces:** 3.3 V microSD/SDHC FAT32; SD adapter for Canon
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** https://www.kingston.com/en/memory-cards/industrial-grade-microsd-uhs-i-u3
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Mass and maximum operating current absent from reviewed datasheet. Confirm host/card/format compatibility and verify full written capacity; preserve checksums and backup independently. Supplied Pi boot card belongs to host kit, not this pair.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Mass and maximum operating current absent from reviewed datasheet. Confirm host/card/format compatibility and verify full written capacity; preserve checksums and backup independently. Supplied Pi boot card belongs to host kit, not this pair.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E45, E49

## GND-020 — Host-to-removable-card interface

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** StarTech.com
- **Part/configuration:** SDMSDRWU3AC
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** USB-A/USB-C SD and microSD reader
- **Dimensions/mass:** 73 x 20 x 11 mm; 14 g
- **Power:** 5 V USB bus powered; consumption unknown
- **Interfaces:** USB bus power; SD/microSD UHS-I
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** https://www.startech.com/en-fr/hdd/sdmsdrwu3ac
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Actual maximum current not established by reviewed page; host bus and media interoperability require verification.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Actual maximum current not established by reviewed page; host bus and media interoperability require verification.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E30

## GND-021 — Printer ink and physical photo paper

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** Canon
- **Part/configuration:** RP-108
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Compatible Canon ink/paper pack, 108 postcard-size sheets/prints
- **Dimensions/mass:** Postcard-format media; pack mass/envelope not established
- **Power:** Passive consumables
- **Interfaces:** CP1500 with supplied PCPL-CP400 cassette
- **Cost/availability:** USD 39.99 observed indicative retail; tax/shipping excluded
- **Order/reference route:** https://www.usa.canon.com/
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Manufacturer compatibility is established; pack mass and retail envelope not captured. Consumable dimensions other than print format are not mission-critical; do not infer cartridge substitution.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Manufacturer compatibility is established; pack mass and retail envelope not captured. Consumable dimensions other than print format are not mission-critical; do not infer cartridge substitution.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E48

## GND-022 — Ground RF/weather enclosure and DC distribution

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-ENC-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom protected modem/LNA/router enclosure set
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** GND-001/002/007/011, coax entries and site bond
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release exact enclosure, glands, seals, brackets, fused DC branches and thermal ventilation design; verify ingress, condensation, accessible service, touch safety and temperature. Mains must not be improvised inside an unapproved enclosure.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release exact enclosure, glands, seals, brackets, fused DC branches and thermal ventilation design; verify ingress, condensation, accessible service, touch safety and temperature. Mains must not be improvised inside an unapproved enclosure.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E28, E31, S45
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-023 — Mains distribution, protective earth and shutdown

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-AC-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom site installation using appropriately listed commercial electrical hardware
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** DP711, rotator, host PSU, display and printer supplied adapters
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Define site jurisdiction/service, outlet type, breaker/RCD or GFCI as applicable, exact listed parts and cable ratings; load and fault/earthing review before energizing. No homemade mains PSU. Professional electrical work is external expertise and separately costed.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Define site jurisdiction/service, outlet type, breaker/RCD or GFCI as applicable, exact listed parts and cable ratings; load and fault/earthing review before energizing. No homemade mains PSU. Professional electrical work is external expertise and separately costed.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E14, E17, E32
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-024 — Host data and network cabling

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-GND-DATA-HAR-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom length/configuration cable kit
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** USB host to DMC-3 and controller; Ethernet to existing network; display uses Pi kit cable
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release actual port/gender map, manufacturer cable SKUs, lengths, shielding and retention. Verify data recovery after disconnect/power cycle. Existing internet/router infrastructure is a required declared dependency, not included hardware.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release actual port/gender map, manufacturer cable SKUs, lengths, shielding and retention. Verify data recovery after disconnect/power cycle. Existing internet/router infrastructure is a required declared dependency, not included hardware.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S45, E20
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## GND-025 — RF switching hardware alternate under evaluation

- **State:** CANDIDATE / EVIDENCE INCOMPLETE
- **Manufacturer/design authority:** Mini-Circuits
- **Part/configuration:** RC-2SPDT-A18
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Candidate dual absorptive RF switch, not yet selected constituent
- **Included/alternative relationship:** GND-007 alternative; not additional purchase
- **Dimensions/mass:** 4.5 x 6 x 2.25 in nominal body; 960/980 g conflict
- **Power:** 24 V; up to 500 mA in stated switched condition; included mains adapter
- **Interfaces:** SMA female; USB-B/Ethernet control; included AC/DC-24-3W1 supply
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** https://www.minicircuits.com/pdfs/RC-2SPDT-A18.pdf
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Datasheet says 960 g while drawing says 980 g; reconcile revision. Prove safe default, interlock and ratings before selection. Internal termination only 1 W; transmitter must be inhibited during switching.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Datasheet says 960 g while drawing says 980 g; reconcile revision. Prove safe default, interlock and ratings before selection. Internal termination only 1 W; transmitter must be inhibited during switching.
- **Design maturity:** Manufacturer product proposal; not bought or tested
- **Evidence:** E42, E43

## FLT-020 — Independent launch/handling hazard isolation

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-SAFE-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom safety integration, replacing reliance on an undefined EPS switch option
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Battery, all solar sources, EGSE, separation actuators, RBF, RF and antenna release paths
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release fault tree, inhibit truth table and independently inspectable schematic. Choose exact switches with manufacturer travel/contact/environment evidence; Honeywell SE/XE researched but not admitted. Demonstrate no alternate feed path and correct reset/recovery. No architecture credit merely for three switches.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release fault tree, inhibit truth table and independently inspectable schematic. Choose exact switches with manufacturer travel/contact/environment evidence; Honeywell SE/XE researched but not admitted. Demonstrate no alternate feed path and correct reset/recovery. No architecture credit merely for three switches.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S01, S03, S33, E12
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-021 — External cell/panel structural and electrical integration

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-SOL-INTEG-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom face-by-face integration and harness requirements for FLT-005 through FLT-008
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Cell circuits to MPPT; deployer rails, camera field and antenna/switch clearance
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release six face drawings and exact panel variants; derive hot/cold Voc/current limits and require data for actual cells/coverglass/interconnects. Include diode/potting/retention parts if design requires them; no generic cell curves. Test continuity, insulation, IV response and mounting.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release six face drawings and exact panel variants; derive hot/cold Voc/current limits and require data for actual cells/coverglass/interconnects. Include diode/potting/retention parts if design requires them; no generic cell curves. Test continuity, insulation, IV response and mounting.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S04, S22, E04
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-022 — Wire/hardware retention, insulation and contamination control

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-MAT-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom controlled materials and application schedule
- **Included/alternative relationship:** Constituents assigned to FLT-015/017/018/019/021, not duplicate mass
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Harness, optics, panel, chassis and thermal-interface materials
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Itemize manufacturer/product/lot for every tape, adhesive, coating and sleeve; specify cure, thickness, preparation and keep-outs. Retain outgassing/compatibility and process evidence, inspect coupons. 3M5413 sheet reports TML1.50%, CVCM0.50%; do not describe generic Kapton tape as space-qualified. Stycast resin needs its exact catalyst/process.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Itemize manufacturer/product/lot for every tape, adhesive, coating and sleeve; specify cure, thickness, preparation and keep-outs. Retain outgassing/compatibility and process evidence, inspect coupons. 3M5413 sheet reports TML1.50%, CVCM0.50%; do not describe generic Kapton tape as space-qualified. Stycast resin needs its exact catalyst/process.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** E47, E50
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## FLT-023 — Venting, service access and closeout identification

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-CLOSEOUT-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom closure/vent/access/label parts schedule
- **Included/alternative relationship:** Structure/integration constituent set, not an independent mass allocation
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Structure pressure equalization, camera cover removal, RBF access and connector service
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Define vent paths and obstruction controls, captive access covers if needed, label material and witness marks; prove no loose items or obstructed optics/antenna/rails. Establish ascent pressure requirement before vent verification. No new hole geometry claimed.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Define vent paths and obstruction controls, captive access covers if needed, label material and witness marks; prove no loose items or obstructed optics/antenna/rails. Establish ascent pressure requirement before vent verification. No new hole geometry claimed.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S01, S33, S49
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## SUP-001 — Ground handling, charging and programming access

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-EGSE-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom spacecraft electrical ground-support interface and keyed test harness
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Selected EPS service/charge port, OBC programming, safe power and telemetry
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Release selected pinouts, isolation/fusing and keyed mating connectors. Use approved cell/pack charging behavior only; prevent launch inhibit defeat by EGSE. Verify polarity, no backfeed, safe reset and service disconnect. Include exact programmer hardware after OBC revision frozen.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Release selected pinouts, isolation/fusing and keyed mating connectors. Use approved cell/pack charging behavior only; prevent launch inhibit defeat by EGSE. Verify polarity, no backfeed, safe reset and service disconnect. Include exact programmer hardware after OBC revision frozen.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S03, S08, E25
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## SUP-002 — Assembly support, transport and ESD protection

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-HANDLING-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom handling tray, restraints, covers and ESD workstation kit
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** 1U frame, exposed panels/optics and service ports
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Specify actual cradle/cover drawings, conductive/insulating materials, ESD mat/strap/tester SKUs and storage/shipping protections. Test restraint and clearance without loading cells or release hardware; define battery shipping requirements before shipment.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Specify actual cradle/cover drawings, conductive/insulating materials, ESD mat/strap/tester SKUs and storage/shipping protections. Test restraint and clearance without loading cells or release hardware; define battery shipping requirements before shipment.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S01, S33, S49
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## SUP-003 — Conducted RF commissioning hardware

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-RF-TEST-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom attenuator/load/cable test kit and calibration plan
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** AX100 transmit/receive ports and ground RF chain
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Select exact 50-ohm loads, DC blocks, attenuators, adapters and power ratings once frequency/power are frozen; calibrate complete chain, prove receiver input protection and transmitter load. Equipment rental/calibration is testing cost, not AI expense.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Select exact 50-ohm loads, DC blocks, attenuators, adapters and power ratings once frequency/power are frozen; calibrate complete chain, prove receiver input protection and transmitter load. Equipment rental/calibration is testing cost, not AI expense.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S10, E31
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required

## SUP-004 — Electrical/functional acceptance instrumentation and fixtures

- **State:** CUSTOM/TO BE VERIFIED
- **Manufacturer/design authority:** DEGENERATE-1
- **Part/configuration:** D1-VERIFY-001
- **Quantity:** 1 assembly/set unless explicitly noted
- **Description:** Custom verification fixture and instrument schedule
- **Dimensions/mass:** Design not released; dimensions and mass unknown
- **Power:** To be established from connected loads
- **Interfaces:** Supply rails, harnesses, deployment, image capture and reconstruction
- **Cost/availability:** Not quoted; no purchase made
- **Order/reference route:** Custom fabrication; no order release
- **Selection rationale:** Necessary to implement the existing Earth-image mission or safely connect, assemble and operate its hardware
- **Remaining uncertainty:** Specify measurement uncertainty/range for DMM, scope/probes, electronic load, continuity/insulation tests and deployment capture. Select identifiable instruments before use; record calibration and exact fixture BOM. No invented test results; this is an unbuilt verification work package.
- **Blocked work:** Integrated build/operation release until the stated verification is complete
- **Verification/release path:** Specify measurement uncertainty/range for DMM, scope/probes, electronic load, continuity/insulation tests and deployment capture. Select identifiable instruments before use; record calibration and exact fixture BOM. No invented test results; this is an unbuilt verification work package.
- **Design maturity:** Requirements/work-package definition only; detailed design and constituent BOM not released
- **Evidence:** S03, S08, S10, S49
- **Required release artifacts:** Controlled drawing or schematic and interface pin map; Exact constituent BOM and material/process specifications; Analysis with source-backed properties and tolerances; Acceptance procedure with numerical criteria derived from connected equipment; As-built inspection and test record; independent review where required
