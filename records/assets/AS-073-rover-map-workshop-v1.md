---
id: AS-073
title: Rover map workshop - configurable offline editor
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
file: assets/rover-map-workshop-v1.html
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-015]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

Uploaded in the Studio by Claude.

Designer tool requested2026-10-28, not a player clue/public hint. Self-contained HTML with Design and Test modes. Separate5–10 row/column dropdowns; optional shared start/finish; layered sun/shade/radiation/flat/uphill/downhill/cliff brushes; optional directional border arrows;4sample markers with manually editable100g-step weights; configurable maximum battery, solar credit, rover exposure and per-sample exposure limits.

New selected rule: uphill uses2x battery; downhill uses0. Implementation convention displayed in editor: destination square determines terrain cost; multiply the entire loaded movement cost before any solar credit. Sun/radiation are independent overlays. Downhill entry is possible at0battery and solar credit can recharge to configuredcap. Startfull; revisits allowed; pickup once/damage retained. Test finish ends mission only when all4samples are aboard (passing through earlier allowed); sharedbase requires leaving/returning. No new shortest-route objective or arbitrary no-revisit rule.

Click/drag painting, protected markers, undo/redo design edits, autosave, strict JSON save/load, example-map reset and blankmap. Resizing preserves overlapping terrain and exposes cropped sample markers as unplaced; base/backupfinish coordinates clamp safely. Same stable sample inputs preserve focus when editing consecutive fields. Play mode has livebattery/radiation/weight, per-sample damage, buttons/arrows/WASD/clicks, undo/reset and moveledger. No automatic unique-route claim.

Template source/rover-map-editor.html; builder source/build_rover_map_editor.py. Output/html/rover-map-editor/index.html; README and original-puzzle.json alongside. Optional localpreview http://127.0.0.1:8768/rover-map-editor/index.html. File opensoffline withnoexternalresources. Autosave follows browser/origin; JSON is portablebackup. Current fixedmap v4 is defaultseed; editing does not overwrite the approved/pending printablemap or automatically synchronize userdesigns intoStudio.

Browser regression tmp/test_rover_map_editor.cjs passed: all5–10 dimensions, layeredbrushes/clickdrag/undo, arrows andclear, weights/markers/configlimits, sharedbase andrestoredfinish, resize/clamp/reload, autosave, JSONdownload/import/invalidrejection, original14-moveledger, loadeduphillcost, zerobatterydownhill, cappedsolar/downhillcharging, repeatedpickups/radiation, keyboard, mobile5x5play and10x10design nooverflow, noJSerrors. Desktopdesign/play andmobileplay renders inspected. Fixed an inputfocus bug andmobiletableoverflow beforefinalQA. These softwarechecks do notcountasphysical/playerplaytesting.

Actual HTML uploaded; served appcontent verified after excluding hostingCloudflarebeacon/whitespace transforms. Localfilehasnoinjectedbeacon. Kept AS-072 fixedmap playground separately; this editor does not supersede the printablemapassets.
