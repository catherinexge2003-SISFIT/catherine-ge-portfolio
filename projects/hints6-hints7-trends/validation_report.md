# Validation Report

## Overall Assessment

**Ready to share with caveats.**

## Methodology review

The project uses official NCI HINTS 6 (2022) and HINTS 7 (2024) public-use data as independent repeated cross-sectional samples.

The focal variables are directly comparable across both cycles:

- `SocMed_TrueFalse`
- `SocMed_MakeDecisions`

Both use the same four agreement response categories and are asked of social-media users.

The pooled variance structure follows the official NCI HINTS merging-tool logic:

- 100 Rizzo replicate weights for two cycles
- jackknife multiplier = 0.98
- df = 98
- MSE replicate variance

## Execution verification

GitHub Actions executed the full pipeline successfully against the official NCI files.

Verified analytic sample:

- HINTS 6: n = 4,912
- HINTS 7: n = 5,926
- pooled: n = 10,838

All 100 replicate regressions completed successfully.

## Primary calculation spot-check

Primary survey-year interaction:

- beta = 0.1820
- SE = 0.1859
- OR = 1.20
- 95% CI = 0.83–1.73
- t = 0.9793
- two-sided p = 0.330 using df = 98

The p-value was independently recomputed from the saved t statistic and df.

## Weighted prevalence spot-check

Use of social-media information for personal health decisions:

- 2022, no difficulty judging: 13.4% (95% CI 9.8%–17.0%)
- 2022, difficulty judging: 18.8% (15.8%–21.7%)
- 2024, no difficulty judging: 15.1% (12.5%–17.8%)
- 2024, difficulty judging: 24.2% (21.8%–26.6%)

## Interpretation

The descriptive gap is larger in HINTS 7, but the formal interaction test is not statistically significant. The evidence therefore does not establish that the exposure–outcome association changed between survey cycles.

## Required caveats

- repeated cross-sectional, not longitudinal
- no causal inference
- no within-person change
- a single HINTS item is not presented as a validated digital-health-literacy scale
