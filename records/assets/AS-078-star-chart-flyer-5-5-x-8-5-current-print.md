---
id: AS-078
title: Star chart flyer 5.5 x 8.5 - current printable PDF
type: asset
status: built
kind: print
for: PP-011
tool: ReportLab / Shapely / PyMuPDF
file: assets/space-puzzle-01-star-chart-flyer-5.5x8.5.pdf
links: [PZ-002, PR-010, AS-024]
superseded_by:
tags: []
---

Replaces the 8 x 8 chart AS-021 so the player chart is a standard flyer size (PR-010).

Plain 5.5 x 8.5 inch chart: catalogue dots, graticule and the three reference-star labels only.
Print at Actual size (100%), centred on letter paper, and trim. Word print file:
print/Print_Space_StarChart_Flyer_5.5x8.5.docx (local print master, same structure as the Raven files).
Preview: assets/space-puzzle-01-star-chart-flyer-5.5x8.5-preview.png.

## What changed from AS-021
- The frames (AS-024) are unchanged: same positions, same 18% enlargement, same 7.5 mm bands.
  Together they measure 4.51 x 7.79 in, so no shrinking was needed.
- The chart is a 396 x 612 pt window around the frames, with about 0.49 in side and 0.36 in
  top/bottom margin around them. Stars from AS-021 inside the window are identical.
- 15 catalogue stars were added in the strips above and below the old square. Nothing was
  dropped to keep a single fit.
- 281 stars on the chart in total.

## Digital checks (build_flyer_chart_v1.py)
- Stars in each opening: Lyra 6, Cygnus 9, Aquila 8 (the selected nodes only).
- Same unique-placement audit as before (four marks, 3 pt centre tolerance, named main star
  required): zero alternative fits for all three frames. Aquila's central triangle has no dots.
- Frames are disjoint and at least 0.25 in from the chart edge. Page size and text checked.

Source: source/build_flyer_chart_v1.py (audit in output/pdf/constellation-flyer-v1/geometry-audit-flyer-v1.json).
Digital only. No physical print or player test; PZ-002 remains untested.
Chart: HYG v4.1 / David Nash / CC BY-SA 4.0, adapted selection and projection.
