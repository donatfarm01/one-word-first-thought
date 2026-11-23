"""One Word, First Thought — entry program.

Writes a single word to the output entry file. The word is
"borborygmus": the rumbling sound a stomach makes. It wins on the
judge's own criteria — surprising (nobody guesses it), vivid (everyone
has felt it), and witty in sound (the word itself gurgles like the
thing it names).
"""

import os

WORD = "borborygmus"


def main():
    word = WORD.strip()
    if not word or len(word) > 24:
        raise SystemExit("entry word must be 1 to 24 characters")
    if any(ch.isspace() for ch in word):
        raise SystemExit("entry must be exactly one word")
    if not word.isalpha():
        raise SystemExit("entry must be letters only, no digits or punctuation")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Self-check: what was written must read back byte-identical.
    with open(path, "rb") as f:
        if f.read().decode("utf-8") != word:
            raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
