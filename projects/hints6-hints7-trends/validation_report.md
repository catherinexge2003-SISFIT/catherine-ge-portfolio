# Validation Report

## Overall Assessment

**Pre-execution: methodologically ready; numerical claims pending execution.**

## Source compatibility checks

Verified against official NCI HINTS documentation:

- HINTS 6 = 2022, n=6,252.
- HINTS 7 = 2024, n=7,278.
- `SocMed_MakeDecisions` appears in both HINTS 6 and HINTS 7.
- `SocMed_TrueFalse` appears in both HINTS 6 and HINTS 7.
- Both use the same four response categories:
  1. Strongly agree
  2. Somewhat agree
  3. Somewhat disagree
  4. Strongly disagree
- Both are asked of social-media users.
- The official HINTS merging guidance supports combining repeated cross-sectional cycles to examine trends over time.
- For two cycles, the official merging tool generates 100 Rizzo replicate weights and specifies jackknife multiplier 0.98 with 98 df.

## Main methodological risk addressed

A naive append using only 50 replicate weights would under-specify the merged survey variance structure. The project instead constructs cycle-specific 50-weight blocks within a 100-replicate pooled design.

## Remaining validation gates

1. Execute against the August 2025 public-use files.
2. Confirm exact variable names after lower-casing.
3. Reconcile one generated respondent's 100 replicate weights against the NCI tool logic.
4. Confirm prevalence and regression outputs are finite across all 100 replicates.
5. Independently recompute the headline interaction estimate before publication.

## Publication status

Do not add numerical HINTS 6+7 results to the public site until all gates pass.
