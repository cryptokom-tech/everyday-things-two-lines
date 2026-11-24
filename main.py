"""Everyday Things, Two Lines, Longer Run.

Competition: u-suga-everyday-things-two-lines-longer-run-f8734479

Writes the two-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default "/output") and self-checks the output before exiting.
Standard library only, deterministic, no network.
"""

import os

ENTRY = (
    "A toaster is a tiny sunbed for bread: it lies flat under hot glowing "
    "wires until its top turns golden brown, then pops up when it's done.\n"
    "The sunbed maps the heat, the lying flat and the golden-brown tan, "
    "but leaves out that bread can't get up and walk away \u2014 and a "
    "toaster never asks how dark you want it, it just guesses."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    # Self-checks.
    assert written == ENTRY, "entry.txt does not equal ENTRY"
    assert 1 <= len(written) <= 400, f"char length {len(written)} out of range"
    assert written.strip(), "entry is whitespace-only"
    assert written.count("\n") == 1, "entry must have exactly 2 lines"
    assert not written.endswith("\n"), "trailing newline present"
    lines = written.split("\n")
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    for line in lines:
        assert line == line.rstrip(), "trailing whitespace on a line"
        assert line.endswith("."), "line does not end with '.'"
    # Strengthened checks.
    assert len(written.encode("utf-8")) == 325, (
        f"UTF-8 byte length {len(written.encode('utf-8'))} != 325"
    )
    for line in lines:
        assert line[0].isupper(), "line does not start with a capital letter"
    assert "toaster" in lines[0], "line 1 must contain 'toaster'"
    assert "sunbed" in lines[1], "line 2 must contain 'sunbed'"

    print(
        f"OK: wrote {path} "
        f"({len(written)} chars, {len(written.encode('utf-8'))} bytes, "
        f"{len(lines)} lines)"
    )


if __name__ == "__main__":
    main()
