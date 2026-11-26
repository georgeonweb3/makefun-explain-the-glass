#!/usr/bin/env python3
"""Entry for make.fun "Five Seconds to Explain the Glass".

Writes one sentence to /output/entry.txt: the single sentence a house cat
would say in its own defence in the five seconds after sweeping a glass off
the table. Gate: UTF-8 text of 1 to 200 characters, not only whitespace,
one sentence, in the cat's own voice, no apology and no confession.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "It sat on my side of the table for three days, I gave it one warning, "
    "and this morning it finally met the floor."
)

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"


def main() -> None:
    # The grader sets MAKEFUN_OUTPUT_DIR=/output; honour it first, then the
    # generic OUTPUT_DIR override used for local runs, then /output.
    out_dir = os.environ.get(
        "MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
