# CIGCS Proof Schema

Each CIGCS proof case is a deterministic evidence object demonstrating whether a governed glyph render transition is admitted or blocked at the render boundary.

## Required Fields

- case_id
- title
- category
- expected_result
- expected_reason
- invariants

## Result Semantics

`blocked` means the render transition is refused before effectuation.

`admitted` means the render transition is permitted only after admissibility, safety, artifact validity, and boundary verification succeed.

## Milestone 1 Scope

Cases CB-001 through CB-010 establish the Render Boundary Enforcement doctrine.

Milestone 1 demonstrates that no glyph can render when the render boundary is missing, bypassed, invalid, expired, unsigned, mismatched, or indeterminate.

## Invariant Coverage

- Invariant 3 — Fail-Closed Invalid State Handling
- Invariant 7 — No Bypass of Enforcement
- Invariant 8 — Render Requires Valid Authorization Artifact
