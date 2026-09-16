# Build-and-operate completeness audit

2026-09-15. Question: **“If someone were given only this register and its referenced evidence, what physical component, interface, mounting item, harness, ground item, or supporting hardware would still be missing if they attempted to build and operate Degen-1?”**

**Answer: a builder still could not build the spacecraft from this package.** The register covers the identified functions, but several COTS configurations and all custom detailed designs remain unreleased. A list of work packages is not a fabrication package. The requested two-state closure has not been achieved, and the project remains at Level 0.

## Pass 1: omissions found and added to the proposal

| Omission in the 29-line proposal | Added coverage | What this fixes / what remains |
|---|---|---|
| Named protected ground power source and leads | GND-003, GND-011 | Exact supply plus downstream custom protection; regulator/component schematic still required. |
| Automatic rotator interface, field wiring and safe stop | GND-005, GND-012/013 | Exact rotator candidate and custom interface/cables; controller design and current evidence incomplete. |
| Nonconductive antenna support and conductor exclusion | GND-014, GND-008 | Requirements now explicitly follow the M2 manual; stock section, clamps and site analysis not released. |
| LNA damage prevention during uplink | GND-007, GND-015/017/025 | Exact LNA plus real interlock/filter work; switching circuit unbuilt and switch candidate incomplete. |
| Surge protection, weather housing and mains distribution | GND-016/022/023, GND-008 | Exact surge part and site work packages; site-specific electrical/structural release required. |
| Display, transfer media/reader and ink/paper | GND-018 through GND-021 | Named models replace implicit peripherals; remaining data gaps retained. |
| Ground USB/network/control cable kit | GND-024 | All host endpoints must appear in a released cable schedule, not assumed supplied. |
| Independent source isolation implementation | FLT-020 and FLT-002 constituent | Explicit safety assembly, including solar/EGSE paths; no unsupported actuator admitted. |
| Face-specific panel wiring and retention | FLT-021 | Six faces covered with custom drawings required, including changed antenna face. |
| Adhesives, insulation, ties, locking/bonding consumables | FLT-022 and FLT-019 | Material/process schedule is required; no generic tape/potting properties. |
| Vent paths, removable covers, access and labels | FLT-023 | Closeout drawing checklist exists; no invented vent geometry. |
| Charging/programming and handling equipment | SUP-001/002 | Explicit EGSE/cradle/ESD work packages, not unlisted bench accessories. |
| RF loads/attenuators and electrical verification fixtures | SUP-003/004 | Supporting hardware captured; exact instrument selection belongs to testing preparation. |

## Pass 2: functional coverage and remaining release blockers

