---
id: AS-080
title: Constellation cutouts - solution GIF (flyer chart)
type: asset
status: built
kind: image
for:
tool: Python / Pillow / PyMuPDF / Shapely
file: assets/constellation-solution-v2.gif
links: [PZ-002, AS-078, AS-081]
superseded_by:
tags: []
---

Designer solution animation for PZ-002 only. Not a player clue or public hint. Replaces AS-077,
which showed the old 8 x 8 chart.

Frames are placed in the uncle's night order (Q-009): Lyra, Cygnus, Aquila. Visible stars are counted
one at a time from the main star, and the counts fill the slots. The last screen shows envelope 698.
Built from the real flyer chart PDF (AS-078) and the exact frame geometry. The script asserts the
visible stars match 6 / 9 / 8. 79 encoded frames, about 26 seconds, 594 x 1147 px, looping, 1.8 MB.
Source: source/build_constellation_solution_gif_v2.py. Digital animation only, not a playtest.
