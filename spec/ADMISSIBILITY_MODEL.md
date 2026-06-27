# CIGCS Admissibility Model

## Purpose

Defines the formal rule system for determining whether a glyph is admissible prior to render authorization.

This model sits between:
- Glyph generation (candidate state)
- Render authorization (boundary gate)

It is an independent evaluation layer.

---

## 1. Admissibility Definition

A glyph ? is admissible under constraint set G if and only if:

A(?, G) = 1

where:

- A is a deterministic evaluation function
- G is a finite constraint set
- ? is a canonical glyph representation

---

## 2. Constraint Semantics

Each constraint in G is:

- binary (true/false)
- conjunctive (ALL must pass)
- deterministic (no probabilistic evaluation)

Failure of any constraint ? A(?, G) = 0

---

## 3. Failure Modes

Admissibility fails under:

- missing required glyph fields
- invalid schema structure
- undefined glyph identifiers
- malformed canonical representation
- constraint violation
- evaluation indeterminacy

Indeterminacy is treated as failure (fail-closed).

---

## 4. Relationship to Render Boundary

Admissibility is required but not sufficient for render.

Render requires:

- A(?, G) = 1
- Safety predicate = 1
- Valid RAA
- Boundary verification success

---

## 5. Theoretical Position

Admissibility is a governance layer over state existence.

It answers:

> “Is this state allowed to exist at all under current constraints?”

not:

> “Can it be executed?”

---

## 6. Milestone Scope

CB-011 ? CB-020 instantiate this model.

Each case represents one admissibility failure or success condition.
