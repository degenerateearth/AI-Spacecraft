# Configuration log

Rev A — 2026-09-14. Initial issued package for Degen-1. Owner scope: occasional recognizable Earth images, US-operated, nominal 450–500 km LEO, flexible rideshare if it lowers cost/complexity, lowest reasonable COTS build cost, distinct program cost categories and no arbitrary financial ceiling.

Working calculations were revised before this release to add the CS-101 camera, aperture-panel derating, updated stack allocations, Mode 5 radio framing and independent regulator interface. Only the issued imaging configuration is included in the deliverable package. No hardware has been acquired, modified or tested.

The package is a preliminary engineering design with formal open items. Subsequent revisions must log changed assumptions, affected requirements, budgets, vendor revisions and verification evidence. A hash manifest identifies this issue's exact files.
Rev B — 2026-09-14. Updated the constitution and supporting documentation to make the consumer-AI/free-software constraint explicit. Added the eight-category cost ledger, status schema, and AI toolchain boundary procedure. No spacecraft mission, design, or success-level claim was silently changed.

CAD-001 — 2026-09-14. Translated Revision A allocations into a FreeCAD 1.1.3
parametric envelope model. Retained documented Z locations and expanded EPS/AntS
from old sketch placeholders to published envelope dimensions. Assumptions and
23 bounding-envelope overlaps recorded; real material interference is not proven.
Added native/STEP exports, generation script, source traceability, mass ledger,
software verification and O19–O22. No flight hardware, FEA, thermal simulation,
expert review, design release or higher success level results from this work.

PA-001 — 2026-09-15. Audited exactly the existing B01–B16 BOM lines. Added one
component card per line, a sortable master audit, source/order-route check and a
reproducible generator that fails if BOM IDs, quantities or cost allowances drift.
Recorded current vendor facts separately from project requirements, assumptions
and unknowns. B01's public €3,450 listing exceeds its €3,000 base allowance; the
controlled BOM was not rebased. B08 availability remains unconfirmed. No new
component, purchase, supplier contact, test or procurement release resulted.

ERA-001 — 2026-09-15. Selected the University of Hawaiʻi *A Guide to CubeSat
Mission and Bus Design*, Edition 1, as an external development framework and
supplemented it with primary CubeSat, NASA, FCC, NOAA, FAA and future launch-ICD
sources. Audited the full repository against 108 applicable readiness items:
3 complete, 21 provisionally addressed, 26 in progress, 28 not started and 30
blocked. Added O23–O29. Corrected project status from Level 1 to Level 0 with
partial evidence toward Level 1 because internal design closure, hardware,
testing, regulatory approval and expert review do not exist. No architecture or
mission change resulted.

LDG-001 — 2026-09-15. Compared three public 1U launch/deployer paths and
selected a standard EXOpod Nova 1U slot as provisional mechanical reference.
Retained ISISPACE/ISILaunch as the commercial alternate and Voyager/NRCSD as a
lower-orbit fallback. Moved LCH-001 from BLOCKED to IN PROGRESS. Public sources
do not establish an available 450–500 km slot, firm 1U price, mission ICD or
one-year orbit residence. This planning decision changes no component, CAD
geometry, launch commitment, orbit, cost estimate, licensing status or
Constitution success level. Evidence: engineering/09, Launch_Deployer_Trade.csv,
S33–S40, O01/O30/O31 and R03–R05/R11.

PIR-001 — 2026-09-15. Defined the present public-information development phase
and separated work that can proceed now from final closure requiring vendor,
integrator, regulator, test-facility or expert evidence. Added the known
downstream dependency register and reassessed the 108-row readiness matrix.
Retained the public EXOpod Nova baseline as provisional. No external contact,
component, requirement waiver, flight release or success-level change resulted.

THM-001 — 2026-09-15. Executed the approved D1-AN-THM-001 preliminary
transient thermal-power model using standard-library Python and public/project
inputs. Modeled all 1.0635 kg in 11 nodes across 10 orbital, environment,
attitude, heater-fault and conductance cases. Central nominal, cold, hot and
fixed-camera recovery cases do not close battery temperature and stored energy;
a deliberately low-conductance nominal sensitivity closes, making the thermal
interface a controlling design variable. R08/R10/R22 now record simulated
failure; O03 remains critical; THM-002 and EPS-007 moved to IN PROGRESS. No
hardware, paid software, external contact, test, expert review, architecture
change or success-level increase resulted.

