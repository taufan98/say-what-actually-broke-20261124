# Say What Actually Broke — writes one line of honest error copy to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets, no input files.
#
# The line names the real failure (a save that failed because the disk is
# full) in plain words, tells the user what to do next, and lands the joke
# on a single read: the disk is full of other people's unsaved work.

import os
from pathlib import Path

LINE = (
    "Your file didn't save: the disk is full, mostly of unsaved work from "
    "people who kept clicking Remind me later. Free up space and try again."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
stripped = LINE.strip()
if not 1 <= len(stripped) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if len(stripped.splitlines()) != 1:
    raise SystemExit("entry line must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
