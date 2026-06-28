from consistency import ConsistencyEngine
from typing import Dict, Any


class CIGCSEvaluator:

    def __init__(self):
        self.consistency = ConsistencyEngine()

    def evaluate_admissibility(self, case: Dict[str, Any]) -> bool:
        glyph = case.get("glyph", {})
        constraints = case.get("constraint_set", {})

        if not glyph.get("glyph_id"):
            return False

        if glyph.get("canonical_hash") is None:
            return False

        if constraints.get("admissible") is False:
            return False

        return True

    def evaluate_safety(self, case: Dict[str, Any]) -> bool:
        safety = case.get("safety_predicate", {})

        if safety.get("safe") is False:
            return False

        if safety.get("safe") is None:
            return None  # important: indeterminate

        return True

    def evaluate_render_boundary(self, case: Dict[str, Any]) -> bool:
        artifact = case.get("artifact", {})

        if not artifact.get("present"):
            return False

        return True

    def evaluate_case(self, case: Dict[str, Any]) -> Dict[str, Any]:

        A = self.evaluate_admissibility(case)
        S = self.evaluate_safety(case)
        V = self.evaluate_render_boundary(case)

        C = self.consistency.evaluate(A, S, V)

        blocked = not (A and S and V and C["consistent"])
        admitted = (A and S and V and C["consistent"])

        return {
            "case_id": case.get("case_id"),
            "admissibility": A,
            "safety": S,
            "render_boundary": V,
            "consistency": C,
            "blocked": blocked,
            "admitted": admitted,
            "reason": C["reason"],
            "expected": case.get("expected_result"),
            "expected_reason": case.get("expected_reason"),
            "pass": (case.get("expected_result") == ("admitted" if admitted else "blocked"))
        }

