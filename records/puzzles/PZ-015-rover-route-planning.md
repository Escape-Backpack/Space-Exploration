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
