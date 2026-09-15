# D1-ENV-001 — Mechanical and environmental design

Revision A | Analysis plans plus explicit screening; qualification remains open.

## Structure and launch survival

Purchase a metal 1U flight structure and its intended rail, fastener and board-mounting system. Retain supplier materials, surface treatments and joint geometry. Flight harnesses require strain relief and positive retention. No friction-fit hobby headers, loose SD cards, consumer battery holders, adhesive-only heavy components or unapproved rework are accepted. Approved locking methods and workmanship instructions must be selected with the assembly contractor.

Rails carry dispenser interface loads into frames; board standoffs carry PCB mass into frames. Battery support must use the supplied retention system. Verify cell restraint independent of electrical terminals. Solar substrates transfer loads through approved attachment points. Antenna elements must be restrained by spacecraft hardware in the stowed state; the dispenser is not the antenna hold-down mechanism.

The rail drawing is governed by the selected dispenser ICD and CDS [S01]. Require supplier drawings, material certificates, fastener specifications, installation sequence, vent paths, mass properties and actual flight configuration CAD. Check access and serviceability with the panels and antennas installed. Outgassing evidence is required for adhesives, coatings, wire insulation and polymer components; inspect venting of every enclosed volume. Prefer already characterized material systems and minimize late finish changes.

### Preliminary load screen

For scale only, assume a 20 g quasi-static limit acceleration (A; not a launch requirement). The 1.2762 kg design mass produces 250.3 N. Uniform division over four rails is 62.6 N/rail, but real restraint preload and dynamic load sharing may be highly unequal. An EPS mass of 184 g produces 36.1 N, and with an assumed 25 mm lever arm about 0.90 N m. These are input loads, not strength margins. Use the launch coupled-loads envelope for final analysis.

Require a structural finite-element model including joint stiffness, dispenser boundary conditions, battery and daughterboard retention, panel supports, harness masses and material allowables. Extract modes, random vibration responses, stress, fastener preload/separation, buckling and fatigue where applicable. Compute `MS=allowable/(factor*applied)-1` using approved yield/ultimate factors and documented allowables. No positive structural margin or first-mode frequency is claimed without this model. A convenient 100 Hz target may guide early stiffness but is not adopted as a universal acceptance criterion.

Qualification/acceptance profiles must be agreed with the integrator. GEVS B [S15] is a tailoring reference; do not expose hardware to an arbitrary generic gRMS value. Shaker-fixture dynamics, notching, force limits and battery state matter. Components with heritage still require final assembly workmanship/acceptance testing. Current EPS and AntS webpages do not identify individual shipped-unit vibration/shock testing [S02,S05].

## Thermal architecture

Six dark solar faces offer limited radiator area. Put the battery toward the interior, provide a characterized conductive route to the structure, and use controlled isolation to prevent excessive cold coupling. Retain EPS heater sensing and add independent overtemperature protection if the provided architecture lacks the required failure protection. Place radio heat spreading to the frame; avoid coupling peak radio heat directly into the battery. Use qualified optical films only on available non-cell areas and preserve antenna/rail interfaces.

Project targets: battery +5 to +35 C during normal operation; charge only from +5 to +40 C at <=0.8 A until the vendor approves a different profile; inhibit charging below +5 C or above +40 C. Nonbattery electronics target -10 to +50 C. Deploy the antenna only from +5 to +45 C, providing margin inside the current published deployment range [S05]. These targets are allocations, not predicted temperatures. S03 distinguishes battery charge, limited-current charge and discharge ranges; the broader EPS marketing operating range is not permission to charge at subzero temperature.

### Executed screening

`thermal_screen.csv` uses a single isothermal node with radiating area 0.06 m2, effective Earth-view area 0.02 m2, and assumed projected areas 0.01–0.01732 m2. Solar flux 1322–1414 W/m2, albedo 0.20–0.35 and IR 200–260 W/m2 are illustrative bounding inputs. Optical absorptivity/emissivity are assumed, not measured. Electric power extraction is subtracted from absorbed solar heat, with internally dissipated power then added.

