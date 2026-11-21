---
id: AS-081
title: Constellation frames - cutting sheet, spread for cutting
type: asset
status: built
kind: print
for: PP-012
tool: ReportLab / Shapely / PyMuPDF
file: assets/space-puzzle-01-frame-cutting-sheet-spread.pdf
links: [PZ-002, AS-078, AS-079]
superseded_by:
tags: []
---

Current frame cutting sheet for PZ-002. Replaces AS-024 so the frames are easy to cut at home.

The three frames are spread apart on one Letter page instead of sitting in their final fitted
positions (which left only about 0.5 mm between Lyra and Cygnus). Each frame is only moved, never
rotated or resized: same shapes, 7.5 mm bands, arrows and labels as AS-024. Gaps between frames:
Cygnus/Aquila 37 mm, Lyra/Cygnus 66 mm, Lyra/Aquila 87 mm. All frames are at least 0.5 in from the
page edge. The page says they are spread apart and still fit together on the chart.

Print on opaque cardstock at 100% / Actual size and check the 1 inch scale bar. Cut the outer solid
lines and remove the dashed insides. Word print file: print/Print_Space_ConstellationFrames.docx.
The fitted positions are shown on the designer key (AS-079) and in the solution GIF (AS-080).
Preview: assets/space-puzzle-01-frame-cutting-sheet-spread-preview.png.

Source: source/build_frames_cutting_sheet_v2.py (moves in output/pdf/constellation-frames-spread-v2/layout.json).
Digital check only: frame geometry reused unchanged from geometry-audit-v2.json, spacing and page bounds
asserted. No physical print or cut test; PZ-002 remains untested.
