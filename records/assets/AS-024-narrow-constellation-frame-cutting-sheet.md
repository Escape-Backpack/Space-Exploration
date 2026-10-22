---
id: AS-024
title: Constellation frames - current cutting PDF
type: asset
status: built
kind: print
for: PP-012
tool: ReportLab / Shapely / Poppler
file: assets/space-puzzle-01-frame-cutting-sheet.pdf
links: []
superseded_by:
tags: []
---

## Studio-hosted file - 2026-10-21
The current PDF is uploaded to Studio file storage and verified byte-for-byte
against output/pdf/constellation-frames-v2/02_Constellation_Frames.pdf. Local production output remains unchanged.
The file field now points to the Studio-served asset so the online download works.


## Revised product - 2026-10-21
Letter cutting sheet containing three silhouette frames. Retained band follows the entire single opening at 7.5 mm width. Each frame bears only its constellation name and generic MAIN STAR label, plus four corner arrows. No actual star names and no rectangular card surrounds. All three frames fit simultaneously on AS-021. Print on opaque cardstock, then cut outer solid contours and dashed interiors. Keep arrows and labels. No Aquila island or bridge.

Source: source/build_constellation_frames_v2.py. Deterministic vector artwork, no
ImageGen prompt. README, optional exact-scale SVG cutting paths and geometry audit
are in the output directory. The SVG omits required printed arrows and text.

## Geometry and checks
One uniform 18% enlargement of the v1 catalogue geometry enables the full-width bands
to fit together on the square board. No stars/groups moved independently. Square
crop removes background stars only; all selected target nodes retained (Q-005).
All target dot sets, no-island construction and Aquila's empty central triangle
rechecked. Outer frames disjoint and within the board; minimum outer clearance about
0.52 mm between Lyra/Cygnus. Hand cutting and simultaneous physical fit need testing.

Named-anchor correspondence condition is unchanged, but pairings now appear on the
uncle note instead of the frames. Prior conservative pair-distance audit remains
applicable at 3 pt centre tolerance after enlargement/cropping; no physical tolerance
or playtest pass claimed. PDF page/text bounds checked and all four rendered pages
visually reviewed. PZ-002 remains untested; exact dates/final code order unassigned.

HYG v4.1 / David Nash / CC BY-SA 4.0; adapted selected-star chart. Shared under the
same licence; URLs in package README and designer guide.
