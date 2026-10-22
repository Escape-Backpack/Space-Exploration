---
id: PZ-011
title: Canadarm paper model
type: puzzle
# idea | candidate | decided | built | parked
status: candidate
# The structure beat this puzzle belongs to (one ID)
beat: ST-004
# Props the player needs, e.g. [PP-001]
props: [PP-013, PP-014, PP-010]
# Puzzles that must be solved first, e.g. [PZ-002]
needs: []
# cipher | physical | search | logic | wordplay | other
mechanic: physical
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

## Illustrated observation-page preview - 2026-10-22
AS-043 is a candidate first-page preview of the mixed-clue note: start/first
reading and Test 1 (elbow diagram plus inferred wrist compensation). Tests 2/3
are not yet laid out. Complete instruction log, revised board and printed dials
remain unfinished. No new code, puzzle placement or physical-test evidence.

## Clue development: mixed angles and sketches - 2026-10-22
Designer likes the AS-042 sequential motion but finds six fully explicit commands
too simple. Wants to explore a mix of angles and sketches in the uncle note.
Keep the start and cumulative one-joint-at-a-time mechanism. Exact clue wording,
sketches and difficulty are still proposals, not finalized.

Assistant proposal: a warm three-entry experiment log, with a complete start sketch
and first readout, then one readout after each two-movement entry. Clearly identify
which joint each clue concerns. Mix these six clue forms:
1. Elbow 60 degrees, direction shown by a CCW curved sketch arrow.
2. Wrist compensates by the same amount in the opposite direction (CW 60).
3. Shoulder dial sketch from 90 to 150, CCW (infer 60).
4. Wrist right-angle/quarter-turn sketch with CCW arrow (infer 90).
5. Return elbow to its starting mark (infer CW 60).
6. Wrist/hand sketch faces right, parallel to the board's bottom edge (infer CW 90
   from the state after move 5). Only the wrist adjusts; upstream joints stay fixed.

These interpretations were checked to reproduce all three existing AS-042 checkpoint
joint states. The final hand's absolute direction is horizontal/right. Explicit UP
reference and joint names prevent diagram rotation or joint ambiguity. A small
recording mark after each pair should establish when to read; no number after every
individual motion. The starting sketch must show reference marks needed by clue 5.

No new note PDF/sketch artwork or physical/player test yet. The proposed dial labels
are game calibration values, not real-arm telemetry. Candidate code remains unassigned.

## Smooth sequential movement GIF - 2026-10-22
AS-042 demonstrates the current candidate sequence: shown start, six separate
relative joint turns and three later readouts. Smooth movement, one active joint
setting at a time, and checkpoint pauses per user request. Schematic joint scales
and a redrawn candidate board are included in the GIF; printed pack remains the
older prototype and still needs revision. No final code, dimensions or dial geometry
approved by this animation; test_status remains untested.

## Current direction: starting pose and sequential moves - 2026-10-22
Designer likes the physical arm/readout but rejects the independent paired-sketch
clues. Show a complete starting pose so players can position the arm and read the
first digit, then give a sequence of movements leading to later readout positions.
Continue from the previous state; do not reset for each reading. This supersedes
independent sketch matching as the route to the answer. A starting-pose drawing
remains useful. Designer suggests angles on the arm as a possible aid.

Assistant implementation proposal: degree scales around shoulder, elbow and wrist
pivots with an indicator on the moving link. Commands specify joint, turn amount
and clockwise/counterclockwise direction as seen with printed face up. An upstream
joint turn carries its downstream links; preserve other joint settings. Read only
at marked checkpoints, including the start. No exact scale construction, command
values, checkpoint count, final answer or difficulty newly selected.

A checked candidate example uses four readings: start; elbow CCW 60 and wrist CW
60; shoulder CCW 60 and wrist CCW 90; elbow CW 60 and wrist CW 90. These are examples
for review, not approved clue text. Construction data/checks are in
output/design/canadarm-sequence-v2/candidate-sequence.json. Motion sampled inside
the old board area with constant link lengths and fixed base; four endpoints differ.
The old numbered board does not match these new endpoints and must be redesigned.
Joint scales, physical precision, slack and cumulative error remain untested.

## Earlier independent-pose prototype - retained history
AS-037 and AS-041 show the old paired-sketch mechanism; neither is a finished
implementation of this new sequence. No angle-scale artwork has been built yet.

## Candidate paper prototype - 2026-10-21
AS-037 provides a board, prepared three-link arm and four test pairs across two
observation pages. Each pair shares elbow E, with UP arrows preserving orientation.
The hand's circular reading opening is an assistant proposal to avoid covering the
digit. PP-013/PP-014 hold construction. Geometry and PDF checks passed within the
limited scope documented in AS-037; physical/player tests not performed.

No new puzzle number or prerequisite selected. Candidate digit sequence is designer
only and not stored in answer. publish_hints remains no; test_status remains untested.

## How it works
Designer selects **sketch matching** rather than explicit joint-angle settings
(2026-10-21). Players interpret the uncle's technical drawings to recreate arm poses,
then extract digits from the board using the arm. No numerical angle arithmetic.

The selected approach is decided; exact dimensions, clue layout, digit extraction,
number of poses, final answer, difficulty, puzzle position and packing remain open.
AS-037 is a candidate implementation for review, not an approved final mechanism.

## Clue wording

## Hints
1.

## Solution

## Playtest evidence
<!-- Add dated observations only after a test: version/files tested, physical or
digital, what the player tried, where they stalled, hints used, interpretation,
change made and retest result. After a relevant edit, mark untested again. -->
