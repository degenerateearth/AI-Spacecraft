# CAD-001 execution record

2026-09-14. Installed FreeCAD 1.1.3 Python API generated native geometry and STEP;
the installed GUI executed the macro and exported assembly.png. The exported image
was visually inspected. Native application UI inspection was attempted, but the
computer-use app approval timed out; the rendered artifact and native-file checks
provided independent views of the resulting geometry without relying on UI control.

Initial verification found a script TypeError restoring a spreadsheet numeric
cell using an integer. Corrected by converting the saved cell value to string.
The corrected check passed in a fresh process, including parameter edit/restore,
STEP readback, and fresh generation against the saved geometry signatures.
This is a software scripting correction, not a hardware or design test result.

The principal engineering finding is that previously plausible allocation boxes
do not demonstrate assembly fit. Source-sized EPS and AntS plus explicit panels
reveal conflicts hidden by the original smaller sketch placeholders. Actual
material interference awaits controlled supplier geometry. No fit-enabling
architectural corrections were silently applied.
