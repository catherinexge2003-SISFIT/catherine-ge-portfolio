# Preliminary Results

## Primary analysis

Analytic complete-case sample: **n = 5,183**.

Weighted prevalence of reporting use of social-media information to make personal health decisions:

- difficulty judging whether health information is true or false: **24.1%**
- no reported difficulty judging truthfulness: **15.1%**

Adjusted weighted logistic model:

- adjusted OR: **1.83**
- 95% CI: **1.42–2.34**
- p < **0.001**

The model adjusts for age group, education, race/ethnicity, imputed income category, sex assigned at birth, confidence filling out medical forms, and whether the respondent used the Internet to look for health or medical information.

Variance for the focal coefficient is estimated with the 50 HINTS JK1 replicate weights.

## Interpretation

The result is consistent with an association between difficulty evaluating the truthfulness of social-media health information and reported use of social-media information for personal health decisions.

It does **not** establish that difficulty evaluating information causes greater reliance on social-media health information, nor does it establish subsequent health behaviour change.

## Status

Preliminary. Robustness checks and a fuller survey-analysis audit are still required before this should be treated as a finished research output.


## Robustness checks

### Secondary outcome: discussion with a health-care provider

Using `SocMed_DiscussHCP` as the outcome and the same primary exposure/adjustment set:

- complete-case n = **5,184**
- adjusted OR = **2.07**
- 95% CI = **1.61–2.66**
- p < **0.001**

Respondents who reported difficulty judging whether social-media health information was true or false also had higher odds of reporting that they use social-media information in discussions with a health-care provider.

### Alternative exposure: perceived amount of false or misleading information

Using `MisleadingHealthInfo` as the exposure (a lot/some vs a little/none) and `SocMed_MakeDecisions` as the outcome:

- complete-case n = **5,181**
- adjusted OR = **0.47**
- 95% CI = **0.35–0.62**
- p < **0.001**

This association runs in the opposite direction: respondents who perceived a greater amount of false/misleading health information on social media had lower odds of reporting use of social-media information for personal health decisions.

### Interpretation of the contrast

The two exposures should not be collapsed into a single construct.

- `SocMed_TrueFalse` reflects **personal difficulty evaluating truthfulness**.
- `MisleadingHealthInfo` reflects **perceived prevalence of misinformation in the environment**.

Their opposite associations with health-decision use suggest potentially distinct mechanisms. This is an exploratory finding and should be tested with models that retain the original ordinal response structure.

## Remaining checks

- ordinal sensitivity analysis retaining the four response levels;
- mode-effect assessment if an appropriate administration-mode variable is available/documented for this public-use file;
- missing-data sensitivity;
- final PRICSSA reporting audit.


## Ordinal sensitivity analysis

To test whether the primary finding was an artifact of dichotomising the four-level `SocMed_MakeDecisions` response, a proportional-odds sensitivity model retained the original ordinal outcome.

- complete-case n = **5,183**
- proportional-odds OR for stronger agreement/use = **1.50**
- 95% CI = **1.25–1.78**
- p < **0.001**
- focal coefficient variance estimated with the 50 HINTS JK1 replicate weights

The direction remains consistent with the primary binary model, reducing concern that the main association is driven only by the binary cut-point.