The equilibrium estimates are approximately -18 C for the cold sunlight case, +19 C nominal sunlight, +50 C hot sunlight and -78 C eclipse equilibrium. Eclipse equilibrium is **not** an actual 36-minute eclipse temperature; thermal inertia is absent. These results demonstrate that passive survival/charging is not closed by the current screen. They must not be used as hardware qualification predictions.

### Thermal closure method

Build at least a battery, avionics, structure and six-panel node network. Each node obeys `C_i*dT_i/dt = Q_i + sum(G_ij*(T_j-T_i)) + radiation_exchange_i`. Include battery internal resistance versus SOC/temperature, heater PWM, power conversion losses, operational modes, shadow transitions, cell extraction, varying beta and optical properties at end of life. Run cold startup after launch storage, long eclipse, repeated low-generation recovery, hot continuous-sun and high-beta cases, and heater-stuck-on/off cases. Model actual thermal conductances and uncertainties; correlate using thermal-balance testing and measured time constants.

Close the heater budget jointly with energy. The assumed 0.10 W orbit-average heater load is restrictive. If the model needs more than the available energy reserve, change thermal paths/optical surfaces or reduce operations; do not merely increase battery capacity. A larger battery does not fix a persistent negative orbit-energy balance. A 1 W heater stuck on threatens both energy and temperature and must have a bounded shutoff path.

The approved preliminary transient model is now implemented in
`analysis/thermal_transient.py` and reported in
`engineering/11_Transient_Thermal_Power_Analysis.md`. Its central nominal 475 km
case predicts -3.3 to +9.5 °C at the battery, 64.8% heater duty and -0.88 Wh/orbit
stored-energy balance. The fixed camera-face recovery case also fails when
thermal control is coupled. A low-conductance sensitivity case passes nominal,
so no blanket failure of the eventual hardware is claimed; the current thermal
interface and heater allocation are simply not closed.

## Radiation and other LEO exposure

Create an orbit/epoch-specific radiation environment and shielding sector model before making a twelve-month reliability claim. Run trapped particle and solar/proton/heavy-ion cases using an appropriate validated environment tool and retain all inputs/model versions. Assess total ionizing dose at the CPU, memory, EPS controller, switches, radio and adapter regulators, plus displacement damage to solar cells. Apply a preliminary radiation design margin factor 2 to the calculated mission dose when evaluating test evidence. This factor is a project allocation, not a universal standard.

Obtain part-level or assembly-relevant dose/SEE evidence tied to delivered lot/revision. Destructive latchup and power MOSFET failure cannot be fixed by a watchdog; power limiting is useful only if its response prevents damage. Memory upset recovery uses CRC, independent boot images and persistent counters, but does not provide quantified mission reliability. No arbitrary aluminum thickness is presented as sufficient shielding. NASA guidance emphasizes the application-specific nature of SEE assurance [S17].

Assess atomic oxygen/UV damage to exposed polymers, cell coverglass and adhesive edges; spacecraft charging and electrical bonding; vacuum effects on heat transfer and lubricant; and micrometeoroid/debris risk. Preserve material certificates and test evidence. This design accepts single-string critical hardware to control cost, so single-point failures remain. No numeric probability of one-year survival is claimed.

## Orbit lifetime and disposal

Use the as-built mass and projected drag area distribution, including deployed antenna influence, to propagate atmospheric decay. A rough nominal ballistic coefficient with m=1.0635 kg, Cd=2.2 and mean area=0.015 m2 is 32.2 kg/m2; plausible areas 0.01–0.01732 m2 give approximately 48.3–27.9 kg/m2. This is not a lifetime prediction.

Run launch dispersions, earliest/latest epochs, attitude cases, solar minimum and high-activity density cases. High drag must retain orbit for the operational year; low drag must meet post-mission disposal timing. Apply the applicable FCC requirements [S16] and integrator criteria, with reentry casualty/demise and collision analyses. NASA's deorbit overview [S18] supports treating this as an explicit design trade. A 475 km starting altitude is only a candidate. If no interval closes, change launch orbit or add a disposal device and re-open size, mass, cost, hazards and reliability. Do not promise passive deorbit solely from altitude.
