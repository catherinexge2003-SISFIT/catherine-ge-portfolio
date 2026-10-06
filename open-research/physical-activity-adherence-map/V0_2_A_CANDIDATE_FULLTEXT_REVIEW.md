# v0.2 A-Candidate Full-Text Review

Status: **full-text adjudication complete for A candidates**.  
This review does not modify frozen v0.1 and does not yet assign PA011+ IDs.

## Decision rule

Each candidate must:

1. pass the existing inclusion rules;
2. add a mechanism, temporal structure, comparator structure, or engagement problem not already adequately represented in v0.1;
3. be interpretable without inventing BCTTv1 codes;
4. preserve the distinction between intervention exposure, behavioral outcome, and maintenance.

---

## R01 — Simoes et al. (2026)

**DOI:** https://doi.org/10.2196/73388  
**Decision:** **PASS — core v0.2 candidate**

### Population
Adults and older adults; N=53; mean age 44.0 years.

### Design
Sequential multiple assignment randomized trial (SMART).

Initial allocation:
- app + tailored messages;
- app + tailored messages + gamification I;
- educational-information control.

At week 6, intervention participants were classified as responders/nonresponders from step-count response. Nonresponders could be rerandomized and receive an intensified gamification/support package.

### Digital components
- Pacer smartphone app;
- daily-step self-monitoring;
- tailored messages;
- ranking;
- virtual challenges/badges;
- social interaction/support features.

### Author-described mechanism/components
- self-monitoring;
- goal setting;
- tailored feedback/messages;
- graded tasks;
- rewards/badges;
- social comparison;
- social support;
- educational instructions.

### Time structure
- 0–6 weeks: initial intervention;
- week 6: response classification / possible rerandomization;
- 6–12 weeks: adapted second stage;
- 12–24 weeks: follow-up; participants were advised to continue monitoring step count in the app without direct researcher intervention.

### Behavioral outcomes
Objective accelerometer-measured:
- daily steps;
- sedentary behavior;
- MVPA.

### Key result relevant to the map
The study demonstrates a response-adaptive intervention structure rather than a fixed digital package. Group 1 showed sustained step-count increases through follow-up; responder trajectories were favorable, while the control group declined at follow-up.

### Coding pressure
The current v0.1 schema cannot represent:
- **response-triggered adaptation**;
- different intervention components across stages;
- the distinction between active adaptive treatment and later self-directed app monitoring.

### Main caution
Do not summarize this as “gamification worked.” The SMART design, small sample, changing treatment sequences, and responder classification make component attribution more complex.

---

## R02 — Sagelv et al. / ONWARDS (2025)

**DOI:** https://doi.org/10.1136/bmjsem-2023-001816  
**Decision:** **PASS — core v0.2 candidate**

### Population
Self-reported inactive adults; N=183; age 22–55 years.

### Arms
- **A:** activity tracker + PAI app;
- **B:** A + home-based online training;
- **C:** B + online peer support.

There was no inactive/no-intervention control.

### Digital components
- wearable activity tracker;
- PAI personalized activity metric/app;
- online exercise videos;
- closed social-media peer-support group.

### Author-described components
- goal setting;
- monitoring;
- personalized feedback;
- structured home exercise;
- peer/social support.

### Time structure
18-month intervention with assessments at 6, 12, and 18 months.

### Behavioral outcomes
ActiGraph-measured:
- MVPA;
- light PA;
- total PA;
- steps;
- sedentary time.

### Key result relevant to the map
No sustained group-by-time advantage across the three increasingly intensive digital packages. Group C showed a temporary 6-month MVPA advantage, but the groups converged later. Overall MVPA declined from baseline over 18 months.

### Engagement / data issue
Accelerometer follow-up completeness declined substantially; only 42.7% provided accelerometer data at 18 months.

### Coding pressure
This study requires explicit representation of:
- **nested active comparators**;
- “more components” versus “more effect”;
- attenuation over long follow-up;
- missing follow-up data as an interpretation constraint.

