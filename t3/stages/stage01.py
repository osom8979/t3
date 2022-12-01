# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_S, BLOCK_Z


class Stage01(Stage):

    board = [
        [D, D, D, D, D, D, D, D, D, D],
        [D, D, D, D, D, D, D, D, D, D],
        [E, D, E, E, E, D, E, D, E, E],
        [E, E, E, E, E, E, E, D, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E, E, E],
    ]

    history = [BLOCK_O, BLOCK_I, BLOCK_S, BLOCK_Z, BLOCK_Z, BLOCK_T]
