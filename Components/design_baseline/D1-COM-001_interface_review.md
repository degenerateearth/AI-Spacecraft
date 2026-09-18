# D1-COM-IF-001 — radio interface evidence review

Revision A · 2026-09-18 · DOCUMENT REVIEW / PROJECT REQUIREMENTS

Scope: selected Ebyte E22-400M22S only. No hardware, RF, environmental or
integrated spacecraft test was performed. Website work is paused at owner request.

## Evidence identity

Ebyte User Manual, revision-history entry 1.5 dated 2024-12-31; archived
2026-09-16, re-examined 2026-09-18. PDF page numbers below are one-based file
pages, not printed footers. Pages 5 and 6 were rendered and visually checked;
remaining cited text was extracted with pypdf. No values came from another module.

- Document: https://www.cdebyte.com/pdf-down.aspx?id=3511
- Current product/order route: https://www.cdebyte.com/products/E22-400M22S
- Local archive: `SOURCES/components/Ebyte_E22-400M22S/E22-400M22S_User_Manual.pdf`
- SHA-256: `8c7baff5430e0a9becc7ed778035af546512b0a1c67b81c1d23bddd401f18df1`
- Copyrighted PDF remains local; this review records claims and provenance.

## Documented design -> conflict -> correction

| ID | Documented design | Evidence/conflict | Correction and consequence |
|---|---|---|---|
| COM-C01 | 95/100/105 mA TX bounds and 6/6.5/7 mA RX bounds | PDF p5 lists only 100 and 6.5 in typical column; minimum and maximum cells are blank | Withdraw bounds; do not choose protection thresholds using 105 mA as a guarantee. Source-backed operating envelope still required. |
| COM-C02 | Thickness unknown | PDF p6 explicitly dimensions height 3.00 +/- 0.1 mm | Transfer dimension; module outline becomes 20.0 +/- 0.1 by 14.0 +/- 0.1 by 3.00 +/- 0.1 mm. This is not installed clearance or a carrier footprint release. |
| COM-C03 | 1.8–3.7 V advertised range | PDF p4 feature list says 2.5–3.7 V; p5 operating table says 1.8–3.7 V | Retain recommended nominal 3.3 V. Do not claim full RF performance at 1.8 V; reconcile converter tolerance/ripple/transient limits before release. |
| COM-C04 | VCC supply input | PDF p7 direction column labels VCC output while function describes supply | Treat VCC as power input per supply requirements; preserve apparent documentation error for review, not a new power output. |
| COM-C05 | TCXO exists | PDF p8–9 identifies internal DIO3/TCXO use but does not specify voltage selection, startup delay or ppm bound | Do not copy another module's TCXO setup. Search exact-module manufacturer firmware/settings before driver release and Doppler calculation. |

## Pin-level carrier requirements

The following requirements implement the existing architecture; they are not
claims that a schematic or firmware exists. Module numbering is per PDF p7.

| Pins | Connection | Evidence / release condition |
|---|---|---|
| 1–5,10–12,20,22 | Ground | Manufacturer p7; continuous return and RF layout require PCB review |
| 9 | Protected 3.3 V input | Manufacturer p5,7; capacitor exact parts and power-off behavior unresolved |
| 6 | OBC RXEN output | Active high, p7; keep low outside receive as project requirement |
| 7,8 | TXEN wired to DIO2 | Manufacturer p8–9; do not additionally drive DIO2 with an MCU output |
| 13 | DIO1 to OBC interrupt input | Manufacturer p7; IRQ configuration and OBC physical pin not released |
| 14 | BUSY to OBC input | Manufacturer p7; timeout/recovery logic required, not endless polling |
| 15 | Active-low reset from OBC | Manufacturer p7; timing and power-off isolation require chip documentation |
| 16 | MISO to OBC input | Manufacturer p7; shared-bus contention analysis required |
| 17,18,19 | MOSI,SCK,NSS from OBC | Manufacturer p7; no 5 V signaling; power-off isolation unresolved |
| 21 | 50-ohm RF carrier path | Manufacturer p7; exact launch/filter/antenna path remains custom design |

