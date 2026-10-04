# Analysis Plan

## Population

Primary analysis:

- age >= 18 years
- valid NHANES MEC weight
- non-missing self-reported leisure PA
- non-missing BMI and selected covariates
- >= 4 PAM days with >= 1,200 valid minutes/day

## Device outcome

For each qualifying day:

`PAXMTSD / PAXVMD`

Participant metric: mean across qualifying days.

Primary transformation: `log1p(mean_mims_per_valid_minute)`.

## Self-report exposure

Leisure MET-min/week:

- vigorous leisure: 8 MET × days/week × minutes/day
- moderate leisure: 4 MET × days/week × minutes/day

If `PAQ650=2`, vigorous leisure contribution = 0.
If `PAQ665=2`, moderate leisure contribution = 0.
Refused/don't know codes are missing.

Primary transformation: `log1p(leisure_MET_min_week)`.

## Primary model

Survey-weighted linear regression using `survey::svyglm` in R:

`log_device ~ log_leisure + age_group + sex + race + education + BMI`

## Secondary model

Add `log_leisure × age_group`.

## Descriptive outputs

- analytic n
- weighted demographic characteristics
- self-report distribution
- device movement-density distribution
- survey-weighted model coefficients

## Sensitivity

- valid-day completeness threshold
- minimum number of qualifying PAM days
- model without BMI
- categorical self-report exposure (zero / low / medium / high) if continuous relationship is strongly nonlinear

## Claims allowed

- association
- measurement relationship
- evidence of heterogeneity by age if interaction supports it

## Claims not allowed

- validation of one measure against the other as a gold standard
- causal effect
- device-measured MVPA unless a validated MIMS intensity algorithm is explicitly introduced
