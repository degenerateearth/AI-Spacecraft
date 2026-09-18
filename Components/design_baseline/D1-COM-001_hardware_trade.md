# D1-COM-TRD-002 — onboard radio hardware evidence trade

Revision A · 2026-09-18 · INCOMPLETE TRADE / NO REPLACEMENT SELECTED

Scope is the spacecraft radio and its physical interfaces. Ground systems and
host image-transport development are paused by owner instruction. No new module
has been purchased, tested, qualified or admitted to the complete Phase 1 baseline.

## Current hardware correction

D1-BPB-001 previously allocated RADIO_TXEN at connector pin 45 while D1-COM-001
used local module DIO2 to drive TXEN. The records allowed conflicting interpretations.
Revision B reserves carrier pin 45 as NC. Module pins 7/8 share only the local
switch-control net. D1-COM-001_pinmap.json covers all 22 module and 50 connector
pins. It is intended connectivity, not a released schematic: isolation devices,
default-state networks and exact MCU pins remain required. No direct connection
is thereby approved between powered OBC signals and an unpowered radio.

## Alternative screening

| Candidate | Evidence gained | Remaining selection blocker |
|---|---|---|
| Ebyte E22-400M22S | Full module pin/outline record; corrected current claims; locally archived manufacturer demo | Module-specific TCXO voltage/delay/accuracy and worst-case current evidence still unresolved; generic demo does not close them |
| Dorji DRF1268T | Visually inspected schematic on PDF p4: oscillator is supplied from DIO3; DIO2 and SW control RF switch | Oscillator is only identified as 32 MHz in drawing, with no exact oscillator model or supply rating; schematic is not sufficient to choose DIO3 voltage. Previously recorded power-condition conflict remains |
| HopeRF RFM98W-433S2 | Exact order code on manufacturer V2 p122; register documentation; crystal-based architecture avoids an externally programmed TCXO supply | p110 specifies crystal-selection considerations rather than actual fitted crystal frequency-error bounds; p13 TX/RX currents are typical; exact module mass and controlled thermal/RF bounds remain unverified |

Do not infer that a schematic reveals the ratings of an unnamed oscillator.
The HopeRF part is a candidate to investigate, not an interchangeable replacement:
it changes footprint, register interface, power, temperature constraints and RF
performance. Its datasheet p80 limits +20 dBm transmission to 1% duty cycle and
3:1 antenna VSWR. That restriction cannot be omitted from any eventual hardware
selection. Its p12 operating-temperature table and p80 prose use different ranges;
the narrower p12 table controls screening until resolved. p121 explicitly warns
that its reference schematics may omit required components. Therefore a nominal
reference circuit cannot be treated as a complete fabrication BOM.

## Physical design closure still required

1. Exact oscillator evidence or better documented module/discrete-reference design.
2. Defensible normal and fault current envelopes for EPS protection; typical
   consumption must not masquerade as a guaranteed maximum.
3. Exact back-power isolation, reset/pull network and decoupling parts.
4. RF matching/launch/filter and selected coax connector drawing.
5. Released carrier schematic/PCB with placement/keep-outs and mounting interface.
6. Assembly mass/materials and property evidence for later thermal/structural work.

No thermal simulation or integrated link calculation was performed. Source
provenance is retained in the radio follow-up and alternative JSON manifests.
The new pin map resolves one interface contradiction; it does not close these
remaining release items or establish that the spacecraft is buildable.
