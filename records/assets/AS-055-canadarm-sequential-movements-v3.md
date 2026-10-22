---
id: AS-055
title: Canadarm A and B sequence - smooth solution GIF
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for:
# Generator or tool used
tool:
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/canadarm-sequential-movements-v3.gif
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-011]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

Uploaded in the Studio by Claude.

Designer solution animation only, not a player clue or public hint. Replaces AS-042.
Five selected A/B movements, one relative joint at a time, with three uncalibrated
free C sweeps to find the unique reachable number. Four readings including start.
Matches the AS-053 printable board rendered directly into animation. Candidate
5938 remains unassigned. All four aperture centres match board target centres;
constant link lengths, fixed base/upstream positions and single-joint changes checked.
230 encoded frames, 30.55 seconds, 900 x 1120, looping, smooth quintic easing,
50 ms motion frames. Four checkpoint renders visually inspected. Joint scales
are illustrative; no physical/player test. Uploaded/downloaded bytes verified.
Source: source/build_canadarm_sequence_gif_v3.py.
Local: output/gif/canadarm-sequence-v3/Canadarm_Sequential_Movements.gif.
Audit and checkpoint inspection PNG alongside GIF. Note and arm cutting sheet
still need later revision; this update changes only designer animation.
