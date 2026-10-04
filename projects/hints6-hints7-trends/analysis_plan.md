# Analysis Plan

## Aim

Estimate whether social-media health-information judgement and health-decision use changed between HINTS 6 and HINTS 7, with primary emphasis on whether the association between difficulty judging truthfulness and decision use differs by survey cycle.

## Population

Respondents with valid values for both `SocMed_TrueFalse` and `SocMed_MakeDecisions`.

## Primary estimand

The exponentiated coefficient for the interaction:

`difficulty_judging × HINTS7`

from a pooled weighted logistic model.

- OR > 1: the association is stronger in HINTS 7 than HINTS 6.
- OR < 1: the association is weaker in HINTS 7 than HINTS 6.
- The analysis remains associational.

## Weighting

Use the NCI Rizzo-method merged replicate-weight structure:

- 100 pooled replicate weights for two cycles
- jackknife multiplier = 0.98
- df = 98
- MSE form of replicate variance

## Descriptive analysis

Report weighted prevalence of using social-media information for health decisions in four cells:

- HINTS 6 / difficulty judging
- HINTS 6 / no difficulty
- HINTS 7 / difficulty judging
- HINTS 7 / no difficulty

## Sensitivity

1. Additive pooled model without the year interaction.
2. Cycle-specific weighted logistic models.
3. Report unweighted analytic n for every model.
4. Do not pool variables unless response coding is confirmed identical across cycles.

## Claims allowed

- "associated with"
- "population-level difference between survey cycles"
- "the association differed/did not differ by cycle" when supported

## Claims not allowed

- causal effect
- individual change over time
- validated digital-health-literacy construct
