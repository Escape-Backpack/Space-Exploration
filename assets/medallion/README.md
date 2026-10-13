# Space Exploration medallion - one-piece v1

Main model: `Space_Medallion_OnePiece_v1.stl`.
Import in millimetres at 100% scale. It is one connected solid: no glue or assembly.

## Geometry and orientation

- Diameter: 50 mm. Total thickness: 4.4 mm.
- Body: 3.8 mm. Telescope/Moon/orbit relief: 0.6 mm above the body.
- Back engraving: 0.4 mm deep, including the text, compass and border.
- Print as supplied: **engraved back DOWN, telescope relief UP**.
- The back is mirrored in the model so it reads normally when turned over.
- The front profile is traced from the selected concept, with slight seams opened
  and the outer border reconstructed as a true circular ring. Filament texture,
  shading and the concept image's apparent sculpting are not part of the model.

## Back lettering changes

The designer reported poor S, B and K letters in an earlier medallion's
"ESCAPE BACKPACK" line. The exact printed file, slicer profile and material
are unconfirmed; this report is not a diagnosis of the printer.

- Brand lettering: actual 4.0 mm capital height, replacing the reference's
  2.25 mm capital height. Arial Regular replaces emboldened Arial Bold there.
- Main words: 4.6 mm capital height.
- Wider curved layout: the closest brand letter pair is 0.831 mm apart.
- Brand A/B/P solid centres fit inscribed disks at least 0.939 mm in diameter.
  This is a centre-size measurement, **not** a claim that every gap is 0.939 mm.
- The back text, compass and border stay separated; the text-to-border
  clearance is 1.321 mm.
- Recess depth stays 0.4 mm. The design still requires short underside bridges;
  enlarging the letters cannot guarantee a clean print.

## Starting print setup

Assumption from the shared kit: stock 0.4 mm nozzle on a Prusa i3 MK3S+.
Use your actual printer and filament profiles; this package contains no G-code.

- Use 0.20 mm layers, **including the first layer**.
- Keep automatic supports and raft OFF so they do not fill the engraved recesses.
- Print the dark-blue body first. For yellow relief, add one manual colour change
  immediately before layer 20, Z = 4.00 mm. The body ends at Z = 3.80 mm.
  At these layer settings there are 19 body layers and 3 relief layers.
- The STL does not encode filament colours or the pause.
- Check the first two layers in the slicer's preview: S, B and K grooves should
  be present; the small centres of A, B and P are intentionally solid plastic.
- Also review the first roof over the engraving for short bridging paths.
- Use the calibrated first layer for your printer. First-layer spreading can
  close grooves even when they exist in the mesh. In PrusaSlicer, official
  profiles normally enable elephant-foot compensation; Prusa gives around
  0.2 mm as a typical starting value for a 0.4 mm nozzle. Do not blindly increase it.

Official references:
[First-layer compensation](https://help.prusa3d.com/article/elephant-foot-compensation_114487),
[minimum features and bridges](https://help.prusa3d.com/article/modeling-with-3d-printing-in-mind_164135),
[colour change](https://help.prusa3d.com/article/color-change_1687).

## Low-cost lettering test

`Space_Back_Lettering_Test_1.2mm_v1.stl` is the same 50 mm back at full size
on a 1.2 mm thin disk, without the front relief. Print back DOWN, at 100%, with
the same first-layer and material settings intended for the medallion.
It reproduces the first six 0.20 mm layers of the back/body and needs no
colour change. Check S, B and K before printing the full keepsake.

## Validation and files

Both exported STLs pass edge-closure, winding, connected-solid, non-degenerate
facet and positive-volume checks. Their mesh volumes agree with the analytic
polygon layers. Full model bounds are 50 x 50 x 4.4 mm; test disk is 50 x 50 x 1.2 mm.
The exact geometry preview and normal-reading SVG profiles were visually reviewed.

**No printer-profile slicing or physical test print has been completed.**

- `space-medallion-geometry-preview-v1.png`: exact front/back profile preview.
- `front-relief-v1.svg`, `back-engraving-v1.svg`: 50 mm CAD profiles.
- `geometry_report_v1.json`: dimensions, letter spacing, centre measurements.
- `mesh_check_v1.json`, `lettering_test_mesh_check_v1.json`: exported mesh checks.
- `front_trace_mask_v1.png`: manufacturing-trace intermediate, not new concept art.

Rebuild from the project root with:
`python source/build_space_medallion_v1.py`.
Requires numpy, Pillow, OpenCV, matplotlib and Shapely 2.1+; font outlines use
Windows Arial/Arial Bold. Once exported, the STL needs neither those libraries
nor the fonts to print.
