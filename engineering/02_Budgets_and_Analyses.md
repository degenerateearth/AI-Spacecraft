# D1-ANA-001 — Budgets and analytic screening

Revision A | All numbers below are preliminary; inputs are explicitly editable.

## Mass and volume

The BOM sums to 1063.5 g (C). Uniform 20% growth gives 1276.2 g. A conservative project mass ceiling of 1330 g leaves 53.8 g after growth. This is a project target, not a statement that all modern 1U dispensers impose 1330 g. The selected deployer sets the final limit [S01].

The 300 g panel allocation includes six panels. AntS uses a conservative 90 g allocation, not a legacy 18 g figure. EPS mass includes its battery. Harness, thermal materials and adapter have separate allowances. The camera and its bracket are included. No extra battery, deployer, ballast or ground equipment is hidden in the mass total. Mass must be measured after each integration step and reconciled against the assembly BOM.

Internal Z allocation, centered coordinates in mm: camera bay -49 to -22, with lens along +X; adapter -21 to -15; EPS/battery -12 to +14.5; carrier and its two top-side modules +20 to +36; upper service clearance +36 to +44; AntS +44 to +51; top panel provision +51 to +54. Approximate outside rail span is 100 x 100 x 113.5 mm. These intervals leave internal clearance but do not establish X/Y fit, fastener access, connector bend radii or actual mating heights. The vendor CAD and dispenser drawing are mandatory before release.

With EPS at z=+1.25, avionics at z=+28, AntS at z=+47.5, adapter at z=-18 and the 70 g camera/bracket at z=-35.5, the illustrative center of mass is z=+3.8 mm when other masses are symmetric. A camera center at x=+25 mm shifts total x center of mass approximately +1.65 mm. This is not a verified mass-properties result. Require measured center of mass within a project target of +/-10 mm on all axes. Record measured inertia for separation and RF/thermal attitude modeling.

## Orbit and eclipse

Two-body circular period: `T=2*pi*sqrt((Re+h)^3/mu)`. Zero-beta maximum cylindrical-shadow duration: `Te=T/pi*asin(Re/(Re+h))`. At 475 km this gives T=94.101 min, eclipse=35.833 min, sunlight=58.268 min, approximately 5589 orbits/year. Penumbra, oblateness, beta evolution and altitude decay are omitted. Adopt 38 min for environmental test eclipse segments to cover analysis uncertainty; re-evaluate at the minimum mission altitude.

## Solar generation

For equal panels on all six orthogonal faces, geometric power is `Pface*(abs(sx)+abs(sy)+abs(sz))`. For a unit Sun vector the sum ranges from 1 to sqrt(3); an isotropic attitude average is 1.5. This proves a geometric lower bound only for intact, equally capable, unobstructed faces. One failed face destroys that bound. No isotropic tumble guarantee is assumed for survival. With five 2.3 W faces and a 1.8 W camera face, the isotropic mean is (5*2.3+1.8)/4=3.325 W BOL, and the geometric minimum is 1.8 W. These replace the equal-face geometry in the released model.

Apply separate allocations: end-of-life factor 0.85; temperature factor 0.90; shadow/assembly factor 0.90; MPPT/harness efficiency 0.90. Thus EOL power during sunlight is 1.115 W for the camera-face lower bound and 2.060 W for the unequal-face isotropic mean. These factors require radiation/thermal/IV verification. Albedo generation is ignored. Distribution efficiency is separately 0.85, including the adapter, and battery charging efficiency is 0.90. Efficiencies are not measured vendor claims.

## Load allocation at delivered load rails

| Load | Nominal allocation | Recovery allocation | Evidence |
|---|---:|---:|---|
| OBC | 0.18 W | 0.08 W | A; clock/sleep schedule to demonstrate |
| EPS housekeeping/internal overhead | 0.14 W | 0.12 W | A; includes published 93 mW PDU idle, not just that figure |
| Interfaces/carrier/sensors | 0.03 W | 0.02 W | A; USB off |
| Radio RX | 0.20 W continuous | 0.396 W for 20% of time | A nominal; recovery budgets datasheet max current |
| Radio TX | 3.3 W for 2% of orbit | 3.3 W for 0.5% | S10 maximum temperature current used; replace RX while TX nominally |
| Camera | 0.02 W average, 2 W peak | OFF | A; capped daily powered time |
| Heater | 0.10 W average | 0.10 W average | A; 1 W at 10% duty equivalent |

Add 20% load growth. Nominal total=0.8784 W. Recovery total=0.49884 W; recovery calculation conservatively adds TX energy without subtracting RX overlap. The onboard heater may have different instantaneous wattage: the 1 W value is an allocation requiring configuration or modulation confirmation.

