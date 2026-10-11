"""Missing-data / model-specification sensitivity checks for the HINTS 7 project."""

from pathlib import Path
import math

import numpy as np
import pandas as pd
import patsy
import statsmodels.api as sm


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "hints7_public.dta"


def positive_or_missing(series: pd.Series) -> pd.Series:
    return series.where(series > 0)


def fit_jk(df: pd.DataFrame, formula: str, required: list[str]) -> dict:
    analysis = df.dropna(subset=required + ["PERSON_FINWT0"]).copy()

    y, X = patsy.dmatrices(formula, analysis, return_type="dataframe")
    full = sm.GLM(
        y,
        X,
        family=sm.families.Binomial(),
        freq_weights=analysis["PERSON_FINWT0"],
    ).fit()

    coefficient = float(full.params["hard_to_judge"])

    replicate_coefficients = []
    for index in range(1, 51):
        replicate = sm.GLM(
            y,
            X,
            family=sm.families.Binomial(),
            freq_weights=analysis[f"PERSON_FINWT{index}"],
        ).fit(maxiter=100, disp=0)
        replicate_coefficients.append(
            float(replicate.params["hard_to_judge"])
        )

    replicate_coefficients = np.asarray(replicate_coefficients)
    standard_error = math.sqrt(
        (49 / 50)
        * np.sum((replicate_coefficients - coefficient) ** 2)
    )

    lower = coefficient - 1.96 * standard_error
    upper = coefficient + 1.96 * standard_error

    return {
        "n": len(analysis),
        "or": math.exp(coefficient),
        "ci_low": math.exp(lower),
        "ci_high": math.exp(upper),
    }


def main() -> None:
    df = pd.read_stata(DATA, convert_categoricals=False)

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

    crude = fit_jk(
        df,
        "uses_for_decisions ~ hard_to_judge",
        ["uses_for_decisions", "hard_to_judge"],
    )

    demographic = fit_jk(
        df,
        "uses_for_decisions ~ hard_to_judge + "
        "C(AgeGrpB) + C(Education) + C(RaceEthn5) + C(BirthSex)",
        [
            "uses_for_decisions",
            "hard_to_judge",
            "AgeGrpB",
            "Education",
            "RaceEthn5",
            "BirthSex",
        ],
    )

    full = fit_jk(
        df,
        "uses_for_decisions ~ hard_to_judge + "
        "C(AgeGrpB) + C(Education) + C(RaceEthn5) + "
        "C(IncomeRanges_IMP) + C(BirthSex) + "
        "C(ConfidentMedForms) + searched_health_info",
        [
            "uses_for_decisions",
            "hard_to_judge",
            "AgeGrpB",
            "Education",
            "RaceEthn5",
            "IncomeRanges_IMP",
            "BirthSex",
            "ConfidentMedForms",
            "searched_health_info",
        ],
    )

    base = df.dropna(
        subset=["uses_for_decisions", "hard_to_judge", "PERSON_FINWT0"]
    ).copy()

    full_covariates = [
        "AgeGrpB",
        "Education",
        "RaceEthn5",
        "IncomeRanges_IMP",
        "BirthSex",
        "ConfidentMedForms",
        "searched_health_info",
    ]

    base["complete_full"] = base[full_covariates].notna().all(axis=1)

    weighted_complete = float(
        np.sum(base["complete_full"].astype(float) * base["PERSON_FINWT0"])
        / np.sum(base["PERSON_FINWT0"])
    )

    print(f"Base valid exposure/outcome n: {len(base):,}")
    print(
        "Full-model complete share (unweighted): "
        f"{base['complete_full'].mean():.1%}"
    )
    print(
        "Full-model complete share (weighted): "
        f"{weighted_complete:.1%}"
    )

    for label, result in [
        ("Crude", crude),
        ("Demographic-adjusted", demographic),
        ("Full-adjusted", full),
    ]:
        print(
            f"{label}: n={result['n']:,}; "
            f"OR={result['or']:.2f}; "
            f"95% CI {result['ci_low']:.2f}-{result['ci_high']:.2f}"
        )


if __name__ == "__main__":
    main()
