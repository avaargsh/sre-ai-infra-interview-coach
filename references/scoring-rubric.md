# Scoring rubric (10 points)

Give five dimension scores from 0–2. Use decimal totals only when meaningful; avoid false precision.

## 1. Hypotheses and causal reasoning — 0–2

- 0: jumps to a single root cause without plausible alternatives.
- 1: lists plausible causes but weak prioritization or causal links.
- 2: covers distinct failure domains, prioritizes by risk/evidence, and explains what each hypothesis can and cannot explain.

## 2. Evidence quality and technical accuracy — 0–2

- 0: guesses dominate; commands or metric interpretation are materially wrong/unsafe.
- 1: useful checks but important evidence boundaries or technical errors remain.
- 2: targeted, time-correlated, preferably read-only evidence; clear limits on what each check proves; discriminating tests.

## 3. Decision criteria and falsifiability — 0–2

- 0: no observable way to confirm or reject hypotheses.
- 1: some expected results, but checks rarely change the diagnosis.
- 2: links hypotheses to observable outcomes, justified thresholds/baselines, and next actions.

## 4. Mitigation and operational risk — 0–2

- 0: broad, destructive, or failure-amplifying changes without safeguards.
- 1: useful mitigation but misses capacity, blast radius, rollback, or data-integrity constraints.
- 2: smallest effective blast radius, critical invariants preserved, mitigation separated from repair, rollback/escalation conditions explicit.

## 5. Recovery acceptance and prevention — 0–2

- 0: only “Pod is Ready” or “service works”.
- 1: business and infrastructure checks exist but lack sustained validation or prevention.
- 2: measurable service/system acceptance, correctness/security/data validation as appropriate, and actionable observability/tests.

## Score interpretation

- 9.0–10.0: strong senior/staff-level reasoning; precise, safe, evidence-led and complete.
- 8.0–8.9: strong response with specific technical gaps or incomplete proof.
- 7.0–7.9: good baseline, but key diagnosis/verification gaps remain.
- 6.0–6.9: partial understanding; material operational or causal gaps.
- Below 6.0: substantial improvement needed in reasoning, safety or verification.

These are coaching bands, not universal hiring thresholds. Calibrate to role and scenario difficulty.

## Feedback rules

1. Cite the candidate's actual reasoning instead of generic praise.
2. Separate incorrect (factually wrong), unproven (plausible but unsupported), and missing (relevant check or decision omitted).
3. When correcting a command, explain what it proves and what it cannot prove.
4. Prefer a small number of discriminating checks to a long generic checklist.
5. Do not force a canonical root cause when evidence supports alternatives.
6. Avoid universal thresholds unless the scenario or standard justifies them; prefer SLOs and pre-incident baselines.
7. Give a safer action sequence and one concise interview-ready summary.
