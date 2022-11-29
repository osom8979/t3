# -*- coding: utf-8 -*-


from t3.stages.stage import Stage
from t3.objects.block import E, D, BLOCK_I, BLOCK_O, BLOCK_T


class Stage00(Stage):

    board = [
        [D, D, E, E, D, E, E, D, E, E],
        [D, D, E, E, D, E, E, D, D, E],
        [E, E, E, E, D, E, E, D, E, E],
        [E, E, E, E, D, E, E, E, E, E],
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

    history = [BLOCK_O, BLOCK_I, BLOCK_T]
