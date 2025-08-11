#!/usr/bin/env python3
# run.py — launch the GUI directly without using console entry points.

import os
import sys

# Allow running without "pip install -e ."
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from mdtxupdater.gui import main

if __name__ == "__main__":
    main()
