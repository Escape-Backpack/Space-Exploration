---
id: AS-074
title: Rover cartographic style concept - Churchill-inspired preview
type: asset
# idea | candidate | decided | built | parked
status: candidate
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-015
# Generator or tool used
tool:
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/rover-cartographic-style-v1.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

Uploaded in the Studio by Claude.

Style concept requested2026-10-29, not an approved finalmap replacement. User asks for moredetailed map like recentlycreated Churchillmap. Reference inspected: C:/EscapeBackpack/Canada-Exploration/assets/churchill-map/Churchill_Map_v7_Preview.png; copied its continuous-terrain cartography, mutedpalette, thin grid, small white-rimmed locationbadges, compass and separatelegend into fictional Mars geography.

Same fixedv4 5x5 game layout: samplecoordinates/weights, start/finish, sun/radiation/blockedcells and directionalborders retained. Added decorative craters, windcontours, drychannels and mergedcliffplateaus; landforms add no movementrules. Explicit cliff×badges and radiationhatching/sunicons preserve rule readability. No new uphill/downhillcells invented. Native vectorart, not ImageGen. Preview rendered in Chromium and visually inspected.

Builder source/build_rover_styled_map_v1.py; local output/design/rover-cartographic-v1/ has SVG,2100x1680PNG, previewHTML andstyle-audit.json. ActualPNG/SVG uploaded/download-hashverified. Editor AS-073 and playerPDFAS-069 unchanged pending style feedback. No physical/player test.
