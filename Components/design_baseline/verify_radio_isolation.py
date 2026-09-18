"""Check design-source connectivity. This is not schematic ERC or hardware proof."""
from pathlib import Path
import json
b=Path(__file__).resolve().parent
d=json.loads((b/'D1-COM-001_isolation_netlist.json').read_text())
m=json.loads((b/'D1-COM-001_pinmap.json').read_text())
module={x['module_pin']:x for x in m['module_pins']}
assert len(d['parts'])==16 and len(d['channels'])==8
for u in ['U1','U2']:
    p=d['parts'][u]['pins'];assert set(p)==set(map(str,range(1,17)))
    assert p['16']=='+3V3_A' and p['15']=='+3V3_RF' and p['10']=='GND_SYS'
    assert p['9']=='ISO_OE_N'
assert len({(x['ref'],x['channel']) for x in d['channels']})==8
assert len({x['module_pin'] for x in d['channels']})==8
for x in d['channels']:
    p=d['parts'][x['ref']]['pins'];row=module[x['module_pin']]
    assert row['connector_pins']==[x['connector_pin']]
    assert p[str(x['A_pin'])]=='HOST_'+x['signal']
    assert p[str(x['B_pin'])]=='RF_'+x['signal']
    assert p[str(x['DIR_pin'])]==('+3V3_A' if x['direction']=='A_TO_B' else 'GND_SYS')
    assert (row['direction']=='input')==(x['direction']=='A_TO_B')
assert m['carrier_auxiliary_pins']==d['connector_additions']
assert 45 in m['carrier_no_connect_pins']
for u in ['U1','U2']:
    caps=[x for ref,x in d['parts'].items() if ref.startswith('C') and x['placement']==u]
    assert len(caps)==2 and {x['pins']['1'] for x in caps}=={'+3V3_A','+3V3_RF'}
for x in d['channels']:
    pulls=[v for ref,v in d['parts'].items() if ref.startswith('R') and v['pins']['1']=='RF_'+x['signal']]
    assert len(pulls)==1
    assert pulls[0]['pins']['2']==('+3V3_RF' if x['signal']=='SPI_CS_N' else 'GND_SYS')
print(json.dumps({'result':'PASS','IC_pins_covered':32,'channels':8,'constituent_parts':16,'checks':['Carrier-to-module mapping','Direction straps','Separated host and RF nets','Both IC supplies/grounds/enables','Two bypass capacitors per IC','Radio-side default pulls','Pin 45 remains NC'],'scope':'Design-source consistency only. Does not check MCU/module electrical compatibility, PCB/ERC, rail discharge, timing, leakage or physical behavior.'},indent=2))
