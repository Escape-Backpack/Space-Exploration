---
id: PZ-015
title: Rover route planning
type: puzzle
# idea | candidate | decided | built | parked
status: candidate
# The structure beat this puzzle belongs to (one ID)
beat:
# Props the player needs, e.g. [PP-001]
props: [PP-015]
# Puzzles that must be solved first, e.g. [PZ-002]
needs: []
# cipher | physical | search | logic | wordplay | other
mechanic: logic
# 1 (easy) to 3 (hard)
difficulty:
# 4-5 characters the cipher can encode (see backpack.json). The envelope it opens is marked
# with the matching symbols; props with envelope: <this ID> go inside.
answer:
# What players call this puzzle on the hint page, e.g. "The luggage tag" (spoiler-free)
hint_title:
# Explicit opt-in for the PUBLIC hint page. Candidates are never published.
publish_hints: no
# Independent of design/build status: untested | passed | changes-needed
test_status: untested
# physical | digital (a digital walkthrough does not verify a physical prop)
test_method:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It is then hidden unless the board's "parked" filter is on.
superseded_by:
tags: []
---

## Current grid prototype v2 - 2026-10-28
User requests a new map using the selected sun/cargo/slopes/radiation rules and the proposed orthogonal movement/pickup details. AS-062 player map, AS-063 preview and AS-064 designer key replace the first trail-network map. Fictional 7-column x 6-row terrain grid; 32 traversable cells, four samples (100/100/100/200 g), four radiation cells, ten sun cells and three directed slope borders. Candidate capacity75; not a designer-selected final capacity. All four samples required, start A6, finish G1. Keep answer blank and publish_hints no.

Implementation rules printed on sheet: no diagonal moves, blocked cells, square revisits, waiting recharge or sample dropping. Pay 1 plus carried grams/100 BEFORE entering a square; must afford entire cost. Then sun gives+1 capped75. Pickup on arrival; new weight counts from next move. Entered radiation square adds1 rover exposure and1 to each sample already aboard; limits2 rover/1 eachsample. Arrows restrict crossing only their specific shared border; all other open shared borders bidirectional. These are prototype implementation choices explicitly stated for review; no repair shelter.

Exhaustive stateful DFS with no arbitrary length cutoff finds exactly1 valid route. Five removal checks confirm rule effects: no sun credit0 routes; no cargo penalty2; no radiation limits14; rover radiation limit only3; ignore arrows6. Geometry/data output/design/rover-grid-v2/grid.json; validator source/validate_rover_grid_v2.py; builder source/build_rover_grid_v2.py; PDF/PNG/ledger output/pdf/rover-grid-v2/. The valid21-move route uses75netenergy, arrives0, rover2exposures. Samples4 and2 each exposedonce,6 and7 zero. Candidate pickup code4267 replaces the old illustrative4726 but remains unassigned.

Player sheet is Landscape Letter with native Handlee11.5/12pt instruction text, labelled cell coordinates, symbol+colour terrain, weights and slope arrows. Designer key has route on page1 and per-move resource ledger on portraitLetter page2. All three final pages rendered and visually inspected; native text bounds checked. Studio binaries uploaded/download-byte-verified. No physical/player test; test_status stays untested. Review complexity/bookkeeping and terrain art before final production.

Earlier versions below are historical where they conflict with this revision.


## Grid-route revision - 2026-10-28
Designer likes the route-planning idea but rejects the first map execution and requests more detail/complexity. Selected additions: sunlight/shade, sample weight, one-way slopes, radiation. Repair shelter rejected; do not add a repair/reset point. No new map produced yet.

