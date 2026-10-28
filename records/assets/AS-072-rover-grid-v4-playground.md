---
id: AS-072
title: Rover grid v4 - interactive playground with revisits
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: text
# The prop this asset is for (one ID)
for:
# Generator or tool used
tool:
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/rover-grid-v4-playground.html
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-015]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

Uploaded in the Studio by Claude.

Current designer HTML simulator, not a player clue/public hint. Existing standalone output/html/rover-playground/index.html refreshed in place. Supports revisits, repeated terrain effects, samplepickup once, preserved damage; liveKPIs, keyboard/buttons/clicks, undo/reset andlog. No designer solution embedded. Browser regression tmp/test_rover_playground_v4.cjs passed.
See PZ-015 for current rules/checks. PDF source/build_rover_grid_v4.py; HTML source/build_rover_playground.py; validator source/validate_rover_grid_v4.py. All finalPDFpages rendered/inspected; HTMLbrowserchecked. Studio PDFs/PNG download hashes verified; HTMLcontent verified after excluding hosting beacon/whitespace changes. No physical/player playtest.
