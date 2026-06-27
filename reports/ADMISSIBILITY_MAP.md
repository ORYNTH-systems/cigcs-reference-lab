# CIGCS Admissibility Map

## Purpose

This document maps admissibility evaluation outcomes across CB-011 to CB-020.

It aligns constraint violation classes with invariant behavior and evidence output.

---

## CB-011 ? CB-020 Scope

| Case | Category | Outcome |
|------|----------|--------|
| CB-011 | Valid admissibility | admitted |
| CB-012 | Single constraint violation | blocked |
| CB-013 | Missing glyph field | blocked |
| CB-014 | Schema invalidity | blocked |
| CB-015 | Indeterminate evaluation | blocked |
| CB-016 | Unknown glyph identifier | blocked |
| CB-017 | Invalid pose state | blocked |
| CB-018 | Disallowed asset identifier | blocked |
| CB-019 | Disallowed classification | blocked |
| CB-020 | Multi-violation collapse | blocked |

---

## Governance Alignment

Admissibility is the precondition layer that determines whether a glyph is eligible for authorization.

Render boundary enforcement (Milestone 1) assumes admissibility has already been evaluated.

Together they form a two-stage enforcement pipeline:

1. Admissibility Predicate (CB-011–CB-020)
2. Render Boundary Enforcement (CB-001–CB-010 already established execution-side enforcement)
