# Execution Status

**Status: Ready to share with caveats.**

The NHANES 2013–2014 pipeline executed successfully end-to-end against official CDC/NCHS public-use XPT files.

## Validation completed

- official PAXDAY, PAQ, DEMO and BMX files downloaded and read successfully;
- device outcome uses `PAXMTSD / PAXVMD` and is described as MIMS movement density, not MVPA;
- self-reported leisure activity uses GPAQ recreational items with 8 METs for vigorous and 4 METs for moderate activity;
- survey design uses `WTMEC2YR`, `SDMVSTRA` and `SDMVPSU`;
- coefficient inference uses 15 survey design degrees of freedom;
- primary valid-day rule is explicitly analyst-defined;
- five valid-day/wear sensitivity specifications were run;
- BMI, socioeconomic and age-heterogeneity sensitivity models were run.

## Primary inference

Population: adults age 20+.

Primary analytic n = **4,726**.

For the model

`log1p(device movement density) ~ log1p(leisure MET-min/week) + age + sex + BMI`

the focal self-report coefficient was:

- beta = **0.00876**
- SE = **0.00248**
- 95% CI = **0.00347–0.01404**
- p = **0.0030**

Higher self-reported leisure physical activity was positively associated with higher device-measured movement density.

## Robustness

The focal coefficient remained positive across every prespecified valid-day/wear sensitivity:

- beta range: **0.00754–0.00876**
- all p <= 0.0034

Additional model checks:

- without BMI: beta = 0.01050, p < 0.001
- adding collapsed race/ethnicity and education: beta = 0.01077, p < 0.001

Public reporting must retain the cross-sectional, non-causal and measurement-non-equivalence caveats.
