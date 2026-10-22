---
id: AS-016
title: Shaped constellation cutting sheet
type: asset
status: candidate
kind: print
for: PP-012
tool: ReportLab / Shapely / Poppler
file: assets/shaped-constellations-v1/Constellation_Shaped_Windows_v1.pdf
links: []
superseded_by:
tags: []
---

## Printable prototype - 2026-10-21
One letter sheet holds three 4 x 4 inch opaque cards. Each has one continuous silhouette opening and four corner arrows, including a named reference corner. Aquila has no island or bridge. Print at the same scale as AS-015, cut the outer borders and remove each dashed interior before play. Keep the arrows; use printed side up, with rotation allowed.

Source: source/build_shaped_constellation_puzzle_v1.py. Deterministic vector artwork;
no ImageGen prompt. Build instructions, attribution and limitations are in
assets/shaped-constellations-v1/README.md. Companion PNG and geometry audit are there.

## Verification
One-page letter PDF checked and rendered page visually inspected. All intended window
counts match Q-005. The exhaustive conservative distance-bound search found no
alternative four-corner correspondence when the named corner is on its named star,
at 3 pt star-centre tolerance; arbitrary rotations and reflections are covered.
This digital tolerance is not a measured physical cutting/alignment tolerance.
No physical print, cutting or player test. Candidate artwork; PZ-002 remains untested.
