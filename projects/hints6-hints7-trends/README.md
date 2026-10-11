# HINTS 6 + HINTS 7 Repeated Cross-Sectional Analysis

## Research question

Did the relationship between difficulty judging the truthfulness of health information on social media and using social-media information for personal health decisions differ between HINTS 6 and HINTS 7?

## Design

Repeated cross-sectional secondary analysis of the U.S. National Cancer Institute Health Information National Trends Survey (HINTS):

- HINTS 6
- HINTS 7

The cycles are treated as independent probability samples of U.S. adults, consistent with the NCI HINTS data-merging guidance.

## Primary variables

- Exposure: `SocMed_TrueFalse`
- Outcome: `SocMed_MakeDecisions`
- Survey cycle: HINTS 6 vs HINTS 7
- Full-sample weight: `PERSON_FINWT0`
- Replicate weights: `PERSON_FINWT1`–`PERSON_FINWT50` per cycle

Negative HINTS special codes are treated as missing.

Exposure and outcome are dichotomised consistently with the existing HINTS 7 project:

- strongly/somewhat agree = 1
- somewhat/strongly disagree = 0

## Survey-weight construction

The analysis follows the logic of the official NCI HINTS Data Merging Code Tool.

For two cycles, the merged file has:

- one full-sample weight: `nwgt0`
- 100 Rizzo replicate weights: `nwgt1`–`nwgt100`

For a respondent in HINTS 6:
- `nwgt1`–`nwgt50` use HINTS 6 replicate weights
- `nwgt51`–`nwgt100` use that respondent's full-sample weight

For a respondent in HINTS 7:
- `nwgt1`–`nwgt50` use that respondent's full-sample weight
- `nwgt51`–`nwgt100` use HINTS 7 replicate weights

Variance is estimated with the official multiplier 0.98 and 98 degrees of freedom.

## Primary analysis

Weighted logistic regression:

`health_decision_use ~ difficulty_judging + survey_year + difficulty_judging × survey_year`

The interaction term tests whether the exposure–outcome association changed between survey cycles.

## Secondary outputs

- weighted outcome prevalence by year and exposure group
- cycle-specific odds ratios
- additive model without interaction
- complete-case counts by cycle
- replicate-weight confidence intervals

## Interpretation limits

This is repeated cross-sectional, not longitudinal, research. Changes between HINTS 6 and HINTS 7 describe population-level differences between independent survey samples; they do not represent within-person change.

## Official sources

- HINTS public datasets: https://hints.cancer.gov/data/download-data.aspx
- HINTS Data Merging Code Tool: https://hints.cancer.gov/data/data-merging-tool.aspx

Raw public-use datasets are not committed to this repository.
