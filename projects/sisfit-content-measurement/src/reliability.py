"""Calculate inter-rater reliability for the SISFIT content coding study."""

from pathlib import Path
import argparse
import csv
import math
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
CODING = ROOT / "coding"

BINARY_VARIABLES = [
    "purpose_clear",
    "risk_relevant",
    "self_monitoring_prompt",
    "commercial_call_to_action",
]

ORDINAL_VARIABLES = [
    "plain_language",
    "evidence_traceability",
    "actionability",
    "uncertainty_calibration",
    "causal_claim_strength",
    "safety_boundary",
    "behavior_change_support",
]


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["content_id"]: row for row in csv.DictReader(handle)}


def parse_score(value):
    value = (value or "").strip()
    if not value or value.upper() == "NA":
        return None
    return int(value)


def percent_agreement(a, b):
    if not a:
        return float("nan")
    return sum(x == y for x, y in zip(a, b)) / len(a)


def unweighted_kappa(a, b):
    n = len(a)
    if n == 0:
        return float("nan")

    categories = sorted(set(a) | set(b))
    observed = percent_agreement(a, b)

    ca = Counter(a)
    cb = Counter(b)
    expected = sum((ca[c] / n) * (cb[c] / n) for c in categories)

    if math.isclose(1 - expected, 0):
        return float("nan")

    return (observed - expected) / (1 - expected)


def linear_weighted_kappa(a, b):
    n = len(a)
    if n == 0:
        return float("nan")

    categories = sorted(set(a) | set(b))
    if len(categories) == 1:
        return float("nan")

    index = {category: i for i, category in enumerate(categories)}
    max_distance = len(categories) - 1

    observed_disagreement = 0.0
    for x, y in zip(a, b):
        observed_disagreement += abs(index[x] - index[y]) / max_distance
    observed_disagreement /= n

    ca = Counter(a)
    cb = Counter(b)

    expected_disagreement = 0.0
    for x in categories:
        for y in categories:
            weight = abs(index[x] - index[y]) / max_distance
            expected_disagreement += (
                (ca[x] / n) * (cb[y] / n) * weight
            )

    if math.isclose(expected_disagreement, 0):
        return float("nan")

    return 1 - (observed_disagreement / expected_disagreement)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--coder1",
        default=str(CODING / "coder1.csv"),
        help="CSV file for coder 1",
    )
    parser.add_argument(
        "--coder2",
        default=str(CODING / "coder2.csv"),
        help="CSV file for coder 2",
    )
    args = parser.parse_args()

    coder1 = read_csv(Path(args.coder1))
    coder2 = read_csv(Path(args.coder2))

    shared_ids = sorted(set(coder1) & set(coder2))

    if not shared_ids:
        raise RuntimeError("No shared content_id values between coder files.")

    print(f"Shared coded units: {len(shared_ids)}")
    print()

    for variable in BINARY_VARIABLES + ORDINAL_VARIABLES:
        a = []
        b = []

        for content_id in shared_ids:
            x = parse_score(coder1[content_id].get(variable))
            y = parse_score(coder2[content_id].get(variable))

            if x is None or y is None:
                continue

            a.append(x)
            b.append(y)

        agreement = percent_agreement(a, b)

        if variable in ORDINAL_VARIABLES:
            kappa = linear_weighted_kappa(a, b)
            metric = "linear-weighted kappa"
        else:
            kappa = unweighted_kappa(a, b)
            metric = "Cohen kappa"

        print(
            f"{variable}: n={len(a)}; "
            f"agreement={agreement:.1%}; "
            f"{metric}={kappa:.3f}"
        )


if __name__ == "__main__":
    main()
