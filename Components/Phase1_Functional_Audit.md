# D1-CMP-AUD-002 — Phase 1 functional component audit

Revision A · 2026-09-15  
Governing rule: `review/Phase1_Component_Evidence_Standard.md`

## Audit conclusion

The current documented spacecraft does **not** yet have a complete, publicly
fact-checkable component set. **No component is admitted to the Phase 1 baseline
by this audit.** Eight named COTS products remain the recommended candidate set,
and all are
`CANDIDATE / EVIDENCE INCOMPLETE` until a property-by-property applicability
matrix proves that every mission-relevant value is present in primary public
documentation. Five integration functions are unreleased custom designs or
allowances. The ground station is also incomplete.

This is an evidence finding, not a conclusion that the components will fail. It
means a claim that the spacecraft is presently functional would depend on
undocumented assumptions.

## Recommended Phase 1 candidate set

| Function | Candidate | Disposition | Reason |
|---|---|---|---|
| Structure | ISISPACE 1U, SKU 100000 | CANDIDATE / EVIDENCE INCOMPLETE | Current order route, but no public controlled mechanical package or mass |
| EPS/battery | ISISPACE ICEPS2 Type A | CANDIDATE / EVIDENCE INCOMPLETE | Strong public electrical data, but current capacity/configuration contradiction and missing installed thermal properties |
| Solar panels | ISISPACE customizable 1U family | CANDIDATE / EVIDENCE INCOMPLETE | Family is current; exact six-face configurations and IV/mechanical evidence are absent; Pumpkin C03 is an incomplete and currently unavailable alternative |
| OBC | GomSpace NanoMind A3200 | CANDIDATE / EVIDENCE INCOMPLETE | Good public data for preliminary work; exact delivery/software/fault evidence remains |
| Carrier | GomSpace NanoDock DMC-3 | CANDIDATE / EVIDENCE INCOMPLETE | Current order page plus datasheet, 2025 option sheet and qualification certificate; exact ordered configuration and certificate applicability must be established |
| Radio | GomSpace NanoCom AX100-U part 200315, Mode 5 | CANDIDATE / EVIDENCE INCOMPLETE | Current product, public datasheet and lifecycle PCN; exact firmware/manual, acceptance evidence and authorized frequency remain unresolved |
| Antenna | ISISPACE 1U–3U Turnstile, 5 V | CANDIDATE / EVIDENCE INCOMPLETE | Public family values exist; tuned configuration, commands, pattern and deployed geometry are not public |
| Camera | **SkyFox piCAM/FM** | **CANDIDATE / EVIDENCE INCOMPLETE** | Exact part, current €4,950 price/lead time and unusually complete 2025 datasheet; radiation, exact optical acceptance data and delivered-unit environmental evidence remain unresolved |
| Custom integration | D1-IF, harness, thermal interface, bracket/baffle and fasteners | CUSTOM COMPONENT REQUIRED / DESIGN INCOMPLETE | These are not purchasable components until detailed design creates constituent part numbers |

The property matrix also audits two Pumpkin alternatives. They do not replace
the recommended structure or panel candidates: the current selectable store
entries are marked unavailable, and mission-critical configuration data remain
missing.

The complete downstream physical proposal is now enumerated in
`Components/Proposed_Operating_Component_Set.md` and its generated CSV/cards.
That list covers all flight and ground hardware needed by the current concept;
it does not change any gate result in this audit.

## Changes from the previous audit

1. **Camera recommendation changed.** CrystalSpace CS-101 remains a real current
   product but public evidence gives only size, mass and pixel count. Power,
   supply, protocol, pinout, thermal limits and optics are critical and absent.
   SkyFox piCAM/FM supplies these publicly and directly matches the modest mission.
2. **DMC-3 availability finding corrected.** A current GomSpace product page was
   located. It links DS 1012962 rev 1.12, a 2025 option sheet and qualification
   certificate. B08 is a current quote-route candidate, not an unconfirmed legacy
   part.
