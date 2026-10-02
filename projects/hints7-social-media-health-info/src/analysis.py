"""Reproducible HINTS 7 secondary analysis.

Primary question:
Among U.S. adults who use social media, is difficulty judging whether health
information is true or false associated with using social-media information
to make personal health decisions?

Raw HINTS public-use data are intentionally not committed.
"""

from pathlib import Path
import math

import numpy as np
import pandas as pd
import patsy
import statsmodels.api as sm
from scipy.stats import norm


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "hints7_public.dta"


def positive_or_missing(series: pd.Series) -> pd.Series:
    """Treat HINTS negative special codes as missing."""
    return series.where(series > 0)


def weighted_mean(x: pd.Series, w: pd.Series) -> float:
    return float(np.sum(x * w) / np.sum(w))


def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError(
            f"Missing {DATA}. Download the official HINTS 7 STATA public-use package "
            "from https://hints.cancer.gov/data/download-data.aspx"
        )

    df = pd.read_stata(DATA, convert_categoricals=False)

    required = [
        "SocMed_TrueFalse",
        "SocMed_MakeDecisions",
        "ConfidentMedForms",
        "AgeGrpB",
        "Education",
        "RaceEthn5",
        "IncomeRanges_IMP",
        "BirthSex",
        "Electronic2_HealthInfo",
        "PERSON_FINWT0",
    ] + [f"PERSON_FINWT{i}" for i in range(1, 51)]

    missing_columns = [c for c in required if c not in df.columns]
    if missing_columns:
        raise KeyError(f"Missing expected HINTS variables: {missing_columns}")

    for variable in [
        "SocMed_TrueFalse",
        "SocMed_MakeDecisions",
        "ConfidentMedForms",
        "AgeGrpB",
        "Education",
        "RaceEthn5",
        "IncomeRanges_IMP",
        "BirthSex",
        "Electronic2_HealthInfo",
    ]:
        df[variable] = positive_or_missing(df[variable])

    df["hard_to_judge"] = np.where(
        df["SocMed_TrueFalse"].isin([1, 2]),
        1,
        np.where(df["SocMed_TrueFalse"].isin([3, 4]), 0, np.nan),
    )

    df["uses_for_decisions"] = np.where(
        df["SocMed_MakeDecisions"].isin([1, 2]),
        1,
        np.where(df["SocMed_MakeDecisions"].isin([3, 4]), 0, np.nan),
    )

    df["searched_health_info"] = np.where(
        df["Electronic2_HealthInfo"] == 1,
        1,
        np.where(df["Electronic2_HealthInfo"] == 2, 0, np.nan),
    )

    covariates = [
        "hard_to_judge",
        "uses_for_decisions",
        "AgeGrpB",
        "Education",
        "RaceEthn5",
        "IncomeRanges_IMP",
        "BirthSex",
        "ConfidentMedForms",
        "searched_health_info",
    ]

    analysis = df.dropna(subset=covariates + ["PERSON_FINWT0"]).copy()

    overall = weighted_mean(
        analysis["uses_for_decisions"], analysis["PERSON_FINWT0"]
    )
    exposed = weighted_mean(
        analysis.loc[analysis["hard_to_judge"] == 1, "uses_for_decisions"],
        analysis.loc[analysis["hard_to_judge"] == 1, "PERSON_FINWT0"],
    )
    unexposed = weighted_mean(
        analysis.loc[analysis["hard_to_judge"] == 0, "uses_for_decisions"],
        analysis.loc[analysis["hard_to_judge"] == 0, "PERSON_FINWT0"],
    )

    formula = (
        "uses_for_decisions ~ hard_to_judge + C(AgeGrpB) + C(Education) + "
        "C(RaceEthn5) + C(IncomeRanges_IMP) + C(BirthSex) + "
        "C(ConfidentMedForms) + searched_health_info"
    )

    y, X = patsy.dmatrices(formula, analysis, return_type="dataframe")

    full_model = sm.GLM(
        y,
        X,
        family=sm.families.Binomial(),
        freq_weights=analysis["PERSON_FINWT0"],
    ).fit()

    coefficient = float(full_model.params["hard_to_judge"])

    replicate_coefficients = []
    for index in range(1, 51):
        replicate_model = sm.GLM(
            y,
            X,
            family=sm.families.Binomial(),
            freq_weights=analysis[f"PERSON_FINWT{index}"],
        ).fit(maxiter=100, disp=0)
        replicate_coefficients.append(
            float(replicate_model.params["hard_to_judge"])
        )

    replicate_coefficients = np.asarray(replicate_coefficients)
    R = 50
    variance = (R - 1) / R * np.sum(
        (replicate_coefficients - coefficient) ** 2
    )
    standard_error = math.sqrt(float(variance))
    z_score = coefficient / standard_error
    p_value = 2 * (1 - norm.cdf(abs(z_score)))

    lower = coefficient - 1.96 * standard_error
    upper = coefficient + 1.96 * standard_error

    print(f"Complete-case n: {len(analysis):,}")
    print(f"Weighted outcome prevalence overall: {overall:.3%}")
    print(f"Weighted prevalence, difficulty judging truthfulness: {exposed:.3%}")
    print(f"Weighted prevalence, no reported difficulty: {unexposed:.3%}")
    print(f"Adjusted OR: {math.exp(coefficient):.3f}")
    print(
        "95% CI: "
        f"{math.exp(lower):.3f} to {math.exp(upper):.3f}"
    )
    print(f"JK1 SE (log-odds): {standard_error:.4f}")
    print(f"Two-sided p-value: {p_value:.6g}")


if __name__ == "__main__":
    main()
