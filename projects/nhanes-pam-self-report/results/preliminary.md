# Preliminary Results

## Research question

Among U.S. adults age 20+ in NHANES 2013–2014, is self-reported leisure-time physical activity associated with device-measured movement density?

## Analytic sample

Primary analytic n = **4,726**.

Primary PAM completeness rule:

- at least 1,200 valid minutes in a qualifying day;
- at least 4 qualifying days per participant.

This is an analyst-defined completeness rule, not a CDC standard.

## Measures

Self-report:

- leisure MET-min/week from GPAQ recreational activity items;
- vigorous leisure scored at 8 METs;
- moderate leisure scored at 4 METs.

Device outcome:

- mean daily `PAXMTSD / PAXVMD`;
- interpreted as MIMS movement density;
- not interpreted as MVPA minutes.

## Primary model

`log1p(device movement density) ~ log1p(leisure MET-min/week) + age + sex + BMI`

Focal self-report coefficient:

- beta = **0.00876**
- SE = **0.00248**
- 95% CI = **0.00347–0.01404**
- p = **0.0030**
- survey design df = **15**

### Interpretation

Higher self-reported leisure physical activity was associated with higher device-measured movement density after adjustment for age, sex and BMI.

The coefficient is on a log1p–log1p scale and is intentionally not translated into "minutes of MVPA" or a one-for-one agreement metric.

## Robustness

The focal association remained positive across all five prespecified valid-day/wear specifications, with beta values from 0.00754 to 0.00876.

It also remained positive:

- without BMI adjustment: beta = 0.01050, p < 0.001;
- with additional collapsed race/ethnicity and education terms: beta = 0.01077, p < 0.001.

## Age heterogeneity

The age-interaction model did not show a clear pattern strong enough to support a public subgroup-effect claim. These terms are retained as exploratory output rather than promoted as a headline result.

## Interpretation limits

- cross-sectional only;
- no causal claim;
- device-measured MIMS movement density and self-reported leisure activity capture different constructs;
- neither is treated as a gold-standard validation target for the other;
- PAM completeness restrictions may affect generalisability.
