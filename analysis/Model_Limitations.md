# Model scope and independent checks

The Python model performs scalar mass/cost addition, two-body eclipse/range/Doppler geometry, orbit energy balance with recharge losses, battery DOD and a scalar RF budget. Inputs are estimates or specified acceptance targets unless a source is stated in the engineering documents. No measured flight performance is used.

The nominal geometry factor in inputs is normalized to a 2.3 W reference face; it is (5*2.3+1.8)/(4*2.3). Recovery uses the minimum aperture-face power. The reported `sunlight_power_EOL_W` is for a reference 2.3 W face; actual nominal and minimum powers are obtained from the associated geometry/aperture factors. `solar_energy_Wh` and `fixed_attitude_solar_Wh` use those factors correctly.

`power_sensitivity.csv` is a generic equal-face sweep, not a second representation of the released unequal-face baseline. Geometry=1 is a fixed direction and geometry=1.5 is an isotropic attitude mean. The face-power column represents all faces in that stress case. It deliberately includes failures. `thermal_screen.csv` is a single-node equilibrium illustration with assumed optical properties; it omits camera-aperture thermal detail and cannot predict component transients. It shows why a correlated thermal model is still necessary.

Battery stress case disables the camera. Routine average power includes its capture and processing allowance. RF and camera operation are mutually exclusive; peak RF and peak imaging cases must be tested separately. No camera acquisition-opportunity probability, orbit decay, finite-element structural response, battery cycle aging, detailed thermal transient or radiation transport has been executed.

Changing model inputs requires updating narrative budgets and generating a new release hash manifest. Script assertions test the chosen budget checks, not applicability of the input assumptions. An aerospace auditor should challenge the assumptions before relying on the positive arithmetic margins.
