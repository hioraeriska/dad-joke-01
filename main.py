"""Dad Joke Showdown entry: one original dad joke, written to entry.txt.

The joke is the whole entry: a single line of at most 200 characters.
"""

from __future__ import annotations

import os
from pathlib import Path

LINE = "My wife asked what my book of dad jokes is called. I said, 'A groan-up's guide to fatherhood.'"


def check_length(text: str) -> None:
    """Reject text outside the gate's 1-200 character window."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")


def check_not_blank(text: str) -> None:
    """Reject text that is only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def validate(text: str) -> None:
    """Enforce the gate: 1-200 characters, not only whitespace."""
    check_length(text)
    check_not_blank(text)


def resolve_output_dir() -> Path:
    """Return the output directory from MAKEFUN_OUTPUT_DIR (default: output)."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))


def get_entry_path(out_dir: Path) -> Path:
    """Return the entry file path inside out_dir."""
    return out_dir / "entry.txt"


def write_entry(text: str, out_dir: Path) -> None:
    """Write text to entry.txt inside out_dir, with no trailing newline."""
    out_dir.mkdir(parents=True, exist_ok=True)
    get_entry_path(out_dir).write_text(text, encoding="utf-8")


def main() -> None:
    """Write the joke, with no trailing newline, to entry.txt."""
    validate(LINE)
    out_dir = resolve_output_dir()
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
