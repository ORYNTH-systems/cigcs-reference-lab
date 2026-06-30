class ConsistencyEngine:

    def evaluate(self, admissibility, safety, render_boundary):

        if safety is None:
            return {
                "consistent": False,
                "reason": "safety_indeterminate"
            }

        if admissibility is True and safety is False:
            return {
                "consistent": False,
                "reason": "admissibility_safety_conflict"
            }

        if admissibility is True and render_boundary is False:
            return {
                "consistent": False,
                "reason": "render_boundary_missing"
            }

        if admissibility is True and safety is True and render_boundary is True:
            return {
                "consistent": True,
                "reason": "all_constraints_satisfied"
            }

        return {
            "consistent": False,
            "reason": "constitutional_constraints_not_satisfied"
        }
