# D1-LCH-001 — Launch and deployer planning baseline

Revision A | 15 September 2026 | Public-information trade only

## Gate result

DEGENERATE-1 adopts a **standard 1U slot in the EXOLAUNCH EXOpod Nova as its provisional mechanical integration reference**. The selected configuration deliberately stays inside the ordinary CubeSat Design Specification envelope rather than using Nova's expanded protrusion or mass capability. This preserves broader rail-deployer compatibility.

This decision is a planning reference. It is not a launch selection, reservation, quote, contract, manifest, mission-specific interface control document (ICD), safety acceptance, flight approval, or orbit assignment. LCH-001 remains **IN PROGRESS** and LCH-002 remains **BLOCKED**.

No current public source establishes a purchasable 1U launch to exactly 450–500 km. SpaceX's direct rideshare page sells plate capacity beginning at 50 kg, not individual 1U deployer slots [S34]. A 1U project therefore needs a launch integrator that aggregates CubeSats and supplies the dispenser, mission coordination, and mission-specific requirements.

## Mission constraints used for the trade

- One 1U rail-interface spacecraft; current estimated mass is 1.0635 kg and 1.2762 kg with 20% growth.
- Occasional recognizable Earth imagery and health telemetry for 365.25 days after separation.
- US private operation; licensing path and legal operator remain open.
- Nominal planning altitude 450–500 km, with another common rideshare orbit allowed only when it materially reduces total cost or complexity and passes one-year residence and post-mission disposal analyses.
- No propulsion, pressure vessel, explosive device, deployable solar array, or precision-pointing system.
- No launch, quote request, vendor contact, or paid service was authorized or performed in this gate.

## Candidate comparison

The machine-readable comparison is [Launch_Deployer_Trade.csv](../review/Launch_Deployer_Trade.csv).

### LD-01 — EXOLAUNCH EXOpod Nova through a commercial rideshare integrator

The June 2024 EXOpod Nova User Manual Rev. 1.2 explicitly supports 1U payloads, states backwards compatibility with fully CDS-compliant CubeSats, and provides usable dimensions, mass, center-of-gravity guidance, rail finish, deployment dynamics, and fit-check expectations [S33]. EXOLAUNCH advertises launch mission management and deployment services and has flown EXOpod on multiple launch vehicles. Mission, orbit, schedule, customer safety requirements, price, and controlled integration documents require direct coordination.

**Disposition:** selected provisional mechanical reference. It offers the best current public dimensional definition of the surveyed commercial options. A future quote or mission ICD may replace it through configuration control.

### LD-02 — ISISPACE/ISILaunch with ISIPOD or a subdivided QuadPack

ISISPACE currently offers end-to-end launch, integration, and deployer services and publicly supports 1U through 16U payloads [S36]. Its public deployer brochure lists a dedicated 1U ISIPOD, 1.75 kg maximum payload mass, up to 9 mm side volume, and a quote-based service path [S37]. The current spacecraft mass with project growth is below that published mass. The selected B01 structure is from the same supplier and an older structure brochure states compatibility with common rail deployers, but this does not establish acceptance of the integrated spacecraft.

**Disposition:** commercial alternate and useful compatibility check. No current controlled customer ICD, 1U price, available mission, or orbit was found publicly.

### LD-03 — Voyager/Nanoracks NRCSD deployment from the ISS

NASA's current Small Spacecraft Systems State of the Art identifies NRCSD support for 1U and describes deployment from the ISS into approximately 400–420 km at 51.6 degrees [S40]. The public NRCSD IDD provides a detailed 1U interface and safety process, including 2.40 kg maximum mass, 113.50 ±0.10 mm rail length, three physical deployment switches linked to independent inhibits, RBF/ABF access, 30-minute hazardous-function delay, and ISS battery review [S38].

**Disposition:** lower-orbit fallback, not the reference. The published altitude is outside the preferred range and may not retain this ballistic 1U for 365.25 days across deployment date, area, attitude, and solar-activity cases. The crewed-spacecraft battery and safety process also adds evidence and schedule burden. An orbit lifetime analysis and current service confirmation would be mandatory before reconsideration.