TMI-001 — 2026-09-15. Recorded the **Thermal Model Incident** after the owner
challenged whether D1-AN-THM-001 represented an actual vendor part or physical
test. It did not. Reclassified all outputs as HYPOTHETICAL PARAMETRIC
SENSITIVITY — NOT COMPONENT-SPECIFIC, withdrew hardware-validation readiness
credit, reopened R08/R10/R22 interpretation, and instituted a critical-property
evidence gate for component selection and future simulation. Original results
remain preserved as experimental evidence. No hardware was tested and no expert
review occurred.

CMP-002 — 2026-09-15. Added D1-CMP-STD-001 and applied the owner's strict Phase
1 evidence requirement to required spacecraft and ground functions. Generated
an initial 86-row component/property matrix, later expanded to 105 rows after
auditing two Pumpkin structure/panel alternatives. No physical component passed the Phase 1
baseline gate. Corrected NanoDock DMC-3 availability using its current product
page, 2025 option sheet and qualification certificate. Added SkyFox piCAM/FM as
a better documented candidate and marked CS-101 unsuitable while that alternative
exists, without changing the controlled BOM. Archived eight exact manufacturer
documents locally with hashes; excluded copyrighted PDFs from Git. No purchase,
supplier contact, hardware test, baseline component selection or success-level
change occurred.
Six Pumpkin manufacturer documents/pages were then added to the local archive,
bringing the manifest to fourteen exact files.

GATE-001 — 2026-09-15. The owner directed that component evidence closure must
be the first step. Established D1-GATE-001 as the controlling first engineering
gate, ahead of further simulation, higher-fidelity CAD, procurement or integrated
performance claims. Existing preliminary work remains preserved without added
credibility. No component passed, no baseline hardware changed and no purchase or
external contact occurred.

CMP-003 — 2026-09-15. Created D1-CMP-SET-001, a complete proposed operating
set with 19 flight and 10 ground physical-component lines. Added exact COTS
candidates where supported, eight named custom-development assemblies, and five
explicit `NO COMPLIANT PART IDENTIFIED` ground/integration selections. Recorded
the piCAM substitution's bookkeeping-only mass/cost effect. The set is not a
Phase 1 baseline; 0 components were admitted and no controlled BOM, purchase,
hardware, external contact or evidence level changed.

CMP-004 — 2026-09-16. Completed Revision A of the Phase 1 closure review package.
Expanded the earlier 29-line proposal to a 52-record flight, ground and support
register after reviewing 50 additional manufacturer-document URLs and archiving
27 exact retrieved files with hashes. Replaced the proposed AntS family with the
better-documented SAM-S candidate without admitting it; selected bounded ground
components for bench power, antenna, printing, LNA and surge protection; defined
25 custom work packages; and retained 22 evidence-incomplete COTS/configuration
exceptions. Added missing rotator cables/control, nonconductive antenna support,
RF interlock/filtering, protected power, media/consumables, closeout, EGSE,
handling and verification fixtures. Internal register/hash verification passed
with zero errors. G1 remains open: no flight component or custom design was
admitted, no hardware was purchased or tested, and no new CAD, simulation,
performance or flight-readiness claim resulted.

DES-001 — 2026-09-16. The owner clarified that purchase is not a design
requirement and set a viable theoretical spacecraft design meeting educational
standards as the goal. Established D1-DES-STD-001. The completion standard now
requires exact verifiable COTS selections, released custom designs, reconciled
interfaces and reproducible analyses, but does not require purchase, fabrication
or physical testing. Evidence labels remain unchanged: theoretical completion
cannot imply tested, qualified, independently reviewed or flight-ready status.

ARCH-001 — 2026-09-16. Compared the mixed commercial baseline with BIRDS,
PyCubed, OreSat, VST104-Sierra, OpenLST and UPSat using public primary design
records. Selected a BIRDS-derived 1U architecture as the design-development
reference because it best matches the mission and exposes the complete spacecraft
concept. Degen-1 will release its own current avionics layouts and exact BOMs;
unpublished BIRDS core layouts and obsolete parts are not treated as evidence.
OreSat, VST104, OpenLST and UPSat remain subsystem references. This decision
does not close G1, admit a component, validate a performance claim or transfer
flight heritage to Degen-1.

