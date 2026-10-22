---
id: AS-015
title: Opening constellation player chart
type: asset
status: candidate
kind: print
for: PP-011
tool: ReportLab / Shapely / Poppler
file: assets/shaped-constellations-v1/Star_Chart_Player_v1.pdf
links: []
superseded_by:
tags: []
---

## Printable prototype - 2026-10-21
One monochrome letter portrait chart, with real catalogue positions at one common scale. No constellation outlines or highlighted answer stars. Vega, Deneb and Altair are named starting points for AS-016. Selected background stars are omitted where necessary; no catalogue positions are relocated.

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