Energy accounting: `Erequired = Pload/eta_distribution * (Tsun + Teclipse/eta_charge)/3600`. This handles eclipse recharge explicitly. Nominal required solar energy is 1.689 Wh/orbit versus 2.001 Wh available: +0.312 Wh, or +18.4% of required energy. Fixed-attitude nominal deficit is 0.606 Wh/orbit. Recovery needs 0.959 Wh versus 1.083 Wh available: +0.124 Wh. This separation is essential: six faces do not justify permanent full-power operation.

Recovery RX duty is 12 s per minute; the radio must wake and receive within the allocated window. Ground commands repeat across at least one full window cycle. Firmware transitions to recovery when generation and state-of-charge trends are inadequate, regardless of perceived attitude. Nominal heating can average at most about 0.235 W before consuming all model energy reserve. Preserve growth reserve in operations rather than deliberately operating at that bound. The sensitivity CSV includes poor generation and high heater cases, some of which fail. A thermal solution demanding sustained high heater power requires redesign.

Peak bus load allocation: OBC 0.9 W, radio 3.3 W, EPS/interface 0.17 W and heater 1 W, with 20% growth, gives 6.444 W delivered. At 85% conversion this is 7.58 W battery-side, approximately 1.26 A at 6 V. Verify actual per-channel current limits, wiring drops, transients and startup. Do not deploy the antenna while transmitting; a separate 2 W deployment allocation applies.

## Battery and lifetime

Use 22.5 Wh BOL, derated to 18 Wh at EOL (80%, A). A routine 20% depth-of-discharge design limit permits 3.6 Wh. Routine eclipse discharge is approximately 0.617 Wh, or 3.43% EOL DOD. A stress eclipse with 120 s TX and continuous 1 W heating, with imaging disabled uses 1.453 Wh, or 8.07%. Neither calculation proves a calendar or cycle lifetime. Require evidence for at least 6000 shallow cycles plus ground storage at actual temperature, charge voltage and current.

Voltage cannot be treated as a precise SOC measurement under load. Use calibrated coulomb counting with voltage/temperature correction; trend errors and periodically reconcile during appropriate rest conditions. Reserve energy for antenna release and initial acquisition; do not spend the full DOD allowance in routine operations.

## Radio link

Planning carrier 437 MHz is a calculation placeholder, not a frequency assignment. Use 1200 bit/s Mode 5/Golay framing; no coding gain is credited. Current AX100 deliveries support only Mode 5 per S11. The receiver threshold of -123 dBm is a procurement/bench-test requirement for the complete modem at packet error rate <=1% with the selected packet length and configuration, not the -137 dBm/100 bit/s marketing figure.

At 10 degrees elevation, circular geometry gives 1633.16 km slant range. `FSPL=32.44+20log10(f_MHz)+20log10(d_km)=149.51 dB`.

| Term | Downlink | Uplink |
|---|---:|---:|
| Transmitter at connector | 29 dBm | 30 dBm |
| Ground antenna gain | +16 dBi | +16 dBi |
| Space antenna reference gain | 0 dBi | 0 dBi |
| Space feed loss | -1 dB | -1 dB |
| Ground feed loss | -1 dB | -1 dB |
| Propagation allowance | -1 dB | -1 dB |
| Polarization allowance | -3 dB | -3 dB |
| Tumble/pattern allowance | -6 dB | -6 dB |
| Free-space loss | -149.51 dB | -149.51 dB |
| Received power | -116.51 dBm | -115.51 dBm |
| Margin over -123 dBm threshold | 6.49 dB | 7.49 dB |

The 6 dB fade allowance does not bound turnstile nulls. Packet repetition, pass diversity and measured full-sphere antenna coverage are required. If measured threshold is only -120 dBm, downlink margin falls to 3.49 dB. Additional losses may require a higher elevation mask or reduced data rate. Maximum orbital-speed Doppler estimate is +/-11.1 kHz; tune with predicted Doppler and acquire residual clock drift, rather than relying solely on radio AFC.

64 bytes/min generates 92,160 bytes/day before framing. At 1200 bit/s and a conservative 50% net efficiency, 1229 s/day are needed. The 2% orbit-average TX allowance gives 1728 s/day, but contacts must supply the necessary visibility. Four 6-minute passes provide only 1440 s before fades and acquisition; they are an illustrative scenario, not a computed schedule. Store at least 30 days of health telemetry, downsample in recovery to a summary every 10 minutes, and never increase duty merely to empty a backlog. Exact contact coverage awaits the ground location and orbit.