DD-001 — 2026-09-16. Opened the BIRDS-derived detailed-design selection
register and selected exact battery, camera, radio-module, solar-cell,
backplane-connector and principal EPS parts. Added custom OBC, EPS, backplane,
radio-carrier, panel and pack records with explicit release paths. Selected a
passive magnetic-control assembly using one K&J `D84` and two custom 95 mm ×
1 mm HyMu 80 rods based on Quetzal-1 geometry and flight evidence. The magnet
is exact COTS; the rods and retainers remain custom. No Degen-1 dynamics result,
pointing claim, hardware test or transferred flight heritage was created.

DD-002 — 2026-09-16. Selected the D1-ANT-001 architecture: a custom four-element
436.5 MHz canted turnstile based on the tested OreSat feed record and a
four-channel resistor-release system based on Quetzal-1 flight hardware.
Selected exact principal feed, termination, connector, load-switch, burn-
resistor, indication-switch and I/O-expander parts. Defined custom element,
line, mechanism and PCB work packages, prototype geometry, electrical bounds,
interfaces, rejected alternatives and the RF/deployment verification path.
Pinned and archived open-source evidence with license files and hashes. This
selects a custom design direction; it does not establish integrated RF
performance, release reliability, launch compliance or physical test evidence.

DD-003 — 2026-09-16. Selected the D1-STR-001 nominal frame architecture from
the MIT-licensed BIRDS-4 flight-model CAD at a pinned commit. Archived the full
assembly and eleven unique frame STEP files and added a reproducible FreeCAD
extractor. The 22 top-level frame instances occupy a nominal
100 × 100 × 113.5 mm envelope. An all-6061 density calculation gives 152.363 g,
but remains an assumption because grouped upstream parts include hardware and
do not control every material. Selected certified 6061-T6 and a controlled
hard-anodized rail finish for the Degen-1 derivative. Native drawings,
tolerances, fasteners, interfaces, analysis and verification remain open; no
fabrication, fit check, load test or transferred qualification was claimed.

DD-004 — 2026-09-17. Selected the D1-FAB-001 launch-inhibit and front-access
architecture. Replaced the earlier `SDS002` with exact low-current-qualified
`SDS002RULC` switches and replaced the -4.5 V-characterized `SQA403EJ` with
`SiA4265EDJ-T1-GE3`, whose on-resistance is specified at -2.5 V and -1.8 V.
Selected two exact Same Sky switched-jack/plug pairs, a JST ten-position service
interface and seven independently controlled series MOSFET devices. Archived
the pinned BIRDS FAB evidence and current manufacturer PDFs. A reproducible
Boolean checker passes all 43 stated state/single-stuck-on cases. This is logic
evidence only; schematic, PCB, mechanical actuation, worst-case electrical and
thermal analysis, full fault tree and physical verification remain open.

DD-005 — 2026-09-17. Issued D1-HAR-001 as the complete connection-level harness
baseline for the current architecture: one battery loom, five independent
solar-panel looms, three independent deployer-switch leads, one camera cable,
one exact 100 mm U.FL RF cable and one removable service cable. Selected exact
TE/Raychem Spec 55 wire variants, JST PA locking connector configurations,
Molex PicoBlade housings/carrier header, the Hirose RF assembly and Western
Filament PTFE lacing. Selected exact YAGEO Nexensos `32208571` Pt1000 elements
for the five solar panels, while retaining their attachment, lead transition and
readout as custom verification work. A schedule checker accounts for all twelve
assemblies and their preliminary conductor quantities. CAD-routed cut lengths,
camera mating finish, panel lead transitions, strain relief, electrical/RF
analysis and all physical workmanship/test evidence remain open.

DD-006 — 2026-09-18. Paused website work at owner request and resumed radio
interface evidence closure. D1-COM-001 Revision B withdraws unsupported TX/RX
current bounds and transfers the manufacturer-drawn 3.00 +/- 0.1 mm height.
D1-COM-IF-001 records power-range and pin-direction inconsistencies, required
TCXO evidence, carrier connections and release/verification tasks. No hardware
testing, integrated analysis or maturity increase credited.

DD-007 — 2026-09-18. Archived and audited the exact Ebyte product-page demo
without executing vendor code. Conditional generic TCXO settings do not close
exact-module setup. Archived the Chinese manual and Dorji DRF1268T primary
datasheet for an alternative trade; documented its out-of-band power condition.
No substitution or maturity increase. Restored Git HTTPS helper discovery and
pushed prior engineering commits to the existing GitHub remote.
