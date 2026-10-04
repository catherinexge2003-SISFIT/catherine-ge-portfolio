"""Small deterministic tests for the reliability helper functions."""

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "reliability.py"

spec = importlib.util.spec_from_file_location("reliability", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol


assert module.parse_score("NA") is None
assert module.parse_score("") is None
assert module.parse_score("2") == 2

assert close(module.percent_agreement([0, 1, 1], [0, 0, 1]), 2 / 3)

# Perfect agreement with variation should produce kappa = 1.
assert close(module.unweighted_kappa([0, 1, 0, 1], [0, 1, 0, 1]), 1.0)
assert close(module.linear_weighted_kappa([0, 1, 2, 1], [0, 1, 2, 1]), 1.0)

# A non-perfect ordinal example should remain bounded.
value = module.linear_weighted_kappa([0, 1, 2, 2], [0, 1, 1, 2])
assert -1.0 <= value <= 1.0

print("reliability tests: PASS")
