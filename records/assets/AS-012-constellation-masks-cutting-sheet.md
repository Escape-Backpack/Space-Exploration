---
id: AS-012
title: Constellation masks - cutting sheet
type: asset
status: candidate
kind: print
for: PP-012
tool: ReportLab / NumPy / Poppler
file: assets/constellation-cutouts-v1/Inuit_Constellation_Cutouts_Letter_v1.pdf
links: []
superseded_by:
tags: []
---

## Output
One-page cutting sheet. Preview: cutouts-preview.png. Remove main windows and all three small sights per card before play.

## Source and reproduction
Built by source/build_constellation_cutouts_v1.py from the pinned local catalogue
subset source/star-chart-v1/bright-stars-hyg-v41.json. Deterministic vector drawing;
no ImageGen illustration or generation prompt. Layout, cutting and player rules live
in the prop record. Full geometry in assets/constellation-cutouts-v1/geometry-audit-v1.json.

HYG v4.1 by David Nash: https://github.com/astronexus/HYG-Database . Catalogue subset
and adapted projected chart data shared under CC BY-SA 4.0. Source attribution,
modifications and reproduction commands are in assets/constellation-cutouts-v1/README.md.

## Checks - 2026-10-21
One-page letter media box (612 x 792 pt), embedded IBM Plex Mono fonts, selectable text.
PDF text bounds checked; rendered page visually reviewed using Poppler. All three
masks have unique ringed-reference-star fits at the documented 4 pt centre tolerance.
Both alternative triples and swapped correspondences have side-distance lower bounds
above that threshold; rotation/reflection included. The intended counting windows
contain exactly the selected 2, 7 and 3 stars. This is digital geometry evidence only.
No physical print, hand-cutting, tolerance, opacity or gameplay test performed.

## Scope
Prototype art remains candidate pending designer review. The dated observation note
and final code order are not made. No public hints or envelope labels were generated.
