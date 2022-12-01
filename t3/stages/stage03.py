# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_Z, BLOCK_J, BLOCK_S


class Stage03(Stage):

    board = [
        [D, E, D, E, D, E, D, D, D, E],
        [D, D, D, D, D, D, E, D, D, D],
        [E, D, D, D, E, D, E, D, D, D],
        [D, D, D, D, D, E, E, D, D, D],
        [D, D, D, D, D, D, E, D, D, E],
        [D, D, D, D, D, D, D, D, D, E],
        [E, E, E, E, D, D, E, E, D, D],
        [E, E, E, E, E, E, E, E, E, D],
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

    history = [
        BLOCK_I,
        BLOCK_O,
        BLOCK_J,
        BLOCK_S,
        BLOCK_I,
        BLOCK_O,
        BLOCK_T,
        BLOCK_S,
        BLOCK_S,
        BLOCK_Z,
        BLOCK_S,
        BLOCK_T,
        BLOCK_T,
    ]
