"""Inspect archived vendor code without executing it; standard-library only."""
import hashlib,io,json,sys,zipfile
from pathlib import Path
p=Path(sys.argv[1]); z=zipfile.ZipFile(p)
inner=[n for n in z.namelist() if n.endswith('sx126x-driver.zip')]
assert len(inner)==1
d=zipfile.ZipFile(io.BytesIO(z.read(inner[0])))
def read(suffix):
    names=[n for n in d.namelist() if n.endswith(suffix)]
    assert len(names)==1, names
    b=d.read(names[0]);return names[0],b.decode('utf-8-sig'),hashlib.sha256(b).hexdigest()
findings=[]
for suffix,terms in [('src/radio/sx126x/sx126x.c',['USE_TCXO','TCXO_CTRL_1_7V']),('src/radio/sx126x/sx126x.h',['RADIO_TCXO_SETUP_TIME'])]:
    n,t,h=read(suffix)
    findings.append(dict(file=n,sha256=h,matches=[{'line':i,'text':l.strip()} for i,l in enumerate(t.splitlines(),1) if any(v in l for v in terms)]))
projects=[]
for n in d.namelist():
    if n.endswith('.uvprojx'):
        t=d.read(n).decode('utf-8-sig');projects.append({'file':n,'declares_USE_TCXO':'USE_TCXO' in t})
print(json.dumps({'archive_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'findings':findings,'projects':projects,'conclusion':'Generic conditional TCXO example; no exact-module configuration verified. No code executed or hardware tested.'},indent=2))
