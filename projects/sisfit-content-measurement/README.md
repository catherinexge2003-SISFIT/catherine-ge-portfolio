# SISFIT Content Measurement Pilot

## Working title

**Operationalising Communication, Safety and Behaviour-Support Features in Digital Health-Education Content: A Reproducible Coding Framework Pilot**

## Purpose

This project develops and tests a reproducible coding framework for public-facing SISFIT health-education content.

The project asks whether communication features can be defined and coded consistently enough for later observational content research. It does **not** infer audience health outcomes from engagement metrics.

## Current stage

**Human inter-rater reliability stage.**

A 30-item reliability set (`PUB-001`–`PUB-030`) is frozen. Codebook v0.2 is frozen before formal human double coding.

The earlier 30-item AI/agent scoring exercise is retained only as a **codebook-development rehearsal**. It is not a human second coder and is not formal inter-rater reliability.

Formal human coders:
- Catherine
- Starr

Both must independently code all 30 frozen items before reliability is calculated or disagreements are discussed.

## Constructs

The v0.2 framework operationalises:

1. purpose clarity
2. plain language
3. evidence traceability
4. actionability
5. uncertainty calibration
6. causal-claim strength
7. risk relevance
8. safety/referral boundaries
9. self-monitoring prompts
10. behaviour-change support
11. commercial call to action

The framework is custom to this project. It is conceptually informed by:
- AHRQ Patient Education Materials Assessment Tool (PEMAT)
- CDC Clear Communication Index

It is not presented as a validated derivative of either instrument.

## Frozen reliability materials

- `codebook.md` — Codebook v0.2
- `coding/human_reliability_manifest.csv` — 30 frozen IDs
- `coding/HUMAN_RELIABILITY_PROTOCOL.md` — independence and analysis contract
- `coding/coder_catherine_template.csv`
- `coding/coder_starr_template.csv`
- `src/reliability.py` — pre-adjudication reliability analysis
- `results/STATUS.md` — current project status

The content bodies remain in the audited local sample bundle rather than being duplicated into this repository.

## Reliability plan

Binary variables:
- exact agreement
- ordinary Cohen's kappa

Ordinal variables:
- exact agreement
- linearly weighted Cohen's kappa on the fixed 0–1–2 scale

Conditional NA logic is handled explicitly, especially for `safety_boundary`.

If kappa is non-estimable because a variable has no category variation, agreement is still reported and the non-estimability is documented.

## Governance boundary

Current phase uses only SISFIT-authored public content.

Excluded:
- user comments
- private messages
- private groups
- client records
- health records
- identifiable user data
- inferred audience outcomes

Any later linkage to users, comments, private analytics or intervention outcomes requires a separate governance/ethics decision.

## Release boundary

This project is a **research-development artifact**, not yet a completed reliability study.

Promotion to a finished portfolio research output requires:
1. both human coder files locked before discussion;
2. reliability calculated before adjudication;
3. underperforming variables reviewed;
4. a fresh reliability set if codebook definitions materially change;
5. final corpus and downstream analysis documented.
