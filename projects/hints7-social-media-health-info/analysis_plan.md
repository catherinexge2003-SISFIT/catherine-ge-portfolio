# Analysis Plan

## Study design

Cross-sectional secondary analysis of the 2024 HINTS 7 public-use dataset.

## Population

Primary analytic population: HINTS 7 respondents with valid responses to both `SocMed_TrueFalse` and `SocMed_MakeDecisions`, plus complete values for the prespecified adjustment set.

## Primary exposure

`SocMed_TrueFalse`

Question: "I find it hard to tell whether health information on social media is true or false."

Coding:
- exposed = 1: strongly agree / somewhat agree
- exposed = 0: somewhat disagree / strongly disagree
- negative HINTS special codes are treated as missing/inapplicable

## Primary outcome

`SocMed_MakeDecisions`

Question: "I use information from social media to make decisions about my health."

Coding:
- outcome = 1: strongly agree / somewhat agree
- outcome = 0: somewhat disagree / strongly disagree
- negative HINTS special codes are treated as missing/inapplicable

## Prespecified adjustment set

- `AgeGrpB`
- `Education`
- `RaceEthn5`
- `IncomeRanges_IMP`
- `BirthSex`
- `ConfidentMedForms`
- `Electronic2_HealthInfo`

Rationale: demographic composition, general health-information seeking and a health-literacy proxy may confound the association between perceived information-evaluation difficulty and reported use of social-media health information.

## Survey design

Point estimates use `PERSON_FINWT0`.

Variance estimates use `PERSON_FINWT1`–`PERSON_FINWT50` with delete-one JK1 replication:

`v(theta) = (R-1)/R * Σ(theta_r - theta_full)^2`, R = 50.

## Primary model

Weighted binomial logistic regression:

`uses_for_decisions ~ hard_to_judge + age + education + race/ethnicity + income + birth sex + confidence with medical forms + online health-information seeking`

Primary estimand: adjusted odds ratio for `hard_to_judge`.

## Secondary / sensitivity analyses

- ordinal model preserving 4-level outcome;
- secondary outcome: `SocMed_DiscussHCP`;
- alternative exposure: `MisleadingHealthInfo`;
- mode-effect assessment;
- comparison of complete-case and reduced-adjustment specifications.

## Interpretation constraints

- cross-sectional data;
- self-reported measures;
- no causal language;
- no inference that platform use produces behaviour change;
- no inference that difficulty judging truthfulness constitutes a validated digital-health-literacy scale.