## Selected rule direction
- Grid-based travel: moving one square uses 1 battery unit before cargo penalties.
- Start with a full battery. Maximum capacity still unset.
- Traversing a sun area gives +1 battery, capped at maximum capacity. Exact trigger (per entered square or per area crossed) and spend/charge timing remain unspecified.
- Every 100 g of carried samples adds 1 battery usage per square. Sample weights and rounding for nonmultiples of 100 g remain unspecified; propose multiples of 100 g for simplicity, not yet a decision.
- One-way slopes permitted as a route constraint; arrow direction must be unambiguous. No selected layout yet.
- Rover may be exposed to radiation at most twice; each individual sample may be exposed at most once. Track exposure separately for each sample already collected; no shelter/repair reset. Exposure trigger (square or area traversal), pickup timing and sample handling still need clear definitions.

## Consequences and open engineering details
If sun supplies +1 per movement and recharge applies after spending movement energy, it offsets the base cost: empty rover net 0 in sun vs 1 shade; carrying100 g net1 vs2; carrying200 g net2 vs3. It does not replenish the moving rover's battery on net. This is a conditional arithmetic observation, not a selected event-timing rule. Clarify if actual net recharging is desired rather than reduced drain. No waiting/loitering recharge rule selected.

Next prototype must specify orthogonal vs diagonal movement, radiation exposure units, sunlight trigger/timing, pickup rules and whether revisits are allowed. Old v1 no-revisit/no-recharge/12-unit/2-or4 trail-cost rules do not automatically carry forward. Site count, capacity, masses, extraction and route uniqueness must be engineered and checked together. Old candidate4726 is obsolete as evidence for the revised rules, answer stays blank, untested and hints unpublished. Scientific realism of radiation/cargo rules is simplified game behaviour, not a factual Mars claim.

Earlier prototype descriptions below are historical where they conflict with this revision.


## Current prototype - 2026-10-28
User requests a map with instructions to review. Candidate PP-015 supplies a fictional Mars trail network with lander start, station finish, four flagged sample sites and three ordinary junctions. Normal trails cost 2 battery units, rocky trails 4. Budget 12; visit all four sample sites, never revisit a location, finish at station. No recharging or off-trail travel. Read the large sample-site digits in visit order; small boxed numbers are travel costs. Costs cover a whole section between connected locations, in either direction. These are prototype rules, not newly approved final decisions.

Builder: source/build_rover_route_v1.py. Exhaustive enumeration of all simple start-to-finish paths finds nine that visit all sample sites; exactly one costs at most 12. Next cheapest costs 14. Audit: output/pdf/rover-route-v1/route-audit.json. Player and designer PDFs rendered and inspected; native text bounds/page size checked. Digital graph uniqueness is not a physical or player playtest. Keep test_status untested, answer blank and publish_hints no.

## Candidate solution - designer only
Lander > Basalt (4) > Crater Rim (7) > Ridge (2) > Dry Channel (6) > Station.
Costs 2+2+2+4+2 = 12. Candidate extraction 4726 is not an assigned game answer. Designer key shows the route separately from the player sheet.

## Next review
Review whether the small network is interesting enough, whether battery constraints feel natural, and whether to keep instructions on the map or later move them to a Sky Observations page. No new finale marks, game placement or envelope assigned.

## Earlier concept


## How it works
Designer selects route planning as the next puzzle to develop (2026-10-28). Rover theme is an initial proposal; no map, route rules, code, puzzle position, dimensions or props selected. Keep separate from PZ-012, the historical rover-track Morse idea; this does not replace it.

Starting proposal for discussion: a printed terrain map and Bob's mission note. Plan a route from a landing site to a destination, visiting required sample sites and avoiding impassable terrain, with a limited movement budget. Players must choose between alternative routes; it should not become another set of explicit movement commands like PZ-011. Route extraction should follow naturally from visited locations; exact method and number of digits remain open. All constraints and costs must be supplied in the game; no outside Mars knowledge required.

Before artwork, select the constraints, build a small route graph, and verify that exactly one route meets them. No unique route or physical/player test yet.

## Clue wording

## Hints
1.

## Solution

## Playtest evidence
<!-- Add dated observations only after a test: version/files tested, physical or
digital, what the player tried, where they stalled, hints used, interpretation,
change made and retest result. After a relevant edit, mark untested again. -->
