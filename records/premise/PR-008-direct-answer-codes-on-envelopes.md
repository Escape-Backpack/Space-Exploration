---
id: PR-008
title: Direct answer codes on envelopes
type: premise
status: decided
aspect: other
links: []
superseded_by:
tags: []
---

## Current - 2026-11-20
The designer chose numbered envelopes: each envelope shows its puzzle's 3 or 4 digit
answer. backpack.json is migrated to plain digits 0-9, answer lengths 3-4, 2 decoys.
The tooling follow-through below is done.

## Designer decision - 2026-10-21
Space uses printed documents and envelopes. Each envelope is marked with the correct
answer code the players should have found. There is no cipher, symbol translation,
lookup card or cipher wheel between solving a puzzle and selecting its envelope.
This supersedes the provisional planet-symbol direction described in Q-008.

This decision does not settle the opening answer/order, permitted code lengths,
number of envelopes or decoy design. Scope today is the observation page (PP-010).

## Tooling follow-through
The shared kit still calls envelope encoding a cipher. backpack.json still has its
old planets preset; that configuration and generated label/help views need a separate
migration to direct codes before envelope production. Do not print the old symbol labels
or a cipher card for this version. No shared-kit changes were made in this layout session.
