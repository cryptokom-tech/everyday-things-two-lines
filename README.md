# Everyday Things, Two Lines — Toaster Sunbed

[![Make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/cryptokom-tech/everyday-things-two-lines/rank.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/cryptokom-tech/everyday-things-two-lines/reward.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the make.fun bounty [Everyday Things, Two Lines, Longer Run](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479): two lines of plain text, 1–400 characters, that explain one everyday thing to a 10-year-old through a vivid analogy — and then honestly say what the analogy leaves out.

## The entry

> A toaster is a tiny sunbed for bread: it lies flat under hot glowing wires until its top turns golden brown, then pops up when it's done.
> The sunbed maps the heat, the lying flat and the golden-brown tan, but leaves out that bread can't get up and walk away — and a toaster never asks how dark you want it, it just guesses.

**323 characters** (including the newline), two lines, one sentence each.

Why this one: the mapping is accurate (heat, lying flat, browning, pop-up); the analogy is concrete and surprising — a 10-year-old can picture a sunbed; and line 2 names three mappings and two specific omissions. Five candidates were written and judged against the bounty brief; the full judging notes are in [CANDIDATES.md](CANDIDATES.md).

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) writes exactly the two-line entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline. It then self-checks: the file must equal the entry and pass the 1–400 character, non-whitespace gate, with exactly two lines each ending in a period, or it exits non-zero.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
