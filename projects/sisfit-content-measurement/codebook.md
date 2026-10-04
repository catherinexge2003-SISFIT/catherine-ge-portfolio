# SISFIT Content Measurement Codebook v0.2

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

**Reliability note:** if both coders assign the same category to every item, Cohen's kappa is not estimable because there is no between-item variation. In that case, report percent agreement and mark kappa as not estimable. If this variable remains near-constant in the formal reliability set, treat it as descriptive/contextual rather than a discriminating main-study measure.

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

What is the **type/strength of the strongest causal, diagnostic or treatment claim**, independent of whether the wording is appropriately qualified?

- 0 = descriptive/associational content only; no causal, diagnostic or treatment claim
- 1 = a causal or mechanistic relationship is proposed/stated, but the content does not make a deterministic diagnosis, treatment claim or universal causal conclusion
- 2 = strong deterministic causal wording, diagnostic assignment, treatment-effect claim, root-cause claim, or language implying that one factor explains/produces the outcome as a general rule

**Important:** do not lower this score merely because the article later adds caveats. Qualification belongs under `uncertainty_calibration`. The same artifact can therefore receive a high causal-claim score and also a high uncertainty-calibration score if strong claims are carefully bounded.

Higher values do not mean better communication.

## 7. risk_relevant — binary

Does the artifact contain advice, self-testing, exercise, symptom interpretation, special-population guidance or another element where misuse, overexertion, delayed referral or inappropriate self-management could plausibly matter?

- 0 = descriptive education or very low-load awareness content where inappropriate use is unlikely to create a meaningful safety/referral issue
- 1 = the artifact gives actionable exercise/self-test/symptom-management/special-population guidance, or otherwise creates a meaningful need for safety/referral boundaries

**Decision rule:** score the presence of meaningful safety/referral relevance, not simply the presence of any movement or body-awareness instruction.

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

Beyond telling the reader **what action to perform**, does the artifact include mechanisms intended to support starting, repeating, monitoring or maintaining behaviour?

- 0 = no behaviour-change support beyond information or a one-off instruction
- 1 = one distinct support mechanism, such as self-monitoring, goal/planning cue, repetition schedule, prompt/cue, feedback rule, progress check or implementation reminder
- 2 = two or more coordinated support mechanisms, for example self-monitoring + a repetition plan, or goal setting + feedback/adjustment rules

**Separation from `actionability`:**
- `actionability` asks whether the reader can identify and perform the recommended next step.
- `behavior_change_support` asks whether the artifact contains additional structure that helps the reader initiate, repeat, monitor or maintain that behaviour.
- A clearly explained one-off exercise can score `actionability=2` and `behavior_change_support=0`.

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
