#!/usr/bin/env python3
"""Dependency-free structural validator for the interview-coach Skill."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not SKILL.is_file():
        fail("SKILL.md is missing")

    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("frontmatter must start at the first line")

    match = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.DOTALL)
    if not match:
        fail("frontmatter closing delimiter not found")

    frontmatter = match.group(1)
    name = re.search(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name:
        fail("name is missing or invalid")
    if name.group(1) != ROOT.name:
        fail(f"name '{name.group(1)}' must match directory '{ROOT.name}'")
    if not description or not description.group(1).strip():
        fail("description is missing")
    if len(name.group(1)) > 64:
        fail("name exceeds 64 characters")
    desc = description.group(1).strip().strip("\"'")
    if len(desc) > 1024:
        fail("description exceeds 1024 characters")

    required_sections = [
        "## Scenario requirements",
        "## Do not reveal the answer in the question",
        "## Topic selection and non-repetition",
        "## Evaluate the user's answer",
        "## Safety and production realism",
        "## Progress continuity",
    ]
    for section in required_sections:
        if section not in content:
            fail(f"required section missing: {section}")

    required_files = [
        "agents/openai.yaml",
        "references/scoring-rubric.md",
        "references/scenario-design.md",
        "references/progress-template.md",
        "references/answer-template.md",
        "QUICKSTART.md",
        "README.md",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "SECURITY.md",
        "LICENSE",
    ]
    for relative in required_files:
        if not (ROOT / relative).is_file():
            fail(f"required file missing: {relative}")

    metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    for key in ("display_name:", "short_description:", "default_prompt:"):
        if key not in metadata:
            fail(f"agents/openai.yaml is missing {key}")

    print("PASS: frontmatter, workflow sections, UI metadata, and required files")
    

if __name__ == "__main__":
    main()
