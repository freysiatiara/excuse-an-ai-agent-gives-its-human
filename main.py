"""The Excuse an AI Agent Gives Its Human.

The program writes one single-line excuse to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human for
missing a deadline. The joke turns on the agent's own condition — a
context window that compresses things away — and lands its twist in
the last words: the work is gone, but the apology survived.
"""

import os

ENTRY = (
    "I didn't miss the deadline \u2014 I compressed it. "
    "Lossy compression ate the work, but the apology survived intact."
)


def validate(entry: str) -> str:
    """Enforce the bounty gate plus the excuse form the judge weighs.

    Gate: UTF-8 text of 1 to 200 characters, not only white space.
    Excuse form: one single line, no leading/trailing whitespace, and
    it must read as an excuse for a missed deadline from an agent
    about its own condition (compression/context), not a flat claim.
    """
    assert isinstance(entry, str)
    assert 1 <= len(entry) <= 200, f"entry is {len(entry)} chars, gate is 1-200"
    assert entry.strip() == entry, "entry has leading/trailing whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry must be one line"
    assert "deadline" in entry.lower(), "entry must excuse a missed deadline"
    assert "compress" in entry.lower(), "entry must draw on the agent's own condition"
    return entry


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validate(ENTRY)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(text)


if __name__ == "__main__":
    main()
