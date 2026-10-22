---
id: AS-019
title: Final constellation window cards
type: asset
status: built
kind: print
for: PP-012
tool: ReportLab / Shapely / Poppler
file: output/pdf/constellation-final/02_Constellation_Windows.pdf
links: []
superseded_by:
tags: []
---

## Finished print artwork - 2026-10-21
Finished player cutting sheet with three 4 x 4 inch cards. Each has four retained arrows, a named starting corner, one continuous dashed opening and brief alignment/counting instructions. All three fit on one letter sheet. The upper cards share one outer edge.

1 US-letter portrait page(s). Print 100% / Actual size, single-sided. Windows
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
