# D1-TRD-ARCH-001 — Open-bus architecture trade

Revision A · 2026-09-16  
Evidence state: **DOCUMENTED TRADE STUDY; no hardware tested**

## Decision question

Which publicly documented architecture provides the most credible path to a
complete, auditable, education-grade 1U Earth-imaging design without depending
on private vendor interfaces?

The comparison is about the public design record. Flight heritage of a related
revision is supporting evidence, not proof that a Degen-1 derivative will work.

## Mandatory criteria

1. A 1U implementation must be physically possible.
2. Hardware must be represented by exact COTS parts or released custom designs.
3. Schematics, PCB source or a declared custom-layout task, mechanical interfaces,
   firmware and test information must be publicly reviewable.
4. The design must support command, health telemetry, image capture, storage and
   image downlink without a hidden command protocol.
5. Known radiation, power, safety or integration failures must remain visible.
6. The editable toolchain must be free/open where reasonably practical.

## Results

| Candidate | Public strengths | Controlling defects | Disposition |
|---|---|---|---|
| Existing ISISPACE/GomSpace/SkyFox mix | Current identifiable products; compact flight-oriented packaging | Several command definitions, option codes, pinouts and cross-vendor configuration details are not public; 22 evidence-incomplete selections remain in the Phase 1 register | Rejected as the design-development baseline; retained as a commercial comparison |
| BIRDS-4/BIRDS-5 1U bus | Repeated 1U educational missions; English platform ICD; structure CAD; board schematics and BOMs; firmware; antenna, battery and environmental procedures; documented energy figures; direct Earth-imaging precedent | Core OBC/EPS PCB layouts are not public; some 2018 BOM entries are obsolete or ambiguous; the exact current radio configuration and procurement route require reconciliation | **Selected reference architecture for a Degen-1 custom derivative** |
| PyCubed v05 | Complete KiCad source, fabrication data, STEP, firmware and integrated OBC/EPS/radio | The project warns of serious proton sensitivity in the ATSAMD51 used by v00–v05; example command handling includes static tokens and unrestricted evaluation/execution; solar-input topology conflicts with ordinary two-cell 1U body panels | Rejected unchanged; retained as an implementation reference |
| OreSat0 / OreSat current repositories | Coherent open card-cage architecture; 1U flight article; open C3, backplane, battery and solar designs; strong fabrication notes and test culture | Flown C3 v5 had both receiver defects; current C3 v6 is a post-flight redesign with no public board power characterization found; flown battery v3.0 is an older Eagle design while current KiCad layout is explicitly in progress | Strong reference, not a single reproducible current baseline |
| VST104-Sierra | Complete KiCad OBC, exact BOM alternatives, broad protected interfaces and STM32L496 firmware scaffold | No mission flight software; needs both 3.3 V and 5 V; no matched EPS/radio in the VST104 set; no flight or radiation-test record found | Retained as OBC fallback/reference |
| OpenLST rev 2.1 | Complete KiCad, Gerbers, exact BOM, firmware, ground tools and extensive related Planet LST flight heritage | Reference PA RFFM6403 is discontinued; STA1120A evidence/order route is incomplete; board connector selections are unfinished; a current derivative requires RF redesign and test | Retained as radio fallback/reference |
| UPSat open bus | Flown fully open satellite with EPS, OBC, communications, camera software, structures and verification history | The integrated spacecraft is 2U; 2016 parts/tooling need obsolescence review; a 1U repack would be a new mechanical and thermal design | Retained as subsystem and verification reference |

## Selected architecture direction

Degen-1 will use a **BIRDS-derived 1U mechanical and electrical architecture with
project-released custom avionics boards**. The selection is architectural, not an
authorization to copy an unavailable board layout or to treat old BOM entries as
current.

The reasons are:

- BIRDS demonstrates that the chosen stack style, passive-stability concept,
  body-mounted solar generation, low-data-rate UHF link and small camera payload
  can coexist in 1U;
- the public platform ICD, circuit schematics, firmware and verification records
  expose more of the complete spacecraft than the commercial mixed-vendor design;
- Degen-1 can recreate the missing layouts in KiCad and record every substitution,
  instead of relying on private command dictionaries; and
- the architecture already separates platform, communication, antenna, payload
  and backplane functions in a form that can be audited by students and engineers.

## Frozen functional partition

