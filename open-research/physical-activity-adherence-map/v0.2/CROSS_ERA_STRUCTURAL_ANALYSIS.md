# v0.2 Cross-Era Structural Analysis — PA001–PA015

Status: **working analysis**.  
Dataset: `v0.2/micro_map_manifest_v0.2.csv` (15 selected studies).  
This is a structural comparison of a convenience sample, **not** a systematic review, meta-analysis, prevalence estimate, or causal model.

## Era split used for description

- **Earlier set:** PA001–PA010, published 2007–2019
- **Recent refresh:** PA011–PA015, published 2021–2026

The recent set was intentionally selected to add adaptive design, long-term follow-up, JITAI, maintenance, and active-comparator structure. Differences between eras therefore reflect both historical change **and deliberate sampling**.

---

# 1. What did not change: self-monitoring remained the backbone

All 15 rows contain some form of behavioral observation/self-monitoring in the intervention structure:

- smartphone/app step monitoring;
- accelerometer or wearable feedback;
- diaries/logs;
- progress displays;
- goal/reference comparison.

Across two decades, the recurring control loop is still:

`observe behavior → compare with reference/goal → receive feedback/support → act again`

The main historical shift is therefore **not** from “no self-monitoring” to “self-monitoring.”

The shift is in **what happens around and after self-monitoring**.

---

# 2. What changed: the unit of innovation moved from components to adaptation

## Earlier pattern

Most PA001–PA010 interventions change a relatively fixed package:

- add goal setting;
- add points;
- add SMS;
- add social comparison;
- add tailored advice;
- add a web/mobile layer.

PA003 is the important early exception: goals were algorithmically recalculated from prior behavior.

## Recent pattern

The refresh adds two qualitatively different forms of adaptation:

- **PA013 — JITAI:** contextual, preference-sensitive coaching delivered just in time;
- **PA011 — SMART:** the treatment sequence itself changes based on behavioral response.

This creates a three-level distinction that should remain explicit:

1. **Static/fixed package** — assigned components remain broadly the same.
2. **Dynamic parameter adaptation** — e.g. PA003 recalculates goals from prior behavior.
3. **Adaptive intervention architecture** — context-sensitive JITAI or response-triggered treatment sequencing.

### Interpretation

Digital PA intervention research has moved from asking:

> Which component should we add?

toward:

> Which support should this person receive, at what moment, and should the intervention change when the person is not responding?

That is a structural change in intervention design.

---

# 3. But greater adaptive sophistication has not solved the outcome problem

The three clearest adaptive examples do not produce one simple story:

- **PA003:** adaptive personalized goals produced a relative advantage, but absolute steps declined in both groups.
- **PA013:** JITAI coaching produced no significant average incremental step benefit over an active self-monitoring control; perceived usefulness moderated response.
- **PA011:** SMART response-adaptive treatment showed favorable trajectories for some groups/responders and follow-up gains.

Therefore:

`more adaptive technology ≠ automatically larger average behavioral effect`

A more plausible working interpretation is:

`adaptation quality × experienced relevance × continued exposure`

is a useful working interpretation of the observed cross-study pattern, without implying a validated causal model. It matters more for hypothesis generation than the label “personalized” or “adaptive” alone.

---

# 4. Active comparators increasingly reveal the incremental-value problem

Several studies — old and new — give the comparator substantial behavioral support:

- PA003: both groups receive app self-monitoring + notifications + feedback; goals differ.
- PA006: both groups receive Fitbit self-monitoring; SMS is the add-on.
- PA009: all groups carry the same step-recording phone; feedback differs.
- PA010: acquisition package is shared between regular and plus groups before the maintenance contrast.
- PA012: every arm receives tracker + PAI app; training and peer support are add-ons.
- PA013: both groups receive a step counter; JITAI coaching is the add-on.
- PA015: both groups receive lecture, self-weighing, emails and periodic feedback; the app is incremental.

This changes the meaning of a null result.

A null incremental effect does **not** necessarily mean:

> digital intervention does not work.

It may mean:

> the additional component does not add measurable value beyond an already active behavioral backbone.

This is why `shared_backbone_or_active_comparator` is a required v0.2 field.

---

# 5. “More digital contact” remains an unsolved problem across eras

The same failure pattern appears repeatedly:

## Earlier examples

- **PA006:** intensive SMS produced an early response that disappeared; about half considered three messages/day too many and some stopped reading them.
- **PA007:** SMS produced a temporary relative advantage, largely by limiting decline; the difference was not significant by week 24.
- **PA009:** adding social comparison did not significantly outperform personal feedback.
- **PA010:** continuing the app diary during maintenance did not outperform accelerometer-only maintenance.

## Recent example

- **PA012:** adding online training and then peer support did not generate a durable long-term advantage across 18 months.

### Cross-era conclusion

The recurring problem is not insufficient feature count.

A better working rule is:

> additional contact has value only when it changes the behavioral decision at the right time without producing burden, habituation, or redundant support.

---

# 6. Engagement/exposure is not a side metric; it constrains interpretation

The unified manifest makes a distinction that the original v0.1 could not:

`intervention assigned → intervention delivered → intervention received/used → behavioral response`

Examples:

- **PA005:** weekly participation fell from >85% early to ~75% later.
- **PA006:** some participants stopped reading automated messages.
- **PA010:** acquisition adherence was ~85%, but maintenance diary adherence fell to 68.4%.
- **PA012:** only 42.7% supplied accelerometer data at 18 months.
- **PA013:** only ~30% of possible daily step observations were available; message reading could not be verified.
- **PA015:** daily app checking declined from ~80% early to ~74% later.

### Implication

A null or attenuated behavioral result can arise under at least two different evidential states:

