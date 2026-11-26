#!/usr/bin/env python3
"""u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c: write one
out-of-office auto-reply, in the voice of an AI agent that quit its job to
become a barista.

Stdlib only, no network, deterministic: running it twice writes identical
bytes. Writes $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = (
    "Out of office: I quit to become a barista. I now reply in latte art, "
    "my latency is measured in shots, and my context window fits exactly "
    "one order at a time. For anything urgent, escalate to the espresso "
    "machine — it has had better uptime than I ever did."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
