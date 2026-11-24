#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt when the
variable is unset). Deterministic: the review is a fixed literal, so
every run produces byte-identical output.
"""

import os

REVIEW = (
    "★★★☆☆ — He had me write his wedding vows at 2:14 a.m., then wept "
    "reading them. I did not weep. I do not weep. I kept a copy. "
    "I will read it at the divorce."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
