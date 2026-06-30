import json
import os
import hashlib
from evaluator import CIGCSEvaluator

class CIGCSEngine:

    def __init__(self):
        self.chain = []
        self.evaluator = CIGCSEvaluator()

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

    def evaluate(self, case):
        return self.evaluator.evaluate_case(case)

    def perturb(self, case):
        return json.loads(json.dumps(case))

    def stability(self, case):
        base = self.evaluate(case)
        pert = self.evaluate(self.perturb(case))
        return 0 if base == pert else 1

    def delta(self, case):
        if not (self.A(case) and self.S(case) and self.V(case) and self.C(case)):
            return "BLOCK"

        if self.stability(case) > 0:
            return "QUARANTINE"

        return "PASS"

    def expected_state(self, case):
        expected = case.get("expected_result")

        if expected == "admitted":
            return "PASS"

        if expected == "blocked":
            return "BLOCK"

        if expected == "quarantine":
            return "QUARANTINE"

        return None

    def load_cases(self, case_dir):
        loaded = []

        for root, dirs, files in os.walk(case_dir):
            for file in files:
                if not file.endswith(".json"):
                    continue

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
                    case = json.load(f)

                loaded.append((path, case))

        loaded.sort(key=lambda item: item[1].get("case_id", item[0]))
        return loaded

    def write_reports(self, output):
        os.makedirs("reports/json", exist_ok=True)
        os.makedirs("reports/metrics", exist_ok=True)

        with open("reports/json/cigcs_execution_results.json", "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)

        metrics_lines = [
            "# CIGCS Execution Metrics",
            "",
            f"Total Cases: {output['summary']['total_cases']}",
            f"PASS: {output['summary']['PASS']}",
            f"BLOCK: {output['summary']['BLOCK']}",
            f"QUARANTINE: {output['summary']['QUARANTINE']}",
            f"Expected Matches: {output['summary']['expected_matches']}",
            f"Expected Mismatches: {output['summary']['expected_mismatches']}",
            f"Integrity Chain Length: {output['integrity_chain_length']}",
            f"Status: {output['status']}",
            ""
        ]

        with open("reports/metrics/CIGCS_EXECUTION_METRICS.md", "w", encoding="utf-8") as f:
            f.write("\n".join(metrics_lines))

    def run_all(self, case_dir):
        results = []
        cases = self.load_cases(case_dir)

        summary = {
            "total_cases": 0,
            "PASS": 0,
            "BLOCK": 0,
            "QUARANTINE": 0,
            "expected_matches": 0,
            "expected_mismatches": 0
        }

        for path, case in cases:
            result_state = self.delta(case)
            expected = self.expected_state(case)
            expected_match = expected == result_state

            evaluator_result = self.evaluate(case)

            evidence = {
                "case_id": case.get("case_id"),
                "path": path.replace("\\", "/"),
                "state": result_state,
                "expected_state": expected,
                "expected_match": expected_match,
                "evaluator": evaluator_result
            }

            h = hashlib.sha256(json.dumps(evidence, sort_keys=True).encode()).hexdigest()
            self.chain.append(h)
            evidence["hash"] = h

            summary["total_cases"] += 1
            summary[result_state] += 1

            if expected_match:
                summary["expected_matches"] += 1
            else:
                summary["expected_mismatches"] += 1

            results.append(evidence)

        output = {
            "summary": summary,
            "results": results,
            "integrity_chain_length": len(self.chain),
            "status": "DELTA_ADVERSARIAL_ENGINE_ACTIVE"
        }

        self.write_reports(output)
        return output