| Degen-1 item | Baseline direction | Present evidence state |
|---|---|---|
| Structure and rails | Custom D1-STR-001 derived from public BIRDS 1U drawings and checked against the provisional EXOpod Nova envelope | Selected direction; Degen-1 production drawings not released |
| Backplane and harness | Custom D1-BPB-001 using the BIRDS 50-pin stack interface as the starting pin map | Selected direction; pin-level Degen-1 ICD not released |
| OBC and nonvolatile storage | Custom D1-OBC-001 derived from the BIRDS-4 PIC/flash architecture and firmware; every obsolete/ambiguous part must be replaced before schematic release | Selected direction; layout and current BOM not released |
| Power, inhibits and distribution | Custom D1-EPS-001 derived from the BIRDS FAB/EPS safety architecture, with three independent deployment inhibits, RBF isolation, battery protection and separately switched payload/radio rails | Selected direction; schematic and current BOM not released |
| Battery | Custom D1-BAT-001 using six exact Panasonic `BK120AAHU` NiMH cells in a 3S2P topology | Exact cell and topology selected; pack drawing, analysis and verification remain open |
| Solar panels | Custom D1-SOL-001 body panels based on the BIRDS/OreSat public panel evidence; exact cell and panel circuit remain to be released | Open detailed design |
| TT&C and image downlink | Custom D1-COM-001 carrier using exact Ebyte `E22-400M22S` / Semtech SX1268 module; public Degen-1 waveform and packet protocol | Exact module selected; carrier, waveform and link closure open |
| Antenna/deployment | Custom D1-ANT-001 derived from the documented BIRDS tape-antenna mechanism and launch-inhibit logic | Selected direction; drawings and release circuit not released |
| Camera | SkyFox Labs `piCAM/FM`, default approximately 60-degree optics, IR-cut and infinity focus | Exact payload selected; carrier, delivered connector suffix and protection release open |
| Passive attitude behavior | Permanent magnet plus hysteresis material only if exact sizing and image-probability analysis close; no active pointing is added | Open detailed design |
| Flight software | Degen-1 fork/reimplementation of the BIRDS state-machine and command concepts with authenticated command parsing, bounded buffers and no dynamic evaluation | Custom work package |
| Ground segment | SDR/packet modem, directional antenna, rotator and image reconstruction matched to the released space link | Custom integration plus exact COTS items |

## Design boundary exposed by the trade

No reviewed open design simultaneously provides a current exact BOM, complete
1U fabrication package, demonstrated 12-month radiation tolerance, camera mission,
and fully documented ground link. Degen-1 must perform real electrical, RF,
mechanical and software design work. Reusing public source reduces the amount of
new work; it does not transfer qualification or flight status.

The consumer-AI/free-toolchain experiment can credibly continue through source
reconciliation, KiCad/FreeCAD design, deterministic analysis and prototype test
planning. RF layout review, battery safety review, launch structural review,
environmental qualification and regulatory approval remain expected external or
physical-verification boundaries.

## Primary public records used

- BIRDS platform documentation: https://github.com/BIRDSOpenSource/BIRDS-GeneralDocumentation
- BIRDS-4 OBC: https://github.com/BIRDSOpenSource/BIRDS4-OBC
- BIRDS-4 communications: https://github.com/BIRDSOpenSource/BIRDS4-COM
- BIRDS-4 FAB/EPS: https://github.com/BIRDSOpenSource/BIRDS4-FAB
- BIRDS-4 CAD and procedures: https://github.com/BIRDSOpenSource/BIRDS4-CAD and https://github.com/BIRDSOpenSource/BIRDS4-ProceduresAndReports
- BIRDS-5 published parts/designs/CAD/source: https://github.com/BIRDSOpenSource
- BIRDS-RPM communication record: https://birds-rp.birds-project.com/communication/
- PyCubed hardware/software: https://github.com/pycubed and the August 2024 processor notice in its official documentation
- OreSat hardware: https://github.com/oresat/oresat-c3-hardware, https://github.com/oresat/oresat-batteries, https://github.com/oresat/oresat-solar-hardware, and https://github.com/oresat/oresat-backplane
- VST104-Sierra: https://github.com/visionspacetec/VST104-Sierra
- OpenLST: https://github.com/OpenLST/openlst and https://www.planet.com/open/openlst-hw.git
- UPSat: https://gitlab.com/librespacefoundation/upsat

Exact upstream commit identifiers used for this audit are recorded in
`review/Open_Source_Upstream_Register.md`.
