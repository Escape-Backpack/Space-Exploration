---
id: AS-022
title: Uncle constellation main-star note
type: asset
status: candidate
kind: print
for: PP-010
tool: ReportLab / Shapely / Poppler
file: output/pdf/constellation-frames-v2/03_Uncles_Note_4x6.pdf
links: []
superseded_by:
tags: []
---

## Revised product - 2026-10-21
Candidate handwritten note on the selected 4 x 6 observation form. Supplies the main-star pairings for the frames: Lyra/Vega, Cygnus/Deneb, Aquila/Altair. Gives four-corner alignment/counting instructions. Date/time/location deliberately blank; this is not yet the dated count-order clue. Wording is an assistant draft for review, not a newly approved final clue.

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
