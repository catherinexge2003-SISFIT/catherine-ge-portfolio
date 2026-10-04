# NHANES Device-Measured Movement vs Self-Reported Leisure Physical Activity

## Research question

Among U.S. adults in NHANES 2013–2014, how is self-reported leisure-time physical activity associated with device-measured movement, and does that relationship vary by age group?

## Why this project

This project deliberately adds a different quantitative method and measurement domain to the portfolio:

- device-derived behavioural data
- repeated daily measurements
- self-report versus objective measurement
- NHANES complex survey design

It does **not** treat MIMS as minutes of moderate-to-vigorous physical activity.

## Data

Official CDC/NCHS NHANES 2013–2014 public-use files:

- `PAXDAY_H.xpt` — day-level physical activity monitor summary
- `PAQ_H.xpt` — Global Physical Activity Questionnaire-derived items
- `DEMO_H.xpt` — demographics and survey design variables
- `BMX_H.xpt` — BMI

The day-level PAM file is used instead of the very large minute-level file.

## Device-derived outcome

For each valid day:

`movement_density = PAXMTSD / PAXVMD`

where:

- `PAXMTSD` = day sum of triaxial MIMS units
- `PAXVMD` = valid minutes in that day

Primary participant-level device metric:

mean movement density across days with at least 1,200 valid minutes, requiring at least 4 valid days.

The 1,200-minute threshold is an analyst-defined completeness rule for this project and is reported explicitly rather than presented as a CDC standard.

## Self-reported exposure

Leisure-time MET-min/week:

`8 × PAQ655 × PAD660 + 4 × PAQ670 × PAD675`

with zero assigned for the corresponding vigorous/moderate leisure component when the respondent explicitly reports no participation.

## Survey analysis

NHANES MEC examination weights are used because PAM and BMI are examination-derived:

- weight: `WTMEC2YR`
- strata: `SDMVSTRA`
- PSU: `SDMVPSU`

Primary model:

`log1p(device movement density) ~ log1p(leisure MET-min/week) + age group + sex + race/ethnicity + education + BMI`

Secondary model adds:

`log1p(leisure MET-min/week) × age group`

## Interpretation limits

- The device metric is MIMS movement density, not MVPA minutes.
- Self-reported leisure activity and 24-hour device movement measure related but non-identical constructs.
- Cross-sectional association only.
- Measurement discordance must not be described as respondent error without additional validation evidence.

## Official sources

- PAM day file documentation: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/PAXDAY_H.htm
- Physical Activity Questionnaire: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/PAQ_H.htm
- Demographics/weights: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/DEMO_H.htm
- Body measures: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles/BMX_H.htm
