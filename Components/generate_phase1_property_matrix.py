"""Generate the Phase 1 component property evidence matrix from controlled rows."""
from __future__ import annotations
import csv
from pathlib import Path

OUT = Path(__file__).with_name("Phase1_Component_Property_Matrix.csv")

def row(component, prop, value, status, source, location, blocks="", note=""):
    return dict(component=component, property=prop, value=value, evidence_status=status,
                primary_source=source, source_location=location,
                analysis_or_decision_blocked=blocks, note=note)

R = []

def add(c, rows):
    for x in rows:
        R.append(row(c, *x))

add("ISISPACE 1U structure / SKU 100000", [
 ("commercial identity","ISISPACE 1-Unit CubeSat structure; storefront SKU 100000","VERIFIED","S06","current storefront","","Exact manufacturer sales/configuration code beyond reseller SKU is not shown"),
 ("orderability and price","EUR 3450; availability 4-6 weeks","VERIFIED_INDICATIVE","S06","current storefront","","Not a received quote or stock confirmation"),
 ("external/deployer envelope","UNKNOWN for the delivered structure","UNKNOWN","S06; S01; S33","storefront; external standards","Detailed deployer fit and rail compliance","Project envelope is not a manufacturer drawing"),
 ("internal envelope and mounting drawing","UNKNOWN","UNKNOWN","S06","checked current storefront","CAD placement; mounting; access; fasteners","No public controlled manufacturer drawing located"),
 ("mass","UNKNOWN","UNKNOWN","S06","checked current storefront","Mass margin and center of mass","Prior 150 g value is a project allocation"),
 ("material/rail finish/tolerances","UNKNOWN","UNKNOWN","S06","checked current storefront","Structural and wear/compliance analysis","Generic CubeSat/deployer rules cannot establish this product"),
 ("fasteners and torque","UNKNOWN","UNKNOWN","S06","checked current storefront","Load path and assembly release"),
 ("separation-switch accommodation","UNKNOWN exact option and geometry","UNKNOWN","S06","checked current storefront","Inhibit design and final CAD"),
 ("environmental qualification/acceptance","Flight heritage claim only; test evidence UNKNOWN","UNKNOWN","S06","checked current storefront","Launch survival claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("Pumpkin CubeSat Kit 1U skeletonized structure / Rev D component set", [
 ("commercial identity","Rev D set: base 710-00294, chassis walls 703-00289, cover 710-00296; AntS cover 710-00784 is a separate alternative","VERIFIED_SET","S53; S54","manufacturer CAD index and current store pages","Final end-plate/switch configuration","No single purchasable kit SKU for this exact set is exposed"),
 ("orderability and price","Current store lists component-family prices but marks the selectable products Unavailable","NOT_CURRENTLY_OBTAINABLE","S54; S55","current store pages","Phase 1 COTS identity and cost closure","A contact route is not evidence of commercial obtainability under the Phase 1 rule"),
 ("external/internal geometry","Public Rev D assembly CAD and 97 x 97 mm internal cross-section are identified","VERIFIED_PUBLIC_MODEL","S53; S54","CAD index; chassis page","Deployer-fit and internal-layout modeling","CAD license permits integration modeling but restricts manufacturing/RFQ use"),
 ("mass","Exact Rev D three-piece 1U set mass not established in the reviewed public pages; only historical complete-flight-model and relative values located","UNKNOWN","S54; S57","pages and manual checked","Mass budget and center of mass"),
 ("materials/finish","5052-H32 sheet; machined feet/spacers 6061-T6; stainless fasteners; launcher-contact rails hard anodized and remaining surfaces gold alodined","VERIFIED_FAMILY","S56","manufacturer FAQ","Exact part drawing/material callout acceptance remains"),
 ("fasteners/interfaces","Ten M3 x 5 mm stainless flathead screws for standard structure; current pages state four cover and six base screws","VERIFIED_FAMILY","S54; S56","structure and product pages","Torque/locking and exact assembly release","Torque and locking compound are not established"),
 ("separation-switch accommodation","Multiple exact cover/base alternatives are published, including dual-switch and AntS-compatible assemblies","PARTIAL","S53; S55","CAD index and store pages","Inhibit layout and exact spacecraft assembly","Project has not selected a compatible exact set"),
 ("operating/storage limits","Historical manufacturer manual states -40 to +85 C for parts destined for space; exact current Rev D structure acceptance limits not established","PARTIAL_LEGACY","S57","manufacturer user manual","Current configuration environmental basis"),
 ("qualification/acceptance","Store claims flight qualified/space proven; no configuration-specific public qualification or delivered-unit acceptance report located","UNKNOWN","S54; S55","current store pages checked","Launch survival claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("ISISPACE ICEPS2 Type A", [
 ("commercial identity","ICEPS2 Type A; exact sales/order code and option set UNKNOWN","PARTIAL","S02; S03","product page; datasheet cover","Configuration control"),
 ("orderability and price","Current quote route; public price UNKNOWN","PARTIAL","S02","current product page","Cost closure"),
 ("dimensions","96 x 92 x 26.45 mm","VERIFIED","S02","product specification",""),
 ("mass","184 +/- 5 g","VERIFIED","S02","product specification",""),
 ("battery energy/configuration","22.5 Wh on current page; 28.8 Wh, 2S1P, 7.2 V, 4 Ah in linked issue 1.2 datasheet","CONFLICT","S02; S03","page specification; datasheet battery table","Energy, life, peak-current and thermal analysis"),
 ("output domains","VD0 unregulated x1; VD1 5 V x4; VD2 3.3 V x4","VERIFIED_FAMILY","S02","product specification","Final interface","Exact delivered limits/revision still required"),
 ("output voltage/current and transients","Datasheet gives static channel tables; complete integrated transient envelope for Degen-1 is not established","PARTIAL","S03","electrical tables","OBC/radio/camera supply compatibility and D1-IF design"),
 ("connectors/pinout/protocol","Public datasheet gives interfaces; as-ordered pinout/manual and command protocol are incomplete publicly","PARTIAL","S03","interfaces; delivery contents","Harness and flight software release"),
 ("operating/charge/discharge/storage limits","Product range -20 to +70 C; issue 1.2 gives battery charge/discharge limits","PARTIAL","S02; S03","product page and temperature tables","Complete safety/life case","Exact configuration conflict remains"),
 ("battery cell identity/cycle/calendar life","UNKNOWN","UNKNOWN","S02; S03","documents checked","12-month energy retention and safety assurance"),
 ("installed thermal properties/heater topology","Heat capacity, installed conductance, sensor placement and exact heater/control configuration UNKNOWN","UNKNOWN","S02; S03","documents checked","Component-specific thermal prediction; TMI-001"),
 ("inhibit/RBF topology","Option families described; exact selected three-switch/RBF source-to-hazard topology UNKNOWN","UNKNOWN","S03","inhibit sections","Launch hazard independence and switch harness"),
 ("qualification and shipped-unit acceptance","Page lists QT/AT scope; vibration/shock and acceptance TVAC not shown","PARTIAL","S02","qualification table","Launch survival/acceptance claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("ISISPACE 1U customizable solar-panel family", [
 ("commercial identity","1U family; six exact face configurations/order codes UNKNOWN","UNKNOWN","S04","configuration selector","Configuration control"),
 ("orderability and price","Current quote route; public price UNKNOWN","PARTIAL","S04","current product page","Cost closure"),
 ("mass","50 g per 1U panel, configuration dependent","VERIFIED_FAMILY","S04","product specification","Exact mass rollup"),
 ("dimensions/mechanical drawing","Thickness 1.2-2.0 mm typical; exact planforms/apertures/mounting UNKNOWN","UNKNOWN","S04","product specification","CAD fit, camera aperture, AntS mounting"),
 ("cell technology/per-cell BOL","GaAs, 30%, approximately 1.23 W and 2.7 V per cell","VERIFIED_APPROXIMATE","S04","product specification","Guaranteed face power","Approximate catalog values are not configuration acceptance values"),
 ("hot/cold/EOL IV behavior","UNKNOWN curves and tolerances for selected layouts","UNKNOWN","S04","checked page","Orbit/attitude/temperature power closure"),
 ("harness/connectors","Custom flat inline Omnetics, Spec44 AWG26, harness included; exact pinout/length UNKNOWN","PARTIAL","S04","product specification","Harness release and voltage-drop analysis"),
 ("temperature/radiation","-40 to +80 C; manufacturer states 2 years minimum LEO","VERIFIED_CLAIM","S04","product specification","Orbit-specific degradation remains analysis/test work"),
 ("qualification/acceptance","Page lists QT functional/thermal/vibration/shock and AT functional/thermal cycling only","VERIFIED_SCOPE","S04","qualification table","As-delivered launch/TVAC acceptance strategy"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("Pumpkin CubeSat Kit fixed solar-panel family", [
 ("commercial identity","Fixed-panel family; exact 1U side/end configurations and order codes not exposed by the current selector","UNKNOWN","S58","current store page","Configuration control"),
 ("orderability and price","USD 2500-5650 family range; exact selections shown Unavailable","NOT_CURRENTLY_OBTAINABLE","S58","current store page","Phase 1 COTS identity and cost closure"),
 ("dimensions/mass/mounting","0.8 mm thickness and separate clip system documented; exact planforms, mass, hole pattern and clip allocation are UNKNOWN","PARTIAL","S58; S59","store pages","CAD fit and mass properties"),
 ("cell technology/electrical output","Triple-junction cells over 32% AM0 efficiency claimed; exact cell identity, stringing, BOL IV limits and tolerances UNKNOWN","UNKNOWN","S58","current store page","Orbit/attitude/temperature power closure"),
 ("hot/cold/EOL behavior","UNKNOWN for any selectable 1U configuration","UNKNOWN","S58","page checked","Twelve-month energy balance"),
 ("harness/connectors/pinout","UNKNOWN for any selectable 1U configuration","UNKNOWN","S58","page checked","Harness release and loss analysis"),
 ("operating/storage/radiation limits","UNKNOWN for the selectable fixed-panel configuration","UNKNOWN","S58","page checked","Thermal and degradation analysis"),
 ("qualification/acceptance","Page states vacuum bakeout and irradiance test for every panel plus family heritage; test limits and configuration-specific report are not public","PARTIAL","S58","current store page","Launch and acceptance claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("GomSpace NanoMind A3200", [
 ("commercial identity","NanoMind A3200; exact current sales code/revision UNKNOWN","PARTIAL","S07; S08","current page; datasheet","Configuration control"),
 ("orderability and price","Current quote route; public price UNKNOWN","PARTIAL","S07","current page","Cost closure"),
 ("dimensions/mass","65 x 40 x 7.1 mm and 24 g including shield in registered datasheet","VERIFIED_DOCUMENT","S08","mechanical/physical tables","Confirm delivered revision"),
 ("supply/power","3.2-3.4 V; documented current by clock/workload and extra loads","VERIFIED_DOCUMENT","S08","electrical tables","Integrated transient compatibility remains open"),
 ("connectors/pinout","Two 20-position FSI connectors and public pinout","VERIFIED_DOCUMENT","S08","connector sections","Exact carrier option mapping"),
 ("interfaces/protocols","I2C, UART, CAN, SPI, ADC; CSP/GOSH","VERIFIED","S07; S08","current page and datasheet",""),
 ("storage/processor/RTC/sensors","Public memory, processor, RTC, temperature, magnetometer and gyro descriptions","VERIFIED","S07; S08","feature tables","Gyro performance/range needed for imaging screen remains to confirm"),
 ("operating/storage limits","Operating limit documented; storage/survival and all component derating evidence incomplete","PARTIAL","S08","ratings tables","Thermal/survival and reliability analysis"),
 ("software/manual/errata","Commercial software packages noted; current BSP/API license, manual and errata not public","UNKNOWN","S07; S08","documents checked","Flight-software schedule and command/fault implementation"),
 ("radiation/qualification/life","Older public radiation claim exists; exact current hardware application and one-year reliability evidence incomplete","PARTIAL","S08","radiation/environment sections","Part-level radiation assurance and life claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("GomSpace NanoDock DMC-3 / part 200232", [
 ("commercial identity","NanoDock DMC-3; qualification certificate identifies product 200232","VERIFIED","S44; S47","current page; certificate p4",""),
 ("orderability and price","Current add-to-quote route; public price UNKNOWN","PARTIAL","S44","current page","Cost closure"),
 ("dimensions/mass","91.9 x 88.7 x 8.6 mm; 51 g without daughterboards","VERIFIED","S45","datasheet p4/p14",""),
 ("mounting/stack interfaces","PC/104 fit, mechanical drawing, FSI and stack connector identities/pinouts documented","VERIFIED","S45","datasheet pp6-15",""),
 ("power/data routing","CAN/I2C permanent; supply and connector populations configured by option sheet","VERIFIED_CONFIGURABLE","S45; S46","datasheet pp5-13; option sheet","Exact option selection"),
 ("operating limits","-40 to +85 C; board is passive in flight except USB circuit powered only from USB","VERIFIED","S45","datasheet pp4,14",""),
 ("environmental qualification","Certificate gives product 200232 sine/random/quasi-static/shock, TVAC, stress and heritage scope","VERIFIED_MANUFACTURER_CERTIFICATE","S47","certificate pp4-6","Launch tailoring/as-delivered acceptance remains later"),
 ("exact ordered configuration","Connector option, omitted bottom connectors, terminations and supply routing not yet selected","UNKNOWN_PROJECT_DECISION","S46","option sheet","Configuration control and harness release"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","exact configuration row","Admission to Phase 1 baseline")])

add("GomSpace NanoCom AX100-U / part 200315 Mode 5", [
 ("commercial identity","AX100-U sales part 200315; Mode 5 only per lifetime-extension PCN","VERIFIED","S09; S11","current page; PCN",""),
 ("orderability and price","Current add-to-quote route; public price UNKNOWN","PARTIAL","S09","current page","Cost closure"),
 ("dimensions/mass","65 x 40 x 6.5 mm; 24.5 g","VERIFIED","S09; S10","page; datasheet",""),
 ("supply/current/power","3.3 V; RX and TX current tables including temperature maxima documented","VERIFIED_DOCUMENT","S10","electrical table","Integrated rail transient compatibility remains open"),
 ("RF range/output/sensitivity/data rate","430-440 MHz UHF; 24-30 dBm; public modulation/rate/sensitivity details","VERIFIED_DOCUMENT","S09; S10; S11","current page; datasheet; PCN","Authorized operating frequency and final link case"),
 ("connectors/pinout","20-position FSI and MCX; public connector pinout","VERIFIED_DOCUMENT","S09; S10","page and datasheet connector section","Carrier option map and coax selection"),
 ("data protocol","I2C/UART/CAN, CSP/GOSH; framing/FEC described","VERIFIED","S09; S10","current page; datasheet","Exact current firmware/API manual"),
 ("operating/storage limits","Operating -30 to +85 C; full storage/survival evidence for delivered revision incomplete","PARTIAL","S09; S10","ratings sections","Thermal/survival analysis"),
 ("qualification/radiation/life","Workmanship and product information public; configuration-specific qualification/acceptance and one-year radiation evidence incomplete","UNKNOWN","S09; S10; S11","documents checked","Launch survival and radiation/life assurance"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("ISISPACE VHF/UHF Antenna 1U-3U / 5 V turnstile", [
 ("commercial identity","1U-3U family, turnstile and 5 V choices; exact order code/frequency UNKNOWN","PARTIAL","S05","current selector","Configuration control"),
 ("orderability and price","Current quote route; public price UNKNOWN","PARTIAL","S05","current page","Cost closure"),
 ("stowed dimensions/mass","98 x 98 x 7 mm with cover; less than 90 g","VERIFIED_FAMILY","S05","product specification","Exact configured mass"),
 ("power/control","less than 60 mW nominal at 5 V; 2 W deployment; I2C","VERIFIED_FAMILY","S05","product specification","Pinout/command and transient details"),
 ("RF properties","145-868 MHz family; greater than 10 dB return loss; UHF 0 dBi main beam; greater than 50 MHz family bandwidth","VERIFIED_FAMILY","S05","product specification","Integrated tuned pattern and link margin"),
 ("connector/pinout","Miniature 9-pin Omnetics named; exact pinout and RF connector for selected variant UNKNOWN","UNKNOWN","S05","checked page","Harness and coax release"),
 ("deployment geometry/constraints","Up to four 55 cm elements; deployment time under 5 s; exact turnstile element layout/envelope UNKNOWN","PARTIAL","S05","overview/specification","CAD clearance and dynamics"),
 ("temperature","Operational -20 to +60 C; deployment -5 to +60 C","VERIFIED_FAMILY","S05","product specification",""),
 ("qualification/acceptance","Page lists QT/AT scope; no public detailed report for selected configuration","PARTIAL","S05","qualification table","Launch and deployment reliability claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

add("SkyFox Labs piCAM/FM", [
 ("commercial identity","piCAM/FM Flight Model","VERIFIED","S48; S49","product page; datasheet pp1-2",""),
 ("orderability and price","EUR 4950 quantity one; 2-4 weeks plus shipping","VERIFIED_INDICATIVE","S48","current product page","Export/delivery confirmation remains"),
 ("dimensions/mass/mounting","33 x 33 x 19 mm body plus optics; 48 x 33 bracket, four M2.5 holes; 40 g lens-dependent","VERIFIED","S48; S49","page; datasheet pp2,4","Exact selected lens envelope/mass"),
 ("supply/current/power","2.7-3.6 V, 3.3 V nominal, 95 mA datasheet operating current; page says 90 mA","CONFLICT_MINOR","S48; S49","page; datasheet p3","Power allocation and rail compatibility","Use 95 mA for screening only after resolving whether it is a guaranteed maximum"),
 ("connector/pinout","Molex PicoBlade 53261 six-pin; full signal table and boot sequence","VERIFIED","S49","datasheet pp4-5","Mating harness parts still need selection"),
 ("protocol/data product","3.3 V UART 1.2-921.6 kbps; one-byte commands; VGA RGB JPEG ASCII-hex framing","VERIFIED","S49","datasheet pp2,6-10",""),
 ("optics/exposure","Default approximately 60 degree diagonal, IR cut, infinity focus, automatic shutter/day-night","PARTIAL","S48; S49","page; datasheet pp2,10","Exact lens distortion/MTF/exposure bounds and image-opportunity analysis"),
 ("operating/storage limits","Operating -30 to +85 C; storage -40 to +85 C; application note inconsistently calls -40 to +85 operating","CONFLICT","S49","datasheet pp3,13","Thermal operating limit and test criteria"),
 ("mechanical/thermal integration","Manufacturer recommends four standoffs, insulated from outer parts and 1 mm aperture gap","VERIFIED_GUIDANCE","S49","datasheet p13","Bracket design and installed conductance remain custom"),
 ("radiation/latchup","Manufacturer states COTS parts and no radiation-hardened ICs; recommends external current limiting","VERIFIED_LIMITATION","S49","datasheet pp13-14","One-year radiation survival and D1-IF protection design"),
 ("qualification/acceptance/life","Vendor states TRL9 and more than one year on orbit; public delivered-unit qualification/acceptance report and reliability basis not located","UNKNOWN","S48; S49","page; datasheet checked","Launch survival and one-year configuration-specific claim"),
 ("Phase 1 gate","CANDIDATE / EVIDENCE INCOMPLETE","FAIL","D1-CMP-STD-001","all rows above","Admission to Phase 1 baseline")])

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(R[0]))
    w.writeheader(); w.writerows(R)
print(f"wrote {len(R)} evidence rows to {OUT}")
