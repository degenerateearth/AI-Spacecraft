# C01 — SkyFox Labs piCAM/FM flight camera candidate

Audit date: 2026-09-15  
Phase 1 state: **CANDIDATE / EVIDENCE INCOMPLETE**  
Baseline state: **not selected; no BOM/CAD change authorized by this audit**

## Identification and order route

| Field | Public manufacturer value |
|---|---|
| Manufacturer | SkyFox Labs s.r.o. |
| Exact variant | `piCAM/FM` (Flight Model) |
| Product/order URL | https://www.skyfoxlabs.com/product/27-picam |
| Published quantity-one price | €4,950 |
| Published lead time | 2–4 weeks plus shipping |
| Country | Czech Republic |
| Export note | Vendor marks product dual use; actual export path remains to confirm |

## Verified public properties

| Property | Value | Primary evidence |
|---|---|---|
| Body | 33 × 33 × 19 mm plus optics | S49 pp2,4 |
| Mounting | 48 × 33 mm bracket; four M2.5 holes; STEP available | S49 pp2,4 |
| Mass | 40 g, lens dependent | S48/S49 p2 |
| Supply | 2.7–3.6 V; 3.3 V nominal | S49 p3 |
| Operating current | 95 mA in datasheet; product page says 90 mA | S48/S49 p3; discrepancy retained |
| Data | 3.3 V CMOS UART, 1.2–921.6 kbit/s | S49 pp2–10 |
| Product | 640 × 480 RGB JPEG, ASCII-hex framed | S49 pp2–10 |
| Command | Public one-byte command and output protocol | S49 pp6–10 |
| Default optics | Approximately 60° diagonal, IR cut, infinity focus | S49 pp2,10 |
| Temperature | Datasheet ratings list operating −30 to +85°C and storage −40 to +85°C | S49 p3 |
| Aperture guidance | 1 mm gap on all sides; no direct optics/wall contact | S49 p13 |
| Radiation limitation | COTS construction, no radiation-hardened ICs; external latchup current limiter recommended | S49 pp13–14 |

## Evidence gaps that prevent baseline selection

- The application note calls the operating range −40 to +85°C while the ratings
  table says −30 to +85°C. The controlling operating limit is unresolved.
- The public 95 mA value is not labeled minimum/typical/maximum clearly enough to
  establish peak and startup current over temperature.
- Exact selected lens envelope, mass, distortion, MTF, exposure limits and
  acceptance data are absent.
- No public configuration-specific vibration/TVAC acceptance report or reliability
  basis establishes this delivered variant for a 12-month mission.
- The vendor explicitly states that radiation-hardened ICs are not used. Part-level
  data needed for a mission radiation analysis are not public.
- The required external latchup limiter and switched 3.3 V interface do not yet
  exist as a released component/design.

Therefore piCAM/FM is a stronger candidate than CS-101 but cannot enter the Phase
1 baseline under D1-CMP-STD-001. The missing properties remain UNKNOWN; none are
replaced by generic camera values.

## Local evidence custody

The exact manufacturer PDF was retrieved locally and hashed in
`SOURCES/components/LOCAL_ARCHIVE_MANIFEST.csv`. The PDF is excluded from the
public repository because no redistribution license was established. The `.url`
file identifies the authoritative copy.
