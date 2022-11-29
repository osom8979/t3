# -*- coding: utf-8 -*-

from typing import Dict, Final, List, Tuple

from arcade import Texture

from t3.objects.matrix import Matrix
from t3.objects.board import Board


class History:

    PREVIEW_COLS: Final[int] = 4
    PREVIEW_ROWS: Final[int] = 2

    def __init__(
        self,
        size: int,
        history: List[Matrix],
        block_width: int,
        block_height: int,
        block_margin: int,
        board_margin: int,
        block_textures: Dict[int, Texture],
    ):
        self._block_width = block_width
        self._block_height = block_height
        self._block_margin = block_margin
        self._board_margin = board_margin
        self._offset_x = 0
        self._offset_y = 0
        self._boards = [self._create_board(block_textures) for _ in range(size)]
        self._history = history

        for i in range(size):
            if i >= len(history):
                break
            self._boards[i].set_matrix(history[i])

    def _create_board(self, block_textures: Dict[int, Texture]) -> Board:
        return Board(
            History.PREVIEW_COLS,
            History.PREVIEW_ROWS,
            self._block_width,
            self._block_height,
            self._block_margin,
            block_textures,
        )

    def update_offset(self, offset_x: int, offset_y: int) -> None:
        self._offset_x = offset_x
        self._offset_y = offset_y

        x = offset_x
        y = offset_y
        for board in self._boards:
            board.update_offset(x, y)
            y += board.height + self._board_margin

    def update_textures(self):
        for board in self._boards:
            board.update_textures()

    def draw(self) -> None:
        for board in self._boards:
            board.draw()
