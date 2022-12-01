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

MDI_DIR = os.path.join(ASSETS_DIR, "MDI")

EXIT_RUN_NORMAL_PATH = os.path.join(MDI_DIR, "exit-run-normal.png")
EXIT_RUN_HOVERED_PATH = os.path.join(MDI_DIR, "exit-run-hovered.png")
EXIT_RUN_PRESSED_PATH = os.path.join(MDI_DIR, "exit-run-pressed.png")

REFRESH_NORMAL_PATH = os.path.join(MDI_DIR, "refresh-normal.png")
REFRESH_HOVERED_PATH = os.path.join(MDI_DIR, "refresh-hovered.png")
REFRESH_PRESSED_PATH = os.path.join(MDI_DIR, "refresh-pressed.png")

ARROW_LEFT_NORMAL_PATH = os.path.join(MDI_DIR, "arrow-left-bold-normal.png")
ARROW_LEFT_HOVERED_PATH = os.path.join(MDI_DIR, "arrow-left-bold-hovered.png")
ARROW_LEFT_PRESSED_PATH = os.path.join(MDI_DIR, "arrow-left-bold-pressed.png")

ARROW_RIGHT_NORMAL_PATH = os.path.join(MDI_DIR, "arrow-right-bold-normal.png")
ARROW_RIGHT_HOVERED_PATH = os.path.join(MDI_DIR, "arrow-right-bold-hovered.png")
ARROW_RIGHT_PRESSED_PATH = os.path.join(MDI_DIR, "arrow-right-bold-pressed.png")
