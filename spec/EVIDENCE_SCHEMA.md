# CIGCS Evidence Record Format

Each executed proof case produces a deterministic evidence record.

## Required Fields

- case_id
- category
- timestamp
- expected_result
- actual_result
- pass_fail
- failure_reason
- invariants_checked
- render_attempted
- render_blocked
- boundary_status

## Determinism Rule

Given identical inputs, evidence records MUST be identical.

No stochastic behavior is permitted.
