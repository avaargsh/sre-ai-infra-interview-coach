# Contributing

Thanks for helping improve scenario quality, scoring consistency, installation docs, and tests.

## Scenario requirements

1. One primary failure mechanism, with a small number of realistic alternatives.
2. Architecture, time window, at least three observable symptoms, and feasible operating constraints.
3. Three or four questions spanning hypotheses, verification, decision criteria, mitigation, acceptance and prevention.
4. No answer hints, root-cause giveaway, or hidden answer key in the user-facing prompt.
5. Internally consistent metrics; qualify commands and metrics that depend on product/kernel versions.
6. Risky operations require explicit preconditions, blast-radius limits and rollback checks.
7. Meaningfully different from recent scenarios, not merely a renamed product.
8. Answerable in 5–10 minutes.

## Scoring changes

Explain why a rubric change improves calibration. Do not reward verbosity or vocabulary in place of technical accuracy. Give credit for justified uncertainty and safe alternatives.

## Before submitting

Run:

    python tests/validate_skill.py
    python tests/check_references.py
    python scripts/package_skill.py

For behavior changes, include a sanitized example showing initial-question behavior and answer-evaluation behavior. Do not include real credentials, personal information, customer data, or confidential company incident reports.

## Reporting an issue

Include the trigger, expected behavior, actual behavior, minimal reproduction, and Skill version/commit. Remove sensitive data before opening an issue.
