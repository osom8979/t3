# -*- coding: utf-8 -*-

from typing import List

from t3.stages.stage import Stage
from t3.stages.stage00 import Stage00


def create_stages() -> List[Stage]:
    return [Stage00()]
