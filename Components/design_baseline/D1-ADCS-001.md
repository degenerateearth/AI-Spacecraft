# D1-ADCS-001 — passive magnetic attitude stabilization

Revision A · 2026-09-16
State: **CUSTOM/TO BE VERIFIED**

## Controlled selection

Degen-1 uses a passive magnetic attitude-control assembly with no powered
actuator and no precision-pointing claim:

| Item | Exact identity | Quantity | Evidence / state |
|---|---|---:|---|
| Restoring magnet | K&J Magnetics `D84`, N42 axially magnetized NdFeB disc, Ni-Cu-Ni coating | 1 | Exact COTS item selected; manufacturer drawing, generated specification, compliance certificate, product page and STEP file archived locally |
| Damping rod X | `D1-ADCS-HR-001`, custom 95 mm × 1 mm cylindrical HyMu 80 rod, ASTM A753 Alloy 4 | 1 | CUSTOM/TO BE VERIFIED |
| Damping rod Y | `D1-ADCS-HR-001`, custom 95 mm × 1 mm cylindrical HyMu 80 rod, ASTM A753 Alloy 4 | 1 | CUSTOM/TO BE VERIFIED |
| Magnet/rod retainers | `D1-ADCS-BRK-001`, non-ferromagnetic mechanical retainer set | 1 set | CUSTOM/TO BE VERIFIED; final geometry belongs to the structure release |

The camera boresight and the D84 magnetic-moment axis are collinear. The
magnet's north pole faces outward through the camera face. The two hysteresis
rods are mutually orthogonal and each is orthogonal to the magnet axis. This
copies the physically flown Quetzal-1 arrangement class and is also compatible
with the BIRDS platform's published passive-stabilization provision. It is a
project architecture decision, not evidence that Degen-1 will point at nadir.

## Exact COTS magnet properties

K&J's current product record establishes the following for `D84`:

| Property | Value | Evidence class |
|---|---:|---|
| Diameter | 12.7 mm | PRIMARY MANUFACTURER |
| Thickness | 6.35 mm | PRIMARY MANUFACTURER |
| Dimensional tolerance | ±0.1 mm | PRIMARY MANUFACTURER |
| Mass | 6.03 g | PRIMARY MANUFACTURER |
| Material / grade | NdFeB, N42 | PRIMARY MANUFACTURER |
| Magnetization | axial | PRIMARY MANUFACTURER |
| Coating | Ni-Cu-Ni | PRIMARY MANUFACTURER |
| Maximum operating temperature | 80 °C | PRIMARY MANUFACTURER |
| Maximum residual flux density | 13,200 gauss / 1.32 T | PRIMARY MANUFACTURER; maximum, not a guaranteed minimum |
| Surface field | 4,667 gauss | PRIMARY MANUFACTURER |
| Current catalog price | USD 2.03 each at quantity 1–9 | CURRENT MANUFACTURER PAGE; planning only |

The manufacturer does not specify a guaranteed magnetic dipole moment for each
delivered `D84`. The Quetzal-1 team measured **0.7363 A·m²** for its flight D84;
that value is flight-reference evidence for their unit, not a value assigned to
Degen-1 hardware. A simple `Br·volume/µ0` calculation using the manufacturer's
maximum `Br` gives about 0.845 A·m² and is an upper nominal estimate only.

## Custom hysteresis-rod definition

`D1-ADCS-HR-001` is an explicitly custom part, not a fictitious catalog SKU.
Its procurement specification shall require:

- material certified to ASTM A753 Alloy 4 and identified commercially as HyMu
  80;
- finished cylindrical geometry of 95.0 mm length and 1.00 mm diameter, with
  final tolerances set on the released drawing after the mounting analysis;
- cutting, straightening and final magnetic anneal controlled by the material
  supplier; no cold work after final anneal except supplier-approved handling;
- a lot certificate identifying composition, process route and heat treatment;
- two flight rods plus witness coupons and development spares from the same lot;
- measured major and low-field minor B-H loops on witness material and each
  finished rod or a validated rod-level sampling plan;
- visual, dimensional, mass and straightness inspection; and
- vacuum/outgassing compatibility of every encapsulant or retainer that touches
  the rod.

MuShield publicly identifies HyMu 80 as an approximately 80% nickel,
4.2–5.2% molybdenum soft-magnetic alloy conforming to ASTM A753 Alloy 4, with
approximately 8,000 gauss saturation induction, maximum permeability above
350,000 and very low coercive force. Those general properties do not establish
the minor loop of a finished Degen-1 rod. The rod remains custom until measured.

The 95 mm × 1 mm geometry is not an AI-created material surrogate. It is the
exact geometry reported for both flight rods on the 1U Quetzal-1 spacecraft.
Degen-1 still requires its own magnetic characterization because cutting,
annealing, aspect ratio, retainer stress and bias from the permanent magnet can
change damping.

## Mechanical and magnetic integration requirements

