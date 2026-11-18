"""news-image-20261118 entry: copy the finished image to the output dir.

The image (entry.png, 1024x1024) sums up Wednesday 18 November 2026:
the Gulf strikes, the Kerch Bridge, the Shenzhen summit, Alaska, Ebola.
Stdlib only, no network, deterministic: the output bytes equal entry.png.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
assert SRC.is_file(), "entry.png missing next to main.py"
assert SRC.stat().st_size <= 1_048_576, "entry.png over the 1 MiB limit"

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
print("wrote", OUT_DIR / "entry.png")
