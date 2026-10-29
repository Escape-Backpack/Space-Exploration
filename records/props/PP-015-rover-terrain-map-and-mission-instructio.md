---
id: PP-015
title: Rover terrain map and mission instructions
type: prop
# idea | candidate | decided | built | parked
status: candidate
# physical | printed | digital
form: printed
# make | buy | print | 3d-print
source: print
# Where the player finds it: start (loose in the box) or the puzzle whose answer opens its envelope, e.g. PZ-004
envelope:
# On the public reset page: return (back in its envelope) | keep (the team takes it home) | none (not mentioned). Blank = return.
after_game:
# Name on the public reset page, if the title isn't what players call it (optional)
reset_name:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It is then hidden unless the board's "parked" filter is on.
superseded_by:
tags: []
---

## Cartographic style proposal - 2026-10-29
AS-074 (preview) / AS-075 (nativeSVG) explore the Churchillmap visualstyle on the unchanged fixedv4 roverlayout. More continuous landforms, mutedMars palette, crater/contour details, iconbadges, compass andlegend. This is a requested proposal forreview, not a chosen replacement forAS-069 or mapeditorAS-073.


## Revisits allowed - current v4, 2026-10-28
PZ-015 now permits revisiting squares. Updated player map AS-069 and preview AS-070 replace v3. New designer example AS-071 removes unique-path claims; current HTML AS-072 allows backtracking and only collects each sample once without resetting damage. Physical map, capacity, samplemasses and costs unchanged. Print100%/Actualsize; no playtest or envelope assignment.

Earlier no-revisit rules and unique-path claims below are superseded.


## Current 30-unit grid v3 - 2026-10-28
Current map AS-065/preview AS-066 are the30-unit redesign requested by the designer.5x5grid,73ptcells, LandscapeLetter. Designer key AS-067 includes14-step battery/cargo/radiation ledger. Exact current rules/validation are in PZ-015. Old AS-062/063/064 superseded; previous75-unit sheet not current. Print100%/Actualsize. No physical/player test or envelope assignment.

Earlier versions below are historical where they conflict with this revision.


## Current grid prototype v2 - 2026-10-28
Current sheet AS-062 and preview AS-063 implement the grid rules in PZ-015. Landscape Letter11x8.5in, seven by six61ptcells, map on left and Bob mission instructions on right. Print at100%/Actual size. Radiation marked R/RAD, sun icon, blocked rockytexture and directional border arrows supplement colour. Four circle digits with100/200g labels. AS-064 is designer-only with route/ledger. Old AS-059/060/061 superseded. Final capacity/dimensions/layout/art remain candidate; no playtest or envelope assigned. Sources and digital verification are in PZ-015.

Earlier versions below are historical where they conflict with this revision.


## Grid-route revision - 2026-10-28
PZ-015 now defines the selected grid-route direction (sunlight, cargo mass, one-way slopes, rover/sample radiation limits; no repair shelter). Existing AS-059/060 player map and AS-061 key remain only the earlier trail-network prototype and do not implement these rules. Revised map/instructions not yet built; do not use v1 validation as evidence for new rules.

Earlier prototype descriptions below are historical where they conflict with this revision.


## Prototype - 2026-10-28
One Letter portrait sheet containing a fictional Mars survey trail map, legend and Bob's instructions. Player version: output/pdf/rover-route-v1/Rover_Terrain_Map_and_Instructions.pdf; PNG preview alongside. Native vector paths and IBM Plex Mono labels, native Handlee 12 pt mission text. Print at 100% / Actual size; no cutting or movable props required. Final dimensions, artwork style and packing remain proposals. Map is schematic fictional terrain, not an actual Mars navigation map.

## Rules and validation
See PZ-015 for candidate rules; designer-only solution PDF and exhaustive route audit are in output/pdf/rover-route-v1/. Player sheet has no highlighted solution. Two trail styles distinguish normal and rocky costs even without colour. All paths are bidirectional; locations are graph vertices. No off-trail travel or repeated location visits. Physical/player testing not performed.

## Reset
Return the map to its eventual envelope; envelope assignment not selected. If players mark routes, use a spare copy or reusable sleeve.