### Main caution
Baseline device reactivity / unusually high measured activity and lack of a nonintervention control mean the trial should not be coded as evidence that the base tracker/app package itself was effective.

---

## R03 — Vos et al. / SNapp (2025)

**DOI:** https://doi.org/10.1016/j.amepre.2024.09.010  
**Decision:** **PASS — core v0.2 candidate**

### Population
Adults living in low-socioeconomic-position neighborhoods in the Netherlands; N=176; mean age about 56 years; 76% female.

### Arms
- step-counter app + just-in-time adaptive coaching;
- step-counter app only.

### Digital components
- SNapp step counter;
- server-generated coaching;
- Telegram push notifications;
- contextual suggestions linked to suitable walking environments.

### Author-described components
- self-monitoring;
- individually tailored feedback;
- preference-sensitive walking advice;
- context-aware walking suggestions.

### Time structure
Participants were followed for 6 or 12 months depending on municipality/funding period; follow-up questionnaires occurred at 3, 6, and 12 months where applicable.

### Behavioral outcome
Daily steps continuously recorded by smartphone sensors.

### Key result relevant to the map
Average intervention effect on steps was not significant. **Perceived usefulness moderated the intervention effect**: participants who experienced the intervention as more useful showed a more favorable response.

### Engagement / exposure issue
Only about 30% of possible daily step-count observations were present, and missingness increased over time. The study could not establish whether coaching messages were actually read.

### Coding pressure
This study adds two constructs the current schema does not capture:
- **contextual/JITAI tailoring**;
- **effect modification by perceived usefulness / experienced relevance**.

It also shows why “intervention delivered” must not be treated as “intervention received.”

### Main caution
The active control already contained self-monitoring, and the intervention’s incremental value was therefore the adaptive coaching layer, not digital self-monitoring itself.

---

## R04 — Brickwood et al. (2021)

**DOI:** https://doi.org/10.2196/18686  
**Decision:** **PASS — core maintenance candidate**

### Population
Older adults >60 years; N=117; mean age 72.4 years.

### Pre-randomization context
Participants had just completed a 12-week individualized community exercise program. Trial baseline therefore represents a **post-program maintenance starting point**, not an untreated baseline.

### Arms
- activity tracker + accredited exercise-physiologist support;
- telephone counseling;
- usual care.

### Digital components
- Jawbone UP24 tracker;
- smartphone app;
- weekly personalized text messages / professional support.

### Author-described components
- self-monitoring;
- goal setting;
- feedback;
- motivational interviewing / self-efficacy support.

### Time structure
12 months, assessed at 3, 6, and 12 months.

### Behavioral outcome
ActivPAL-measured daily steps and nonstepping time; self-reported PA also collected.

### Key result relevant to the map
Tracker and telephone-counseling groups largely maintained steps; usual care declined. Between-group contrasts were not uniformly significant.

### Engagement
Activity-tracker participants wore the device on about 84% of available days.

### Coding pressure
The schema needs to distinguish:
- **maintenance after a prior intervention** from acquisition of a new behavior;
- digital support versus nondigital human support;
- preserved behavior from actual additional gains.

### Main caution
This is a maintenance trial layered on a prior exercise program. It should not be coded as a clean test of tracker efficacy for initially inactive adults.

---

## R05 — Yoshimura et al. (2022)

**DOI:** https://doi.org/10.2196/35628  
**Decision:** **PASS — core long-duration exposure candidate**

### Population
Adults aged 30–60 years; N=109; mean age 47 years.

### Arms
- step-count smartphone app;
- control.

### Shared intervention backbone
Both groups received:
- a 1-hour lecture on weight loss and PA;
- daily self-weighing instructions;
- monthly motivational/advisory emails;
- periodic feedback;
- accelerometer-based step display during assessment periods.

### App-specific components
The app group was asked to:
- open the app daily;
- check step count;
- check group rank.

