# CAD-001 findings and review actions

The documented design is representable as an editable accommodation assembly,
but physical fit is NOT ESTABLISHED. Every modeled solid lies inside the nominal
100 x 100 x 113.5 envelope, while 23 pairwise envelope intersections remain.
Containment alone is not a deployer fit check. No architecture was moved, shrunk,
cut or redesigned to hide collisions.

## Assumptions linked to O19–O22

| ID | Provisional value / reason | Consequence / closure |
|---|---|---|
| CAD-A01 | Existing SCAD square 8 mm rails centered +/-46; 88 mm XY board/reference regions retained | Not supplier rail or PCB shape. Corner overlap may disappear with real cutouts; obtain controlled CAD. |
| CAD-A02 | EPS 96 along X and 92 along Y; centered XY at documented Z | Orientation/connector reach unverified. 90-degree rotation swaps affected panel sides; it does not establish fit. |
| CAD-A03 | Carrier 88 x 88 x 1.6 at Z 20:21.6; A3200 centered (0,-21,28), AX100 (0,21,28) | Two modules side-by-side on top is documented; positions, 2 mm side gap and 1.6 board thickness are assumptions. No invented standoffs/connectors fill the space. |
| CAD-A04 | Side panels 3 mm thick at +/-48.5, tangential width 84, height 98; top/bottom 84 square x3 at +/-52.5 | Top Z allocation is documented; other dimensions are provisional visualization/accommodation allowances. Deliberately no camera or switch cutouts. Do not order panels from this model. |

These assumptions support bounded packaging questions without claiming a
supplier-specific assembly. Increasing fidelity through fabricated mounting,
lens or deployment data would make the result misleading; those operations
are withheld pending evidence, without blocking the useful envelope model.

## Documented design -> CAD conflict -> proposed correction

| ID | Documented design | CAD conflict | Proposed correction for review (not implemented) |
|---|---|---|---|
| CAD-C01 | SCAD 88 square regions and 8 square rails | 16 rail intersections: per rail adapter 24 mm3, carrier 6.4, EPS 636, AntS 343 | Obtain actual frame/PCB/AntS corner reliefs and placements; replace proxies. Do not shrink products to 88 or notch actual parts without approval. |
| CAD-C02 | EPS at Z -12:14.5; six side faces | 96 mm EPS crosses assumed +/-X panel inner plane by 1 mm; 2226 mm3 per panel | Confirm panel thickness, offset and EPS orientation/real contour together. Current assumed skin thickness leaves no established margin. |
| CAD-C03 | AntS at 44:51; side panels reach +49 | Four AntS/side-panel overlaps of 840 mm3 each | Confirm supported AntS/frame/panel interface and side-panel termination; full bounding box may include empty relief. |
| CAD-C04 | Camera center X25 with depth45; aperture required | Camera reaches X47.5 and assumed panel starts47: overlap525 mm3; uncut panel obstructs +X sightline | Obtain lens pupil/barrel/aperture and cell routing. Do not cut a guessed hole or claim 1.8 W from area alone. |
| CAD-C05 | 27 mm camera bay vs 25 mm envelope | Only 1 mm nominal Z clearance each side before bracket, tolerances and harness | Check bracket topology and supplier dimensions before retaining bay height. 20 g allowance does not define bracket geometry. |
| CAD-C06 | DMC + modules in 16 mm bay | Gross module tops are below36, but connector/standoff gap is invented placement, mounting/access unverified | Obtain DMC3 controlled mechanical and mating drawings; verify both top-side modules and coax bend/access. |
| CAD-C07 | Four-element deployable antenna and +X camera | Swept volume and optical pupil unknown; no deployment/field-of-view clearance test possible | Obtain deployment kinematics and lens prescription/envelope. Keep O07/O09 open. |

The numerical overlaps are between *bounding envelopes*. They are neither
confirmed material collisions nor a pass for the real parts. Rail/profile,
panel geometry and vendor corner cutouts are particularly consequential.
The module pair has 2 mm assumed nominal gap; no tolerance margin is credited.
Fastener accessibility, battery restraint, venting, harness bend radius, switch
travel and assembly sequence cannot be accepted at this fidelity.

## Mass properties

No artificial density is applied to boxes. Assigned unit masses use the existing
BOM and retain V (vendor), P (provisional) and A (allocation) qualifiers.
Every BOM line is counted exactly once in the generated ledger, including B03
quantity three. Battery is included in B02; sensors/shields in their parent modules.

- Existing total remains **1063.5 g**, or **1276.2 g** with 20% growth; no independent density-derived total exists.
- **768.5 g** is associated with component envelopes. The other **295 g** comprises frame/fasteners, harness/switch allowance, thermal materials, integration brackets and camera mounting. Rail proxies are not assigned the entire frame mass as if it were uniformly distributed.
- Credible spacecraft COM/inertia: **UNKNOWN**. Real internal mass distributions, mounting and unlocated allowances are missing. `geometry_report.json` reproduces the earlier report's point-mass COM as a separate illustrative calculation; it is not a CAD mass property or R05 closure.

## Evidence and next fidelity gate

Native model/STEP validity and reproducibility are software checks. No physical
hardware, structural or thermal simulation, expert review, launch compatibility
or supplier approval is established. Success level is not increased; R03,R05,
R21,R27,R30 and existing release gates stay open.

First resolve controlled frame/rail and EPS/AntS geometry, selected panel layout,
DMC mounting interfaces, and camera aperture/bracket. Then add hardware, routing,
tolerances and assembly sequence, and rerun interference/mass studies. Supplier
data access is the current fidelity limit; no paid engineering tool is needed
to generate this model. Quote any paid data/service before introducing it.

## LDG-001 external-interface screen

The standard 1U EXOpod Nova planning reference produces no new nominal outer
envelope or mass violation: CAD-001 uses 100 × 100 × 113.5 mm, and the budgeted
mass with growth is 1.2762 kg versus the public 2.5 kg limit [S33]. This is not a
fit pass. Rail tolerances, section/radii, finish, clamping contact, assembled
coplanarity, switch/RBF access, complete mass location, and physical insertion
are absent.

LDC-01 through LDC-06 in [D1-LCH-001](../../engineering/09_Launch_and_Deployer_Baseline.md)
record the documented design, external constraint, CAD conflict, and proposed
correction. CAD-C01–C07 remain open and no geometry was altered to make the
screen appear compliant.
