# D1-PAY-001 — Opportunistic Earth imaging

Revision A | Owner-confirmed scope: occasional recognizable Earth images.

**Phase 1 evidence update, 2026-09-15:** The CS-101 remains the controlled BOM
entry but is not eligible for the Phase 1 baseline because its public material
does not establish critical electrical, protocol, thermal and optical properties.
SkyFox Labs `piCAM/FM` is candidate C01 and is better documented, but it also
remains **CANDIDATE / EVIDENCE INCOMPLETE** under D1-CMP-STD-001. No camera
replacement, purchase or CAD change has occurred.

## Hardware and optical requirements

Select CrystalSpace CS-101 Kikas, 5 MP, with an infinity-focused visible lens [S23]. Published envelope is 42 x 25 x 45 mm and mass 50 g. Allocate 20 g for bracket, short baffle and harness. The current detailed product brief is gated behind a contact form; no form was submitted. Accordingly supply voltage, consumption, shutter type, image format, operating temperatures and serial protocol are unresolved. These must be confirmed before procurement release.

Request a roughly 60-degree horizontal field of view lens with matching sensor orientation, calibrated infinity focus, exposure control down to <=1 ms, and a JPEG or reduced-resolution output path. This FOV is an order requirement, not a claimed standard CS-101 lens. Lens acceptance includes focus and distortion through thermal vacuum, mechanical retention, solar exposure tolerance and stray-light behavior. The spacecraft has no commanded Sun avoidance; if the camera cannot tolerate incidental Sun exposure, add protection or revise the attitude architecture.

At 475 km and 60-degree horizontal FOV, the flat-ground nadir swath approximation is `2*h*tan(FOV/2)=548 km`. At 640 output columns this corresponds to approximately 857 m/pixel at scene center in a nadir-like view. This is geometric sampling, not guaranteed ground resolution, optical MTF, geolocation accuracy or a targetable swath. Limb views are highly distorted. Do not infer exact full-resolution dimensions or resolution from the 5 MP label.

Pixel angular pitch at 640 columns is approximately 1.64 mrad. With a 10 degree/s rotation and <=1 ms exposure, rotational smear is about 0.11 output pixel. Orbital translation contributes roughly 7.6 m in 1 ms, well below a coarse output pixel. At 100 degree/s, rotational smear exceeds one pixel; reject those images or shorten exposure. Confirm rolling/global shutter timing and full-frame readout effects on the delivered camera. Gyro data are useful for selecting exposures, but a gyro alone cannot point the camera at Earth.

## Accommodation

Mount the camera in a 27 mm-high lower bay, orienting its 25 mm dimension along Z and its optical depth toward +X, subject to vendor CAD confirmation. The +X panel receives a lens aperture/baffle relief with an allocated minimum face power of 1.8 W. Five other faces retain 2.3 W each. Require a detailed panel layout: an aperture cutting a series cell can lose an entire string, not just its area fraction. No aperture is authorized in a vendor panel until the supplier signs the cell routing and structural design.

No lens protrusion may interfere with rail travel or the dispenser. Verify boresight clearance with all four antenna elements deployed. Camera mount alignment is referenced to spacecraft axes for image metadata; it does not create an attitude-knowledge guarantee. Keep camera optics capped through integration except controlled optical tests, and remove the cap before final fit check with a documented closeout witness.

## Capture and processing concept

Allocate <=2 W camera peak and <=300 s powered time/day, about 0.007 W daily average for the camera alone. A total 0.02 W orbital average allocation includes OBC processing overhead. If cold-start/readout latency or actual power exceeds these limits, reduce burst count before raising the power allocation. Never capture during RF transmission or low-energy recovery.

Take a small burst during each of several energy-permitted daylight opportunities. Start with up to 10 daily sessions of <=30 s, maximum 20 frames/session, reduced resolution where available. Reject saturated/dark images, rank remaining frames by contrast and Earth-like color/limb features, and retain thumbnails for ground selection. An elementary heuristic is sufficient initially; do not promise Earth recognition from an unvalidated classifier. If most views are space, retain representative frames and adapt timing. Uncontrolled orientation has no deterministic monthly capture guarantee; Monte Carlo attitude/orbit sampling and ground-in-the-loop replay must demonstrate acceptable opportunity rates.

Downlink 160 x 120 thumbnails first, then request selected 640 x 480 products. Budget a typical selected compressed image at 50 kB and a maximum transfer at 100 kB; enforce the cap by recompression/downsampling or reject the image. Compression ratio is scene dependent and must be measured. Do not assume full 5 MP raw images fit the routine UHF service.

At 600 useful bit/s (1200 bit/s at 50% net efficiency), a 50 kB image takes 667 s before retransmissions. At one selected image/week this averages about 95 s/day. Add 1229 s/day health telemetry and a 20% retransmission/contact allowance: approximately 1589 s/day, within the 1728 s/day TX energy allocation. This needs actual contact coverage. Recovery reduces health sampling and disables imaging; it never borrows energy from survival to meet an image schedule.

Store two firmware images in reserved code space and allocate at least 16 MB of existing nonvolatile storage for image/health ring buffers after verifying actual BSP layout. At 100 kB/image, 100 images consume 10 MB; 30 days of 64-byte/min health data consume 2.76 MB. Use per-record CRC, generation counters, bounded queues and discard-oldest policy. Protect boot/configuration areas from image writes. Camera interface failure or full storage must not block watchdog servicing, commands or EPS polling.

## Image verification and licensing inputs

Retain factory optical data, focus/MTF measurements at infinity, flat/dark frames, color response where supplied, bad-pixel map and temperature drift. Test a moving scene/turntable with flight-like exposure and shutter timing; exercise compression, thumbnails, file segmentation and retransmission through the actual radio. After vibration and thermal vacuum, repeat optical checks and inspect for focus shifts and contamination.

Provide NOAA/CRSRA the actual sensor, lens, spectral band, maximum capabilities, image modes, storage, downlink and operational description. Do not describe the system to the regulator solely by the downsampled products planned for routine use. Imaging begins only under the required authorization/conditions. Logs must preserve capture time, available orbit estimate, estimated rotation, exposure, gain, image ID and processing history. No precise ground location is asserted without an attitude/orbit solution.
