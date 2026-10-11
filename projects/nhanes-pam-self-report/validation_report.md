# Validation Report

## Overall Assessment

**Ready to share with caveats.**

## Methodology review

The project uses official CDC/NCHS NHANES 2013–2014 public-use files:

- PAXDAY_H — day-level wrist physical-activity-monitor summary
- PAQ_H — physical-activity questionnaire
- DEMO_H — demographics and complex-survey design variables
- BMX_H — body measures

Official documentation confirms:

- `PAXMTSD` is the day sum of triaxial MIMS values;
- `PAXVMD` is minutes of valid PAM data not flagged for QC issues;
- PAM analyses should use examined-sample weights;
- GPAQ leisure items support 8-MET vigorous and 4-MET moderate scoring;
- when PAQ data are joined to MEC data, MEC weights should be used.

## Population and survey design

Primary analytic population:

- adults age 20+
- complete focal exposure/outcome/covariates
- positive `WTMEC2YR`
- at least 4 qualifying PAM days
- each primary qualifying day has at least 1,200 valid minutes

Survey design:

- weight: `WTMEC2YR`
- strata: `SDMVSTRA`
- PSU: `SDMVPSU`
- design df: 15

The 1,200-minute / 4-day criterion is analyst-defined, not a CDC standard.

## Measurement review

Device outcome:

`mean daily PAXMTSD / PAXVMD`

This is explicitly described as MIMS movement density. It is **not** labelled as MVPA minutes.

Self-report exposure:

leisure MET-min/week from vigorous and moderate GPAQ recreational activity items.

The two measures capture related but non-identical constructs; the device metric is not treated as a gold standard for the self-report measure.

## Primary result

Analytic n = **4,726**.

Model:

`log1p(device movement density) ~ log1p(leisure MET-min/week) + age + sex + BMI`

Focal coefficient:

- beta = 0.00876
- SE = 0.00248
- t = 3.530
- 95% CI = 0.00347–0.01404
- p = 0.0030
- df = 15

## Sensitivity review

The focal coefficient was stable across all prespecified movement-data completeness rules:

| Specification | n | beta | 95% CI | p |
|---|---:|---:|---:|---:|
| >=1200 valid min, >=4 days | 4,726 | 0.00876 | 0.00347–0.01404 | 0.0030 |
| >=1000 valid min, >=4 days | 4,730 | 0.00857 | 0.00338–0.01376 | 0.0031 |
| >=1200 valid min, >=3 days | 4,740 | 0.00872 | 0.00338–0.01406 | 0.0033 |
| >=1200 valid min, >=5 days | 4,707 | 0.00867 | 0.00341–0.01392 | 0.0031 |
| >=1200 wear-classified min, >=4 days | 4,076 | 0.00754 | 0.00465–0.01042 | <0.001 |

Model sensitivity:

- no BMI: beta 0.01050 (95% CI 0.00543–0.01558), p < 0.001
- plus collapsed race/ethnicity and education: beta 0.01077 (95% CI 0.00533–0.01622), p < 0.001

Individual age-interaction coefficients did not provide a clear or consistent pattern; no subgroup-effect claim is promoted.

## Data-flow QA

- DEMO total: 10,175
- age 20+ in DEMO: 5,769
- PAQ total: 9,484
- participants meeting primary PAM completeness before covariate joins: 7,616
- BMX total: 9,813
- primary analytic sample: 4,726
- socioeconomic sensitivity analytic sample: 4,722

Primary analytic participants had a median of 7 qualifying PAM days.

## Required caveats

- cross-sectional association only
- no causal inference
- MIMS movement density is not MVPA
- self-report and device movement are not interchangeable measures
- PAM completeness restriction may introduce selection differences not fully removed by standard MEC weighting
- the valid-day rule is analyst-defined and must remain visible
