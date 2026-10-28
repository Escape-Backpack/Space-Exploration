---
id: AS-068
title: Rover grid v3 - interactive offline playground
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
file: assets/rover-grid-v3-playground.html
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-015]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-072
tags: []
---

Uploaded in the Studio by Claude.

Designer testing tool, not a player clue or public hint. Self-contained offline HTML mirrors AS-065 map and PZ-015 rules. Live battery, rover radiation, cargo and per-sample exposure; direction buttons, arrow/WASD keys or adjacent-square clicks; undo/reset, automatic sample pickup, slope and energy checks, no revisits, success/failure and route log. No designer solution bundled.

Template source/rover-playground.html; builder source/build_rover_playground.py; standalone output/html/rover-playground/index.html. Opens offline in a browser with no dependencies. Optional preview http://127.0.0.1:8767/index.html while local preview server runs.

Headless Chrome/Playwright helper tmp/test_rover_playground.cjs verifies every solution step against the v3 ledger, direction UI/keyboard/clicks, solar credit/weights, slopes, revisits, blocked cells, undo/reset, success and rover radiation failure. Controlled browser fixtures also test sample-specific radiation failure and insufficient battery. Mobile390px layout has no horizontal overflow; no browser JS errors. Desktop screenshot inspected. Software checks do not count as a paper/player playtest.

HTML uploaded to Studio. Hosting injects a Cloudflare beacon and transforms whitespace, so strict served-byte hash check did not match. Local offline file has no beacon or network resources. Served application-content comparison after removing beacon/whitespace: True.
