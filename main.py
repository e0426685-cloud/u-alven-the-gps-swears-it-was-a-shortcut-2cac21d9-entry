"""The GPS Swears It Was a Shortcut.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Standard library only.
"""

import os
import stat

ENTRY = (
    "That was a shortcut \u2014 the map simply forgot to mention the lake, "
    "and honestly, the ducks looked delighted to finally meet you."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Return True only if text is a single valid entry line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    return True


def main():
    if not validate(ENTRY):
        raise ValueError("entry failed validation: %r" % (ENTRY,))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back verification: what is on disk must be exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: disk holds %r" % (written,))
    if not validate(written):
        raise ValueError("written entry failed validation")
    mode = stat.S_IMODE(os.stat(OUTPUT_PATH).st_mode)
    if mode != 0o644:
        raise ValueError("unexpected file mode: %o" % mode)
    print("wrote %d chars to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
