# -*- coding: utf-8 -*-

from t3.stages.stage import Stage
from t3.objects.block import E, D, T, J, L, O, BLOCK_I, BLOCK_O, BLOCK_J, BLOCK_L, BLOCK_T, BLOCK_S, BLOCK_Z


class Stage06(Stage):

    board = [
        [D, D, D, J, D, D, D, T, T, T],
        [D, D, D, J, D, D, D, D, T, D],
        [D, D, J, J, T, D, D, D, D, D],
        [D, D, D, T, T, T, D, D, D, D],
        [D, D, D, D, D, D, L, L, L, D],
        [D, D, O, O, D, D, L, D, E, D],
        [D, D, O, O, D, D, D, D, D, D],
        [D, D, E, D, D, D, E, D, D, D],
        [E, D, E, E, E, E, E, E, D, D],
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
        BLOCK_O,
        BLOCK_T,
        BLOCK_S,
        BLOCK_T,
        BLOCK_Z,
        BLOCK_O,
        BLOCK_L,
        BLOCK_I,
        BLOCK_S,
        BLOCK_I,
        BLOCK_T,
        BLOCK_J,
        BLOCK_Z,
        BLOCK_O,
        BLOCK_T,
        BLOCK_T,
        BLOCK_L,
        BLOCK_J,
        BLOCK_I,
        BLOCK_O,
    ]
