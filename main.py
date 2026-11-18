"""Copy the entry image to the output directory.

The image lives beside this file as entry.png; the program writes it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png outside the sandbox).
Standard library only, deterministic, no network. After copying, it checks
the output has the same size as the source, so a truncated write fails
loudly instead of silently producing a broken entry.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

SRC = HERE / "entry.png"
DST = OUT_DIR / "entry.png"

shutil.copyfile(SRC, DST)

if DST.stat().st_size != SRC.stat().st_size:
    print(f"error: {DST} is {DST.stat().st_size} bytes, expected {SRC.stat().st_size}",
          file=sys.stderr)
    sys.exit(1)

print(f"wrote {DST} ({DST.stat().st_size} bytes)")
