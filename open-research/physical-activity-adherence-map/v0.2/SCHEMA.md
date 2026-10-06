# v0.2 Schema

v0.2 preserves the v0.1 fields and adds only five fields required by the 2020–2026 refresh.

## Existing fields retained

- `study_id`
- `citation`
- `population`
- `target_behavior`
- `adherence_problem`
- `intervention`
- `BCT_or_mechanism`
- `duration`
- `outcome`
- `result_and_DOI`

## New v0.2 fields

### `phase_structure`
Plain-language temporal structure of behavior change exposure.

Examples:
- acquisition → maintenance
- active intervention → reduced-support follow-up
- continuous long-duration exposure
- multistage adaptive intervention

Do not call any long intervention “maintenance” unless the design actually distinguishes maintenance or follow-up.

### `shared_backbone_or_active_comparator`
What all groups receive, or what the active comparator already contains.

Purpose: prevent attributing the whole observed effect to the incremental digital component.

### `adaptation_or_personalization`
Use plain-language categories:

- none / NR
- static tailoring
- contextual / JITAI tailoring
- response-adaptive sequencing

Add a short factual description when needed.

Do not infer a more sophisticated adaptive mechanism than the paper states.

### `engagement_or_exposure`
Observed use, wear, message exposure, adherence, data completeness, or other direct evidence that the intervention was actually received.

Use `NR` when not reported.

Do not treat intervention delivery as equivalent to intervention exposure.

### `maintenance_interpretation`
One concise classification plus detail:

- sustained gain
- preserved behavior
- attenuation
- no maintenance advantage
- not a maintenance design

The classification must follow the actual time structure and comparator.

## Coding constraints

1. Author-described components first; no unverified BCTTv1 numeric codes.
2. Keep relative group advantage separate from absolute behavioral direction.
3. Keep acquisition, active treatment, maintenance, and post-intervention follow-up separate.
4. Active comparators must be described explicitly.
5. Behavior change must remain distinct from physiological or weight outcomes.
6. Engagement/missingness is an interpretation constraint, not a behavioral outcome.
7. Adaptive trials must preserve stage changes and response-triggered treatment changes.
