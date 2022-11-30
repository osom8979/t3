# -*- coding: utf-8 -*-

import os
from typing import Final

from t3 import assets
from t3.module.path import module_directory

ASSETS_DIR: Final[str] = module_directory(assets)

GOWUN_DODUM_DIR = os.path.join(ASSETS_DIR, "GowunDodum")
GOWUN_DODUM_REGULAR_TTF_PATH = os.path.join(GOWUN_DODUM_DIR, "GowunDodum-Regular.ttf")

# LOOPABLE_BG_MUSIC_DIR = os.path.join(ASSETS_DIR, "LoopableBGMusic")
# CATWALK_OGG_PATH = os.path.join(LOOPABLE_BG_MUSIC_DIR, "Catwalk.ogg")
