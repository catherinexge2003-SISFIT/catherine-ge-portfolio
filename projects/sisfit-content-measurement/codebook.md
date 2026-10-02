# SISFIT Content Measurement Codebook v0.1

## General rule

Code the **content artifact as published/presented**, not what the coder thinks the author intended.

Do not infer audience effects.

Use `NA` only where the codebook explicitly allows it.

## Context fields

### content_id
Stable unit identifier.

### title
Public title or repository artifact title.

### artifact_type
Allowed values:
- long_form_article
- short_form_post
- course_education_asset
- public_repository_draft
- other

### topic
Short descriptive topic, not an analytical score.

### eligible_for_main_study
- 1 = published public-facing health-education artifact eligible for the future main corpus
- 0 = pilot/edge-case artifact not eligible for the main corpus

---

# Primary coded variables

## 1. purpose_clear — binary

Does the artifact make its main purpose or central message clear?

- 0 = unclear / multiple competing purposes without a clear main message
- 1 = central purpose is readily identifiable

Do not judge whether the purpose is scientifically correct.

## 2. plain_language — ordinal 0–2

How accessible is the language to a general audience?

- 0 = frequent unexplained technical language, dense phrasing or specialist assumptions
- 1 = mixed; some technical language is explained but important passages remain demanding
- 2 = predominantly everyday language; technical terms are avoided or explained in context

This construct is conceptually informed by AHRQ PEMAT and CDC clear-communication guidance.

## 3. evidence_traceability — ordinal 0–2 or NA

For substantive scientific/health claims, can a reader trace the evidence source?

- 0 = substantive claims are made with no usable source path
- 1 = source is mentioned generically or by author/institution/study without enough information to locate it easily
- 2 = references, links, DOI, guideline identifiers or a sufficiently specific source list are supplied
- NA = the artifact does not make substantive scientific/health evidence claims

Do not score quality of the cited evidence here. This variable measures traceability only.

## 4. actionability — ordinal 0–2

Can the reader identify what action to take?

- 0 = information only; no actionable recommendation
- 1 = an action is suggested but steps/conditions are vague
- 2 = actions are explicit, broken into usable steps, or accompanied by clear implementation guidance

Conceptually informed by PEMAT actionability.

## 5. uncertainty_calibration — ordinal 0–2

How consistently does the artifact calibrate certainty to the strength of the claim?

- 0 = repeated absolute language, unsupported thresholds, universal claims, or strong certainty without visible qualification
- 1 = mixed calibration; some caveats are present but strong statements remain
- 2 = uncertainty/limits are consistently signalled; associations, mechanisms, hypotheses and established facts are distinguished

This is **not** an evidence-quality score.

## 6. causal_claim_strength — ordinal 0–2

What is the strongest causal/diagnostic/treatment claim made?

- 0 = no causal/diagnostic/treatment claim, or explicitly non-causal/descriptive framing
- 1 = mechanism or causal interpretation suggested with qualification
- 2 = unqualified causal, diagnostic, treatment, or deterministic language

Higher values do not mean better communication.

## 7. risk_relevant — binary

Does the artifact contain advice, self-testing, exercise, symptom interpretation, special-population guidance or another element for which inappropriate use could plausibly matter?

- 0 = no meaningful safety/referral relevance
- 1 = safety/referral relevance exists

## 8. safety_boundary — ordinal 0–2 or NA

If `risk_relevant=1`, how clearly are limits/referral conditions communicated?

- 0 = no meaningful safety boundary
- 1 = generic caution, contraindication or “consult a professional” language
- 2 = explicit red flags, stop criteria, referral triggers, excluded populations, or clearly bounded scope

- NA = `risk_relevant=0`

A generic disclaimer does not automatically receive 2.

## 9. self_monitoring_prompt — binary

Does the artifact ask the audience to observe, assess, record or monitor their own state/behaviour?

- 0 = no
- 1 = yes

Examples include self-checks, logs, ratings or repeated monitoring prompts.

This variable is descriptive; it does not imply the self-test is valid.

## 10. behavior_change_support — ordinal 0–2

Beyond information provision, does the artifact contain structured support for doing something differently?

- 0 = information only
- 1 = one support element, such as a prompt, practice instruction, planning cue or self-monitoring task
- 2 = multiple coordinated support elements, such as self-assessment + explicit practice + repetition/monitoring/planning

Do not infer behaviour change actually occurred.

## 11. commercial_call_to_action — binary

- 0 = no product/service/signup/purchase/trial CTA
- 1 = explicit commercial/product CTA

This is contextual, not a quality score.

---

# Coding process

1. Read the entire artifact once without coding.
2. On the second pass, code each primary variable.
3. Add a one-sentence evidence note for any score that depends on a borderline judgement.
4. Do not discuss scores with the other coder until the reliability set is complete.
5. Calculate agreement before adjudication.
6. Resolve disagreements only after reliability statistics have been saved.

## Project decision rules for reliability

These are internal development thresholds, not universal standards.

- kappa >= 0.70: retain variable unless qualitative disagreements reveal a systematic definition problem
- 0.60–0.69: review definition and examples before main coding
- < 0.60: stop and revise/drop the variable before main coding

For ordinal variables, use linearly weighted Cohen's kappa.
For binary variables, use ordinary Cohen's kappa.

Always report percent agreement alongside kappa.
