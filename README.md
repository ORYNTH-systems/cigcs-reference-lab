# CIGCS Reference Lab

This repository contains the public reference proof corpus for the Constraint-Integrated Glyphic Control System (CIGCS).

CIGCS demonstrates render-boundary enforcement for governed glyph representations produced by adaptive interface sources.

The repository is documentation-first and implementation-neutral. It does not disclose proprietary implementation internals.

## Current Status

Milestone 1 is locked.

- CB-001 through CB-010
- Render Boundary Enforcement
- 10 blocked render attempts
- 0 unauthorized renders

## Proof Corpus

The full corpus is organized as 100 deterministic proof cases.

Each case defines a render-governance condition, expected outcome, failure reason, and invariant coverage.

## Repository Structure

- `cases/` — canonical proof case definitions
- `docs/` — proof schema and doctrine notes
- `reports/` — proof and evidence libraries
- `reports/json/` — reserved for structured evidence exports
- `spec/` — public specification references
- `release/` — release notes and archival summaries
- `src/` — intentionally empty placeholder; no executable implementation is disclosed

## License

See `LICENSE`.
