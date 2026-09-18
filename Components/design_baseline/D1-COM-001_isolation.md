# D1-COM-ISO-001 — radio digital power-domain isolation

Revision A · 2026-09-18 · PROPOSED CUSTOM SUBCIRCUIT

## Purpose and status

Replace undefined direct digital connections between the always-powered OBC
and switchable Ebyte module with an explicit eight-channel isolation design.
This is a spacecraft carrier circuit, not ground hardware. Exact parts below
are selected for detailed circuit work; the subcircuit is not yet fabrication
released, electrically proven or admitted as a completely verified Phase 1 item.

## Exact constituent BOM

| References | Qty | Manufacturer / part | Function and evidence |
|---|---:|---|---|
| U1,U2 | 2 | TI SN74AXC4T774PWR | 4 independent-direction channels per device, PW 16-pin TSSOP; SCES898C p3 pinout, p5–6 electrical limits, p20–22 isolation/control |
| C1–C4 | 4 | KEMET C0603C104K5RACTU | 100 nF nominal, 10%, 50 V X7R, one capacitor at each IC supply pin; exact manufacturer specification archived |
| R1,R2 | 2 | Yageo RC0603FR-074K7L | 4.7 kohm 1%; one OE pull-up per IC; connected in parallel on common control |
| R3–R10 | 8 | Same Yageo part | Module-side defaults: NSS high to RF rail; remaining seven signal nets low to ground |

TI lists the orderable active. Distributor snapshot on 2026-09-18 displayed
4,078 units and USD 1.39 single-unit cut-tape price: two ICs cost USD 2.78 before
shipping/tax; this is not total carrier cost or a purchase. Recheck on procurement.
Order routes:
- https://www.ti.com/product/SN74AXC4T774/part-details/SN74AXC4T774PWR
- https://www.digikey.com/en/products/detail/texas-instruments/SN74AXC4T774PWR/10715472
- https://www.digikey.com/en/products/detail/yageo/RC0603FR-074K7L/730159
- https://www.digikey.com/en/products/detail/kemet/C0603C104K5RACTU/1465623

Supplier URLs, document hashes and retrieval date are in the isolation source
manifest. No guessed device mass is added to the spacecraft budget. IC/resistor
mass remains open; capacitor typical mass is not a guaranteed assembly mass.

## Electrical connections

Canonical editable source: `D1-COM-001_isolation_netlist.json`.
Both ICs: pin 16 VCCA=+3V3_A; pin 15 VCCB=+3V3_RF; pin 10=GND;
pin 9 OE=ISO_OE_N from J2.17. Both rails must stay within 0.65–3.6 V
for specified operation; nominal equal 3.3 V rails are a project decision.
Pin 45 is still NC; DIO2/TXEN is local and is not an isolation channel.

| IC/channel | A pin / B pin / DIR pin | Signal | Direction strap |
|---|---|---|---|
| U1/1 | 3 / 14 / 1 | SCK | DIR to VCCA, host to radio |
| U1/2 | 4 / 13 / 2 | MOSI | DIR to VCCA, host to radio |
| U1/3 | 5 / 12 / 7 | MISO | DIR to GND, radio to host |
| U1/4 | 6 / 11 / 8 | NSS | DIR to VCCA, host to radio |
| U2/1 | 3 / 14 / 1 | NRST | DIR to VCCA, host to radio |
| U2/2 | 4 / 13 / 2 | RXEN | DIR to VCCA, host to radio |
| U2/3 | 5 / 12 / 7 | BUSY | DIR to GND, radio to host |
| U2/4 | 6 / 11 / 8 | DIO1 | DIR to GND, radio to host |

TI p21 cautions against external data pull-ups greater than 7 kohm because
data I/Os have weak internal pull-downs. The 4.7 kohm choice follows that
guidance but does not by itself prove module output-drive compatibility.

## Source-backed limits and bounded consequences

- TI p6 specifies power-off data leakage up to 4 microamp per pin over
  -40 to +85 C, and 8 microamp over -40 to +125 C, at the stated test conditions.
  High impedance does not mean zero leakage or galvanic isolation.
- TI p20 specifies automatic isolation below 100 mV on either supply. It
  does not justify ignoring a slowly decaying/floating rail or a 0.1–0.65 V
  intermediate region. OE must be high during intentional rail transitions.
- Two ICs' combined static supply-current maxima sum to 80 microamp over
  the full IC temperature range (40 each; p6, no output load). This excludes
  dynamic switching, pull resistors, capacitor charging and radio current.
- PW outline p40: 4.9–5.1 by 4.3–4.5 mm body, 6.2–6.6 mm lead span,
  1.2 mm maximum height, 0.65 mm pitch; flash allowances and courtyard still
  apply. No placement or spacecraft fit conclusion follows.
- TI p14 gives up to 5 ns data propagation at both supplies 3.3 +/-0.3 V
  under its test loads. This does not establish permissible end-to-end SPI
  speed; return-path delay, OBC sampling and module timing must be reconciled.

## Startup/shutdown design requirements

1. Reset/high-impedance OBC control leaves OE pulled high. The two 4.7 kohm
   pullups present a nominal 2.35 kohm load when OBC actively drives OE low.
2. Keep OE high while enabling RF power. Initialize host NSS high, reset low,
   SCK/MOSI/RXEN low before enabling the translators. No unspecified delay
   constant is substituted for the radio's reset/startup requirements.
3. Enable only after both rails and GPIO directions are valid. Release radio
   reset using the eventual documented timing sequence.
4. Disable OE before normal radio power-off. A fault may remove RF power
   without software cooperation; analyze this separately using IC isolation
   limits and the EPS rail-discharge network.
5. Reinitialize following brownout; do not treat isolated BUSY/DIO1 readings
   as real radio status. A hardware reset/inhibit scheme must also suppress
   unintended transmit behavior while firmware is not executing normally.

## Required checks before circuit release

Reconcile module and MCU VOH/VOL/VIH/VIL, 4.7 kohm output loads and IC input
edge-rate requirements (10 ns/V); establish supply tolerances/overshoot and
OE rise/fall behavior. Model all leakage paths including limiter, translator
and module to size discharge hardware; no discharge part is silently assumed.
Freeze decoupling effective capacitance/placement, schematic ERC, layout and
SPI timing. Determine device mass/materials and radiation/environmental risk.
Do not use catalog junction-to-ambient thermal resistance as a vacuum model.

Verification later: measure unpowered-rail voltage and individual injection
currents with host inputs high/low, either supply absent, transitions and resets;
capture OE/SPI/NRST waveforms; test all channel directions and recovery. Numeric
system acceptance limits remain pending electrical closure. No physical test
or flight suitability is claimed by this circuit definition.
