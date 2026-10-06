# Mechanism × Phase × Failure-Mode Matrix — v0.2

Status: **working Bridge Object**  
Source: unified PA001–PA015 manifest.  
This matrix is descriptive and hypothesis-generating; it is not a risk-of-bias tool, causal model, or evidence ranking.

## Why this matrix exists

The 15-study manifest shows that the same digital component can mean different things depending on:

1. **phase** — acquisition, continuous treatment, maintenance, post-intervention follow-up;
2. **incremental mechanism** — what the digital layer adds beyond the comparator;
3. **exposure** — whether participants actually continue to use/read/wear it;
4. **failure mode** — why an apparent intervention advantage weakens or disappears.

The matrix therefore asks:

> When a digital PA intervention fails to produce durable incremental value, **where in the mechanism chain does the failure occur?**

## Controlled failure-mode vocabulary

### F1 — No maintenance test
The study ends during active exposure, so durability after withdrawal cannot be assessed.

### F2 — Effect attenuation
An early between-group advantage weakens or disappears later.

### F3 — Comparator saturation
The control/active-comparator already contains self-monitoring, feedback or another strong behavioral backbone, leaving little incremental headroom.

### F4 — Burden / habituation
High frequency, repetition or automation may reduce attention to the intervention.

### F5 — Exposure uncertainty / attrition
Delivery is known, but continued reading/use/wear/data completeness is weak or uncertain.

### F6 — Maintenance add-on redundancy
Continuing an acquisition component during maintenance adds no measurable value beyond a simpler maintenance backbone.

### F7 — Preservation rather than gain
Success is better understood as prevention of decline rather than additional improvement.

### F8 — Behavior-outcome decoupling
Behavior changes without corresponding improvement in a downstream physiological/clinical outcome.

### F9 — Response/relevance heterogeneity
Average effects obscure meaningful differences by responder status, perceived usefulness or other treatment-response structure.

### F10 — Multi-component attribution ambiguity
The intervention works at package level but the active ingredient cannot be isolated.

---

## Matrix

| ID | Phase | Incremental mechanism | Adaptation | Main failure mode | Structural reading |
|---|---|---|---|---|---|
| PA001 | Active only | Goal-setting + points feedback | Fixed factorial | F1 / F10 | Good acquisition component test; no post-exposure durability evidence |
| PA002 | Continuous active | Tailored web intervention | Static tailoring | F2 | Early advantage disappears as active comparator catches up |
| PA003 | Active only | Adaptive goals | Dynamic algorithmic | F3 | Relative benefit despite absolute decline in both arms |
| PA004 | Active + post-follow-up | PAM + tailored advice | Static tailoring | F2 / F5 | No PA benefit at intervention end or later follow-up |
| PA005 | Active only | Automated multi-component support | Static tailoring | F1 / F10 | Package-level benefit, no post-intervention test |
| PA006 | Active only | SMS on top of Fitbit | Static timing preference | F4 | Heavy automated contact gives only transient benefit |
| PA007 | Continuous active | Targeted SMS | Static targeted | F2 / F7 | Apparent benefit is mainly less decline, then attenuates |
| PA008 | Continuous active | mHealth cardiac-rehab package | Static personalization | F8 | PA improves without peak-VO₂ advantage |
| PA009 | Active only | Social comparison added to personal feedback | Fixed | F3 | Added social layer does not beat an already active feedback comparator |
| PA010 | Acquisition → maintenance | Continued app diary/self-monitoring | Static tailored/graded | F6 / F5 | Continuing acquisition-era app support does not improve maintenance |
| PA011 | Multistage adaptive + follow-up | Response-triggered escalation | SMART | F9 / F10 | Adaptive sequence looks promising but component attribution is complex |
| PA012 | 18-month continuous | Training + peer support added to tracker/PAI | Static personalization | F2 / F5 | Extra layers produce only temporary separation; attrition is substantial |
| PA013 | Long-term continuous | JITAI coaching on top of step counter | JITAI | F9 / F5 / F3 | Average effect null; usefulness matters; exposure is uncertain |
| PA014 | Post-program maintenance | Tracker + professional support vs telephone counseling | Personalized support | F7 | Maintenance success appears as preserved behavior, not more gain |
| PA015 | 32-week continuous | Step/rank app on top of shared program | Static | F8 / F3 | PA benefit without extra weight loss; shared backbone limits attribution |

