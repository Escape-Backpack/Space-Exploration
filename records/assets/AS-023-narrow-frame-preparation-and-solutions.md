---
id: AS-023
title: Narrow-frame preparation and solutions
type: asset
status: built
kind: print
for: PP-011
tool: ReportLab / Shapely / Poppler
file: output/pdf/constellation-frames-v2/04_Preparation_and_Key.pdf
links: []
superseded_by:
tags: []
---

## Sequence correction - 2026-10-21
Designer now identifies the constellation activity as puzzle two (PZ-002 current
section). The guide's setup sentence about providing materials at the start is an
older prototype assumption, not settled packing for the revised sequence. Use
AS-025 for the revised note instead of AS-022. Map/frame geometry is unchanged.

## Revised product - 2026-10-21
Designer preparation instructions and reduced simultaneous-placement key for AS-021/AS-024, with AS-022 clue note. Covers custom page sizing, matching print scale, cut contours, reset and test gaps. Keep separate from player materials.

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
