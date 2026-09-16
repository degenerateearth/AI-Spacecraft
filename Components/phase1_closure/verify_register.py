import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CLOSURE = ROOT / "Components" / "phase1_closure"
data = json.loads((CLOSURE / "component_register.json").read_text(encoding="utf-8"))
manifest = {
    row["id"]: row
    for row in json.loads(
        (ROOT / "SOURCES" / "components" / "closure_2026-09-15" / "manifest.json").read_text(encoding="utf-8")
    )
}
legacy_sources = set(re.findall(r"\bS\d{2}\b", (ROOT / "review" / "Source_Register.md").read_text(encoding="utf-8")))
items = data["items"]
errors = []
warnings = []

ids = [item["id"] for item in items]
if len(ids) != len(set(ids)):
    errors.append("duplicate component-register IDs")

allowed = {"SUPPORTED", "CUSTOM/TO BE VERIFIED", "CANDIDATE / EVIDENCE INCOMPLETE"}
required = {
    "id", "segment", "function", "quantity", "manufacturer", "part", "status",
    "sources", "dimensions_mass", "power", "interfaces", "uncertainty",
    "verification", "rationale", "mission_admitted"
}
for item in items:
    missing = sorted(key for key in required if key not in item or item[key] in (None, ""))
    if missing:
        errors.append(f"{item['id']}: missing required fields: {', '.join(missing)}")
    if item.get("status") not in allowed:
        errors.append(f"{item['id']}: invalid status {item.get('status')!r}")
    if item.get("mission_admitted") is not False:
        errors.append(f"{item['id']}: mission_admitted must remain false while G1 is open")
    if item.get("status") == "CUSTOM/TO BE VERIFIED":
        if len(item.get("release_artifacts", [])) < 5:
            errors.append(f"{item['id']}: custom work package lacks release-artifact set")
        if "not released" not in item.get("design_state", "").lower():
            errors.append(f"{item['id']}: custom design maturity is overstated")
    if item.get("status") == "SUPPORTED" and not item.get("sources"):
        errors.append(f"{item['id']}: supported item has no primary source")
    for source_id in item.get("sources", []):
        if source_id.startswith("E") and source_id not in manifest:
            errors.append(f"{item['id']}: unknown closure source {source_id}")
        elif source_id.startswith("S") and source_id not in legacy_sources:
            warnings.append(f"{item['id']}: legacy source {source_id} not found in Markdown source register")
        elif not source_id.startswith(("E", "S", "TMI")) and not source_id.startswith("engineering/"):
            warnings.append(f"{item['id']}: nonstandard evidence reference {source_id}")

for source_id, row in manifest.items():
    if row.get("status") != "RETRIEVED":
        continue
    path = ROOT / row["local_path"]
    if not path.exists():
        errors.append(f"{source_id}: archived file missing: {path.relative_to(ROOT)}")
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != row.get("sha256"):
        errors.append(f"{source_id}: archive hash mismatch")

for name in ("component_register.md", "alternative_review.md", "completeness_audit.md", "source_index.md"):
    if not (CLOSURE / name).exists():
        errors.append(f"missing review artifact: {name}")

counts = {}
for item in items:
    counts[item["status"]] = counts.get(item["status"], 0) + 1
if counts != data.get("counts"):
    errors.append(f"stored status counts do not match records: {counts} != {data.get('counts')}")

report = [
    "# Component-register verification",
    "",
    f"Records checked: {len(items)}",
    f"Archived source hashes checked: {sum(1 for row in manifest.values() if row.get('status') == 'RETRIEVED')}",
    f"Errors: {len(errors)}",
    f"Warnings: {len(warnings)}",
    "",
    "This is an internal consistency and archive-integrity check. It is not engineering validation or independent review.",
]
if errors:
    report += ["", "## Errors", ""] + [f"- {line}" for line in errors]
if warnings:
    report += ["", "## Warnings", ""] + [f"- {line}" for line in warnings]
(CLOSURE / "verification_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
print(f"records={len(items)} errors={len(errors)} warnings={len(warnings)}")
sys.exit(1 if errors else 0)
