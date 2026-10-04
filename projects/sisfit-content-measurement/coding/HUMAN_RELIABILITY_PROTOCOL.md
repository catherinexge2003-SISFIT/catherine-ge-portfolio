# Human Inter-Rater Reliability Protocol

## Status

This protocol governs the **formal human reliability stage** of the SISFIT Content Measurement Pilot.

The earlier 30-item agent-produced scoring file is an **AI rehearsal artifact only**. It was used to expose codebook ambiguities and must not be described as a human second coder or as formal inter-rater reliability.

## Frozen materials

- Codebook: `SISFIT Content Measurement Codebook v0.2`
- Codebook Git blob SHA at freeze: `665b9cd11ba17b053cee2f11b9fefb1bfcadc6c2`
- Reliability set: `PUB-001` through `PUB-030`
- Reliability-set size: 30 public-facing SISFIT health-education artifacts
- Reserve/practice items are excluded from the formal reliability statistics.

The frozen content bodies remain in the audited local reliability bundle. The public repository stores the ID manifest and coding protocol, not a duplicate content corpus.

## Human coders

- Coder A: Catherine
- Coder B: Starr

Both coders must code the same frozen 30-item set independently.

## Independence rules

1. Read `codebook.md` in full before coding.
2. Do not inspect the other coder's ratings before both files are locked.
3. Do not discuss borderline items during independent coding.
4. Do not modify codebook v0.2 after formal coding starts.
5. First pass: read the whole artifact without scoring.
6. Second pass: code all 11 variables.
7. Record a short `coder_note` for borderline judgements.
8. Save the raw coding file before any discussion or adjudication.
9. Calculate reliability **before** resolving disagreements.

## Input files

Create completed copies of:

- `coding/coder_catherine_template.csv`
- `coding/coder_starr_template.csv`

Recommended locked filenames after completion:

- `coding/coder_catherine_raw.csv`
- `coding/coder_starr_raw.csv`

Do not overwrite these raw independent files after adjudication.

## Primary reliability metrics

Binary variables:
- ordinary Cohen's kappa
- exact percent agreement

Ordinal 0–2 variables:
- linearly weighted Cohen's kappa using the **fixed codebook scale 0,1,2**
- exact percent agreement

The fixed scale is important: if one category happens not to occur in the 30-item sample, categories 0 and 2 must not be treated as adjacent.

## NA handling

### evidence_traceability

Primary kappa is pairwise complete. If only one coder uses `NA`, the item is excluded from the kappa denominator and the NA mismatch is reported separately.

### safety_boundary

This variable is structurally conditional on `risk_relevant`.

Primary safety-boundary reliability is calculated only where:
- both coders assign `risk_relevant=1`, and
- both provide a non-NA safety score.

The report separately counts:
- risk-relevance gate disagreements;
- safety-boundary NA mismatches.

Do not coerce structural `NA` to 0.

## Non-estimable kappa

If both coders assign one category to all usable items, kappa may be mathematically non-estimable even with 100% agreement.

In that case:
- report percent agreement;
- report kappa as `NA / not estimable`;
- do not call reliability poor solely because kappa is undefined.

This issue is particularly relevant to `purpose_clear`.

## Internal development rules

These are project-development thresholds, not universal psychometric standards.

- kappa >= 0.70: retain unless disagreement review exposes a systematic definition problem
- 0.60–0.69: review wording/examples before main coding
- kappa < 0.60: revise or drop before main coding
- kappa not estimable: inspect agreement and category variation qualitatively

No threshold decision is made from AI rehearsal ratings.

## Run command

```bash
python src/reliability.py \
  --coder-a coding/coder_catherine_raw.csv \
  --coder-b coding/coder_starr_raw.csv \
  --manifest coding/human_reliability_manifest.csv \
  --output-dir results/human_reliability
```

## After calculation

1. archive the raw reliability output;
2. identify variables requiring review;
3. only then discuss item-level disagreements;
4. preserve the original raw coder files;
5. document every adjudication;
6. if a definition changes materially, use a **fresh** reliability set rather than recoding the same 30 items and presenting that as independent reliability.
