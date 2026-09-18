"""Structural consistency checks, not electrical ERC or hardware verification."""
from pathlib import Path
import json
p=Path(__file__).with_name('D1-COM-001_pinmap.json')
d=json.loads(p.read_text(encoding='utf-8'));rows=d['module_pins']
assert sorted(x['module_pin'] for x in rows)==list(range(1,23))
used={}
for x in rows:
    for n in x['connector_pins']:
        assert 1<=n<=50
        if n in used: assert used[n]==x['net'],(n,used[n],x['net'])
        used[n]=x['net']
for pin,net in d.get('carrier_auxiliary_pins',{}).items():
    pin=int(pin);assert pin not in used;used[pin]=net
nc=d['carrier_no_connect_pins']
assert len(nc)==len(set(nc))
assert not(set(nc)&set(used))
assert set(nc)|set(used)==set(range(1,51))
local=[x for x in rows if x['net']=='TXEN_LOCAL']
assert {x['module_pin'] for x in local}=={7,8}
assert all(not x['connector_pins'] for x in local)
assert 45 in nc
assert len([x for x in local if x['direction']=='output_when_configured'])==1
assert [x for x in rows if x['module_pin']==21][0]['connector_pins']==[]
print(json.dumps({'result':'PASS','module_pins_covered':22,'connector_pins_covered':50,'connected_connector_pins':len(used),'no_connect_pins':len(nc),'scope':'Logical pin coverage, net conflicts, local TXEN single driver and RF exclusion only. Not schematic ERC, isolation verification, firmware test or physical test.'},indent=2))
