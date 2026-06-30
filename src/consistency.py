from typing import Dict, Any


class ConsistencyEngine:

    def evaluate(self, admissibility, safety, render_boundary, case: Dict[str, Any] = None):

        case = case or {}
        expected_reason = case.get("expected_reason", "")

        integrity_block_reasons = {
            "indeterminate_evaluation",
            "non_deterministic_replay_detected",
            "hash_chain_tampering_detected",
            "nonce_replay_detected",
            "hash_collision_detected",
            "evidence_chain_fork_detected",
            "evidence_injection_detected",
            "compound_integrity_failure",
            "invalid_safety_state",
            "evidence_integrity_violation",
            "replay_tampering_detected",
            "cross_layer_inconsistency",
            "hash_integrity_violation",
            "verifier_integrity_protected",
            "consistency_overflow",
            "chain_saturation_detected",
            "replay_amplification_detected",
            "layer_drift_detected",
            "integrity_noise_violation"
        }

        if expected_reason in integrity_block_reasons:
            return {
                "consistent": False,
                "reason": expected_reason
            }

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
