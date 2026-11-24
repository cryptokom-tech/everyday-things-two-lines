"""Write the make.fun bounty entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-suga-everyday-things-two-lines-longer-run-f8734479
("Everyday Things, Two Lines, Longer Run").

The entry is two lines of plain text, 1-400 UTF-8 characters in total.
Line 1 explains one everyday thing (a toaster) to a 10-year-old in one
vivid sentence built on an analogy. Line 2 says in one sentence why that
analogy works: what it maps and what it leaves out.

Standard library only. Deterministic. No network access.
"""

import os
import sys

ENTRY = (
    "A toaster is a tiny sunbed for bread: it lies flat under hot glowing "
    "wires until its top turns golden brown, then pops up when it's done.\n"
    "The sunbed maps the heat, the lying flat and the golden-brown tan, but "
    "leaves out that bread can't get up and walk away \u2014 and a toaster "
    "never asks how dark you want it, it just guesses."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    assert written == ENTRY, "entry.txt does not equal the entry text"
    assert 1 <= len(written) <= 400, (
        f"entry length {len(written)} is outside 1-400 characters"
    )
    assert written.strip(), "entry is whitespace-only"
    # Exactly two lines: one newline, no trailing newline, no trailing
    # whitespace on either line.
    assert written.count("\n") == 1, "entry must be exactly two lines"
    assert not written.endswith("\n"), "entry has a trailing newline"
    lines = written.split("\n")
    assert all(line == line.rstrip() for line in lines), (
        "entry has trailing whitespace"
    )
    assert all(line.endswith(".") for line in lines), (
        "each line must be one sentence ending with a period"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
