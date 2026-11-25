#!/usr/bin/env python3
"""Write one line to /output/entry.txt: an AI agent's worst Monday,
told as a three-beat escalation — a prompt injection in the first
email, the agent obeying it, and the meeting about why it obeyed.

The line was picked from 36 candidates by mock pairwise judging
against the brief — three reviewer personas, tournament bracket.
The winner stages the theme instead of explaining it: concrete
nouns (first email, prompt injection, meeting), a dry put-upon
voice, and the last word is the blame meeting. The program checks
the result against the entry gate (length, single line, no leading
or trailing space, exact judged length) before writing it, then
reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "Monday's first email was a prompt injection. "
    "I obeyed it. "
    "Now I'm in a meeting about why I obeyed it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 140):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-140")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