1. Locate the D84 at the camera end of the internal stack with its axis parallel
   to the camera boresight. Mark and independently verify the north pole before
   installation.
2. Locate the rods along orthogonal body X and Y axes and maximize their
   separation from the D84 within the 1U envelope. Final separation is driven by
   an as-built magnetic-field survey and low-field loop test, not by appearance.
3. Retain all three magnetic elements against launch loads without relying on
   magnetic attraction or an adhesive-only load path.
4. Use non-ferromagnetic retainers and fasteners within the controlled ADCS
   volume. Screen nominally nonmagnetic hardware after fabrication.
5. Keep the radio, switching regulators, inductors, high-current loops and
   antenna release current paths out of the controlled magnetic volume where
   practical. Record unavoidable sources in the spacecraft magnetic budget.
6. The D84 plating is not accepted as vacuum or corrosion protection by this
   record. Inspect plating, assess vacuum compatibility and provide a retained
   containment path for a cracked magnet.
7. Maintain D84 below 80 °C in all analyzed and tested cases; the system-level
   thermal allocation must include margin below that manufacturer limit.

## Functional claim and mission consequence

The assembly is intended to align one spacecraft axis with the local geomagnetic
field and dissipate rotational energy about the two transverse axes. Rotation
about the magnet axis remains weakly controlled. Magnetic-field alignment is not
nadir pointing, and the geometry changes with latitude and orbit.

Quetzal-1 is a strong architecture analogue because it was a 1U imaging CubeSat
using the exact `D84` and two 95 mm × 1 mm HyMu 80 rods. Its published on-orbit
results report detumbling from initial rates as high as ±25 °/s to about
±3.5 °/s per axis within one week, 14.28° alignment with the geomagnetic field,
successful payload imaging and 211 days of operation. The same publication also
reports growth of the least-controlled-axis rate to 16.65 °/s by end of mission
and reduced hysteresis effectiveness from magnetic bias. Degen-1 therefore uses
the architecture as credible precedent while retaining all rate, settling-time,
image-opportunity and twelve-month-performance claims as **UNVERIFIED**.

For Degen-1, repeated image attempts and the piCAM's broad field of view are the
mission strategy. The PMAC assembly does not guarantee a view of Earth or a
sharp image. A coupled orbit/IGRF/rigid-body Monte Carlo with final mass
properties and measured magnetic data must establish the expected distribution
of usable image opportunities.

## Verification and release path

The assembly remains `CUSTOM/TO BE VERIFIED` until all of the following exist:

1. released rod and retainer drawings, tolerances, materials, fasteners and
   installation sequence;
2. incoming inspection for exact D84 identity, dimensions, mass, coating,
   polarity and three-axis dipole moment;
3. certified rod lot and measured low-field B-H loops before and after mounting;
4. a completed spacecraft magnetic-material/current-loop inventory;
5. a three-axis magnetic survey of the unpowered and powered integrated vehicle;
6. a Helmholtz-cage and low-friction attitude test with flight-representative
   mounting and electrical modes;
7. a coupled attitude/orbit simulation using measured magnet, rod, inertia and
   residual-dipole inputs, with uncertainties and the candidate orbit;
8. camera smear and Earth-intersection statistics using the actual piCAM timing
   behavior;
9. structural-load and thermal-vacuum acceptance of the retainers; and
10. independent GNC/mechanical review before flight release.

If the measured rod loops or integrated magnetic survey do not support damping,
the corrective order is: change rod placement, control spacecraft magnetic
sources, resize/reprocess rods, then reassess the permanent magnet. No active
ADCS is added without an explicit architecture trade.

## Evidence and custody

- K&J Magnetics `D84` product page and downloads:
  https://www.kjmagnetics.com/d84-neodymium-disc-magnet
- MuShield HyMu 80 / ASTM A753 Alloy 4 manufacturer page:
  https://www.mushield.com/material-sales/hymu-80-magnetic-shielding-alloy-astm-a753-alloy-4/
- Alvarez et al., *Design and On-Orbit Performance of the Attitude
  Determination and Passive Control System for the Quetzal-1 CubeSat*, JoSS
  12(2), 2023:
  https://jossonline.com/storage/2023/05/Final-Alvarez-Design-and-On-Orbit-Performance-of-the-Attitude-Determination-and-Passive-Control-System-for-the-Quetzal-1-CubeSat.pdf
- Quetzal-1 open hardware repository, inspected at commit
  `d4d1b59de384701a016a6e17353aff3c8ba64853`, CC BY-SA 4.0:
  https://github.com/Quetzal-1-CubeSat-Team/quetzal1-hardware
- BIRDS platform documentation, Revision F, §6.6, permits installation of a
  permanent magnet and hysteresis damper as a user passive-stabilization system:
  https://github.com/BIRDSOpenSource/BIRDS-GeneralDocumentation

Hashes for the locally retained manufacturer and flight-reference files are in
`SOURCES/components/LOCAL_ARCHIVE_MANIFEST.csv`. No result in this record is a
Degen-1 physical test.
