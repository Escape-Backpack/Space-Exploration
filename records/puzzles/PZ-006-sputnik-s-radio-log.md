---
id: PZ-006
title: Sputnik's radio log
type: puzzle
# idea | candidate | decided | built | parked
status: candidate
# The structure beat this puzzle belongs to (one ID)
beat: ST-006
# Props the player needs, e.g. [PP-001]
props: []
# Puzzles that must be solved first, e.g. [PZ-002]
needs: []
# cipher | physical | search | logic | wordplay | other
mechanic: counting
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
links: [PZ-012]
# Set to an ID when this record is replaced. It is then hidden unless the board's "parked" filter is on.
superseded_by:
tags: []
---

## How it works
Designer choices - 2026-10-21:
- **Decoding: count beeps on two tracks.** The beeps come in groups; the number of beeps
  in each group is one digit. The tape has two tracks, one per Sputnik frequency. A note
  from the uncle tells players which frequency his receiver picked up, so only that
  track's groups count. The other track is the decoy.
- **Prop form: paper tape strip.** A long narrow strip, like a chart recorder printout,
  rolled up.

- **Track labels: wavelength bands.** The tape labels its tracks "15 m band" and
  "7.5 m band", not by frequency. The uncle's note gives the frequency (20 MHz), and a
  formula he sketched, wavelength (m) = 300 / frequency (MHz), lets players convert:
  300 / 20 = 15 m, so the 15 m track counts. Chosen over frequency labels (too direct)
  and unlabelled tracks read from a radio-dial drawing.
  Check: 300 / 20.005 = 14.996 m and 300 / 40.002 = 7.4996 m, so 15 m and 7.5 m are fair.

Chosen over: short/long as binary, gap timing with a printed ruler, and Morse digits.
Choosing counting also removes this puzzle's overlap with the Morse idea in PZ-012.

Illustrative only (from the option preview, not a decided answer or wording):
top track 4-2-7-3 beeps, bottom track different counts, note "My receiver only picked
up 20 MHz."

## Story facts (checked 2026-10-21)
- Sputnik 1 carried two transmitters, on 20.005 MHz and 40.002 MHz.
- A 1957 account describes 0.3-second pulses, each followed by a pause of similar length
  during which the other frequency transmitted. So on a real recording the two tracks
  alternate: one track's beep sits in the other track's gap.
- The batteries ran out on 26 October 1957; sources differ on 21 or 22 days of signal.
- Sources: Wikipedia "Sputnik 1"; Radio & TV News, February 1958 (rfcafe.com reprint).

## Open
- The answer (4-5 digits) and the decoy track's counts.
- Where the wavelength formula sketch lives (on the note, near a drawing of his radio,
  or on the tape) and its exact wording.
- Whether the tape shows the real alternating timing, and how groups are separated so
  players can tell where one digit ends.
- The note's exact wording and where it lives (an observation page PP-010, the tape
  itself, or elsewhere). Whose receiver it was in 1957 (the uncle's age is not set).
- Tape length, printing and rolling; difficulty; which envelope holds the tape.

## Clue wording

## Hints
1.

## Solution

## Playtest evidence
<!-- Add dated observations only after a test: version/files tested, physical or
digital, what the player tried, where they stalled, hints used, interpretation,
change made and retest result. After a relevant edit, mark untested again. -->
