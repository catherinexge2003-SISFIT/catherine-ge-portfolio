import math
import unittest

from src.reliability import (
    linear_weighted_kappa,
    percent_agreement,
    unweighted_kappa,
    collect_pairs,
    evaluate_variable,
)


class ReliabilityTests(unittest.TestCase):
    def test_percent_agreement(self):
        self.assertAlmostEqual(percent_agreement([0, 1, 1], [0, 0, 1]), 2 / 3)

    def test_binary_perfect_with_variation(self):
        self.assertAlmostEqual(unweighted_kappa([0, 1, 0, 1], [0, 1, 0, 1]), 1.0)

    def test_constant_perfect_kappa_not_estimable(self):
        value = unweighted_kappa([1, 1, 1], [1, 1, 1])
        self.assertTrue(math.isnan(value))
        self.assertEqual(percent_agreement([1, 1, 1], [1, 1, 1]), 1.0)

    def test_ordinal_uses_fixed_zero_one_two_scale(self):
        # Category 1 is absent, but 0 and 2 must remain two steps apart.
        value = linear_weighted_kappa([0, 2, 0, 2], [0, 2, 2, 2])
        self.assertGreater(value, 0)
        self.assertLess(value, 1)

    def test_safety_boundary_excludes_both_low_risk(self):
        a = {
            "PUB-001": {"risk_relevant": "0", "safety_boundary": "NA"},
            "PUB-002": {"risk_relevant": "1", "safety_boundary": "2"},
        }
        b = {
            "PUB-001": {"risk_relevant": "0", "safety_boundary": "NA"},
            "PUB-002": {"risk_relevant": "1", "safety_boundary": "1"},
        }
        pairs = collect_pairs(a, b, ["PUB-001", "PUB-002"], "safety_boundary")
        self.assertEqual(pairs["structural_excluded"], 1)
        self.assertEqual(pairs["a"], [2])
        self.assertEqual(pairs["b"], [1])

    def test_safety_boundary_logs_risk_gate_disagreement(self):
        a = {"PUB-001": {"risk_relevant": "0", "safety_boundary": "NA"}}
        b = {"PUB-001": {"risk_relevant": "1", "safety_boundary": "2"}}
        pairs = collect_pairs(a, b, ["PUB-001"], "safety_boundary")
        self.assertEqual(pairs["risk_gate_disagreements"], 1)
        self.assertEqual(pairs["structural_excluded"], 1)
        self.assertEqual(pairs["a"], [])

    def test_evidence_na_mismatch_reported(self):
        a = {"PUB-001": {"evidence_traceability": "NA"}}
        b = {"PUB-001": {"evidence_traceability": "1"}}
        result = evaluate_variable(a, b, ["PUB-001"], "evidence_traceability")
        self.assertEqual(result["na_mismatch"], 1)
        self.assertEqual(result["n"], 0)
        self.assertTrue(math.isnan(result["kappa"]))


if __name__ == "__main__":
    unittest.main()
