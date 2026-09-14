# D1-AIV-001 — Assembly, integration and verification plan

Revision A | Planned procedures; no test has been performed on hardware.

## Build sequence and records

1. Freeze mission scope, RF route and candidate orbit. Obtain exact vendor revisions and controlled ICDs. Re-run all model inputs against quotes before ordering flight hardware.
2. Receive and serialize hardware. Capture vendor CoC, acceptance data, firmware versions, battery shipping documentation and storage conditions. Inspect for damage and validate packing lists. Open nonconformances before accepting substitutions.
3. Build an engineering flat-sat with representative EPS/OBC/radio/camera interfaces. Use a battery simulator first, then the protected engineering battery. Validate supply tolerance, inhibit paths, watchdog recovery, radio interoperability and camera file handling before flight-stack assembly.
4. Qualify the D1-IF layout and mechanical details using engineering articles. Test dead shorts, feedback fault behavior, output overshoot and unpowered data pins. Close radiation evidence separately. Do not debug an unverified regulator using flight radio hardware.
5. Assemble the flight structure on an ESD-controlled clean bench with approved tooling. Record fastener torque and locking method from supplier drawings; log material lot/cure records and photographs. Install EPS, adapter, avionics, camera and harnesses in the cleared sequence. Use strain relief and verified connector retention.
6. Check camera focus and boresight, install solar panels, then antenna assembly. Measure power IV curves and complete an RF tune on the final assembly. Verify camera aperture, deployed antenna clearance and all rail envelopes.
7. Run baseline functional, mass/property, dimensional and inhibit tests. Complete environmental testing in approved sequence, followed by repeat functional and optical/RF checks. Any rework after environmental testing receives a documented regression/retest disposition.
8. Load final approved firmware/configuration, archive hashes, verify battery SOC, remove optical cap, install RBF and prepare clean shipping configuration. Perform final integrator fit check and delivery review with traceable closeout evidence.

## Test matrix

| Test ID | Procedure / configuration | Acceptance evidence |
|---|---|---|
| T01 | Dimensional inspection and flight-like dispenser fit | Signed measurement report, interference-free insertion/ejection per ICD, all rail/protrusion limits |
| T02 | Mass, center of mass, inertia measurement | <=actual manifest mass; project target <=1330 g; COM target +/-10 mm; measured inertia |
| T03 | Every power branch across temperature, SOC and load steps | Approved operating voltage at device pins; no absolute maximum exceedance; stable recovery and measured efficiency |
| T04 | All eight inhibit-switch states; source permutations; single failed barriers | No RF/release hazard before allowed state; RBF and debug isolation verified to launch limits |
| T05 | Separation delay, reset/brownout/bounce and stuck-switch injection | No early RF/release; bounded retries; stable inhibited defaults |
| T06 | Solar simulator/shadow sweep, hot/cold IV and one-axis exposure | 2.3 W five faces, 1.8 W aperture face at agreed BOL conditions; cold startup and no reverse-current damage |
| T07 | Orbit power replay: >=72 hours, nominal and fixed-attitude recovery | No declining SOC trend after settling; commanded load/duty and temperatures within budget |
| T08 | Battery capacity and representative life evidence | >=18 Wh usable EOL capacity basis at specified discharge conditions; 6000-cycle mission-profile evidence plus calendar storage |
| T09 | End-to-end radio attenuation/Doppler test, EPS/heater/CPU active | <=1% PER at -123 dBm for selected packet/waveform or reclosed link; +/-11.1 kHz Doppler tracking with residual offsets |
| T10 | Full assembly antenna tuning/pattern measurement | Feed loss, return loss and gain coverage meet approved RF model; stowed and deployed characterization |
| T11 | Image capture, optical focus and smear replay | Recognizable calibrated scene at infinity; exposure, compression and bounded memory/CPU behavior |
| T12 | Random/sine vibration and shock as required, flight-like fixture | Signed tailored profile, monitored response, no damage, post-test function/optics/RF within acceptance limits |
| T13 | Thermal vacuum cycling + thermal balance, functional at plateaus | Correlated thermal model; no charge outside allowed range; no reset/leak/optical failure; heater budget closes |
| T14 | Antenna deployment at cold/hot allowed limits, vacuum where required | Every element deploys and indicates status; bounded release energy; no camera or cell interference |
| T15 | Fault campaign: stuck I2C, radio runaway, corrupt image, brownout, bad boot, lost contact | Recovery reaches defined safe state, no boot loop or uncontrolled TX; health accessible |
| T16 | Radiation evidence review and tests for uncovered parts | Environment/dose/SEE assessment and accepted margin; no unsupported critical-part survivability claim |
| T17 | Rehearsed LEOP, image request, ground loss and mission end | Operations runbooks complete; keys/backup and source passivation verified |
| T18 | Optical/EMI/functional regression after environment | Before/after data comparison within signed limits and all anomalies dispositioned |

## Environment profile tailoring

Before T12/T13 define expected flight environment, qualification/protoflight/acceptance philosophy and allowed hardware pedigree. A cost-minimum approach uses one flight model with supplier design qualification evidence, representative engineering hardware for development and a tailored flight acceptance campaign. Qualification gaps cannot be silently waived to save money. Extra qualification articles belong in the cost risk.

The test readiness package specifies fixture drawings, accelerometer/thermocouple locations, calibration, command script, battery state, inhibit state, frequency/PSD/shock response levels, axis order, durations, notching/abort criteria, chamber pressure and hot/cold dwell criteria. Limits are TBD until the launch provider and analysis agree. Never use component absolute maximum ratings as test setpoints. Thermal cycling and vacuum testing are distinct evidence items; a generic vendor temperature range does not substitute for system thermal balance.

For each test record article serial number, hardware/firmware revision, operator, date, calibrated equipment, setup photos, raw time series, deviations, pass/fail against each requirement and independent reviewer. A claimed pass without raw data and configuration traceability is not a closed requirement.

## Procurement and review gates

PDR: mission scope and candidate architecture; budgets with assumptions; cost trade; no hidden unknowns. CDR/fabrication release: all supplier ICDs closed, full schematics/CAD, structural/thermal/radiation analyses, orbit/regulatory route and flight software architecture accepted. Test readiness: procedures/limits/fixtures approved and hazards controlled. Flight readiness: requirements matrix closed with signed evidence, licensing and manifest approvals in hand, anomalies resolved, configuration frozen. No gate is passed by issuing this document.
