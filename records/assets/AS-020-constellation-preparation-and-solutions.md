---
id: AS-020
title: Constellation preparation and solutions
type: asset
status: built
kind: print
for: PP-011
tool: ReportLab / Shapely / Poppler
file: output/pdf/constellation-final/03_Preparation_and_Solutions.pdf
links: []
superseded_by:
tags: []
---

## Finished print artwork - 2026-10-21
Designer-only preparation guide and coloured placement key. Covers print scale, preparation, setup, counting, reset and physical testing. Exact dates, observation-note content and final envelope order remain open.

2 US-letter portrait page(s). Print 100% / Actual size, single-sided. Windows
use opaque cardstock; map uses white paper. Source: source/build_constellation_final.py.
Finished PDF artwork is built; physical props and puzzle playtest are not verified.
No ImageGen prompt: deterministic vector art built directly from the existing audit.

## Geometry and verification
Unchanged star positions, shape polygons, four anchor points and physical scale from
the AS-015/AS-016 audited prototype. Counts remain Q-005; ordering remains Q-009.
Same named-anchor condition and 3 pt centre model tolerance apply. This is a unique
correspondence check, not a measured physical cutting or alignment tolerance.

PDF page size/count and text bounds checked; all four finished pages rendered with
Poppler and visually inspected. Rechecked target dot sets and absence of islands or
dots in Aquila's central triangle. PZ-002 remains untested. Source audit hash and
production metadata included in the output directory; optional SVG contains only
exact-scale cutting paths, not the required printed labels/arrows.

HYG v4.1 / David Nash / CC BY-SA 4.0; adapted selected-star chart. Source and licence
links, build requirements and print instructions are in the output README.txt.
