"""Pre-adjudication inter-rater reliability for the SISFIT content coding study.

Formal use: two independent HUMAN coder files completed against the frozen
30-item set and codebook v0.2. AI rehearsal ratings are not formal inputs.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import csv
import math

ROOT = Path(__file__).resolve().parents[1]

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

ALL_VARIABLES = BINARY_VARIABLES + ORDINAL_VARIABLES
FIXED_ORDINAL_SCALE = (0, 1, 2)


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing coder file: {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No coding rows found in {path}")
    if "content_id" not in rows[0]:
        raise ValueError(f"{path} is missing content_id")
    return rows


def rows_by_id(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    ids = [str(row.get("content_id", "")).strip() for row in rows]
    blanks = [i for i, value in enumerate(ids, start=2) if not value]
    if blanks:
        raise ValueError(f"{label}: blank content_id at CSV rows {blanks}")
    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    if duplicates:
        raise ValueError(f"{label}: duplicate content_id values: {duplicates}")
    return {row["content_id"].strip(): row for row in rows}


def load_manifest_ids(path: Path) -> list[str]:
    rows = read_csv_rows(path)
    ids = [str(row["content_id"]).strip() for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Manifest contains duplicate content_id values")
    return ids


def raw(value) -> str:
    return str(value or "").strip().upper()


def parse_score(value):
    value = raw(value)
    if not value or value == "NA":
        return None
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"Score must be integer or NA; got {value!r}") from exc


def validate_coder(mapping: dict[str, dict[str, str]], expected_ids: list[str], label: str):
    if set(mapping) != set(expected_ids):
        missing = sorted(set(expected_ids) - set(mapping))
        extra = sorted(set(mapping) - set(expected_ids))
        raise ValueError(f"{label}: ID mismatch; missing={missing}; extra={extra}")

    errors = []
    for content_id in expected_ids:
        row = mapping[content_id]
        for variable in ALL_VARIABLES:
            value = raw(row.get(variable))
            if variable in BINARY_VARIABLES:
                allowed = {"0", "1"}
            elif variable == "evidence_traceability":
                allowed = {"0", "1", "2", "NA"}
            elif variable == "safety_boundary":
                allowed = {"0", "1", "2", "NA"}
            else:
                allowed = {"0", "1", "2"}
            if value not in allowed:
                errors.append(f"{content_id}:{variable}={value!r}")

        rr = raw(row.get("risk_relevant"))
        sb = raw(row.get("safety_boundary"))
        if rr == "0" and sb != "NA":
            errors.append(f"{content_id}: risk_relevant=0 requires safety_boundary=NA")
        if rr == "1" and sb not in {"0", "1", "2"}:
            errors.append(f"{content_id}: risk_relevant=1 requires safety_boundary 0/1/2")

    if errors:
        raise ValueError(label + " validation failed: " + "; ".join(errors))


def percent_agreement(a: list[int], b: list[int]) -> float:
    if not a:
        return float("nan")
    return sum(x == y for x, y in zip(a, b)) / len(a)


def unweighted_kappa(a: list[int], b: list[int]) -> float:
    n = len(a)
    if n == 0:
        return float("nan")
    categories = sorted(set(a) | set(b))
    observed = percent_agreement(a, b)
    expected = 0.0
    for category in categories:
        pa = sum(x == category for x in a) / n
        pb = sum(y == category for y in b) / n
        expected += pa * pb
    if math.isclose(1.0 - expected, 0.0):
        return float("nan")
    return (observed - expected) / (1.0 - expected)


def linear_weighted_kappa(
    a: list[int],
    b: list[int],
    scale: tuple[int, ...] = FIXED_ORDINAL_SCALE,
) -> float:
    n = len(a)
    if n == 0:
        return float("nan")

    index = {value: i for i, value in enumerate(scale)}
    if any(x not in index for x in a + b):
        raise ValueError("Ordinal score outside fixed codebook scale")

    max_distance = len(scale) - 1
    observed_disagreement = sum(
        abs(index[x] - index[y]) / max_distance for x, y in zip(a, b)
    ) / n

    expected_disagreement = 0.0
    for x in scale:
        pa = sum(v == x for v in a) / n
        for y in scale:
            pb = sum(v == y for v in b) / n
            distance = abs(index[x] - index[y]) / max_distance
            expected_disagreement += pa * pb * distance

    if math.isclose(expected_disagreement, 0.0):
        return float("nan")
    return 1.0 - observed_disagreement / expected_disagreement


def decision(kappa: float) -> str:
    if math.isnan(kappa):
        return "inspect_non_estimable"
    if kappa >= 0.70:
        return "retain"
    if kappa >= 0.60:
        return "review"
    return "revise_or_drop"


def collect_pairs(
    coder_a: dict[str, dict[str, str]],
    coder_b: dict[str, dict[str, str]],
    ids: list[str],
    variable: str,
):
    a, b = [], []
    both_na = 0
    na_mismatch = 0
    structural_excluded = 0
    risk_gate_disagreements = 0

    for content_id in ids:
        row_a = coder_a[content_id]
        row_b = coder_b[content_id]

        if variable == "safety_boundary":
            risk_a = parse_score(row_a.get("risk_relevant"))
            risk_b = parse_score(row_b.get("risk_relevant"))

            if risk_a != risk_b:
                risk_gate_disagreements += 1
                structural_excluded += 1
                continue

            if risk_a == 0 and risk_b == 0:
                structural_excluded += 1
                continue

        x = parse_score(row_a.get(variable))
        y = parse_score(row_b.get(variable))

        if x is None and y is None:
            both_na += 1
            continue
        if (x is None) != (y is None):
            na_mismatch += 1
            continue

        a.append(x)
        b.append(y)

    return {
        "a": a,
        "b": b,
        "both_na": both_na,
        "na_mismatch": na_mismatch,
        "structural_excluded": structural_excluded,
        "risk_gate_disagreements": risk_gate_disagreements,
    }


def evaluate_variable(coder_a, coder_b, ids, variable):
    pairs = collect_pairs(coder_a, coder_b, ids, variable)
    a, b = pairs["a"], pairs["b"]
    agreement = percent_agreement(a, b)

    if variable in ORDINAL_VARIABLES:
        kappa = linear_weighted_kappa(a, b)
        metric = "linear_weighted_cohen_kappa"
    else:
        kappa = unweighted_kappa(a, b)
        metric = "cohen_kappa"

    return {
        "variable": variable,
        "n": len(a),
        "agreement": agreement,
        "metric": metric,
        "kappa": kappa,
        "decision": decision(kappa),
        "both_na": pairs["both_na"],
        "na_mismatch": pairs["na_mismatch"],
        "structural_excluded": pairs["structural_excluded"],
        "risk_gate_disagreements": pairs["risk_gate_disagreements"],
    }


def fmt(value, digits=3):
    if isinstance(value, float) and math.isnan(value):
        return "NA"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_results(results: list[dict], output_dir: Path, coder_a_path: Path, coder_b_path: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "reliability_by_variable.csv"
    fields = [
        "variable", "n", "agreement", "metric", "kappa", "decision",
        "both_na", "na_mismatch", "structural_excluded",
        "risk_gate_disagreements",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in results:
            clean = row.copy()
            clean["agreement"] = fmt(clean["agreement"], 6)
            clean["kappa"] = fmt(clean["kappa"], 6)
            writer.writerow(clean)

    md_path = output_dir / "reliability_report.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Pre-Adjudication Human Inter-Rater Reliability\n\n")
        handle.write(f"- Coder A file: `{coder_a_path.name}`\n")
        handle.write(f"- Coder B file: `{coder_b_path.name}`\n")
        handle.write("- Codebook: SISFIT Content Measurement Codebook v0.2\n")
        handle.write("- Reliability set: frozen PUB-001 to PUB-030\n")
        handle.write("- Calculated before adjudication/discussion\n\n")
        handle.write("| Variable | n | Agreement | Metric | Kappa | Decision | NA mismatch | Structural excluded | Risk-gate disagreements |\n")
        handle.write("|---|---:|---:|---|---:|---|---:|---:|---:|\n")
        for row in results:
            handle.write(
                f"| {row['variable']} | {row['n']} | "
                f"{fmt(row['agreement'] * 100, 1) if not math.isnan(row['agreement']) else 'NA'}% | "
                f"{row['metric']} | {fmt(row['kappa'])} | {row['decision']} | "
                f"{row['na_mismatch']} | {row['structural_excluded']} | "
                f"{row['risk_gate_disagreements']} |\n"
            )
        handle.write("\n## Interpretation rules\n\n")
        handle.write(
            "The retain/review/revise labels use the project's pre-specified internal "
            "development rules and are not universal psychometric thresholds. A non-estimable "
            "kappa must be interpreted alongside agreement and category variation.\n"
        )
        handle.write(
            "\nFor safety_boundary, the primary denominator includes only items where both "
            "coders independently classified risk_relevant=1 and supplied non-NA safety scores.\n"
        )

    return csv_path, md_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coder-a", required=True)
    parser.add_argument("--coder-b", required=True)
    parser.add_argument(
        "--manifest",
        default=str(ROOT / "coding" / "human_reliability_manifest.csv"),
    )
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / "results" / "human_reliability"),
    )
    args = parser.parse_args()

    coder_a_path = Path(args.coder_a)
    coder_b_path = Path(args.coder_b)
    manifest_path = Path(args.manifest)

    expected_ids = load_manifest_ids(manifest_path)
    if len(expected_ids) != 30:
        raise ValueError(f"Formal reliability manifest must contain 30 IDs; got {len(expected_ids)}")

    coder_a = rows_by_id(read_csv_rows(coder_a_path), "Coder A")
    coder_b = rows_by_id(read_csv_rows(coder_b_path), "Coder B")
    validate_coder(coder_a, expected_ids, "Coder A")
    validate_coder(coder_b, expected_ids, "Coder B")

    results = [
        evaluate_variable(coder_a, coder_b, expected_ids, variable)
        for variable in ALL_VARIABLES
    ]

    csv_path, md_path = write_results(
        results,
        Path(args.output_dir),
        coder_a_path,
        coder_b_path,
    )
    print(f"Validated shared human-coded units: {len(expected_ids)}")
    print(f"Wrote: {csv_path}")
    print(f"Wrote: {md_path}")


if __name__ == "__main__":
    main()
