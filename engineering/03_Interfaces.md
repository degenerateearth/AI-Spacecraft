# D1-ICD-001 — Preliminary interface control specification

Revision A | Functional allocation. Pin-to-pin harness release is OPEN.

## Compatibility findings

An electrical PC/104-style stack is not automatically pin compatible between manufacturers. Do not mate the EPS and carrier through unreviewed stackthrough contacts. Prefer separate manufacturer-approved power/data harnesses into D1-IF; mechanically stack boards with only approved connectors and standoffs. A complete populated-contact map is required even for nominally unused pins.

S03 gives EPS 3.3 V output up to 3.41 V unloaded. The OBC's normal supply range ends at 3.4 V [S08], and the radio has a 3.4 V absolute maximum [S10]. Direct connection is not accepted. D1-IF uses two independently supplied 5 V to 3.3 V conversion branches, one each for OBC and radio. Keep the radio's data pins high impedance while unpowered. Separate the EPS/AntS I2C branches from the radio CAN path so one stuck device does not jam all recovery control.

## Logical connection schedule

| ID | From / to | Interface and design allocation | Closure requirement |
|---|---|---|---|
| H01–H03 | +/-X, +/-Y, +/-Z panels → EPS MPPT1–3 | Per-face two-series-cell strings, opposite faces parallel through blocking paths | Signed hot/cold IV and reverse-current topology; no series connection between opposite faces |
| H04 | EPS switched 5 V A → D1-IF A → DMC OBC supply | 3.30 V nominal; 1 A branch design allocation | Test at load pins including all tolerances/transients |
| H05 | EPS switched 5 V B → D1-IF B → DMC radio supply | 3.30 V nominal; 1.2 A branch design allocation | Confirm startup, output discharge and backfeed isolation |
| H06 | EPS switched 5 V C → AntS 5 V variant | 2 W deployment allocation; no simultaneous TX | Independent hazard inhibits and pin map |
| H07 | A3200 ↔ AX100 | CAN/CSP, initially 125 kbit/s, two endpoint terminations | Carrier routing and firmware support; about 60 ohm unpowered bus resistance |
| H08 | A3200 ↔ ICEPS2 | 3.3 V I2C, 100 kbit/s, OBC master | Supplier command protocol, address, clock stretching, pullups |
| H09 | A3200 ↔ AntS | Separate isolated I2C branch | Address conflict check and unpowered pin behavior |
| H10 | AX100 RF → AntS | 50 ohm coax, right-angle MCX at radio | AntS connector selection; <=1 dB full harness loss |
| H11 | Three separation switches + RBF → EPS | Hardware inhibit inputs/paths | Exact wiring, independence, source isolation and switch travel |
| H13 | Switched payload rail → CS-101 / serial → OBC | 2 W peak camera allocation; UART or RS485 by supplier option | Camera voltage, logic levels, protocol and timeout OPEN; do not assume direct 5 V compatibility |
| H12 | Ground service → test interfaces | Current-limited, removable and keyed | No dual supplies or electrical bypass during delivery |

Connector names H01–H12 are Degen-1 harness IDs, not manufacturer connector identifiers. Freeze supplier part numbers, mating halves, cavities, contact gender, wire gauges, shields, lengths, tolerances and approved torque values in the final harness drawing. No arbitrary vendor pin numbers have been invented.

## D1-IF regulator adapter concept

Two TI TPSM82823-based channels are candidates [S14], each supplied by its corresponding EPS 5 V output. Use the adjustable configuration with 450 kohm top and 100 kohm bottom 0.1% resistors for 3.3 V nominal from the 0.6 V reference. Initial capacitor allocations: 10 uF input and 22 uF output, X7R, rated >=10 V; effective capacitance and stable layout must satisfy the selected datasheet circuit. Place local bulk/decoupling at each module's supply and use the manufacturer's layout guidance. These are design starting values, not a released schematic/BOM.

Reference tolerance +/-1%, resistor ratio tolerance, bias current, temperature, radiation drift, DC line drop and dynamic overshoot must be combined. A preliminary DC tolerance allocation of +/-1.2% gives about 3.260–3.340 V before dynamic effects. Allocate no more than 40 mV additional positive excursion at the radio pins, retaining at least 20 mV to the absolute maximum. The radio datasheet does not provide a clear guaranteed normal supply tolerance around 3.3 V; obtain written acceptance of the complete supply envelope. A bench measurement on one room-temperature unit is insufficient.

Provide independent enable control from EPS branches, output discharge, power-good telemetry, and signal isolation to stop parasitic powering. Use reset supervision referenced to the delivered OBC rail, not a remote EPS measurement. The regulator's own PG upper threshold is not an adequate radio overvoltage protector. Analyze switch short and feedback-open faults; an upstream EPS current limiter may not prevent downstream overvoltage. The open interface action must select an accepted protective topology or obtain a qualified tightly regulated supplier solution. Ordinary catalog regulator radiation behavior is a major residual risk.

No adapter Gerbers or manufacturing files are released. At procurement review compare this adapter's total engineering/qualification expense with a guaranteed compatible EPS output option or integrated bus. Remove the adapter only after the alternative's limits close over environment and aging.

## Safety inhibit allocation

Adopt three independent physical barriers for RF energy and for antenna release until the launch provider approves a different arrangement [S01]. Request the ICEPS2 three-separation-switch/RBF option. Its detailed topology must be assessed from source (battery, every solar path, test port) to hazard. Three switches controlling one common unprotected device are not automatically three independent inhibits. Shared grounds, body diodes, charging paths and data-pin backfeed must be considered [S03].

```text
BATTERY / SOLAR / TEST SOURCES
          |   vendor-controlled source isolation network
       Inhibit A --- Inhibit B --- Inhibit C --- hazard supply --- TX or release driver
          ^             ^             ^
       separate physical switch actuation / independent control as demonstrated

RBF overrides the integrated ground configuration to OFF.
Timers authorize later actions; they are not counted as physical inhibits.
```

This is a required functional topology, not a claim that the selected EPS already implements exactly this series circuit. Supplier evidence may implement an equivalent accepted network. In the inhibit verification fixture, exercise all eight switch states with solar power present and absent, battery present, and authorized service configurations. Inject each single failed barrier and prove the remaining barriers prevent the hazard. Record rail voltages, maximum RF leakage and release current against launch-approved limits. Battery protection exceptions need explicit ICD acceptance.

## Timing and safe defaults

Use at least 30 min delay before any deployable release and at least 45 min before RF after valid separation [S01]; apply any longer launch requirement. Software and hardware default to RF and release disabled. A reset during initial delay conservatively restarts the delay unless independently verified retained timing proves elapsed time. Switch bounce or reassertion resets the separation-valid state. Persist a command inhibit across reboot. Antenna release requires valid separation, elapsed delay, sufficient energy, allowed temperature and an authenticated command or preapproved autonomous commissioning sequence.

## Grounding and EMI

Select one intentional DC reference bond to chassis; route power returns with supply wires. Establish conductive structure bonds independently of anodized rail contact. Separate MPPT/regulator and heater current loops from radio feed and sensor wiring. Document shield termination and signal return paths. Test receiver sensitivity with EPS converters active, radio powered, maximum CPU workload and heater switching. No blanket claim of EMC compliance is made from component assembly grades.
