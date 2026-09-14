# D1-RAM-001 — Preliminary functional FMEA

Qualitative screening; no unsupported failure rates or numeric mission reliability are assigned. Systematic/common-cause faults and critical single-string elements remain. This is the starting point for the detailed hardware FMECA and launch hazard fault trees.

| ID | Failure | Effect | Mitigation | Residual / verification |
|---|---|---|---|---|
| F01 | Battery internal failure | Loss of mission; launch hazard | Pack protection/retention; supplier safety pedigree | Single pack remains a single point; T08/T12 |
| F02 | EPS or regulator destructive SEE | Loss of command/power | Part evidence, limiting, independent reset paths | Watchdog cannot repair damage; T16 |
| F03 | Adapter overvoltage/feedback fault | Avionics damage | Protected/guaranteed supply interface required | Unclosed topology blocks release; T03 |
| F04 | OBC hang or memory corruption | Lost commanding/unsafe schedule | External watchdog, recovery boot, CRC and bounded tasks | Same CPU remains critical; T15 |
| F05 | Camera hang/short/full buffer | Potential bus/power starvation | Separate switched supply, timeouts and storage partition | Image loss acceptable temporarily; T11/T15 |
| F06 | Insufficient solar due to fixed attitude | Battery depletion | Six faces, reduced recovery load, SOC trends | Aperture face minimum and heater assumptions critical; T06/T07 |
| F07 | One panel open or short | Loss of geometric energy guarantee | Axis blocking, branch protection, reduced duty | Year mission not guaranteed after face loss; T06 |
| F08 | Heater stuck on/off or sensor wrong | Battery freeze/overheat/depletion | Independent thermal cutoff, validity checks and timeout | Actual EPS implementation open; T13/T15 |
| F09 | Antenna fails to release | No usable link or severe loss | Redundant release elements, bounded retries, thermal test | Common restraint/system remains critical; T14 |
| F10 | Inadvertent RF/release in dispenser | Launch/other spacecraft hazard | Independent physical inhibits, source-path analysis | Three switch count alone inadequate; T04/T05 |
| F11 | RF stuck transmitting | Energy loss/interference | Independent TX duration limit/power cutoff | Implementation must be shown; T09/T15 |
| F12 | Ground loss or key loss | No image return/commands | Recovery schedule, backups, alternate authorized station | No assured external station agreement; T17 |
| F13 | Fast spin or camera facing space | Unrecognizable images | Exposure selection, burst diversity, thumbnails | No active pointing; Monte Carlo closure O14 |
| F14 | Lens focus shift or contamination | Image mission loss | Qualified retention, cap closeout, optical tests | Camera qualification evidence required; T11/T18 |
| F15 | Excessive orbit lifetime/early decay | Disposal violation or <12 month life | Orbit selection under density uncertainties | No propulsion remedy in current BOM; O01 |
| F16 | Connector/joint loosening | Intermittent or permanent failure | Qualified locking, strain relief, flight assembly acceptance | Actual torque and preload drawing needed; T12 |
| F17 | Unauthorized command | RF/power/payload misuse | Authentication, replay prevention, bounded parameters | License-compatible security configuration; T15 |
| F18 | Post-mission charge/reboot persists | Stored energy and RF persist | Verified charge/source passivation and persistent flags | Supplier capability open; T17 |