## Reference interface values

These values come from EXOpod Nova User Manual Rev. 1.2, Tables 1–2 and §§2.3–2.5, unless marked otherwise [S33]. They are preliminary design inputs and do not supersede a mission ICD.

| Parameter | Public reference value | Current project state | Finding |
|---|---:|---|---|
| Rail span X and Y | 100.0 ±0.1 mm | CAD reference 100 × 100 mm | Nominally aligned; tolerances not modeled or measured |
| 1U rail length Z | 113.5 ±0.5 mm | CAD reference 113.5 mm | Nominally aligned; end geometry and coplanarity unknown |
| Maximum space between rails | 87.2 mm in X and Y | 8 mm square rail proxies leave 84 mm | Bounding proxy is inside the published gap; actual rail profile is unknown |
| Maximum lateral protrusion from rails | 25.0 mm | Side-panel outer faces end at nominal ±50 mm | No nominal envelope excess; panel/rail zero-clearance conflicts remain |
| Maximum 1U mass | 2.5 kg | 1.2762 kg with project growth | Preliminary margin 1.2238 kg; actual manifest value still controls |
| Recommended 1U COG offset | ±20 mm in X, Y, and Z | Project target ±10 mm; CAD COG not credible | Project target is more restrictive, but compliance is unproved |
| Rail material/finish | CDS aluminum choices; Type III hard anodize; Ra ≤1.6 µm | B01 vendor structure selected; certificates absent | Supplier configuration and certificates required |
| Fit verification | Virtual fit check, assembled rail measurement, preferably physical Nova/TestPod fit check | Envelope CAD only | T01/AIV-006 remain blocked |
| Expected tip-off | Below 10 deg/s each axis; ±7.5-degree separation half-cone | No deployment dynamics model | Mission-specific analysis/ICD required |

## Existing design audit

The current envelope CAD stays within the published 100 × 100 × 113.5 mm rail-span/length values and the current mass budget is below the EXOpod Nova 1U public maximum. Those are **MODELED/CALCULATED screens**, not compatibility evidence.

The audit does not establish fit because:

- all four CAD rails are assumed 8 × 8 mm rectangular prisms without the supplier section, radii, finish, tolerances, fasteners, or switch cutouts;
- side-panel and rail envelopes meet at zero clearance and existing CAD-C01–C05 overlaps remain unresolved;
- the assembled rail span, length, end coplanarity, roughness, and finish have not been measured;
- 295 g of allocated hardware is not located in CAD, so center of mass and inertia are not credible;
- RBF access, deployment-switch travel and force, camera aperture, connector access, cable bends, and antenna deployment sweep remain unknown;
- the public Nova manual does not provide the mission-specific customer requirements for electrical inhibits, RF silence, battery acceptance, materials, test levels, delivery, or safety data.

## Documented design conflicts and proposed corrections

