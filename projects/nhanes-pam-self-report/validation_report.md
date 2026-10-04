# Validation Report

## Overall Assessment

**Pre-execution: methodologically ready with explicit measurement caveats; numerical claims pending execution.**

## Official-source checks

Verified against CDC/NCHS NHANES 2013–2014 documentation:

- `PAXDAY_H` is a day-level physical-activity-monitor summary with multiple days per participant.
- `PAXMTSD` is the day sum of triaxial MIMS values.
- `PAXVMD` is the number of valid minutes in the day.
- NHANES instructs analysts using PAM data to use examined-sample weights.
- `PAQ_H` is based on the Global Physical Activity Questionnaire.
- `PAQ655` / `PAD660` capture vigorous recreational days and minutes.
- `PAQ670` / `PAD675` capture moderate recreational days and minutes.
- CDC documentation suggests MET scores of 8.0 for vigorous leisure activity and 4.0 for moderate leisure activity.
- `DEMO_H` supplies `WTMEC2YR`, `SDMVSTRA`, and `SDMVPSU`.

## Measurement decision

The project does not convert MIMS to MVPA minutes. The device metric is explicitly defined as mean daily MIMS per valid minute.

This avoids implying that MIMS has a universal intensity threshold when no validated threshold has been introduced in this analysis.

## Analyst-defined rule

Primary valid day = at least 1,200 valid minutes; participant must contribute at least 4 valid days.

This is an analyst-defined completeness rule, not a CDC standard. It must remain visible in any public interpretation.

## Remaining validation gates

1. Execute all four official XPT downloads.
2. Verify PAQ special-code handling and no-activity zero assignment.
3. Check participant row counts after each join.
4. Inspect the valid-day distribution before/after thresholding.
5. Verify MEC weights and masked strata/PSUs are present for every analytic row.
6. Inspect influential observations in both self-report and MIMS-density measures.
7. Run threshold sensitivity before any headline claim.

## Publication status

Do not add numerical NHANES results to the public site until all gates pass.
