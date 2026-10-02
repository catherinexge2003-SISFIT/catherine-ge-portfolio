"""Ordinal sensitivity analysis for the HINTS 7 project.

Retains the original four-level SocMed_MakeDecisions response and fits a
survey-weighted proportional-odds model. JK1 replicate weights are used for
the focal exposure coefficient variance.

This sensitivity model uses a reduced covariate parameterisation to keep the
custom proportional-odds likelihood stable and auditable.
"""

from pathlib import Path
import math

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit
from scipy.stats import norm


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "hints7_public.dta"


def main() -> None:
    df = pd.read_stata(DATA, convert_categoricals=False)

    variables = [
        "SocMed_TrueFalse",
        "SocMed_MakeDecisions",
        "ConfidentMedForms",
        "AgeGrpB",
        "Education",
        "RaceEthn5",
        "IncomeRanges_IMP",
        "BirthSex",
        "Electronic2_HealthInfo",
    ]

    for variable in variables:
        df[variable] = df[variable].where(df[variable] > 0)

    df["hard_to_judge"] = np.where(
        df["SocMed_TrueFalse"].isin([1, 2]),
        1,
        np.where(df["SocMed_TrueFalse"].isin([3, 4]), 0, np.nan),
    )

    df["searched_health_info"] = np.where(
        df["Electronic2_HealthInfo"] == 1,
        1,
        np.where(df["Electronic2_HealthInfo"] == 2, 0, np.nan),
    )

    # Reverse HINTS coding so higher values indicate stronger agreement/use.
    df["decision_ord"] = np.where(
        df["SocMed_MakeDecisions"].isin([1, 2, 3, 4]),
        5 - df["SocMed_MakeDecisions"],
        np.nan,
    )

    required = [
        "decision_ord",
        "hard_to_judge",
        "AgeGrpB",
        "Education",
        "RaceEthn5",
        "IncomeRanges_IMP",
        "BirthSex",
        "ConfidentMedForms",
        "searched_health_info",
        "PERSON_FINWT0",
    ]

    analysis = df.dropna(subset=required).copy()

    design = pd.DataFrame(
        {
            "hard_to_judge": analysis["hard_to_judge"].astype(float),
            "age": analysis["AgeGrpB"].astype(float),
            "education": analysis["Education"].astype(float),
            "income": analysis["IncomeRanges_IMP"].astype(float),
            "medforms": analysis["ConfidentMedForms"].astype(float),
            "searched_health_info": analysis["searched_health_info"].astype(float),
            "female_birth": (analysis["BirthSex"] == 2).astype(float),
        }
    )

    race = pd.get_dummies(
        analysis["RaceEthn5"].astype(int),
        prefix="race",
        drop_first=True,
        dtype=float,
    )

    design = pd.concat(
        [design.reset_index(drop=True), race.reset_index(drop=True)],
        axis=1,
    )

    for column in ["age", "education", "income", "medforms"]:
        design[column] = (
            design[column] - design[column].mean()
        ) / design[column].std()

    X = np.asarray(design, dtype=float)
    y = analysis["decision_ord"].astype(int).to_numpy() - 1

    def negative_log_likelihood(parameters, weights):
        beta = parameters[: X.shape[1]]

        cut1 = parameters[-3]
        cut2 = cut1 + np.exp(parameters[-2])
        cut3 = cut2 + np.exp(parameters[-1])
        cuts = np.array([cut1, cut2, cut3])

        linear_predictor = X @ beta

        cumulative = np.column_stack(
            [
                np.zeros(len(y)),
                expit(cuts[0] - linear_predictor),
                expit(cuts[1] - linear_predictor),
                expit(cuts[2] - linear_predictor),
                np.ones(len(y)),
            ]
        )

        probability = (
            cumulative[np.arange(len(y)), y + 1]
            - cumulative[np.arange(len(y)), y]
        )
        probability = np.clip(probability, 1e-12, 1)

        scaled_weights = weights / np.mean(weights)
        return -np.sum(scaled_weights * np.log(probability))

    initial = np.zeros(X.shape[1] + 3)
    initial[-3:] = [-1, 0, 0]

    full_fit = minimize(
        negative_log_likelihood,
        initial,
        args=(analysis["PERSON_FINWT0"].to_numpy(),),
        method="L-BFGS-B",
        options={"maxiter": 300},
    )

    if not full_fit.success:
        raise RuntimeError(full_fit.message)

    coefficient = float(full_fit.x[0])

    replicate_coefficients = []

    for index in range(1, 51):
        replicate_fit = minimize(
            negative_log_likelihood,
            full_fit.x,
            args=(analysis[f"PERSON_FINWT{index}"].to_numpy(),),
            method="L-BFGS-B",
            options={"maxiter": 180},
        )

        if not replicate_fit.success:
            raise RuntimeError(
                f"Replicate {index} failed: {replicate_fit.message}"
            )

        replicate_coefficients.append(float(replicate_fit.x[0]))

    replicate_coefficients = np.asarray(replicate_coefficients)

    variance = (49 / 50) * np.sum(
        (replicate_coefficients - coefficient) ** 2
    )
    standard_error = math.sqrt(float(variance))

    lower = coefficient - 1.96 * standard_error
    upper = coefficient + 1.96 * standard_error
    p_value = 2 * (
        1 - norm.cdf(abs(coefficient / standard_error))
    )

    print(f"Complete-case n: {len(analysis):,}")
    print(
        "Proportional-odds OR for higher agreement/use: "
        f"{math.exp(coefficient):.3f}"
    )
    print(
        "95% CI: "
        f"{math.exp(lower):.3f} to {math.exp(upper):.3f}"
    )
    print(f"JK1 SE (log-odds): {standard_error:.4f}")
    print(f"Two-sided p-value: {p_value:.6g}")


if __name__ == "__main__":
    main()
