# Analysis Plan

## Population

Primary analysis:

- age >= 20 years (matching the adult education variable used in socioeconomic sensitivity analysis)
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

`log_device ~ log_leisure + age + sex + BMI`

## Secondary model

Add `log_leisure × age_group`, retaining sex and BMI.

A separate socioeconomic sensitivity model adds collapsed race/ethnicity and education categories.

## Descriptive outputs

- analytic n
- weighted demographic characteristics
- self-report distribution
- device movement-density distribution
- survey-weighted model coefficients

## Sensitivity

- valid-minute completeness threshold (1,000 vs 1,200 minutes)
- minimum number of qualifying PAM days (3, 4, 5)
- alternative wear-classified-minute rule
- model without BMI
- socioeconomic sensitivity model with collapsed race/ethnicity and education

## Claims allowed

- association
- measurement relationship
- evidence of heterogeneity by age if interaction supports it

## Claims not allowed

- validation of one measure against the other as a gold standard
- causal effect
- device-measured MVPA unless a validated MIMS intensity algorithm is explicitly introduced


## Survey inference degrees of freedom

For coefficient inference, the R `survey` package is instructed to use `df.resid = degf(design)` (PSUs minus strata) rather than the more conservative default subtraction of model rank. This is appropriate to report explicitly because the covariates are individual-level rather than PSU-level.
