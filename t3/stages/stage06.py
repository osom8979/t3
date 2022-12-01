# -*- coding: utf-8 -*-


from t3.stages.stage import Stage
from t3.objects.block import E, D, BLOCK_I, BLOCK_O, BLOCK_T, BLOCK_Z


class Stage06(Stage):

    board = [
        [D, D, E, D, E, D, E, E, E, D],
        [D, D, E, D, E, D, D, E, D, D],
        [E, E, E, D, E, D, E, E, D, E],
        [E, E, E, D, E, E, E, E, E, E],
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

    history = [BLOCK_Z, BLOCK_O, BLOCK_I, BLOCK_T]
