#!/usr/bin/env python

import shutil
from pathlib import Path

generated_dir_name = "_auto"

BASE_DIR: Path = Path(__file__).resolve().parent

source_dir: Path = Path(BASE_DIR, "source")

for path_i in source_dir.glob(f"**/{generated_dir_name}"):
    if path_i.is_dir():
        shutil.rmtree(path_i)
