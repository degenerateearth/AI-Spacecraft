#!/usr/bin/env python3
"""Extract BIRDS-4 frame geometry with FreeCAD; no Degen-1 validation claim."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import FreeCAD as App
import Import
import Part


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "SOURCES" / "components" / "BIRDS4_Structure"
ASSEMBLY = SOURCE / "BIRDS4_FM_Final v7.step"
OUTPUT = HERE / "reference_geometry.json"
DENSITY_G_PER_MM3 = 0.00270


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def volume_center(shape):
    solids = list(shape.Solids)
    volume = sum(solid.Volume for solid in solids)
    if volume <= 0:
        raise ValueError("structure reference shape has no positive-volume solids")
    return volume, App.Vector(
        sum(solid.CenterOfMass.x * solid.Volume for solid in solids) / volume,
        sum(solid.CenterOfMass.y * solid.Volume for solid in solids) / volume,
        sum(solid.CenterOfMass.z * solid.Volume for solid in solids) / volume,
    )


doc = App.newDocument("BIRDS4StructureReference")
Import.insert(str(ASSEMBLY), doc.Name)
doc.recompute()

root_assembly = next(obj for obj in doc.Objects if obj.Label == "BIRDS4_FM_Final v7")
parts = []
shapes = []
for obj in doc.Objects:
    if root_assembly not in obj.InList:
        continue
    if not obj.Label.lower().startswith(("b4_frame", "b4_em_frame")):
        continue
    shape = getattr(obj, "Shape", None)
    if shape is None or shape.isNull():
        continue
    shapes.append(shape)
    box = shape.BoundBox
    volume, center = volume_center(shape)
    parts.append(
        {
            "object": obj.Name,
            "upstream_label": obj.Label,
            "type": obj.TypeId,
            "solid_count": len(shape.Solids),
            "volume_mm3": volume,
            "calculated_mass_if_6061_g": volume * DENSITY_G_PER_MM3,
            "center_of_volume_mm": [center.x, center.y, center.z],
            "bbox_mm": [box.XMin, box.YMin, box.ZMin, box.XMax, box.YMax, box.ZMax],
        }
    )

compound = Part.makeCompound(shapes)
box = compound.BoundBox
shape_properties = [volume_center(shape) for shape in shapes]
total_volume = sum(item[0] for item in shape_properties)
center = App.Vector(
    sum(center.x * volume for volume, center in shape_properties) / total_volume,
    sum(center.y * volume for volume, center in shape_properties) / total_volume,
    sum(center.z * volume for volume, center in shape_properties) / total_volume,
)
result = {
    "document": "D1-STR-REF-001",
    "evidence": "MODELED extraction of MIT-licensed upstream STEP; not Degen-1 test evidence",
    "freecad_version": App.Version(),
    "upstream_repository": "https://github.com/BIRDSOpenSource/BIRDS4-CAD",
    "upstream_commit": "3bab47a0f53410ef79005d21321ff659726f0a1c",
    "assembly_file": ASSEMBLY.name,
    "assembly_sha256": sha256(ASSEMBLY),
    "material_assumption": "6061-T6 at 0.00270 g/mm^3 for calculation only; upstream STEP does not control all material properties",
    "part_instance_count": len(parts),
    "parts": parts,
    "combined_volume_mm3": total_volume,
    "calculated_mass_if_6061_g": total_volume * DENSITY_G_PER_MM3,
    "center_of_volume_mm": [center.x, center.y, center.z],
    "combined_bbox_mm": [box.XMin, box.YMin, box.ZMin, box.XMax, box.YMax, box.ZMax],
    "limitations": [
        "STEP nominal geometry contains no Degen-1 tolerances or inspection datum scheme",
        "material and finish are not controlled by the STEP geometry",
        "fasteners, solar panels, deployment switches and other assembly objects are excluded",
        "mass uses a project density assumption and is not measured",
        "BIRDS-4 launch acceptance and flight history do not transfer to a Degen-1 derivative",
    ],
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: result[key] for key in ("part_instance_count", "combined_volume_mm3", "calculated_mass_if_6061_g", "combined_bbox_mm")}, indent=2))
