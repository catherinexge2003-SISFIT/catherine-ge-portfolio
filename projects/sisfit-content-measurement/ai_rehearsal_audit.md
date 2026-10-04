# AI Rehearsal Audit — 2026-10-04

The 30-item agent-produced Coder 2 file is treated as an AI rehearsal artifact only, not as a human second coder or formal human inter-rater reliability.

## Distribution audit

- purpose_clear: 30/30 = 1
- plain_language: 25 = 2; 5 = 1
- evidence_traceability: 14 = 0; 13 = 1; 3 = 2
- actionability: 23 = 2; 5 = 1; 2 = 0
- uncertainty_calibration: 21 = 2; 8 = 1; 1 = 0
- causal_claim_strength: 21 = 1; 9 = 2
- risk_relevant: 28 = 1; 2 = 0
- safety_boundary: 15 = 2; 7 = 1; 6 = 0; 2 = NA
- self_monitoring_prompt: 26 = 1; 4 = 0
- behavior_change_support: 23 = 2; 4 = 1; 3 = 0
- commercial_call_to_action: 23 = 1; 7 = 0

## Problems exposed

1. purpose_clear showed zero variance; v0.2 now specifies percent agreement + kappa not estimable when no variation exists.
2. actionability and behavior_change_support were almost redundant; v0.2 separates one-off executable instructions from mechanisms supporting repetition/monitoring/maintenance.
3. uncertainty_calibration and causal_claim_strength were nearly mirror images; v0.2 makes causal_claim_strength independent of qualification, which remains under uncertainty_calibration.
4. risk_relevant was highly prevalent; v0.2 clarifies that very low-load awareness content may be 0 and that the variable captures meaningful safety/referral relevance.

## Formal next step

Freeze codebook v0.2. Use non-study/reserve items for orientation. Catherine and Starr should independently code the frozen 30-item set without seeing each other's ratings. Save raw files before discussion, then calculate agreement and kappa/weighted kappa before adjudication.

PR #3 remains Draft until human inter-rater reliability is complete.
