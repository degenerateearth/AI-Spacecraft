# DEGEN-1
## 1U CubeSat preliminary engineering design — Revision A

Issued 14 September 2026. Status: **AUDITABLE PRELIMINARY DESIGN / NOT RELEASED FOR FABRICATION OR FLIGHT**.

The design targets one year of opportunistic imaging and housekeeping telemetry in LEO at low build cost using commercially marketed CubeSat subsystems. The owner selected occasional recognizable Earth images, US operation and nominal 450–500 km LEO, with no arbitrary spacecraft budget ceiling. A CrystalSpace CS-101 camera supports opportunistic imaging without precision pointing. Selected-location imaging or mapping would require a revised baseline.

The baseline uses an ISISPACE 1U chassis, six fixed solar panels, ICEPS2 Type A battery/EPS, AntS UHF antenna, and GomSpace A3200/AX100-U avionics on a DMC-3 carrier. One small custom adapter is required to resolve supply-voltage tolerance and inter-vendor routing. No propulsion, reaction wheels, GNSS receiver or deployable solar arrays are included.

The [component audit](Components/README.md) covers every existing B01–B16 BOM line with cost, order route, size, mass, power, interfaces, configuration and procurement blockers. It adds no new spacecraft hardware.

**Planning results:** 1.064 kg current best estimate, 1.276 kg including 20% growth; EUR46,500 base flight-hardware allowance (EUR29,350–70,100 range). These are engineering estimates, not supplier quotations. Spacecraft build, including engineering/prototype hardware, assembly and nonrecurring engineering labor, is EUR152,500 base before contingency. Testing, ground station, licensing, launch and operations are separate categories. The cost report explains inclusions and uncertainty.

The reproducible model closes nominal energy at +18.4% with a tumble-average assumption, and a separate fixed-attitude recovery mode closes at +0.124 Wh/orbit. The nominal mode does **not** close in the fixed-attitude case. Thermal, orbit-lifetime, radiation, inhibit independence and final mechanical/interface compliance remain open. No analysis in this package demonstrates that the assembled spacecraft has survived launch or will actually operate for twelve months.

### Audit reading order

1. [Mission and architecture](engineering/01_Mission_and_Architecture.md)
2. [System budgets and analysis rationale](engineering/02_Budgets_and_Analyses.md)
3. [Interfaces and adapter specification](engineering/03_Interfaces.md)
4. [Mechanical and environmental design](engineering/04_Mechanical_Thermal_Radiation.md)
5. [Flight software and mission operations](engineering/05_Software_and_Operations.md)
6. [Assembly, integration and verification](engineering/06_Integration_and_Verification.md)
7. [Cost and procurement trade](procurement/Cost_and_Procurement.md)
8. [Open issues and review gates](review/Open_Issues.md)
9. [Imaging payload](engineering/07_Imaging_Payload.md) and [US compliance plan](engineering/08_US_Compliance.md)
10. [Requirements traceability](review/Requirements.md), [FMEA](review/FMEA.md), [sources](review/Source_Register.md)

### Reproduction and configuration

Run `python analysis/recalculate.py` using Python 3 (standard library only). Edit `analysis/inputs.json` for assumptions and `procurement/BOM.csv` for estimates. Outputs are `results.json`, `power_sensitivity.csv` and `thermal_screen.csv`. Assertions check model consistency and selected preliminary budget limits; they do not verify flight hardware. The HTML audit book is a generated, readable snapshot of the Markdown documents. The individual Markdown documents and model inputs are authoritative within this package.

The original SVG is an allocation sketch. [CAD-001 FreeCAD model](drawings/freecad/README.md) now provides editable parametric component envelopes and a STEP review export, with explicit assumptions and fit conflicts. It is not manufacturing CAD or supplier geometry. The electrical diagrams specify functional interfaces, not a released pin-to-pin harness. PCB fabrication files, vendor proprietary ICDs, supplier quotes, hardware test reports and flight software implementation remain incomplete.

All external facts carry source IDs resolved in the source register. **V** denotes vendor-stated information; **A** denotes an engineering assumption/allocation; **C** denotes a calculation; **OPEN** denotes missing evidence. Published product changes supersede older brochures. Engineering approval signatures remain blank; AI authorship is not an engineering release.

## Project purpose — added after Revision A

Read the [Project Overview](Project_Overview.md) for the AI-assisted engineering experiment and the owner's [Project Constitution v0.1](Project_Constitution.md) for its principles and success levels. The Revision A audit book remains the earlier technical snapshot; these documents do not imply a new engineering or flight-readiness release.
## Consumer-AI experiment constraint

The baseline engineering interface is a standard $20/month ChatGPT Plus subscription, including Codex/Astra where available, with free/open-source engineering tools wherever practical. Paid AI or software is not introduced silently. See [AI toolchain and boundaries](review/AI_Toolchain_and_Boundaries.md), [project status](review/Project_Status.yaml), and the separate [project cost ledger](procurement/Project_Cost_Ledger.csv).

Project gates and their required evidence are tracked in [MILESTONES.md](MILESTONES.md). GitHub updates are made at those review points.

Before planning major engineering work, consult the [Master CubeSat Readiness Checklist](review/Master_CubeSat_Readiness_Checklist.md). It audits this repository against an independent University of Hawaiʻi CubeSat development framework plus primary launch, NASA and US regulatory sources. The 2026-09-15 audit places the project at Constitution Level 0 with partial evidence toward Level 1; it records 108 applicable activities, including 30 blocked and 28 not started.

Archived external-framework provenance and licensing are recorded in [SOURCES/README.md](SOURCES/README.md).
