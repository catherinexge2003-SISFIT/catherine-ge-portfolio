# HINTS 7 Secondary Analysis: Social-Media Health Information Judgement and Use

## Research question

Among U.S. adults who use social media, is difficulty judging whether health information is true or false associated with using social-media information to make personal health decisions?

## Why this project

This project is designed as a reproducible secondary-data analysis aligned with Catherine Ge's research interests in digital health literacy, health communication, behaviour change and physical activity.

The analysis uses the U.S. National Cancer Institute's Health Information National Trends Survey (HINTS) 7, fielded in 2024. HINTS 7 contains 7,278 respondents and is a nationally representative probability-based survey. Public-use data are available from:

- https://hints.cancer.gov/data/download-data.aspx
- HINTS 7 annotated instrument: https://hints.cancer.gov/docs/Instruments/HINTS7-AnnotatedEnglish.pdf
- HINTS 7 methodology report: https://hints.cancer.gov/docs/methodologyreports/HINTS_7_MethodologyReport.pdf

## Core variables

- `SocMed_TrueFalse`: difficulty judging whether health information on social media is true or false
- `SocMed_MakeDecisions`: use of social-media information to make health decisions
- `MisleadingHealthInfo`: perceived amount of false or misleading health information on social media
- `ConfidentMedForms`: confidence filling out medical forms
- `Electronic2_HealthInfo`: use of the Internet to look for health or medical information
- Demographic adjustment variables: age group, education, race/ethnicity, income, sex assigned at birth
- `PERSON_FINWT0`: full-sample person weight
- `PERSON_FINWT1`–`PERSON_FINWT50`: JK1 replicate weights

## Primary analysis

The current working analysis dichotomises:

- `SocMed_TrueFalse`: strongly/somewhat agree vs strongly/somewhat disagree
- `SocMed_MakeDecisions`: strongly/somewhat agree vs strongly/somewhat disagree

A survey-weighted logistic model estimates the association between difficulty judging truthfulness and use of social-media health information for decisions, adjusting for demographics, medical-form confidence and online health-information seeking.

Variance is estimated using the HINTS 50 replicate weights and the JK1 formula:

`Var(theta) = (R-1)/R * sum((theta_r - theta_full)^2)`

## Preliminary result

Complete-case analytic sample: **n = 5,183**

Weighted prevalence of using social-media information for personal health decisions:

- respondents reporting difficulty judging truthfulness: **24.1%**
- respondents not reporting that difficulty: **15.1%**

Adjusted association:

- **OR = 1.83**
- **95% CI = 1.42–2.34**
- two-sided **p < 0.001**

Interpretation: respondents who reported difficulty judging whether health information on social media was true or false had higher odds of reporting that they use social-media information to make health decisions, after adjustment for the prespecified covariates.

This is a cross-sectional association and must not be interpreted as causal.

## Reproducibility

Raw HINTS data are not committed to this repository. Download the official HINTS 7 STATA public-use package and place:

`hints7_public.dta`

under:

`projects/hints7-social-media-health-info/data/raw/`

Then run:

`python src/analysis.py`

## Planned robustness checks

1. retain the original four-level Likert structure in an ordinal-model sensitivity analysis;
2. test `SocMed_DiscussHCP` as a secondary outcome;
3. examine `MisleadingHealthInfo` as an alternative exposure;
4. assess item/mode effects according to HINTS analytic recommendations;
5. report weighted estimates and uncertainty consistent with PRICSSA guidance.

## Status

**Exploratory / research artifact in development.**

No causal claim is made. Results should be considered preliminary until the analysis plan and robustness checks are finalised.
