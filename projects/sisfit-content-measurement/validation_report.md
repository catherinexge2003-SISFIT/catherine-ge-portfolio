# Validation Report

## Overall assessment

**Measurement framework and formal human-reliability workflow are ready. Human reliability results are pending.**

This is not yet a completed reliability study and must not be described as a validated measurement instrument.

## Research-development question

Can recurring communication, safety and behaviour-support features of SISFIT's public-facing digital health-education content be operationalised and coded reproducibly?

The current phase evaluates the measurement framework itself, not audience response or health outcomes.

## Framework grounding

The custom framework is conceptually informed by:

- AHRQ Patient Education Materials Assessment Tool (PEMAT), especially understandability and actionability;
- CDC Clear Communication Index, including main message, plain language, state of science, behavioural recommendations and risk communication.

The SISFIT codebook is not presented as a validated version or derivative of either instrument.

## Development history

### Feasibility stage

A small feasibility pilot exposed the need to:
- keep evidence traceability separate from evidence quality;
- separate uncertainty calibration from causal-claim strength;
- distinguish risk relevance from safety-boundary quality;
- permit explicit NA handling.

### AI rehearsal stage

A 30-item agent-produced Coder 2 rehearsal was used only to stress-test codebook definitions.

It is **not** treated as:
- a human second coder;
- formal inter-rater reliability;
- evidence that the coding instrument is reliable.

The rehearsal exposed four main issues:
1. `purpose_clear` had near-zero/zero variation;
2. actionability and behaviour-change support needed sharper separation;
3. uncertainty calibration and causal-claim strength needed independent definitions;
4. risk relevance needed a clearer low-risk boundary.

These issues were addressed before freezing codebook v0.2.

## Formal human reliability stage

Frozen materials:

- Codebook: v0.2
- Codebook Git blob SHA: `665b9cd11ba17b053cee2f11b9fefb1bfcadc6c2`
- Human reliability set: `PUB-001`–`PUB-030`
- n = 30
- Human coders: Catherine and Starr
- No discussion/adjudication permitted before both raw files are locked.

The 30 content bodies remain in the audited local frozen sample bundle. The repository stores the sample manifest, protocol and analysis code.

## Statistical plan

Binary variables:
- exact percent agreement
- ordinary Cohen's kappa

Ordinal variables:
- exact percent agreement
- linearly weighted Cohen's kappa on the fixed 0–1–2 codebook scale

### Conditional missingness

`evidence_traceability`:
- pairwise complete primary calculation;
- one-sided NA use is separately reported.

`safety_boundary`:
- reliability is calculated only where both coders independently assign `risk_relevant=1`;
- low-risk structural NA rows are excluded;
- risk-gate disagreements are reported separately.

### Non-estimable kappa

If both coders use only one category, kappa may be undefined despite 100% agreement. The workflow reports this explicitly rather than treating undefined kappa as poor reliability.

## Internal development rules

Pre-specified in codebook v0.2:

- kappa >= 0.70: retain unless qualitative review finds a systematic problem;
- 0.60–0.69: review definition/examples;
- < 0.60: revise/drop before main coding;
- non-estimable: inspect agreement and category variation.

These are internal development rules, not universal psychometric standards.

## Automated QA

The repository reliability implementation currently verifies:

- percent-agreement calculation;
- ordinary kappa with category variation;
- non-estimable kappa under zero variation;
- linearly weighted ordinal kappa on a fixed 0–1–2 scale;
- structural exclusion of `safety_boundary` when both coders mark low risk;
- explicit logging of risk-gate disagreement;
- explicit logging of evidence-traceability NA mismatch;
- exact 30-ID frozen manifest.

GitHub Actions validation passed before this report was updated.

## Governance

Current phase uses only SISFIT-authored public artifacts.

Excluded:
- comments;
- DMs;
- private groups;
- client records;
- health records;
- identifiable audience data;
- inferred audience outcomes.

Any future linkage to private analytics, individual users or outcomes requires a separate governance/ethics assessment.

## Current release decision

**Retain as Draft research-development project until formal human double coding is complete.**

Remaining promotion gates:

1. Catherine completes and locks all 30 ratings.
2. Starr completes and locks all 30 ratings independently.
3. Pre-adjudication reliability outputs are generated and archived.
4. Variables below the internal development rules are reviewed.
5. If codebook definitions change materially, a fresh reliability set is used.
6. Only after the measurement stage is stable should a larger corpus be coded and analysed.