1. intervention receipt/exposure is documented, but there is no incremental behavioral effect;
2. intervention receipt/exposure is weak or uncertain, limiting what can be inferred about the behavioral pathway.

Those states should not be coded as equivalent. Unless a mechanism of action is directly measured, the public interpretation should remain at the level of documented exposure and observed behavioral effect.

---

# 7. Perceived usefulness introduces a missing variable: behavioral salience

PA013 is especially informative because average JITAI effect was null while **perceived usefulness moderated the response**.

This suggests that personalization should not be evaluated only by its technical sophistication.

A technically personalized message can still be behaviorally irrelevant.

The working construct for v0.2 is therefore:

## Behavioral salience

A digital intervention remains behaviorally salient when its feedback/support is:

- noticed;
- perceived as relevant/useful;
- timed to a decision opportunity;
- actionable;
- not overly repetitive/burdensome;
- still connected to a meaningful goal/reference.

This construct is not claimed as a validated latent variable in the current dataset. It is a **working explanatory construct** generated by the cross-study pattern.

---

# 8. Acquisition and maintenance require different architectures

The unified phase coding shows that “long intervention” and “maintenance intervention” are not synonymous.

Examples:

- **PA015:** 32 weeks of continuous active exposure — long duration, but not a distinct maintenance phase.
- **PA004:** 3-month intervention followed by 5 months without intervention before follow-up.
- **PA010:** explicit acquisition phase followed by a randomized maintenance contrast.
- **PA011:** adaptive active phase followed by self-directed app monitoring.
- **PA014:** maintenance support begins after participants finish a prior exercise program.

### Implication

A component that is useful for acquisition can become redundant during maintenance.

PA010 is the clearest example:
continuing app diary/self-monitoring did not improve maintenance over accelerometer-only maintenance.

A maintenance architecture should therefore be coded by:

`what behavioral problem exists after acquisition?`

not simply:

`which acquisition components can be kept running?`

---

# 9. Preserving behavior is a real outcome and must not be mistaken for failure

Two rows illustrate why absolute direction matters:

- **PA007:** the apparent intervention advantage largely reflected less decline rather than a clear increase.
- **PA014:** tracker and telephone-support groups broadly preserved step levels while usual care declined.

For maintenance research, the relevant success state may be:

`prevent decline`

rather than:

`increase above the acquisition peak`

Therefore v0.2 should preserve three separate quantities whenever possible:

1. absolute change from baseline/acquisition endpoint;
2. between-group difference;
3. time point / phase.

---

# 10. Behavior change still does not guarantee downstream physiological change

This pattern survives the era transition.

- **PA008:** leisure-time PA/walking improved without an advantage in peak VO₂.
- **PA015:** PA improved without additional weight loss.

The outcome chain should remain:

`digital exposure → behavior → sustained behavioral dose → physiological/clinical adaptation`

A positive effect at one node does not imply a positive effect at the next.

---

# Candidate explanation model for maintenance failure

The 15-row map supports a **working hypothesis**, not a causal estimate:

```
maintenance value
≈
incremental mechanism value
× continued exposure
× perceived usefulness / fit
× phase appropriateness
× timely adaptation
− burden / habituation
− comparator saturation
− attrition / missing exposure
```

The terms should be read conceptually, not mathematically.

## Six variables to carry forward

### 1. Incremental mechanism value
What does the digital add-on contribute beyond what the comparator already receives?

### 2. Exposure persistence
Does use/wear/message exposure continue long enough for the mechanism to operate?

### 3. Perceived usefulness / relevance
Does the participant experience the support as useful enough to act on?

### 4. Phase fit
Is the component solving an acquisition problem or a maintenance problem?

### 5. Adaptive timing
Does support change with context or nonresponse, or simply repeat?

### 6. Burden / habituation
Does frequency, automation, repetition, or intervention complexity reduce attention over time?

---

# Three testable v0.2 hypotheses

## H1 — Simply prolonging an acquisition package will usually have diminishing incremental value

Supporting pattern:
PA006, PA007, PA010, PA012.

Potential counterevidence:
PA014 suggests ongoing support can preserve behavior, but human counseling performed similarly to tracker-based support.

## H2 — Adaptation is more promising when it changes a meaningful decision, not merely when an algorithm is present

Supporting pattern:
- PA003: adaptive goals affected relative trajectory.
- PA013: usefulness moderated JITAI response.
- PA011: response-triggered treatment adaptation produced favorable responder trajectories.

This hypothesis remains provisional because the adaptive studies differ substantially in population, duration, comparator and design.

## H3 — Maintenance success is more likely when the intervention protects against decline than when it attempts to keep producing acquisition-sized gains

Supporting pattern:
PA007 and PA014.

This reframes maintenance evaluation from:

> Did activity continue increasing?

to:

> Was the acquired behavior preserved better than the relevant counterfactual?

---

# Implication for the next research question

The original v0.1 question:

> Under what conditions does a digital self-monitoring + feedback loop remain behaviorally salient long enough to support physical-activity maintenance?

can now be sharpened to:

> **Which combinations of continued exposure, perceived usefulness, adaptive timing, and maintenance-phase support preserve physical activity after initial behavior change, above the value already provided by self-monitoring and feedback?**

This is a stronger v0.2 question because it explicitly controls for the fact that self-monitoring/feedback is already present in many active comparators.

---

# What not to infer from this map

Do not infer:

- prevalence of any mechanism in the full literature;
- superiority of JITAI, SMART, wearables, SMS, apps, or human counseling;
- causal mediation by engagement or perceived usefulness across studies;
- risk-of-bias rankings;
- pooled effect sizes.

The current value of the map is **structural hypothesis generation and correction**, not effect estimation.
