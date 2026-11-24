#!/usr/bin/env python3
"""Write the make.fun bounty entry text to a single file."""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