3. **B12 is withdrawn as a component.** It is a mass/cost allowance with no
   manufacturer, material, part or geometry. It cannot supply thermal properties.
4. **The earlier 16-line audit was procurement-oriented rather than functional.**
   This audit adds the missing functional coverage test and shows that ground
   station and integration hardware are incomplete.

## Alternatives rejected during this pass

| Candidate | Result | Evidence reason |
|---|---|---|
| GomSpace NanoCam C1U | UNSUITABLE | Manufacturer product page states phased out/no longer available despite good documentation |
| CrystalSpace CS-101 | UNSUITABLE while piCAM/FM exists | Critical electrical, protocol, thermal and optical configuration data are not publicly available |
| GomSpace NanoPower P31u | UNSUITABLE | Manufacturer EOL notice made discontinuation effective 2025-10-01 |
| ISISPACE iOBC | UNSUITABLE as current reference | Storefront says out of stock; public technical brochure is old and supply tolerance is incomplete |
| EnduroSat current OBC/UHF/EPS | UNSUITABLE for this minimum-cost 1U baseline | Current OBC is 123 g/12 V, UHF radio 195 g with 1.2 W receive power, CubeSat EPS is USD 62k–75k, and current catalog no longer presents a 1U structure/panel line |
| ISISPACE TRXVU | CANDIDATE / EVIDENCE INCOMPLETE ALTERNATE only | Current storefront exists, but the detailed public brochure is legacy and exact current configuration/manual is not public |
| Pumpkin CubeSat Kit Rev D 1U skeletonized structure set | CANDIDATE / EVIDENCE INCOMPLETE ALTERNATE | Exact public assembly part numbers and CAD exist, but current selectable parts are marked unavailable; exact set mass, switch/end-plate configuration and qualification evidence are incomplete |
| Pumpkin fixed 1U solar-panel family | CANDIDATE / EVIDENCE INCOMPLETE ALTERNATE | Current family page gives thickness, price range and acceptance claims, but the selector is unavailable and exact configurations, mass, IV data, interfaces and environment limits are absent |

## Explicit evidence gaps and blocked analyses

- **ICEPS2 capacity/configuration:** 22.5 Wh current page versus 28.8 Wh in its
  linked issue 1.2 datasheet. This blocks a fact-based energy/life conclusion.
- **Thermal properties:** no selected thermal-interface hardware, installed
  conductance or component heat-capacity evidence. This blocks component-specific
  thermal prediction. TMI-001 applies.
- **Solar panels:** exact hot/cold/EOL IV curves and six mechanical layouts are
  absent. This blocks attitude/orbit power closure and camera-aperture feasibility.
- **3.3 V distribution:** public ICEPS2 output range and A3200/AX100/piCAM limits
  do not establish a safe integrated transient envelope. The unreleased D1-IF
  cannot close it. This blocks harness and fault-containment release.
- **Structure and deployment:** exact switch hardware, rails, fasteners and
  component-to-structure interfaces are absent. This blocks structural analysis.
- **Ground station:** the antenna alone is selected. End-to-end RF function is not
  established.

## Cost effect supported by public prices

Replacing the previous €6,000 base allowance for CS-101 with the listed
`piCAM/FM` price of €4,950 reduces the provisional flight-camera line by €1,050.
The €2,190 engineering model and €325 evaluation kit are separate development
costs and are not flight substitutes. No other quote-only component cost is
rebased. No hardware has been ordered.

## Required next engineering work

The next credible step is a **property-by-property evidence applicability matrix**
The property-by-property matrix is now established for the eight recommended
COTS candidates and two audited alternatives. Each row cites a document and
location or states `UNKNOWN`, then identifies the analysis prevented. Only a
candidate with no mission-relevant unknown may be proposed for the Phase 1
baseline. The next work is to close public evidence gaps where possible and
complete exact project configurations for configurable parts without ordering.