| Record | Documented design | External constraint | CAD/design conflict | Proposed correction for review |
|---|---|---|---|---|
| LDC-01 | Nominal rail envelope is exactly 100 × 100 × 113.5 mm | Nova controls rail span to 100.0 ±0.1 mm and length to 113.5 ±0.5 mm | CAD has no manufacturing tolerance or measured rail datum | Replace rail proxies with controlled B01 geometry and a tolerance stack; do not shrink or machine flight hardware without supplier/integrator approval |
| LDC-02 | Side panels occupy 84 mm between assumed 8 mm rails | Nova permits 87.2 mm maximum space between rails, but actual clamping contacts and rail geometry control | Panels and assumed rails have zero clearance/intersection boundaries | Obtain B01 and configured panel CAD; add clearance and clamping keep-outs; resolve CAD-C01–C05 before bracket/panel release |
| LDC-03 | ICEPS2 option allocates three separation switches plus RBF | Public Nova manual does not define spacecraft electrical safety architecture; NASA LSP/NRCSD references require three independent RF inhibits, while NRCSD also ties them to three physical switches | Switch topology, travel, force, source isolation, and access are not demonstrated | Obtain the mission-specific ICD and ICEPS2 schematic; perform fault-tree and all-state test before treating the option as compliant |
| LDC-04 | AntS and camera are allocated near external faces | Deployer fit requires no wall contact and integrator-approved deployment behavior | Stowed details, lens clearance, antenna sweep, and premature-release behavior are not modeled | Add controlled stowed/deployed geometry and sweep keep-outs after supplier data; verify in a representative TestPod |
| LDC-05 | Project uses a ±10 mm COG target | Nova recommends ±20 mm for 1U | CAD assigns component envelopes but omits/unlocates mass and cannot calculate credible COG | Preserve the tighter project target; locate every mass and later measure the integrated unit |
| LDC-06 | Planning orbit is 475 km, 51.6 degrees | Public commercial offerings do not commit to that orbit; NRCSD is published at 400–420 km | Power, contact, radiation, thermal, and lifetime work currently uses an unmanifested orbit | Keep 475 km as an analysis case only; obtain candidate injection states before changing the baseline |

No proposed correction has been applied to the spacecraft architecture or CAD geometry in this revision.

## Cost and schedule evidence

SpaceX publicly lists USD 350,000 for a 50 kg SSO rideshare plate and USD 7,000 per additional kilogram [S34]. That is host-launch pricing for a plate, not a 1U deployment-service quote. It does not validate the project's EUR 40,000–120,000 launch/integration allowance.

EXOLAUNCH, ISISPACE, and the ISS deployment route require a mission-specific quote. Public pages expose inquiry routes but do not disclose a complete 1U price, included testing, regulatory support, insurance, schedule, rebooking terms, or delivery orbit. The existing cost range remains an **ASSUMPTION** and no currency conversion is introduced.

The public information also does not establish an available slot or delivery date. SpaceX's rideshare page describes online plate ordering and rebooking terms, while the aggregators select or contract capacity across missions. An actual schedule begins only with a written offer that identifies launch, deployer, integration milestones, delivery date, and slip/reflight terms.

## Regulatory and safety implications

The reference does not change the US licensing plan. A US operator still needs the applicable FCC spacecraft/earth-station authority, NOAA remote-sensing determination or license, debris evidence, and launch-provider payload data. The launch operator generally leads FAA launch authorization and payload review, but DEGENERATE-1 must supply accurate permits, hazards, materials, orbit, and ownership information.

The public NASA LSP program-level requirements are retained as a conservative cross-check, not imposed as an EXOLAUNCH requirement [S39]. They reinforce powered-off delivery through deployment, 45-minute RF silence, three independent RF inhibits, venting, materials control, and mission-specific verification. The eventual signed ICD controls.

## Evidence status and exit criteria

This gate adds DOCUMENTED source research, a CALCULATED mass comparison, and a MODELED envelope screen. It adds no TESTED, EXPERT-REVIEWED, APPROVED, MANIFESTED, or FLIGHT evidence and does not increase the Constitution success level.

The planning gate is complete when this trade, source record, CAD screen, open-issue disposition, and readiness update are configuration controlled. The actual LCH-001/LCH-002 flight gates close only after all of the following exist:

1. written offer or contract naming the launch, integrator, deployer, target orbit/injection tolerances, schedule, price, and responsibilities;
2. controlled mission-specific CubeSat-to-deployer and launch requirements;
3. clause-by-clause compliance matrix accepted by the integrator;
4. updated orbit lifetime, debris, power, thermal, radiation, contact, structure, and operations analyses;
5. accepted regulatory and safety plan; and
6. physical dimensional measurement and representative dispenser fit/ejection evidence.

## Recommended next approval

Authorize **non-binding integrator inquiries** to EXOLAUNCH and ISISPACE using the same one-page mission data sheet, requesting budgetary 1U pricing, candidate missions/orbits, current customer ICDs, included testing and regulatory support, schedule, and payment/rebooking terms. Do not purchase or reserve a slot at that stage.
