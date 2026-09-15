# D1-SYS-001 — Mission and architecture

**Phase 1 component status, 2026-09-15:** This document describes a candidate
architecture. Under D1-CMP-STD-001, no physical component is yet admitted to the
Phase 1 baseline. Product names below are allocations for audit, interface work
or trade study; `procurement/BOM.csv` and the component property matrix carry the
current evidence status.

Revision A | 2026-09-14 | Preliminary

## Mission definition

Demonstrate low-cost opportunistic Earth imaging and spacecraft health monitoring for 365.25 days after separation. Image requirement: return at least one recognizable Earth image during commissioning and target one useful image per month thereafter, including the final mission month. This image cadence is an allocated target, not a demonstrated coverage result. Success is at least one authenticated command and one valid health dataset during each rolling seven-day interval after commissioning, including an interval at mission day 365. The weekly criterion accommodates outages; it is not a promise of continuous ground coverage. Nominal target: daily telemetry retrieval. Minimum useful dataset: battery voltage/current/temperature, solar input power, resets, mode, uptime and radio temperature. Inertial data use sensors already on the OBC and are secondary.

Assume a US private operator, a single spacecraft and no commercial communications service. US operation and low build cost are owner requirements. Noncommercial demonstration is the provisional operating model; radio-service eligibility is not yet determined. Planning orbit: circular 475 km, inclination 51.6 degrees; trade range 450–500 km. Epoch, inclination, RAAN, injection dispersions, ground location and launch provider remain unselected. Higher-inclination rideshares require new radiation, thermal, contact and lifetime analyses. Do not buy an RF variant before the radio-service decision.

Functional operation for a year and remaining in orbit for a year are separate requirements. A lower orbit may decay too early; a higher orbit may not dispose quickly enough. No propulsion is provided. The launch orbit must pass both gates using appropriate atmospheric uncertainty cases.

## Architecture and cost choices

The expensive items are purchased flight-oriented subsystems whose testing/documentation can reduce development effort. Ordinary commercial components are confined mainly to the interconnect/regulator adapter and ground support. A catalog product's heritage is evidence to investigate, not proof of the delivered revision's qualification.

Six photovoltaic faces remove the geometric zero-power orientation of a five-face design. Opposite faces feed three MPPT inputs through vendor-approved isolation, one axis per input. Two cells in series on each face give a nominal planning MPP voltage around 5.4 V [S04]; no opposite faces are placed in series. Cold open-circuit voltage, hot MPP voltage, shadowing and startup behavior require vendor curves. Five faces use a 2.3 W allocation; the +X camera-aperture face uses 1.8 W. The 2.3 W/face allocation is conservative relative to two current catalog cells but remains an RFQ acceptance target [S22].

The integrated two-cell battery simplifies packaging and handling. The CPU and radio share a commercial carrier but have separate switched, regulated power branches. The radio uses CAN/CSP to the OBC; EPS and antenna commands use I2C, with branch isolation. Debug connectors cannot back-power the bus during flight integration.

A 5 V AntS variant provides a deployment interface independently switched from avionics. It carries the +Z panel using the supported accommodation [S05]. A UHF turnstile is selected for broad coverage; actual pattern nulls remain. It is tuned on the assembled spacecraft. Body attitude is uncontrolled. A side-looking CrystalSpace CS-101 camera takes bursts when energy allows; the camera is disabled in recovery. No requirement relies on passive magnetic alignment, spin-axis control or a claimed detumble time. The OBC gyro characterizes rotation; excessive rotation or poor generation reduces operations.

## Functional block diagram

```text
 +/-X panels -- isolated parallel -- MPPT X --+
 +/-Y panels -- isolated parallel -- MPPT Y --+-- ICEPS2 rail / battery / safety inhibits
 +/-Z panels -- isolated parallel -- MPPT Z --+             |
                      +-----------------------------------+-------------------+
                      |                                   |                   |
               switched 5V A                       switched 5V B        switched 5V C
                      |                                   |                   |
             D1-IF regulator A                  D1-IF regulator B       AntS controller
                      |                                   |                   |
               A3200 3.3V <--------- CAN/CSP ------> AX100-U 3.3V --RF--> turnstile
                      |
               isolated I2C branches --------> EPS housekeeping / AntS control
                      |
               temperature / health / gyro telemetry
```

## Operational phases

Ground storage → integrated inhibited state → separation detection → delayed commissioning → antenna release → receive/beacon acquisition → health operations → recovery as necessary → end-of-mission passivation. Commanded RF silence must persist across watchdog resets. Lost ground contact cannot cause unrestricted high-duty transmission. A battery exhausted below the restart threshold must be able to recover from solar power without OBC intervention.

The three-inhibit provision and RBF are a supplier/launch-interface configuration requirement. A single software switch or a timer is not substituted for independent barriers. The EPS optional switch architecture is evaluated at system level with all solar and debug paths included [S03]. The design has no pyrotechnic devices, pressure vessels or propulsion. No new orbital debris is intentionally released.

## Alternative selection rule

RFQ the component baseline and a basic EXA KRATOS or Alen 1U platform simultaneously. Prefer the offer with the lowest total delivered, integrated, verified cost that meets the requirements. The present evidence supports a cost-conscious candidate, not a mathematically proven global minimum. A turnkey quote can win even if its hardware line is higher: reduced adapter design, software integration and retest effort can dominate the difference. No order or supplier message was sent.
