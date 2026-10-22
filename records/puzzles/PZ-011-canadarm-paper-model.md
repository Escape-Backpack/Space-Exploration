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
