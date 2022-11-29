# -*- coding: utf-8 -*-

import os
from typing import Final

from t3 import assets
from t3.module.path import module_directory

ASSETS_DIR: Final[str] = module_directory(assets)
GOWUNDODUM_DIR = os.path.join(ASSETS_DIR, "GowunDodum")
GOWUNDODUM_REGULAR_TTF_PATH = os.path.join(GOWUNDODUM_DIR, "GowunDodum-Regular.ttf")
