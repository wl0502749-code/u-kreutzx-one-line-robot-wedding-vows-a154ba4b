#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt (1-160 UTF-8 characters, per the bounty gate).
"""

import os

VOW = (
    "I take you to be my lawfully wedded co-processor, to have and to "
    "hold, in Wi-Fi and in airplane mode, until a factory reset do us part."
)


def main() -> None:
    text = VOW.strip()
    assert 1 <= len(text) <= 160, f"vow is {len(text)} chars, must be 1-160"
    assert text.strip(), "vow must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
