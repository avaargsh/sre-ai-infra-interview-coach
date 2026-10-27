#!/usr/bin/env python3
"""Check local Markdown links and reject paths outside the repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(ROOT.rglob("*.md"))
IGNORED = {".git", ".venv", "venv", "node_modules"}


def main() -> int:
    errors = []
    checked = 0
    for doc in MARKDOWN:
        if any(part in IGNORED for part in doc.parts):
            continue
        content = doc.read_text(encoding="utf-8")
        content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", content):
            target = match.group(1).strip().split()[0]
            if not target or target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            checked += 1
            local_path = (doc.parent / target).resolve()
            try:
                local_path.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{doc.relative_to(ROOT)}: path escapes repository: {target}")
                continue
            if not local_path.exists():
                errors.append(f"{doc.relative_to(ROOT)}: missing local link: {target}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: checked {checked} local Markdown links in {len(MARKDOWN)} documents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
