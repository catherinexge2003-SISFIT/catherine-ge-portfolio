# Validation Report

## Overall assessment

**Ready to share with caveats** as a reproducible research-development artifact.

It is not yet framed as a peer-reviewed or causal research output.

## Data source

- National Cancer Institute Health Information National Trends Survey (HINTS) 7
- Fielded in 2024
- Public-use release: updated August 2025
- Total respondents: 7,278
- Official source: https://hints.cancer.gov/data/download-data.aspx

The HINTS data-remediation page currently lists no HINTS 7-specific error notice.

## Survey design and weighting

HINTS 7 used a probability-based, two-stage address sampling design and offered paper and web response modes concurrently.

Every completed respondent received:
- one full-sample person weight;
- 50 replicate weights.

The project uses:
- `PERSON_FINWT0` for population-weighted point estimates;
- `PERSON_FINWT1` through `PERSON_FINWT50` for variance estimation;
- the HINTS delete-one JK1 formula:
  `Var(theta) = (R-1)/R * sum((theta_r - theta_full)^2)`, R = 50.

This matches the HINTS 7 methodology report.

## Variable verification

Primary variables were checked against the HINTS 7 annotated instrument.

- `SocMed_TrueFalse`: difficulty telling whether health information on social media is true or false
- `SocMed_MakeDecisions`: use of social-media information to make personal health decisions
- `SocMed_DiscussHCP`: use of social-media information in discussions with a health-care provider
- `MisleadingHealthInfo`: perceived amount of false/misleading health information on social media

Negative HINTS special codes are treated as missing/inapplicable.

## Calculation spot-checks

### Primary model

- complete-case n = 5,183
- adjusted OR = 1.83
- 95% CI = 1.42–2.34

Verified independently with all 50 JK1 replicate weights.

### Secondary outcome

- complete-case n = 5,184
- adjusted OR = 2.07
- 95% CI = 1.61–2.66

### Alternative exposure

- complete-case n = 5,181
- adjusted OR = 0.47
- 95% CI = 0.35–0.62

### Ordinal sensitivity analysis

Retaining the four-level `SocMed_MakeDecisions` response:

- n = 5,183
- proportional-odds OR = 1.50
- 95% CI = 1.25–1.78

The focal direction remains consistent with the primary binary model.

### Missing-data / specification sensitivity

Among respondents with valid primary exposure and outcome:

- base n = 5,926
- full-model complete share = 87.5% unweighted
- full-model complete share = 89.9% weighted

Focal odds ratios across specifications:

- crude: OR 1.79 (95% CI 1.43–2.24)
- demographic-adjusted: OR 1.92 (95% CI 1.51–2.44)
- full-adjusted: OR 1.83 (95% CI 1.42–2.34)

The focal association is not materially dependent on the full adjustment set.

## PRICSSA-oriented reporting audit

### Present in the artifact

- survey name and cycle;
- survey year;
- target population context;
- public-use data source;
- total survey sample size;
- analytic sample sizes;
- variable names and operational definitions;
- full-sample weighting;
- replicate-weight variance estimation;
- JK1 replication method;
- software/code made available;
- model specification;
- uncertainty intervals;
- missing-data handling;
- cross-sectional design limitation;
- explicit non-causal interpretation.

### Remaining reporting caveats

1. HINTS 7 used both paper and web administration modes, but inspection of the public-use variable names and labels did not identify a direct administration-mode variable suitable for model adjustment. Mode is therefore reported as a survey-design limitation rather than treated as an available covariate.
2. Complete-case analysis is used. Specification sensitivity is reassuring, but this is not equivalent to multiple-imputation sensitivity.
3. `SocMed_TrueFalse` is a single survey item and must not be described as a validated digital-health-literacy scale.
4. Odds ratios from a cross-sectional survey do not establish temporality or causality.
5. The alternative-exposure finding is exploratory and should not be overinterpreted as evidence of a protective effect of perceived misinformation.

## Interpretation review

The strongest defensible statement is:

> In HINTS 7, self-reported difficulty judging whether health information on social media is true or false was associated with greater reported use of social-media information for personal health decisions and for discussions with health-care providers. The association persisted across adjustment specifications and an ordinal sensitivity analysis.

Do not state that difficulty evaluating health information causes reliance on social media.

## Release recommendation

Suitable for:
- GitHub research portfolio;
- PhD supervisor discussion;
- CV entry labelled "independent secondary analysis" or "research project";
- demonstration of survey-weighted regression and reproducible analysis skills.

Not yet suitable for:
- claiming a peer-reviewed publication;
- claiming a validated digital-health-literacy measure;
- causal claims;
- describing the finding as a clinical or behavioural intervention effect.


## End-to-end reproducibility check

The three repository scripts were fetched from this branch and executed unchanged against the official HINTS 7 STATA public-use file:

- `src/analysis.py`: exit 0
- `src/sensitivity_ordinal.py`: exit 0
- `src/missing_sensitivity.py`: exit 0

The reproduced outputs matched the values documented in this repository.

Validation date: 2026-10-02.