| Mission/build function | Register coverage | Residual missing evidence or artifact |
|---|---|---|
| Survive launch, retain parts, fit deployer | FLT-001/019/022/023 | Exact structure drawing, loads/materials, joint schedule, tolerances, vent requirements and test basis. Public EXOpod is only a provisional mechanical reference. |
| Safe shipping, assembly, charging and separation | FLT-002/020; SUP-001/002 | Actual battery/charger data, independent inhibit circuit and exact actuator selections; shipping/launch acceptance later. |
| Generate, store and distribute energy | FLT-003 through FLT-008, FLT-014/015/021 | Exact cell/panel/pack configurations, temperature/EOL properties, regulator BOM and rail extrema. No closed energy balance claimed. |
| Thermal survival and battery charge permission | FLT-003/004/018/022 | Installed thermal paths and verified sensing/charge interlocks. Heater/controller/sensor parts must be added to the thermal assembly if actual part limits require them; no inherited hypothetical heater is assumed physical hardware. |
| Boot, recover, command and keep time | FLT-009/010/014; SUP-001 | Actual delivered OBC/carrier configuration, SDK/commands, watchdog recovery and reset/power sequencing. |
| Store image and housekeeping | FLT-009 | Public OBC storage is the proposed flight storage; no unlisted SD card required. Capacity/endurance/radiation suitability and software integrity remain unverified. |
| Observe motion/housekeeping | FLT-009, EPS/panel embedded sensors | Use only documented integrated sensors. No standalone ADCS sensors silently added. Exact sensor readouts and usable thermal telemetry require configuration review. |
| Capture recognizable Earth image | FLT-013/017, FLT-008 | Lens acceptance, unobstructed aperture, exposure/image behavior and body-face geometry. Opportunistic imaging does not establish acquisition probability. |
| Deploy and communicate | FLT-011/012/016/020 | Exact RF tuning/commands, deployed envelope, release paths and waveform/software configuration. No antenna deployment or link demonstration exists. |
| Receive image and send commands | GND-001 through GND-017, GND-022/025 | Fully specified ground modem power/software and RF-chain interlock, filter and cabling. |
| Track pass and protect site | GND-005/008/012/013/014/023 | Site dimensions/weather, rotator duty/loads, control and mains/bonding design. |
| Reconstruct, archive and print | GND-009/010/018/019/020/021/024 | Ground software build, actual modem API, data integrity, media compatibility and a dry-run print. Original image must be preserved; a print derivative must be identified. |
| Assemble, commission and verify | SUP-001 through SUP-004 | Released fixtures, exact constituent hardware/instruments, calibration and acceptance criteria. No test equipment has been purchased or used. |

## Duplicate and hidden-item checks

- Integrated ICEPS2 battery is not a second pack purchase or a second mass allocation. FLT-004 specifies a nested unresolved constituent.
- DMC-3 carrier excludes its OBC/radio daughterboard masses. Flight and ground each need a separately configured carrier; one cannot be counted twice as shared hardware.
- The M2 assembly kit includes its phasing lines and specified hardware. Site feedline, nonconductive support and weather protection are additional. Yaesu kit includes connector shells and specified clamps/bolts; field cable and computer controller are additional.
- Pi kit PSU, mouse, keyboard, supplied boot card and display cable are nested kit constituents; monitor, transfer/backup media and actual host/modem cables are additional. Regional kit configuration remains an evidence gap.
- Printer PSU/cassette are included in the selected kit; RP-108 consumables are not. No printer battery is required for the mains-operated mission workflow.
- Custom harness release must enumerate every mating housing **and contact**, wire, shield termination, strain relief, tie/anchor and label. A connector family name is not a complete order list.
- Custom hardware release must enumerate each screw, washer, spacer, insert, locking/bonding material and torque/inspection instruction by joint. No generic fastener-lot mass is accepted.
- Spare flight units are not an assumed functional requirement. Qualification articles, destructive-test specimens and spares will need explicit quantities and separate testing costs before a test campaign.
- Internet/time/orbit-element supply and a legal site are external operational dependencies. A router or internet service is not silently represented by a computer Ethernet port. If the chosen site lacks them, add exact hardware/service records before site release.
- Launch deployer/adapters and provider-specific handling fixtures are known downstream items. They cannot be selected from an unspecified booking. No procurement or qualification release may pass without reconciliation.
- No propulsion, reaction wheel, magnetorquer, GNSS receiver or precision pointing system was added; the mission remains opportunistic imaging. If an analysis later proves an added function necessary, it must be an explicit architecture change.

## Audit result and continuation boundary

The omission check has been repaired at the **register/work-package level**, not at the as-built level. Every identified function has a register owner; not every owner has a buildable design. The 22 incomplete COTS/variant records remain explicit exceptions to the requested end condition. Further public document retrieval, command/software review, exact circuit/material selection and custom design can still make progress. This review does **not** establish that public information or consumer AI has reached an absolute limit.

Specific obstacles requiring additional evidence include current vendor revision/configuration, mission-relevant thermal/battery/radiation data, ground component maximum ratings and exact software interfaces. Missing mission-specific private ICDs/quotes remain downstream dependencies; missing publicly knowable interface details remain current research work. No paid service or vendor contact was used to bypass either category.
