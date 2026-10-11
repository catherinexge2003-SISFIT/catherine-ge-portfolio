#!/usr/bin/env python3
"""HINTS 6 + HINTS 7 repeated cross-sectional analysis.

Implements the two-cycle Rizzo replicate-weight structure described by the
official NCI HINTS Data Merging Code Tool.

Raw public-use data are downloaded at runtime and are not committed.
"""

from __future__ import annotations

import io
import json
import math
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import statsmodels.api as sm
from scipy.stats import t

H6_URL = "https://hints.cancer.gov/dataset/HINTS6_STATA_20250731.zip"
H7_URL = "https://hints.cancer.gov/dataset/HINTS7_STATA_20250731.zip"
OUT = Path(__file__).resolve().parents[1] / "results"
OUT.mkdir(parents=True, exist_ok=True)

EXPOSURE = "socmed_truefalse"
OUTCOME = "socmed_makedecisions"
FULL_WT = "person_finwt0"
REP_WTS = [f"person_finwt{i}" for i in range(1, 51)]
JK_MULTIPLIER = 0.98
DF = 98


def download_dta(url: str) -> pd.DataFrame:
    response = requests.get(url, timeout=120)
    response.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
        candidates = [n for n in zf.namelist() if n.lower().endswith(".dta")]
        if not candidates:
            raise RuntimeError(f"No .dta file found in {url}")
        with zf.open(candidates[0]) as fh:
            return pd.read_stata(io.BytesIO(fh.read()), convert_categoricals=False)


def normalise(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c).lower() for c in out.columns]
    required = [EXPOSURE, OUTCOME, FULL_WT] + REP_WTS
    missing = [c for c in required if c not in out.columns]
    if missing:
        raise KeyError(f"Missing required HINTS fields: {missing}")
    return out


def recode_likert_binary(series: pd.Series) -> pd.Series:
    x = pd.to_numeric(series, errors="coerce")
    x = x.where(x > 0)
    return x.map({1: 1.0, 2: 1.0, 3: 0.0, 4: 0.0})


def prepare_cycle(df: pd.DataFrame, year: int, block: int) -> pd.DataFrame:
    df = normalise(df)
    out = pd.DataFrame({
        "hard_to_judge": recode_likert_binary(df[EXPOSURE]),
        "uses_for_decisions": recode_likert_binary(df[OUTCOME]),
        "year": year,
        "year7": 1.0 if year == 2024 else 0.0,
        "nwgt0": pd.to_numeric(df[FULL_WT], errors="coerce"),
    })

    # NCI Rizzo method for two merged HINTS cycles:
    # own 50 replicate weights occupy own block; other block uses full weight.
    for j in range(1, 101):
        if block == 1 and j <= 50:
            source = REP_WTS[j - 1]
        elif block == 2 and j > 50:
            source = REP_WTS[j - 51]
        else:
            source = FULL_WT
        out[f"nwgt{j}"] = pd.to_numeric(df[source], errors="coerce")

    return out.dropna(subset=["hard_to_judge", "uses_for_decisions", "nwgt0"])


def weighted_mean(y: np.ndarray, w: np.ndarray) -> float:
    return float(np.sum(y * w) / np.sum(w))


def jk_se(full: float, reps: list[float]) -> float:
    arr = np.asarray(reps, dtype=float)
    return float(math.sqrt(JK_MULTIPLIER * np.sum((arr - full) ** 2)))


def prevalence_cell(df: pd.DataFrame, year: int, exposure: int) -> dict:
    cell = df[(df["year"] == year) & (df["hard_to_judge"] == exposure)]
    y = cell["uses_for_decisions"].to_numpy(float)
    full = weighted_mean(y, cell["nwgt0"].to_numpy(float))
    reps = [
        weighted_mean(y, cell[f"nwgt{i}"].to_numpy(float))
        for i in range(1, 101)
    ]
    se = jk_se(full, reps)
    crit = float(t.ppf(0.975, DF))
    return {
        "year": year,
        "difficulty_judging": exposure,
        "n": int(len(cell)),
        "weighted_prevalence": full,
        "se": se,
        "ci_low": max(0.0, full - crit * se),
        "ci_high": min(1.0, full + crit * se),
    }


def fit_logit(df: pd.DataFrame, weight_col: str, interaction: bool = True):
    X = pd.DataFrame({
        "const": 1.0,
        "hard_to_judge": df["hard_to_judge"],
        "year7": df["year7"],
    })
    if interaction:
        X["hard_to_judge_x_year7"] = df["hard_to_judge"] * df["year7"]
    model = sm.GLM(
        df["uses_for_decisions"],
        X,
        family=sm.families.Binomial(),
        freq_weights=df[weight_col],
    )
    return model.fit(maxiter=100, disp=False)


def replicate_inference(df: pd.DataFrame, interaction: bool = True) -> pd.DataFrame:
    full_fit = fit_logit(df, "nwgt0", interaction=interaction)
    names = list(full_fit.params.index)
    rep_params = []
    for i in range(1, 101):
        rep_params.append(fit_logit(df, f"nwgt{i}", interaction=interaction).params[names].to_numpy())
    rep_params = np.asarray(rep_params)

    rows = []
    crit = float(t.ppf(0.975, DF))
    for idx, name in enumerate(names):
        beta = float(full_fit.params[name])
        se = float(math.sqrt(JK_MULTIPLIER * np.sum((rep_params[:, idx] - beta) ** 2)))
        rows.append({
            "term": name,
            "beta": beta,
            "se_jk": se,
            "or": math.exp(beta),
            "ci_low": math.exp(beta - crit * se),
            "ci_high": math.exp(beta + crit * se),
            "t": beta / se if se > 0 else np.nan,
        })
    return pd.DataFrame(rows)


def main():
    h6 = prepare_cycle(download_dta(H6_URL), 2022, block=1)
    h7 = prepare_cycle(download_dta(H7_URL), 2024, block=2)
    pooled = pd.concat([h6, h7], ignore_index=True)

    prevalence = pd.DataFrame([
        prevalence_cell(pooled, year, exposure)
        for year in [2022, 2024]
        for exposure in [0, 1]
    ])
    prevalence.to_csv(OUT / "weighted_prevalence.csv", index=False)

    primary = replicate_inference(pooled, interaction=True)
    primary.to_csv(OUT / "primary_interaction_model.csv", index=False)

    additive = replicate_inference(pooled, interaction=False)
    additive.to_csv(OUT / "additive_model.csv", index=False)

    summary = {
        "design": "repeated cross-sectional HINTS 6 + HINTS 7",
        "n_total": int(len(pooled)),
        "n_hints6": int(len(h6)),
        "n_hints7": int(len(h7)),
        "replicate_weights": 100,
        "jk_multiplier": JK_MULTIPLIER,
        "df": DF,
        "primary_interaction": primary.loc[
            primary["term"] == "hard_to_judge_x_year7"
        ].to_dict(orient="records")[0],
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
