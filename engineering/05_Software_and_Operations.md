# D1-SW-001 — Flight software and operations specification

Revision A | Software requirements; not executable flight code.

## Runtime architecture

Use the vendor-supported A3200 BSP/RTOS and tested CSP library version. Obtain commercial software license/support terms in the hardware RFQ. Avoid Linux, SD-card root filesystems and unnecessary networking services. Separate time-critical health/recovery tasks from camera capture/compression. Use bounded allocation, queue sizes and CPU time. Camera, radio or I2C timeout cannot block a system-health task.

Boot ROM/internal boot path validates a protected known-good image and a candidate image. Stage updates atomically, verify integrity/authenticity, limit boot attempts and roll back. Confirm that the physical memory map and vendor bootloader support this architecture; it is not assumed from NOR capacity alone. Store configuration in CRC-protected redundant records with monotonic generation counters. Critical RF-disable and mission-end flags survive reset. Memory scrubbing/checksums detect corruption, but no claim of hardware ECC is made.

Allocate watchdog servicing from a health aggregator that requires progress from all critical tasks. Initial timing targets: health sample 10 s, scheduler 1 s, watchdog heartbeat 5 s and external recovery timeout <=60 s; confirm supported EPS/OBC ranges. After three consecutive unsuccessful boots enter the minimal recovery image. EPS supervisor must restore an unresponsive OBC autonomously without depending on the OBC command bus.

## State transitions

| State | Entry / allowed activity | Exit |
|---|---|---|
| INHIBITED | Ground/launch configuration; hazards physically isolated | Valid all-switch separation |
| DELAY | OBC health only; camera and RF off | Valid elapsed release/RF timing |
| DEPLOY | Sufficient battery energy, permitted temperature; bounded release sequence | Telemetry confirms release or retries exhausted |
| COMMISSION | Low duty beacon and command acquisition; no images until authorized and stable | Health and link checkout approved |
| NOMINAL | Duty-budgeted health, image bursts, selective file transfer | Energy/thermal/link fault or end of mission |
| RECOVERY | Camera off; RX 12 s/min; TX <=0.5%; minimal OBC | Sustained energy surplus and thermal conditions |
| RF SILENT | Persistent command or license condition | Authorized explicit release, unless mission end |
| PASSIVATED | Mission end; suppress images/RF; safe energy management | No routine return to service |

Initial SOC thresholds (A): enter recovery below 50%, resume nominal above 70% after two positive-energy orbits, block imaging below 75%, and reserve vendor-safe voltage floor regardless of estimated SOC. Low voltage, temperature or abnormal current can independently force recovery. Validate thresholds with real battery curves and monitor sensor failures. If SOC is invalid, default to the conservative voltage/temperature recovery policy. No setpoint may override battery protection.

## Command and telemetry

Commands: request health; set allowed operating mode; disable RF; request thumbnail/file segment; adjust bounded camera exposure; update approved schedule; reset camera/radio; upload staged firmware; initiate approved passivation. Hazardous commands require authenticated authorization, replay protection and two-step arm/execute with timeout. Design the link/security format around the selected license. Authentication does not imply permission to encrypt traffic in an amateur service.

Each telemetry record contains protocol version, spacecraft ID, sequence, reset counter, timestamp/time validity, mode, battery/solar/rail values, temperatures, deployment status and fault flags. Packets have integrity checks and bounded lengths. Image transfers use image ID, segment index, total segments, per-segment CRC and final file hash; retransmit missing segments only. Retain health packets at highest priority.

AX100 framing is Mode 5 per S11. Confirm supported forward-error options and ground firmware; no legacy AX.25/Viterbi dependency is permitted. Have an independent RF watchdog or EPS-timed radio cutoff to bound unintended TX; verify available hardware behavior. If unavailable, log as a failure-mode gap rather than relying on the main task scheduler.

## Ground segment

Cost baseline: one AX100 ground modem to match flight framing, a suitable carrier/EGSE interface, PC, M2 436CP42UG circular antenna, azimuth/elevation rotator/controller, low-loss coax, bandpass/filtering and surge/weather protection [S28,S29]. The antenna is large (about 5.7 m boom); verify site and mount feasibility. Budget 16 dBi installed antenna gain and <=1 dB receive feed loss, using near-antenna modem placement or an appropriate calibrated front end. Do not assume long unamplified coax meets that loss.

Use 1 W ground RF power only if authorized EIRP, emission and site limits permit. 30 dBm +16 dBi -1 dB feed is a 45 dBm EIRP planning value, not an authorization. Ground model quotes must include two-way operation and the exact Mode 5 waveform. A second ground modem can serve as a development asset; do not count the same radio twice in procurement.

Daily workflow: refresh orbital elements; evaluate pass geometry; check hardware/time synchronization; predict Doppler; receive health before commanding; obey energy flags; request high-priority images; archive raw packets and metadata; reconcile SOC/thermal/reset trends; review conjunction notices. No commanding based solely on unattended image-processing output. Design for remote shutdown and keep an offline command-key backup.

LEOP reserves multiple days for acquisition and catalog identification. Use deployer separation predictions and transmitted unique ID; do not rely on a definitive public orbital element set immediately after launch. Partner ground sites are options subject to agreements and spectrum authority; crowdsourced reception is not guaranteed coverage.

At day 365, confirm mission success evidence then execute authorized end-of-mission operations. Passivation requires supplier-confirmed control of charge sources and stored battery energy; merely turning the OBC off is not passivation. Any residual autonomous recharging or reboot beacon path must be eliminated or explicitly covered in the debris/safety assessment.
