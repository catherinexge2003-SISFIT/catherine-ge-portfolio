# Formal Human Two-Coder Procedure

This directory contains the formal 30-item human reliability workflow.

The earlier AI/agent scoring exercise is **not** a human coder and is documented separately in `../ai_rehearsal_audit.md`.

## Frozen set

- IDs: `PUB-001` through `PUB-030`
- Manifest: `human_reliability_manifest.csv`
- Codebook: `../codebook.md` — v0.2
- Frozen codebook Git blob: `665b9cd11ba17b053cee2f11b9fefb1bfcadc6c2`

## Human coders

- Catherine
- Starr

Each coder must independently code all 30 artifacts.

Start from:
- `coder_catherine_template.csv`
- `coder_starr_template.csv`

The corresponding content bodies remain in the audited local frozen reliability bundle and are identified by content ID.

## Rules

1. Read the codebook before coding.
2. Do not inspect the other coder's scores.
3. Do not discuss borderline items before both raw files are locked.
4. Do not edit codebook v0.2 during formal coding.
5. Read each artifact once without scoring.
6. Score on the second pass.
7. Record borderline evidence in `coder_note`.
8. Save raw independent files before reliability calculation.
9. Calculate reliability before adjudication.
10. Never overwrite the raw independent files after discussion.

Full protocol: `HUMAN_RELIABILITY_PROTOCOL.md`.

## Locked filenames

After completion, save copies as:

- `coder_catherine_raw.csv`
- `coder_starr_raw.csv`

## Reliability command

From `projects/sisfit-content-measurement/`:

```bash
python src/reliability.py \
  --coder-a coding/coder_catherine_raw.csv \
  --coder-b coding/coder_starr_raw.csv \
  --manifest coding/human_reliability_manifest.csv \
  --output-dir results/human_reliability
```

The script validates the entire 30-ID set before calculating reliability.

Outputs:
- `results/human_reliability/reliability_by_variable.csv`
- `results/human_reliability/reliability_report.md`

Do not create adjudicated scores until these pre-adjudication outputs are archived.
