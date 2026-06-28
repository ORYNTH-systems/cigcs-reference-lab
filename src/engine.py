import json
import os
import hashlib

class CIGCSEngine:

    def __init__(self):
        self.chain = []

    # -------------------------
    # CORE CONSTRAINTS
    # -------------------------

    def A(self, case):
        return "case_id" in case

    def S(self, case):
        return case.get("safety_predicate", {}).get("safe", False) is True

    def V(self, case):
        return case.get("artifact", {}).get("present", False) is True

    def C(self, case):
        return not (
            case.get("safety_predicate", {}).get("safe") is False and
            case.get("constraint_set", {}).get("admissible") is True
        )

    # -------------------------
    # ADVERSARIAL PERTURBATION
    # -------------------------

    def perturb(self, case):
        # deterministic "stress transform"
        return json.loads(json.dumps(case))  # structural clone

    def stability(self, case):
        base = self.evaluate(case)
        pert = self.evaluate(self.perturb(case))
        return 0 if base == pert else 1

    # -------------------------
    # ? OPERATOR (FORMALIZED)
    # -------------------------

    def delta(self, case):

        if not (self.A(case) and self.S(case) and self.V(case) and self.C(case)):
            return "BLOCK"

        if self.stability(case) > 0:
            return "QUARANTINE"

        return "PASS"

    # -------------------------
    # EXECUTION ENGINE
    # -------------------------

    def run_all(self, case_dir):

        results = []

        for file in os.listdir(case_dir):
            if not file.endswith(".json"):
                continue

            with open(os.path.join(case_dir, file), "r") as f:
                case = json.load(f)

            result_state = self.delta(case)

            evidence = {
                "case_id": case.get("case_id"),
                "state": result_state
            }

            h = hashlib.sha256(str(evidence).encode()).hexdigest()
            self.chain.append(h)

            evidence["hash"] = h

            results.append(evidence)

        return {
            "results": results,
            "integrity_chain_length": len(self.chain),
            "status": "DELTA_ADVERSARIAL_ENGINE_ACTIVE"
        }
