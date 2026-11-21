---
id: AS-077
title: Constellation cutouts - solution GIF
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for:
# Generator or tool used
tool: Python / Pillow / PyMuPDF / Shapely
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/constellation-solution-v1.gif
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-002, AS-021, AS-024, AS-023]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-080
tags: []
---

Designer solution animation for PZ-002 only. Not a player clue or public hint.

Shows the frames placed in the uncle's night order (Q-009): Lyra, then Cygnus, then
Aquila. Each frame slides onto the chart, the visible stars are counted one at a time
from the main star, and the count fills its slot. The final screen shows envelope 698.

Built from the real printed chart (AS-021, rendered from 01_Star_Chart_8in.pdf) and
the exact frame geometry in geometry-audit-v2.json (AS-024). The script asserts that
the stars inside each opening match the counts 6 / 9 / 8.

Source: source/build_constellation_solution_gif_v1.py. Output also in
output/gif/constellation-solution-v1/ with a final-frame PNG.
79 encoded frames, about 26 seconds, 760 x 1010, looping, 1.8 MB.

Digital animation only. It is not evidence of a physical playtest.
