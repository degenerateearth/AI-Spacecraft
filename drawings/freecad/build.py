"""Run with the installed FreeCAD Python, or via Build_Degen1.FCMacro.
Native Spreadsheet expressions and Part::Box features remain editable without this script.
No density is assigned to component bounding boxes. Units mm, g.
"""
from pathlib import Path
import csv
import hashlib
import itertools
import json
import sys
import FreeCAD as App
import Part

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

def build(output=None):
    out = Path(output or HERE / 'exports')
    out.mkdir(parents=True, exist_ok=True)
    config = json.loads((HERE / 'parameters.json').read_text(encoding='utf-8'))
    doc = App.newDocument('Degen1_CAD001')
    params = doc.addObject('Spreadsheet::Sheet', 'Parameters')
    for col, value in zip('ABCDE', ['Parameter', 'Value mm', 'Evidence', 'Source', 'Requirements']):
        params.set(col+'1', value)
    groups = {}
    solids = []
    row = 2
    for item in config['objects']:
        group = groups.setdefault(item['group'], None)
        if group is None:
            group = doc.addObject('App::DocumentObjectGroup', item['group'])
            groups[item['group']] = group
        obj = doc.addObject('Part::Box', item['name'])
        group.addObject(obj)
        for field, value in [('Evidence',item['basis']),('Source',item['source']),('Requirements',item['requirements']),('Role',item['role']),('BOM',item.get('bom','')),('MaterialBasis','UNKNOWN; envelope volume is not material volume')]:
            obj.addProperty('App::PropertyString',field,'Traceability')
            setattr(obj,field,value)
        obj.Label = item['name'] + (' [REFERENCE]' if item['role'] in ('reference','keepout') else ' [ENVELOPE]')
        aliases = {}
        for axis, val in zip(['SizeX','SizeY','SizeZ','CenterX','CenterY','CenterZ'],item['size']+item['center']):
            alias = item['name']+'_'+axis
            aliases[axis] = 'Parameters.'+alias
            for col, value in zip('ABCDE',[alias,str(val),item['basis'],item['source'],item['requirements']]):
                params.set(col+str(row),value)
            params.setAlias('B'+str(row),alias)
            row += 1
        for axis, prop in zip('XYZ',['Length','Width','Height']):
            obj.setExpression(prop,aliases['Size'+axis])
            obj.setExpression('Placement.Base.'+axis.lower(),aliases['Center'+axis]+' - '+aliases['Size'+axis]+'/2')
        if item['role']=='envelope':
            solids.append(obj)
        if App.GuiUp:
            color = {'Structure':(.55,.57,.60),'Power':(.3,.65,.5),'Avionics':(.3,.5,.8),'Payload':(.9,.6,.2),'Communications':(.7,.4,.6),'SolarPanels':(.2,.3,.5),'References':(.7,.7,.7)}[item['group']]
            obj.ViewObject.ShapeColor = color
            obj.ViewObject.Transparency = 65 if item['group']=='SolarPanels' else 15
            obj.ViewObject.Visibility = item['role']=='envelope'
    unresolved = doc.addObject('App::DocumentObjectGroup','UnresolvedInterfaces')
    for item in config['unresolved']:
        obj=doc.addObject('App::FeaturePython',item['name'])
        obj.Label=item['name']+' [UNKNOWN - NO GEOMETRY]'
        unresolved.addObject(obj)
        for field,value in item.items():
            if field=='name': continue
            obj.addProperty('App::PropertyString',field.title(),'Traceability')
            setattr(obj,field.title(),value)
    bom=list(csv.DictReader((ROOT/'procurement/BOM.csv').open(encoding='utf-8-sig')))
    lookup={r['id']:r for r in bom}
    for obj in solids:
        if obj.BOM in lookup:
            obj.addProperty('App::PropertyFloat','AssignedMass_g','Budget')
            obj.AssignedMass_g=float(lookup[obj.BOM]['unit_mass_g'])
            obj.addProperty('App::PropertyString','MassBasis','Budget')
            obj.MassBasis=lookup[obj.BOM]['mass_basis_V_vendor_A_allocation_P_provisional']+'; assigned BOM mass, not volume times density'
    # BOM ledger: one entry per line, not one per geometric object. No duplicated EPS battery.
    ledger=doc.addObject('Spreadsheet::Sheet','MassLedger')
    for col,value in zip('ABCDE',['BOM','Item','Quantity','UnitMass_g','Basis']): ledger.set(col+'1',value)
    mass=[]
    for i,r in enumerate(bom,2):
        matches=[o.Name for o in solids if o.BOM==r['id']]
        entry={'bom':r['id'],'item':r['item'],'mass_g':float(r['quantity'])*float(r['unit_mass_g']),'basis':r['mass_basis_V_vendor_A_allocation_P_provisional'],'geometry':matches,'position_known':False}
        mass.append(entry)
        for col,value in zip('ABCDE',[r['id'],r['item'],r['quantity'],r['unit_mass_g'],entry['basis']]): ledger.set(col+str(i),value)
    doc.recompute()
    report = audit(doc,solids)
    report['freecad_version']=App.Version()
    report['parameters_sha256']=hashlib.sha256((HERE/'parameters.json').read_bytes()).hexdigest()
    report['mass']={'method':'BOM assigned masses; no density-derived physical mass or credible spacecraft COM', 'bom_total_g':sum(r['mass_g'] for r in mass),'budget_g':1063.5,'with_20_percent_growth_g':1276.2,'geometry_associated_bom_mass_g':sum(r['mass_g'] for r in mass if r['geometry']),'unlocated_or_unmodeled_bom_mass_g':sum(r['mass_g'] for r in mass if not r['geometry']),'credible_spacecraft_com_mm':None,'breakdown':mass}
    # Reproduce the old report's illustrative point-mass calculation separately.
    mx=70*25
    mz=184*1.25+(24+24.5+51)*28+90*47.5+45*(-18)+70*(-35.5)
    report['legacy_point_mass_com_mm']=[mx/1063.5,0,mz/1063.5]
    report['legacy_com_basis']='CALCULATED using D1-ANA-001 assumed positions and symmetry; not CAD-derived/validated COM'
    path=out/'Degen1_CAD001.FCStd'
    doc.saveAs(str(path))
    Part.export(solids,str(out/'Degen1_CAD001_envelopes.step'))
    (out/'geometry_report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return doc, report

def audit(doc,solids=None):
    solids=solids or [o for o in doc.Objects if hasattr(o,'Role') and o.Role=='envelope']
    overlaps=[]
    distances=[]
    for a,b in itertools.combinations(solids,2):
        vol=a.Shape.common(b.Shape).Volume
        distance=a.Shape.distToShape(b.Shape)[0]
        if vol>1e-6: overlaps.append({'a':a.Name,'b':b.Name,'intersection_mm3':round(vol,6),'interpretation':'ENVELOPE overlap; actual material intersection unproven'})
        elif distance<3.001: distances.append({'a':a.Name,'b':b.Name,'distance_mm':round(distance,6),'interpretation':'nominal envelope distance; no tolerance or connector allowance'})
    outside=[]
    envelope=doc.getObject('NominalRailEnvelope').Shape
    for o in solids:
        vol=o.Shape.cut(envelope).Volume
        if vol>1e-6: outside.append({'name':o.Name,'outside_mm3':round(vol,6)})
    camera=doc.getObject('CS101CameraEnvelope').Shape.BoundBox
    bay=doc.getObject('CameraBay').Shape.BoundBox
    signature={o.Name:{'volume_mm3':round(o.Shape.Volume,6),'bounds_mm':[round(getattr(o.Shape.BoundBox,k),6) for k in ['XMin','YMin','ZMin','XMax','YMax','ZMax']],'valid':o.Shape.isValid()} for o in solids}
    return {'evidence':'MODELED and CALCULATED envelope geometry only; no structural/thermal simulation, hardware test or expert review','fit_conclusion':'NOT ESTABLISHED: envelope overlaps and missing interfaces prevent fit release','overlaps':overlaps,'near_contacts':distances,'nominal_external_envelope_violations':outside,'camera_bay_z_clearance_mm':[camera.ZMin-bay.ZMin,bay.ZMax-camera.ZMax],'signatures':signature,'unverified_checks':['actual rail shape','mounting/fastener access','connector mating and cable bends','antenna deployment swept volume','lens aperture/FOV','cell string routing','tolerances','deployer ICD']}

def verify_saved(out):
    out=Path(out)
    expected=json.loads((out/'geometry_report.json').read_text())
    doc=App.openDocument(str(out/'Degen1_CAD001.FCStd'))
    doc.recompute()
    observed=audit(doc)
    assert observed['signatures']==expected['signatures'], 'Saved geometry changed'
    assert observed['overlaps']==expected['overlaps'], 'Saved overlaps changed'
    assert all(v['valid'] for v in observed['signatures'].values())
    # Meaningful edit test: prove spreadsheet drives geometry after reopening without custom proxies.
    sheet=doc.Parameters
    cell=sheet.getCellFromAlias('CS101CameraEnvelope_SizeX')
    original=sheet.get(cell)
    sheet.set(cell,'46')
    doc.recompute()
    assert abs(doc.CS101CameraEnvelope.Shape.BoundBox.XLength-46)<1e-7
    sheet.set(cell,str(original))
    doc.recompute()
    assert audit(doc)['signatures']==expected['signatures']
    step=Part.Shape()
    step.read(str(out/'Degen1_CAD001_envelopes.step'))
    assert step.isValid()
    expected_volume=sum(v['volume_mm3'] for v in observed['signatures'].values())
    assert abs(step.Volume-expected_volume)<1e-3
    result={'saved_reopen_geometry':'PASS','expression_edit_and_restore':'PASS','step_valid':'PASS','step_solid_count':len(step.Solids),'native_solid_count':len(observed['signatures']),'scope':'CAD software checks only'}
    assert result['step_solid_count']==result['native_solid_count']
    fresh, fresh_report=build(HERE/'verification_work')
    assert fresh_report['signatures']==expected['signatures'], 'Fresh generation differs'
    assert fresh_report['overlaps']==expected['overlaps'], 'Fresh generation changed conflicts'
    App.closeDocument(fresh.Name)
    result['fresh_generation_geometry_match']='PASS'
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    App.closeDocument(doc.Name)
    return result

if __name__=='__main__':
    out=HERE/'exports'
    if '--verify' in sys.argv:
        print(json.dumps(verify_saved(out),indent=2))
    else:
        doc,report=build(out)
        print(json.dumps({'overlaps':report['overlaps'],'mass':report['mass']['bom_total_g']},indent=2))
