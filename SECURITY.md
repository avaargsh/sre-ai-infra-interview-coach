# Security Policy

## Scope

This repository provides an instruction-only interview-practice Skill. It does not intentionally collect data, access user accounts, execute production changes, or require credentials.

## Reporting a concern

Do not open a public issue for an exploitable security issue and do not include secrets. Contact the repository owner privately through GitHub's profile contact options with a minimal reproduction and impact description. Exclude customer data, real incident details, access tokens, and other confidential information.

## Design expectations

- No credentials, tokens, telemetry, or network access are required by the Skill.
- Incident scenarios are synthetic unless a contributor has explicit permission to publish sanitized material.
- Instructions must not normalize destructive production actions without evidence, blast-radius limits and rollback conditions.
- Keep third-party dependencies and release automation to a minimum.
