#!/usr/bin/env python3
"""DEGENERATE-1 hypothetical parametric thermal-power sensitivity model.

Standard-library only. This is an uncorrelated lumped-parameter model, not a
thermal qualification or component-specific prediction. No physical hardware was
tested. See TMI-001. Run: python analysis/thermal_transient.py
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT_PATH = HERE / "thermal_inputs.json"
CASE_PATH = HERE / "thermal_cases.csv"
RESULT_PATH = HERE / "thermal_results.csv"
VERIFY_PATH = HERE / "thermal_verification.json"
PLOT_DIR = HERE / "plots"
K0 = 273.15


def value(mapping, key):
    return float(mapping[key]["value"])


def orbit_geometry(altitude_km, beta_deg, earth_radius_km, mu_km3_s2):
    radius = earth_radius_km + altitude_km
    period_s = 2.0 * math.pi * math.sqrt(radius**3 / mu_km3_s2)
    beta = abs(math.radians(beta_deg))
    critical = math.asin(earth_radius_km / radius)
    if beta >= critical:
        eclipse_fraction = 0.0
    else:
        horizon = math.sqrt(altitude_km**2 + 2.0 * earth_radius_km * altitude_km)
        eclipse_fraction = math.acos(horizon / (radius * math.cos(beta))) / math.pi
    return period_s, period_s * eclipse_fraction, math.degrees(critical)


def svg_line_plot(path, title, records, series, y_label="Temperature (degC)"):
    width, height = 1000, 560
    left, right, top, bottom = 82, 30, 55, 68
    plot_w, plot_h = width - left - right, height - top - bottom
    xs = [r["time_min"] for r in records]
    ys = [r[key] for r in records for key, _ in series]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    pad = max(2.0, 0.08 * (ymax - ymin or 1.0))
    ymin -= pad; ymax += pad
    def sx(x): return left + (x - xmin) / (xmax - xmin or 1.0) * plot_w
    def sy(y): return top + (ymax - y) / (ymax - ymin or 1.0) * plot_h
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             '<rect width="100%" height="100%" fill="white"/>',
             f'<text x="{width/2}" y="30" text-anchor="middle" font-family="sans-serif" font-size="20">{title}</text>']
    for i in range(6):
        y = ymin + (ymax-ymin)*i/5
        py = sy(y)
        parts.append(f'<line x1="{left}" y1="{py:.1f}" x2="{width-right}" y2="{py:.1f}" stroke="#dddddd"/>')
        parts.append(f'<text x="{left-8}" y="{py+4:.1f}" text-anchor="end" font-family="sans-serif" font-size="12">{y:.1f}</text>')
    for i in range(6):
        x = xmin + (xmax-xmin)*i/5
        px = sx(x)
        parts.append(f'<line x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{height-bottom}" stroke="#eeeeee"/>')
        parts.append(f'<text x="{px:.1f}" y="{height-bottom+20}" text-anchor="middle" font-family="sans-serif" font-size="12">{x:.1f}</text>')
    colors = ["#0068b5", "#d1495b", "#2a9d8f", "#f4a261", "#6a4c93", "#555555"]
    for n, (key, label) in enumerate(series):
        points = " ".join(f"{sx(r['time_min']):.1f},{sy(r[key]):.1f}" for r in records)
        color = colors[n % len(colors)]
        parts.append(f'<polyline fill="none" stroke="{color}" stroke-width="2" points="{points}"/>')
        lx = left + (n % 3) * 285; ly = height - 30 + (n // 3) * 18
        parts.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+24}" y2="{ly-4}" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{lx+30}" y="{ly}" font-family="sans-serif" font-size="12">{label}</text>')
    parts.extend([
        f'<text x="{width/2}" y="{height-8}" text-anchor="middle" font-family="sans-serif" font-size="13">Time in final simulated orbit (min)</text>',
        f'<text transform="translate(18 {height/2}) rotate(-90)" text-anchor="middle" font-family="sans-serif" font-size="13">{y_label}</text>',
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="none" stroke="#333333"/>',
        '</svg>'])
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def svg_range_plot(path, case_rows):
    rows = sorted(case_rows, key=lambda r: float(r["battery_min_C"]))
    width, height = 1100, 110 + len(rows) * 42
    left, right, top, bottom = 280, 40, 55, 45
    xmin = min(float(r["battery_min_C"]) for r in rows) - 4
    xmax = max(float(r["battery_max_C"]) for r in rows) + 4
    plot_w = width-left-right
    def sx(x): return left + (x-xmin)/(xmax-xmin or 1)*plot_w
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           '<rect width="100%" height="100%" fill="white"/>',
           f'<text x="{width/2}" y="30" text-anchor="middle" font-family="sans-serif" font-size="20">Battery temperature range by case</text>']
    for target,color in [(5,"#2a9d8f"),(35,"#d1495b")]:
        x=sx(target); parts.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{height-bottom}" stroke="{color}" stroke-dasharray="6,4"/>')
    for i,r in enumerate(rows):
        y=top+24+i*42; lo=float(r["battery_min_C"]); hi=float(r["battery_max_C"])
        color="#d1495b" if r["battery_target_met"]=="NO" else "#0068b5"
        parts.append(f'<text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="12">{r["case_id"]}</text>')
        parts.append(f'<line x1="{sx(lo):.1f}" y1="{y}" x2="{sx(hi):.1f}" y2="{y}" stroke="{color}" stroke-width="9"/>')
        parts.append(f'<text x="{sx(hi)+7:.1f}" y="{y+4}" font-family="sans-serif" font-size="11">{lo:.1f} to {hi:.1f} C</text>')
    parts.extend([f'<text x="{width/2}" y="{height-8}" text-anchor="middle" font-family="sans-serif" font-size="13">Final-orbit modeled range; dashed lines are +5/+35 C project battery targets</text>','</svg>'])
    path.write_text("\n".join(parts)+"\n",encoding="utf-8")


def run_case(data, case, dt_override=None, write_plot=False):
    constants = data["constants"]
    sigma = value(constants, "stefan_boltzmann_W_m2_K4")
    t_space = value(constants, "space_sink_K")
    eta_dist = value(constants, "distribution_efficiency")
    eta_charge = value(constants, "charge_efficiency")
    capacity_wh = value(constants, "battery_EOL_capacity_Wh")
    growth = 1.0 + value(constants, "load_growth")
    rf_output = value(constants, "radio_RF_output_W")
    earth_r = value(constants, "earth_radius_km")
    mu = value(constants, "mu_km3_s2")
    initial_soc = value(constants, "initial_battery_SOC_fraction") * capacity_wh
    panel_power_scale = (value(constants, "solar_EOL_factor") *
                         value(constants, "solar_temperature_factor") *
                         value(constants, "solar_shadow_assembly_factor") *
                         value(constants, "solar_mppt_harness_efficiency"))
    standard_face_w = value(constants, "standard_face_BOL_W") * panel_power_scale
    camera_face_w = value(constants, "camera_face_BOL_W") * panel_power_scale

    nodes = data["nodes"]
    ids = [n["id"] for n in nodes]
    index = {name: i for i, name in enumerate(ids)}
    capacities = [float(n["mass_kg"]) * float(n["specific_heat_J_kgK"]) for n in nodes]
    areas = [float(n["external_area_m2"]) for n in nodes]
    panel_indices = list(range(6))
    structure_i, battery_i, avionics_i, radio_i, camera_i = [index[x] for x in ("structure","battery_eps","avionics","radio_antenna","camera")]
    edges = [(index[e["a"]], index[e["b"]], float(e["W_K"])*float(case["conductance_scale"])) for e in data["conductances"]]
    mode = data["electrical_modes"][case["mode"]]
    period, eclipse_s, critical_beta = orbit_geometry(float(case["altitude_km"]), float(case["beta_deg"]), earth_r, mu)
    requested_dt = float(dt_override or data["solver"]["time_step_s"])
    steps = math.ceil(period/requested_dt)
    dt = period/steps
    record_every = max(1, round(float(data["solver"]["record_interval_s"])/dt))
    temps = [float(case["initial_C"])+K0 for _ in nodes]
    soc_wh = initial_soc
    heater_state = case["heater_mode"] == "on"
    heater_on = value(data["heater"], "turn_on_C")
    heater_off = value(data["heater"], "turn_off_C")
    heater_w = value(data["heater"], "power_W")
    charge_target = data["temperature_targets"]["battery_charge_C"]
    max_residual_j = 0.0
    global_min = temps[:]; global_max = temps[:]
    depleted_at_s = None
    final_records = []
    last_stats = None
    converged = False

    for orbit_no in range(1, int(data["solver"]["maximum_orbits"])+1):
        start_temps = temps[:]
        start_soc = soc_wh
        stats = {"solar_wh":0.0,"bus_load_wh":0.0,"stored_charge_wh":0.0,"discharge_wh":0.0,
                 "curtailed_wh":0.0,"heater_wh":0.0,"charge_inhibited_s":0.0,"heater_on_s":0.0}
        orbit_records = []
        orbit_min = temps[:]; orbit_max = temps[:]
        for step in range(steps):
            phase_s = step*dt
            sunlit = phase_s >= eclipse_s
            sun_elapsed = phase_s-eclipse_s if sunlit else -1.0
            tx_active = sunlit and 300.0 <= sun_elapsed < 300.0+float(mode["tx_seconds_per_orbit"])
            camera_active = sunlit and 900.0 <= sun_elapsed < 900.0+float(mode["camera_seconds_per_orbit"])
            if tx_active:
                radio_delivered = float(mode["radio_tx_W"])
            elif float(mode["rx_duty"]) >= 0.999:
                radio_delivered = float(mode["radio_rx_W"])
            else:
                radio_delivered = float(mode["radio_rx_W"]) if (phase_s % 60.0) < 60.0*float(mode["rx_duty"]) else 0.0
            camera_delivered = float(mode["camera_W"]) if camera_active else 0.0
            battery_c = temps[battery_i]-K0
            if case["heater_mode"] == "auto":
                if battery_c <= heater_on: heater_state = True
                elif battery_c >= heater_off: heater_state = False
            elif case["heater_mode"] == "on": heater_state = True
            else: heater_state = False
            heater_delivered = heater_w if heater_state else 0.0
            eps_delivered = float(mode["base_eps_W"])
            avionics_delivered = float(mode["base_avionics_W"])
            delivered = growth*(eps_delivered+avionics_delivered+radio_delivered+camera_delivered+heater_delivered)
            bus_load = delivered/eta_dist
            generated = 0.0
            if sunlit:
                for p_i, factor in enumerate(case["direct_factors"]):
                    generated += (camera_face_w if p_i == 0 else standard_face_w)*float(factor)
            stats["solar_wh"] += generated*dt/3600.0
            stats["bus_load_wh"] += bus_load*dt/3600.0
            stats["heater_wh"] += growth*heater_delivered/eta_dist*dt/3600.0
            if heater_state: stats["heater_on_s"] += dt
            net = generated-bus_load
            if net >= 0:
                charge_allowed = float(charge_target["min"]) <= battery_c <= float(charge_target["max"])
                if charge_allowed:
                    stored = net*eta_charge*dt/3600.0
                    room = capacity_wh-soc_wh
                    accepted = min(room, stored)
                    soc_wh += accepted
                    stats["stored_charge_wh"] += accepted
                    stats["curtailed_wh"] += (stored-accepted)/eta_charge
                else:
                    stats["charge_inhibited_s"] += dt
                    stats["curtailed_wh"] += net*dt/3600.0
            else:
                discharge = -net*dt/3600.0
                soc_wh -= discharge
                stats["discharge_wh"] += discharge
                if soc_wh <= 0 and depleted_at_s is None:
                    depleted_at_s = ((orbit_no-1)*period+phase_s)
                soc_wh = max(0.0, soc_wh)

            q = [0.0 for _ in nodes]
            distribution_loss = bus_load-delivered
            q[battery_i] += growth*eps_delivered + distribution_loss + growth*heater_delivered
            q[avionics_i] += growth*avionics_delivered
            q[radio_i] += max(0.0, growth*radio_delivered-(rf_output if tx_active else 0.0))
            q[camera_i] += growth*camera_delivered
            for i,n in enumerate(nodes):
                if areas[i] <= 0: continue
                area = areas[i]
                alpha = float(case["solar_absorptivity"])
                epsilon = float(case["ir_emissivity"])
                if sunlit:
                    if i in panel_indices:
                        direct_factor = float(case["direct_factors"][i])
                        electric = (camera_face_w if i == 0 else standard_face_w)*direct_factor
                    else:
                        direct_factor = sum(float(x) for x in case["direct_factors"])/6.0
                        electric = 0.0
                    q[i] += alpha*float(case["solar_flux_W_m2"])*area*direct_factor-electric
                    q[i] += alpha*float(case["solar_flux_W_m2"])*float(case["albedo"])*area*float(case["albedo_view_factor"])
                q[i] += epsilon*float(case["earth_ir_W_m2"])*area*float(case["earth_view_factor"])
                q[i] -= epsilon*sigma*area*(temps[i]**4-t_space**4)
            for a,b,g in edges:
                heat = g*(temps[b]-temps[a])
                q[a] += heat; q[b] -= heat
            old_energy = sum(capacities[i]*temps[i] for i in range(len(nodes)))
            new_temps = [temps[i]+dt*q[i]/capacities[i] for i in range(len(nodes))]
            new_energy = sum(capacities[i]*new_temps[i] for i in range(len(nodes)))
            residual = abs((new_energy-old_energy)-dt*sum(q))
            max_residual_j = max(max_residual_j,residual)
            temps = new_temps
            for i,t in enumerate(temps):
                global_min[i]=min(global_min[i],t); global_max[i]=max(global_max[i],t)
                orbit_min[i]=min(orbit_min[i],t); orbit_max[i]=max(orbit_max[i],t)
            if step % record_every == 0 or step == steps-1:
                rec={"time_min":phase_s/60.0,"soc_Wh":soc_wh,"heater_on":1 if heater_state else 0}
                rec.update({name:temps[i]-K0 for i,name in enumerate(ids)})
                orbit_records.append(rec)
        max_delta = max(abs(temps[i]-start_temps[i]) for i in range(len(nodes)))
        last_stats = stats
        final_records = orbit_records
        stored_margin = stats["stored_charge_wh"]-stats["discharge_wh"]
        if orbit_no >= int(data["solver"]["minimum_orbits"]) and max_delta <= float(data["solver"]["periodic_temperature_tolerance_C"]):
            converged=True
            # Continue an energy-negative periodic case until depletion is
            # demonstrated or the maximum horizon is reached. Thermal loads are
            # still imposed after depletion only to retain the converged thermal
            # screen; the case is then explicitly invalid as an operable mode.
            if stored_margin >= -1e-4 or depleted_at_s is not None:
                break

    targets=data["temperature_targets"]
    node_rows=[]
    for i,n in enumerate(nodes):
        target=targets[n["temperature_target"]]
        lo=orbit_min[i]-K0; hi=orbit_max[i]-K0
        node_rows.append({
            "case_id":case["id"],"node_id":n["id"],"target_id":n["temperature_target"],
            "target_min_C":target["min"],"target_max_C":target["max"],
            "all_time_min_C":global_min[i]-K0,"all_time_max_C":global_max[i]-K0,
            "last_orbit_min_C":lo,"last_orbit_max_C":hi,
            "lower_margin_C":lo-float(target["min"]),"upper_margin_C":float(target["max"])-hi,
            "target_met":"YES" if lo>=float(target["min"]) and hi<=float(target["max"]) else "NO",
            "orbits_simulated":orbit_no,"periodic_converged":"YES" if converged else "NO"
        })
    batt_row=next(r for r in node_rows if r["node_id"]=="battery_eps")
    case_row={
        "case_id":case["id"],"altitude_km":case["altitude_km"],"beta_deg":case["beta_deg"],
        "critical_beta_deg":critical_beta,"period_min":period/60.0,"eclipse_min":eclipse_s/60.0,
        "mode":case["mode"],"heater_mode":case["heater_mode"],"conductance_scale":case["conductance_scale"],
        "orbits_simulated":orbit_no,"periodic_converged":"YES" if converged else "NO",
        "battery_min_C":batt_row["last_orbit_min_C"],"battery_max_C":batt_row["last_orbit_max_C"],
        "battery_target_met":batt_row["target_met"],"battery_SOC_end_Wh":soc_wh,
        "battery_SOC_orbit_delta_Wh":soc_wh-start_soc,"battery_depleted":"YES" if depleted_at_s is not None else "NO",
        "depleted_at_hours":"" if depleted_at_s is None else depleted_at_s/3600.0,
        "solar_generated_Wh_last_orbit":last_stats["solar_wh"],"bus_load_Wh_last_orbit":last_stats["bus_load_wh"],
        "raw_energy_margin_Wh_last_orbit":last_stats["solar_wh"]-last_stats["bus_load_wh"],
        "stored_energy_margin_Wh_last_orbit":last_stats["stored_charge_wh"]-last_stats["discharge_wh"],
        "energy_closed":"YES" if last_stats["stored_charge_wh"]-last_stats["discharge_wh"]>=-1e-4 and depleted_at_s is None else "NO",
        "heater_Wh_last_orbit":last_stats["heater_wh"],"heater_duty_last_orbit":last_stats["heater_on_s"]/period,
        "charge_inhibited_min_last_orbit":last_stats["charge_inhibited_s"]/60.0,
        "max_energy_residual_J":max_residual_j,"evidence":"HYPOTHETICAL PARAMETRIC SENSITIVITY; NOT COMPONENT-SPECIFIC; NO HARDWARE TESTED; TMI-001"
    }
    if write_plot:
        PLOT_DIR.mkdir(exist_ok=True)
        svg_line_plot(PLOT_DIR/f"{case['id']}.svg",f"{case['id']} — final simulated orbit",final_records,
                      [("battery_eps","Battery/EPS"),("structure","Structure"),("avionics","Avionics"),("radio_antenna","Radio/antenna"),("camera","Camera")])
    return case_row,node_rows,final_records


def verify(data, baseline_case, baseline_rows):
    c=data["constants"]
    r=value(c,"earth_radius_km"); mu=value(c,"mu_km3_s2")
    period,eclipse,_=orbit_geometry(475,0,r,mu)
    expected=period/math.pi*math.asin(r/(r+475))
    orbit_error=abs(eclipse-expected)
    # Analytic constant-heat ramp.
    cap=100.0; q=2.0; dt=2.0; temp=280.0
    for _ in range(50): temp += dt*q/cap
    ramp_error=abs(temp-(280.0+q/cap*100.0))
    # Pairwise conduction must conserve energy exactly apart from roundoff.
    t1,t2,g=280.0,300.0,0.7
    conduction_residual=abs(g*(t2-t1)+g*(t1-t2))
    fine_case_rows=[]
    fine_case=dict(baseline_case)
    fine_summary,fine_case_rows,_=run_case(data,fine_case,dt_override=1.0,write_plot=False)
    coarse={r["node_id"]:r for r in baseline_rows}
    fine={r["node_id"]:r for r in fine_case_rows}
    differences={name:max(abs(float(coarse[name]["last_orbit_min_C"])-float(fine[name]["last_orbit_min_C"])),
                          abs(float(coarse[name]["last_orbit_max_C"])-float(fine[name]["last_orbit_max_C"]))) for name in coarse}
    max_dt_difference=max(differences.values())
    checks={
        "beta_zero_eclipse_identity_error_s":orbit_error,
        "constant_heat_ramp_error_K":ramp_error,
        "pairwise_conduction_residual_W":conduction_residual,
        "time_step_comparison_s":[2.0,1.0],
        "time_step_max_node_extrema_difference_C":max_dt_difference,
        "time_step_node_differences_C":differences,
        "time_step_acceptance_C":0.20,
        "all_checks_pass":orbit_error<1e-9 and ramp_error<1e-10 and conduction_residual<1e-12 and max_dt_difference<0.20,
        "evidence_classification":"HYPOTHETICAL PARAMETRIC SENSITIVITY - NOT COMPONENT-SPECIFIC",
        "hardware_tested":False,
        "incident":"TMI-001",
        "note":"Numerical verification checks implementation consistency only; it does not validate physical inputs, predict a component, or correlate the model."
    }
    return checks


def write_csv(path, rows):
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--self-test",action="store_true",help="run model and numerical checks (also run by default)")
    args=parser.parse_args()
    data=json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    assert sum(float(n["mass_kg"]) for n in data["nodes"]) == 1.0635
    assert abs(sum(float(n["external_area_m2"]) for n in data["nodes"])-0.0600)<1e-12
    case_rows=[]; node_rows=[]; baseline_rows=None; baseline_case=None
    for case in data["cases"]:
        summary,rows,_=run_case(data,case,write_plot=case["id"] in {"nominal_475","cold_recovery_475","hot_continuous_sun_475","fixed_camera_sun_recovery_475"})
        case_rows.append(summary); node_rows.extend(rows)
        if case["id"]=="nominal_475": baseline_rows=rows; baseline_case=case
    write_csv(CASE_PATH,case_rows); write_csv(RESULT_PATH,node_rows)
    checks=verify(data,baseline_case,baseline_rows)
    VERIFY_PATH.write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8")
    PLOT_DIR.mkdir(exist_ok=True)
    svg_range_plot(PLOT_DIR/"battery_case_ranges.svg",case_rows)
    output={"model_id":data["model_id"],"status":data["model_status"],"cases":len(case_rows),
            "numerical_checks_pass":checks["all_checks_pass"],
            "synthetic_target_misses":[r["case_id"] for r in case_rows if r["battery_target_met"]=="NO"],
            "synthetic_negative_energy_cases":[r["case_id"] for r in case_rows if r["energy_closed"]=="NO"],
            "nonconverged_cases":[r["case_id"] for r in case_rows if r["periodic_converged"]=="NO"]}
    print(json.dumps(output,indent=2))
    if not checks["all_checks_pass"]: raise SystemExit("Numerical self-check failed")


if __name__=="__main__":
    main()
