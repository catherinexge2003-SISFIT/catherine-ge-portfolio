# Coding Notes — Micro Map v0.1

## Core rule
Code what the study actually describes. Do not infer a more specific mechanism than the available source supports.

## Field rules
- `study_id`: PA001–PA010 for v0.1.
- `citation`: authors, year, title, journal, volume/issue/pages when available.
- `population`: sample type, N, and key age/clinical characteristic if reported.
- `target_behavior`: the concrete behavior measured (e.g., MVPA, steps/day, exercise completion).
- `adherence_problem`: plain-language behavioral problem stated or clearly motivated by the paper. If interpretive, mark it `[study rationale]` or `[inferred]`.
- `intervention`: delivery channel + intervention components. Avoid vague labels such as “digital intervention” when components are reported.
- `BCT_or_mechanism`: use author-described mechanism/component terms first. Do **not** assign BCTTv1 numeric codes in v0.1 unless independently verified.
- `duration`: intervention exposure duration.
- `outcome`: actual behavioral outcome(s).
- `result_and_DOI`: short directional result, not a causal overclaim; include DOI URL.

## Result language
Prefer: “associated with higher…”, “group increased…”, “no clear difference…”
Avoid: “proved”, “works”, “best”, or cross-study rankings in v0.1.

## Missing information
Use `NR` rather than guessing.

## Schema pressure tests
- Preserve time point when effects differ over time.
- Keep relative treatment effect and absolute behavioral direction distinct.
- Retain null-effect studies.
- Describe active comparators explicitly.
- Separate behavior change from physiological capacity.
- Do not code transient early response as sustained effect.
- Distinguish personal behavioral feedback from social comparison.
- More digital exposure is not automatically better maintenance.
- Label hybrid interventions as hybrid.
- Encode acquisition and maintenance phases separately when relevant.
