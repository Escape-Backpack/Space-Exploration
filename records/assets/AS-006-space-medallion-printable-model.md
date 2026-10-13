---
id: AS-006
title: Space medallion printable model
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-003
# Generator or tool used
tool: Python CAD (Shapely, OpenCV, matplotlib, numpy)
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/medallion/Space_Medallion_OnePiece_v1.stl
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [AS-004]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Printable model

Created on 2026-10-05 at the designer's request, using the selected AS-004 front.
The builder traces the concept's yellow profile and creates an exact one-piece
solid with an engraved back. This asset is built as a digital model; the physical
medallion is not yet recorded as built or tested.

Builder: `source/build_space_medallion_v1.py`.
Print instructions and all dimensions: `assets/medallion/README.md`.
Package: `assets/medallion/Space_Medallion_Print_Files_v1.zip`.
Preview: `assets/medallion/space-medallion-geometry-preview-v1.png`.
Back-only trial: `assets/medallion/Space_Back_Lettering_Test_1.2mm_v1.stl`.
CAD profiles and measured geometry/mesh reports are in the same directory.

## Lettering review

On 2026-10-05 the designer approved this digital design and requested that its
back lettering be reused for the Norse and Hiking medallions. This approval
does not record a successful physical print.

The designer reported poor S, B and K letters in "ESCAPE BACKPACK" on an
earlier medallion print. The exact file and printer settings were not provided.
The new model enlarges the brand line, uses a more open font, removes the old
outline thickening there, and spreads out both lower text arcs. The actual
curved glyph distances are checked, rather than assuming nominal character
spacing equals a clear physical gap.

No font change is claimed to fix an unconfirmed first-layer or bridging problem.
A matching thin test disk is provided for a physical check before the full print.

## Validation evidence

Both exported STLs passed closed-edge, winding, connected-component,
non-degenerate-facet and positive-volume checks. Exported mesh volume agreed
with the analytic polygon layers. Back-text clearances passed measured guards.
The exact front/back profile preview was visually reviewed, including separate
lower-arc glyphs and normally readable back text.

No printer-profile slicing or physical test was performed. See the JSON reports
for the checks and the README for the assumed nozzle/layer setup.
