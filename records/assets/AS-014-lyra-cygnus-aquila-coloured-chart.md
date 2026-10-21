---
id: AS-014
title: Lyra Cygnus Aquila - coloured chart
type: asset
status: candidate
kind: print
for: PP-011
tool: ReportLab / Poppler
file: assets/lyra-cygnus-aquila-v1/Lyra_Cygnus_Aquila_Colour_Chart_v1.pdf
links: []
superseded_by:
tags: []
---

## Requested update - 2026-10-21
One letter portrait reference chart, with selected Lyra/Cygnus/Aquila outlines in
green/blue/red. One common gnomonic projection (RA 19.6h, declination +27 deg), east
left, same scale for all stars; no independently enlarged fields. Uses the existing
HYG v4.1 catalogue subset (David Nash, CC BY-SA 4.0), with a selected background and
simplified close companions. Exact membership and edges are in
assets/lyra-cygnus-aquila-v1/selected-stars-v1.json. Q-005 specifies the selected counts.

Source: source/build_lyra_cygnus_aquila_v1.py. Preview PNG is next to the PDF with the
same base name. This is a deterministic vector chart, with no ImageGen prompt.
Constellation selection is decided; this particular layout remains candidate.

## Checks
All selected HIP identifiers resolved to the catalogue; asserted plotted node counts
match Q-005. One-page letter PDF and group names verified. Poppler render visually
reviewed. Existing masks do not apply to the new projection/trio. No physical print,
mask fitting or playtest. No final code order or dated observation text assigned.

## Interpretation
Counts apply to the chosen diagram, not every star in the IAU boundaries. Epsilon,
zeta and delta Lyrae each have one plotted node for the selected system/component;
nearby faint companions are not separate answer dots. Iota/kappa Cygni are retained.
This colour sheet is for designer review, not an answer-hidden player map.