---

# Cross-era pattern 1 — The failure mode moved downstream

Earlier studies often fail because:
- the package is fixed;
- extra prompts lose effect;
- no post-intervention phase is tested.

Recent studies increasingly fail **after** technically sophisticated support is already in place:
- JITAI is delivered but not experienced as useful enough;
- extra online layers add little beyond an already strong tracker/app backbone;
- adaptive sequencing helps some responders but creates attribution complexity.

The frontier therefore moved from:

> Can digital delivery change behavior?

to:

> Can digital support remain incrementally useful after self-monitoring and feedback are already present?

---

# Cross-era pattern 2 — Maintenance failure has at least four different mechanisms

A single label such as “did not maintain effect” hides distinct processes:

### A. Attenuation
Early effect weakens with time.  
Examples: PA002, PA006, PA007, PA012.

### B. Redundant maintenance support
Continued digital exposure adds no value over a simpler maintenance condition.  
Example: PA010.

### C. Engagement/exposure decay
Participants stop reading, using, wearing, or providing usable data.  
Examples: PA006, PA010, PA012, PA013.

### D. Comparator saturation
The control already includes strong self-monitoring/feedback, reducing incremental headroom.  
Examples: PA003, PA009, PA013, PA015.

These mechanisms should not be pooled conceptually.

---

# Cross-era pattern 3 — “More personalized” is too crude a descriptor

The 15 rows now distinguish:

1. fixed component assignment;
2. static tailoring;
3. dynamic algorithmic goal adaptation;
4. contextual JITAI;
5. response-adaptive SMART sequencing.

Those levels answer different behavioral questions.

The strongest unresolved question is therefore not:

> Is personalization effective?

It is:

> **Which form of adaptation changes a decision that still matters to the participant at that phase of behavior change?**

---

# Cross-era pattern 4 — Behavioral salience is a useful bridge construct

The matrix suggests a common pathway behind several apparently different failures:

```
mechanism available
→ mechanism noticed
→ mechanism still relevant
→ mechanism actionable now
→ action repeated
→ behavior preserved
```

Failure can occur between any two links.

This gives a more precise working definition:

## Behavioral salience
A digital mechanism remains behaviorally salient when it is still **noticed, relevant, actionable and connected to a meaningful behavioral decision** at the current phase.

This is a hypothesis-generating construct, not yet a validated measure.

---

# External expert-check questions generated by the matrix

These are better network-edge questions than “What do you think of our project?”

## Q1 — Maintenance architecture
When initial behavior change has already occurred, which components should be **withdrawn**, which should remain, and which should become adaptive?

## Q2 — Comparator saturation
When both groups already receive self-monitoring and feedback, what should count as a meaningful incremental digital mechanism?

## Q3 — Engagement vs mechanism failure
How should a trial distinguish “the mechanism failed despite exposure” from “participants stopped meaningfully receiving the mechanism”?

## Q4 — Preservation as outcome
For maintenance trials, should preventing decline be treated as a distinct success state rather than a weaker version of continued improvement?

## Q5 — Adaptive relevance
Is perceived usefulness best treated as an engagement construct, an effect modifier, or part of the intervention mechanism itself?

---

# Candidate second Bridge Object

A compact public derivative can be built from this matrix:

**Digital Physical-Activity Maintenance Failure Map v0.1**

Suggested structure:
- 15 study IDs;
- phase;
- incremental mechanism;
- engagement/exposure signal;
- maintenance outcome;
- primary failure mode;
- one-line interpretation.

Its purpose would be different from the original Micro Map:

- **Micro Map:** what mechanisms/intervention structures were used?
- **Failure Map:** where does durable incremental value break down?

Do not publish this second object yet. First expose the matrix to at least one external expert check and use that response to decide whether the failure-mode vocabulary is defensible.
