# Failure-Mode Taxonomy — Expert Check Packet

Status: **working v0.2 material — not frozen or published**

## Why this check exists

The PA001–PA015 cross-era map suggests that a single label such as “the intervention did not maintain its effect” collapses several structurally different failure modes.

We currently distinguish:

- **effect attenuation** — an early advantage weakens or disappears;
- **comparator saturation** — the comparator already contains a strong behavioral backbone;
- **burden / habituation** — frequency, repetition or automation reduces attention;
- **exposure uncertainty / attrition** — the intervention may be delivered without being meaningfully received;
- **maintenance add-on redundancy** — continuing an acquisition component adds no measurable maintenance value;
- **preservation rather than gain** — success is prevention of decline rather than further improvement;
- **behavior-outcome decoupling** — behavior changes without a corresponding downstream physiological/clinical change;
- **response / relevance heterogeneity** — average effects conceal differences by responder status or perceived usefulness;
- **multi-component attribution ambiguity** — package effects cannot identify the active ingredient.

These are descriptive coding categories, not claims of causal mechanisms.

## Terminology grounding

Before requesting external review, we cross-walked the working labels against implementation-fidelity, treatment-fidelity, digital-engagement, process-evaluation, and behavior-maintenance frameworks.

The implementation/exposure versus mechanism-of-impact distinction is therefore **not claimed as novel**. See:

`TERMINOLOGY_CROSSWALK.md`

## Narrow expert-check question 1

Is our **operational mapping** of these PA trials onto implementation/exposure versus incremental behavioral-effect failure defensible, and are we using the most appropriate established terminology?

Example contrast:

- PA006: SMS was delivered repeatedly, but some participants stopped reading messages and many judged the frequency excessive.
- PA013: JITAI coaching was delivered, but actual message reading was not verifiable and only ~30% of possible daily step observations were present.

Our proposed rule:

> Do not infer failure of a hypothesized behavioral mechanism from a null behavioral result when meaningful intervention receipt/exposure is weak or uncertain. Code the implementation/exposure evidence separately, and reserve mechanism-of-impact claims for studies that actually measure them.

For public wording, prefer **no incremental behavioral effect despite documented exposure** over **mechanism failed** unless a mechanism of action was directly measured.

## Narrow expert-check question 2

Should **preservation of behavior** be coded as a distinct maintenance success state rather than as a weaker form of continued improvement?

Example:

- PA014: tracker/professional-support and telephone-counseling groups largely maintained step levels while usual care declined.
- PA007: an apparent intervention advantage largely reflected less decline rather than absolute increase.

Our proposed rule:

> In maintenance research, “preserved behavior relative to a declining counterfactual” should be distinguishable from “continued gain.”

## Why the distinction matters

Without these distinctions, three very different observations can collapse into the same label:

1. the intervention was used but did not work;
2. the intervention was not meaningfully used;
3. the intervention successfully prevented decline but did not increase behavior further.

## Materials

- Unified PA001–PA015 manifest:
  https://github.com/catherinexge2003-SISFIT/catherine-ge-portfolio/blob/main/open-research/physical-activity-adherence-map/v0.2/micro_map_manifest_v0.2.csv
- Mechanism × Phase × Failure-Mode Matrix:
  https://github.com/catherinexge2003-SISFIT/catherine-ge-portfolio/blob/main/open-research/physical-activity-adherence-map/v0.2/MECHANISM_PHASE_FAILURE_MATRIX.md
- Frozen v0.1 DOI:
  https://doi.org/10.5281/zenodo.23178043

## Useful response

A useful expert response can be very short:

- keep the distinctions as written;
- merge specific categories;
- rename one or more categories;
- point out a conceptual problem or established terminology we should use instead.

Maintainers: Catherine Ge and Starr Choi  
SISFIT Open Research