### Time structure
32-week intervention, with assessments at 10–12 and 30–32 weeks.

### Behavioral outcomes
Objective triaxial-accelerometer:
- step count;
- MVPA.

Also measured:
- body weight.

### Key result relevant to the map
The app group showed a more favorable step-count trajectory, especially on weekends, but **did not obtain additional weight loss**.

### Engagement
Daily app checking declined over time but remained substantial: about 80% early and about 74% during weeks 12–32.

### Coding pressure
This paper requires explicit coding of:
- **shared intervention backbone**;
- incremental app component;
- engagement over time;
- behavioral outcome versus downstream physiological/weight outcome.

### Main caution
The app should not be treated as the whole intervention. The correct contrast is the incremental effect of step/rank app exposure on top of a shared behavior-change program.

---

# Cross-paper schema pressure test

The five A candidates expose recurring weaknesses in the v0.1 schema.

## Pressure 1 — One “intervention” field is no longer enough

Modern trials contain:
- shared treatment backbones;
- nested add-on components;
- multistage intervention sequences;
- response-triggered adaptation.

**Required distinction:** what everyone receives versus what differs between arms.

## Pressure 2 — Acquisition and maintenance are not equivalent

Three different temporal structures appear:

1. **Active acquisition → post-intervention maintenance**  
   Example: R04 starts after a previous exercise program.

2. **Active intervention → reduced-support follow-up**  
   Example: R01 ends researcher interference after week 12 but continues self-monitoring.

3. **Long-duration continuous exposure**  
   Example: R05 remains an active 32-week intervention and should not automatically be called maintenance.

## Pressure 3 — Delivery ≠ exposure ≠ engagement

Examples:
- R03 could not confirm message reading and retained step data on only ~30% of possible days.
- R05 app checking declined over time.
- R04 tracker wear remained relatively high.

The map needs to preserve actual use/exposure information when reported.

## Pressure 4 — Personalization now has multiple forms

“Tailored” is too broad.

At minimum, distinguish:
- static personalization;
- contextual/JITAI tailoring;
- response-adaptive treatment sequencing;
- user-perceived relevance/usefulness.

## Pressure 5 — Active comparator structure changes interpretation

A null between-group effect can mean very different things when the comparator is:
- education only;
- self-monitoring app;
- tracker/app base package;
- telephone counseling;
- the same behavior-change backbone without one digital add-on.

## Pressure 6 — Outcome hierarchy must remain explicit

R05 reinforces v0.1:
- increased PA behavior does not guarantee greater weight loss.

R02 reinforces:
- short-term relative advantage can disappear over longer follow-up.

---

# Minimal schema change for v0.2

Do not create a large new ontology. Add only five fields:

1. **phase_structure**  
   Acquisition / active intervention / maintenance / post-intervention follow-up.

2. **shared_backbone_or_active_comparator**  
   What both/all arms receive before identifying the incremental digital component.

3. **adaptation_or_personalization**  
   None / static tailoring / contextual-JITAI / response-adaptive sequencing, with plain-language detail.

4. **engagement_or_exposure**  
   Use, wear, message exposure, adherence, or data completeness when reported.

5. **maintenance_interpretation**  
   Sustained gain / preserved behavior / attenuation / no maintenance advantage / not a maintenance design.

Existing fields remain:
population, target behavior, adherence problem, intervention, mechanism/component, duration, outcome, result + DOI.

---

# Adjudication

All five A candidates pass the existing inclusion rules and each adds nonredundant structure.

**Recommended v0.2 core refresh set:**
- R01 Simoes 2026 — adaptive SMART
- R02 ONWARDS 2025 — long-term nested digital components
- R03 Vos 2025 — JITAI + usefulness moderation
- R04 Brickwood 2021 — post-program maintenance + digital vs human support
- R05 Yoshimura 2022 — long-duration app exposure + behavior/weight divergence

These are now ready for formal PA011–PA015 assignment **if the v0.2 schema change above is accepted**.