## Initialization release checklist

1. Reconcile exact module TCXO control voltage/startup time against manufacturer
   example source and SX1268 commands. Record file revision/hash and line references.
2. Define reset, BUSY timeout and command-status error recovery from chip manual.
3. Configure DIO2 switch control while separately driving RXEN. Define safe
   transitions that never request simultaneous transmit and receive paths.
4. Define calibration, regulator, PA and OCP configuration for SX1268 and this
   module, not a substituted SX1262 board. Require exact register/command table.
5. Select packet type and full modulation/packet parameters only after public
   evidence supports sensitivity, bandwidth and oscillator-error analysis.
6. Define power-off GPIO states and verify no back-power path in the schematic.
7. Release the same waveform/configuration on ground and flight implementations.

These are incomplete release tasks, not a working initialization algorithm.

## Verification path and priority

Public-information work next: retrieve exact Ebyte firmware/settings; reconcile
TCXO configuration; source chip-level command/timing evidence; evaluate a better
documented module if critical evidence cannot be obtained. Do not immediately
contact the vendor or substitute assumed limits. A custom carrier does not make
missing COTS properties acceptable.

Later bench procedure: inspect orientation/pin continuity; verify protected supply
and zero unintended power-off injection against released limits; capture reset,
BUSY, SPI and switch controls; exercise timeout recovery; conduct attenuated
two-radio packet tests at both planning frequencies; characterize power and
current across released voltage/temperature conditions. Numeric acceptance limits
cannot be issued until the corresponding source/design bounds are released.

No evidence supports declaring the ground modem, orbital link, current limiter,
radio flight suitability or full spacecraft functional at this stage.

## Public-source follow-up — 2026-09-18

Retrieved the demo linked directly from the exact Ebyte product download page:
https://www.cdebyte.com/products/E22-400M22S/4 . Exact download URLs and hashes
are in `D1-COM-001_followup_sources.json`. Local vendor archives are excluded
from public Git pending redistribution review.

The nested `sx126x-driver.zip` is a generic Semtech driver distribution for
Nucleo boards. `src/radio/sx126x/sx126x.c` line 95 requests 1.7 V only inside
`USE_TCXO`; `sx126x.h` line 34 defines 5 ms under that conditional. None of
the six supplied Keil project files contains `USE_TCXO`. These values are
**example code**, not verified E22-400M22S operating requirements. No driver
was compiled, executed, flashed or tested. The exact-module configuration
gap COM-C05 remains open. Chinese manual PDF p6 also describes DIO3 powering
the TCXO without supplying the needed voltage/startup bounds in that passage.

Reproduce the source inspection, from repository root:

```text
python Components/design_baseline/audit_radio_demo.py SOURCES/components/Ebyte_E22-400M22S/manufacturer_demo_2026-09-18.zip
```

Compare output with `D1-COM-001_demo_audit.json`. This checks source contents
and hashes only; it cannot verify behavior or establish electrical ratings.

### Alternative actively examined: Dorji DRF1268T

Manufacturer datasheet Rev 1.00 Dec 2018 has a pin table (p2), electrical and
absolute limits (p3), circuit schematic (p4), and mechanical drawing (p5).
It explicitly states a +/-1 ppm TCXO (p2), but the conditions covering that
accuracy are not established by that statement. Its operating band is
410–460 MHz, while the power row on p3 specifies a 915 MHz condition. That
row cannot substantiate output power in our band. Current commercial
obtainability, exact mass, oscillator implementation/configuration, and
condition-specific current/RF limits still require evidence review.

Decision: **CANDIDATE / EVIDENCE INCOMPLETE, not a replacement selection**.
Do not silently transfer its ppm value or circuit to Ebyte. Next engineering
action is to examine its schematic and official example/settings alongside
current manufacturer product evidence, then compare against Ebyte and a
crystal-based documented alternative. If neither module meets required
properties, a custom RF board using a fully documented transceiver/reference
design is a trade candidate, not a released custom part by declaration.
