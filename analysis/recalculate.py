"""Degen-1 Rev A analytic screening model. Python 3, standard library only.
No orbit propagation, FEA, radiation transport or flight certification is performed.
Run from any directory: python analysis/recalculate.py
Inputs and outputs resolved relative to this file; no network calls.
"""
from pathlib import Path
import math,json,csv
p=Path(__file__).resolve().parent
x=json.loads((p/'inputs.json').read_text())
R=x['earth_radius_km'];r=R+x['altitude_km'];mu=x['mu_km3_s2']
T=2*math.pi*math.sqrt(r**3/mu); eclipse=T/math.pi*math.asin(R/r);sun=T-eclipse
eta=x['distribution_efficiency'];chg=x['charge_efficiency']
psun=x['face_BOL_W']*x['EOL_factor']*x['temperature_factor']*x['shadow_factor']*x['mppt_harness_efficiency']
base=x['base_load_W'];rx=x['radio_RX_W'];tx=x['radio_TX_W'];heater=x['heater_average_W']
load=(x["camera_average_W"]+base+rx+(tx-rx)*x['TX_duty']+heater)*(1+x['power_growth'])
e_load_sun=load/eta*sun/3600
e_load_eclipse=load/eta*eclipse/3600
e_sun=psun*x["nominal_geometry_factor"]*sun/3600
fixed_sun=psun*x["camera_face_BOL_W"]/x["face_BOL_W"]*sun/3600
safe_load=(x["safe_base_W"]+x["safe_radio_RX_W"]*x["safe_RX_duty"]+tx*x["safe_TX_duty"]+x["safe_heater_W"])*(1+x["power_growth"])
safe_required=safe_load/eta*(sun+eclipse/chg)/3600
e_required=e_load_sun+e_load_eclipse/chg
capacity=x['battery_BOL_Wh']*x['battery_EOL_fraction']
usable=capacity*x['design_DOD']
peak_eclipse=((base+rx)*eclipse+(tx-rx)*120+1.0*eclipse)/3600*(1+x['power_growth'])/eta
elev=math.radians(x['elevation_deg'])
slant=math.sqrt(r*r-R*R*math.cos(elev)**2)-R*math.sin(elev)
fspl=32.44+20*math.log10(x['frequency_MHz'])+20*math.log10(slant)
def link(pt):
    return pt+x['space_gain_dBi']+x['ground_gain_dBi']-fspl-sum(x[k] for k in ['space_feed_loss_dB','ground_feed_loss_dB','propagation_loss_dB','polarization_loss_dB','tumble_allowance_dB'])
with (p.parent/'procurement/BOM.csv').open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
mass=sum(float(a['quantity'])*float(a['unit_mass_g']) for a in rows)
cost={v:sum(float(a['quantity'])*float(a['unit_'+v+'_EUR_estimate']) for a in rows) for v in ['low','base','high']}
# Sensitivities assume uniform load in sunlight/eclipse. Range values are engineering assumptions.
cases=[]
for geom in [1,1.5]:
  for face in [2.3,1.8]:
    for heat in [.15,.5,1.0]:
      L=(x["camera_average_W"]+base+rx+(tx-rx)*x['TX_duty']+heat)*(1+x['power_growth'])
      available=psun*geom*face/x['face_BOL_W']*sun/3600
      req=L/eta*(sun+eclipse/chg)/3600
      cases.append(dict(geometry_factor=geom,face_W=face,heater_W=heat,energy_margin_Wh=available-req,closed=available>=req))
with (p/'power_sensitivity.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cases[0]);w.writeheader();w.writerows(cases)
# Simple isothermal shell screening; external flux assumptions, not mission thermal predictions.
sigma=5.670374419e-8
thermal=[]
for label,S,alb,ir,alpha,eps,Aproj,Pinternal in [
 ('cold_sun',1322,.20,200,.65,.85,.01,.8),
 ('nominal_sun',1361,.30,237,.75,.80,.015,1.0),
 ('hot_sun',1414,.35,260,.90,.75,.01732,1.5),
 ('eclipse_equilibrium',0,0,200,.65,.85,.01,.8)]:
  # Solar/albedo absorbed heat uses incident solar flux minus illustrative electric extraction.
  solar=max(0,alpha*S*Aproj-(2.3*Aproj/.01 if S else 0))
  Q=solar+alpha*alb*S*.01+eps*ir*.02+Pinternal
  temp=(Q/(eps*sigma*.06))**.25-273.15
  thermal.append(dict(case=label,heat_W=Q,isothermal_equilibrium_C=temp))
with (p/'thermal_screen.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=thermal[0]);w.writeheader();w.writerows(thermal)
max_load=e_sun*eta*3600/(sun+eclipse/chg)
max_heater=max_load/(1+x['power_growth'])-x['camera_average_W']-base-rx-(tx-rx)*x['TX_duty']
out=dict(period_min=T/60,eclipse_min=eclipse/60,sunlight_min=sun/60,orbits_per_year=365.25*86400/T,
  sunlight_power_EOL_W=psun,average_load_with_growth_W=load,solar_energy_Wh=e_sun,required_solar_energy_Wh=e_required,
  energy_margin_Wh=e_sun-e_required,energy_margin_pct_of_required=100*(e_sun/e_required-1),
  routine_eclipse_Wh=e_load_eclipse,routine_DOD_pct=100*e_load_eclipse/capacity,battery_EOL_Wh=capacity,
  usable_battery_Wh=usable,stress_eclipse_Wh=peak_eclipse,stress_DOD_pct=100*peak_eclipse/capacity,
  max_average_heater_for_energy_balance_W=max_heater,
  fixed_attitude_solar_Wh=fixed_sun,safe_load_W=safe_load,safe_energy_required_Wh=safe_required,safe_energy_margin_Wh=fixed_sun-safe_required,nominal_fixed_attitude_margin_Wh=fixed_sun-e_required,
  mass_CBE_g=mass,mass_with_growth_g=mass*(1+x['mass_growth']),mass_headroom_g=x['mass_limit_g']-mass*(1+x['mass_growth']),
  slant_range_km=slant,FSPL_dB=fspl,downlink_received_dBm=link(x['downlink_dBm']),
  downlink_margin_dB=link(x['downlink_dBm'])-x['receiver_required_dBm'],
  uplink_received_dBm=link(x['ground_TX_dBm']),uplink_margin_dB=link(x['ground_TX_dBm'])-x['receiver_required_dBm'],
  max_doppler_Hz=x['frequency_MHz']*1e6*math.sqrt(mu/r)/299792.458,
  raw_telemetry_bytes_per_day=64*1440,cost_EUR=cost,thermal_screen=thermal)
(p/'results.json').write_text(json.dumps(out,indent=2)+'\n')
# Engineering model consistency checks, not hardware verification.
assert 90<T/60<100
assert 0<eclipse<T/2
assert out['energy_margin_Wh']>0
assert peak_eclipse<usable
assert fixed_sun>safe_required
assert mass*(1+x['mass_growth'])<x['mass_limit_g']
assert link(x['downlink_dBm'])-x['receiver_required_dBm']>=3
print(json.dumps(out,indent=2))
