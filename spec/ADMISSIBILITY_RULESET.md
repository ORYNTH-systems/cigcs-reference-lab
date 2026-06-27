# CIGCS Admissibility Ruleset

## Constraint Definition

A constraint is a deterministic boolean function evaluated against a canonical glyph representation.

## Evaluation Rule

A(?, G) = 1 only if ALL constraints evaluate to TRUE under conjunctive evaluation.

If ANY constraint fails ? A(?, G) = 0

## Failure Classification

- schema_invalid ? structural mismatch
- missing_field ? incomplete glyph
- constraint_violation ? rule failure
- indeterminate ? fail-closed
- unknown_identifier ? rejection

## Determinism Rule

All evaluations must be:

- deterministic
- stateless
- repeatable
- independent of execution order
