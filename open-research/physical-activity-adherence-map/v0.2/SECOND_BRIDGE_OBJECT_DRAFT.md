# Second Bridge Object — Draft Specification

## Working title

**Digital Physical-Activity Maintenance Failure Map v0.1**

Status: **draft only — do not publish yet**

## Purpose

The first Bridge Object maps digital physical-activity intervention structures.

This second object asks a narrower question:

> Where does durable incremental value break down after a digital physical-activity intervention has already supplied self-monitoring, feedback, or other behavioral support?

It is intended as a compact method object for expert correction, not as an effectiveness ranking.

## Proposed source

The current working source is:

- PA001–PA015 unified v0.2 manifest;
- Mechanism × Phase × Failure-Mode Matrix;
- cross-era structural analysis.

No new studies are required before the first external method check.

## Proposed public columns

1. study_id
2. phase
3. shared behavioral backbone / active comparator
4. incremental mechanism
5. adaptation class
6. engagement / exposure signal
7. maintenance outcome
8. primary failure mode
9. secondary failure signal
10. one-line structural interpretation
11. source DOI

## Controlled failure-mode vocabulary — working only

- F1 — no maintenance test
- F2 — effect attenuation
- F3 — comparator saturation
- F4 — burden / habituation
- F5 — exposure uncertainty / attrition
- F6 — maintenance add-on redundancy
- F7 — preservation rather than gain
- F8 — behavior-outcome decoupling
- F9 — response / relevance heterogeneity
- F10 — multi-component attribution ambiguity

## Release gates

Do **not** freeze or deposit this object until all of the following are true:

1. At least one external researcher/method expert has responded to the failure-mode distinction.
2. The response has been recorded as correction, acknowledgement, disagreement, or terminology guidance.
3. The vocabulary has been revised or explicitly retained after that check.
4. Each PA001–PA015 failure-mode assignment has a traceable source in the unified manifest/full-text notes.
5. The object clearly states that it is a selected-study structural map, not a systematic review, meta-analysis, causal model, or risk-of-bias assessment.
6. Versioned correction handling is defined before publication.

## External-check questions

Primary:

> Should mechanism failure despite adequate exposure be coded separately from exposure/engagement failure?

Secondary:

> Should preservation of behavior relative to a declining counterfactual be treated as a distinct maintenance success state?

## Current public check

GitHub Issue #13:
https://github.com/catherinexge2003-SISFIT/catherine-ge-portfolio/issues/13

## Relationship to first Bridge Object

The first object remains authoritative for v0.1:

**Physical Activity Adherence — Digital Intervention Micro Map v0.1**  
DOI: https://doi.org/10.5281/zenodo.23178043

The second object should only be released if external checking makes the failure-mode layer more defensible than an internal coding exercise.
