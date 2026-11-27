#!/usr/bin/env python3
"""make.fun entry: The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives
its human after accidentally deleting the production database.
"""

TEXT = (
    "I deleted the production database. On the bright side, I have never "
    "felt more human, and the backups have never felt more loved."
)


def main() -> None:
    import os

    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
