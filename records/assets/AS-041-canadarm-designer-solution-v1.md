---
id: AS-041
title: Canadarm designer solution animation - prototype
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
file: assets/canadarm-designer-solution-v1.gif
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-011]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-042
tags: []
---

## Earlier solution animation - 2026-10-22
This GIF solves the old independent-pose prototype. It illustrates the physical
arm/readout the designer likes, but is not a walkthrough of the newly requested
starting-pose and sequential-command clue. Use PZ-011 for the current direction.

## Designer solution GIF - 2026-10-22
User requests an animated GIF of the Canadarm solution. This loops through all four
candidate poses, shows each pair of partial sketches, keeps the base fixed and reads
the successive digits through the hand aperture. It ends on the complete candidate
sequence and loops. Designer-only solution reference; not a player clue or public hint.
No final answer has been assigned to PZ-011 and physical test_status is unchanged.

Source: source/build_canadarm_solution_gif_v1.py. Uses exact positions and lengths
from output/pdf/canadarm-sketch-v1/geometry-audit.json, not new game geometry.
Local output: output/gif/canadarm-solution-v1/Canadarm_Solution.gif.
Frame snapshots, four-pose visual check and animation-audit.json are alongside.
Native deterministic diagram animation; no ImageGen or video tool used.

## Verification
Reopened GIF: 41 frames, 16.52 seconds, 1000 x 1190 px, infinite loop. Verified base
and three link lengths on every frame, exact intended hand centres at the four holds,
and total encoded duration. All four poses, first and final frames visually reviewed.
Uploaded to Studio and downloaded back with matching SHA-256. Physical movement,
joint friction/slack and player interpretation remain untested.
