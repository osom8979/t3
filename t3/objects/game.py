# -*- coding: utf-8 -*-

from math import floor
from typing import List, Optional

from t3.objects.block import create_block_textures
from t3.objects.board import Board
from t3.theme.flat import FlatTheme
from t3.theme.theme import Theme
from t3.variables.block import BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_MARGIN
from t3.variables.board import BOARD_COLS, BOARD_ROWS


class Game:
    def __init__(
        self,
        board_cols=BOARD_COLS,
        board_rows=BOARD_ROWS,
        block_width=BLOCK_WIDTH,
        block_height=BLOCK_HEIGHT,
        block_margin=BLOCK_MARGIN,
        theme: Optional[Theme] = None,
    ):
        self._theme = theme if theme else FlatTheme()
        self._block_textures = create_block_textures(
            block_width,
            block_height,
            self._theme,
        )

        self._board = Board(
            board_cols,
            board_rows,
            block_width,
            block_height,
            block_margin,
            self._block_textures,
        )

        # TODO: initialize matrix

        self._board.update_textures()

        self._total_delta = 0.0
        self._drop_delta = 0.0
        self._drop_threshold = 1.0

        self._game_over = False
        self._paused = False

        self._block_history: List[int] = list()
        self._cursor_x = 0

    # def _draw_current_block(self) -> None:
    #     if not self._current_block:
    #         return
    #
    #     for y in range(len(self._current_block)):
    #         for x in range(len(self._current_block[0])):
    #             value = self._current_block[y][x]
    #             if value == E:
    #                 continue
    #
    #             color = COLORS[self._current_block[y][x]]
    #             center = calc_block_center(
    #                 x + self._current_block_x,
    #                 y + self._current_block_y,
    #                 BLOCK_WIDTH,
    #                 BLOCK_HEIGHT,
    #                 BLOCK_MARGIN,
    #                 )
    #             center_x = center[0]
    #             center_y = SCREEN_HEIGHT - center[1]
    #             draw_rectangle_filled(
    #                 center_x,
    #                 center_y,
    #                 BLOCK_WIDTH,
    #                 BLOCK_HEIGHT,
    #                 color,
    #             )

    def resize(self, width: float, height: float) -> None:
        half_width = width // 2
        half_height = height // 2
        x = floor(half_width - self._board.half_width)
        y = floor(half_height - self._board.half_height)
        offset_x = x if x > 0 else 0
        offset_y = y if y > 0 else 0
        self._board.update_offset(offset_x, offset_y)

    def update(self, delta_time: float) -> None:
        self._total_delta += delta_time

    def draw(self):
        self._board.draw()
        # self._draw_current_block()

    # def new_stone(self):
    #     self._current_block = choice(list(BLOCKS.values()))
    #     self._current_block_x = int(BOARD_COLS / 2 - len(self._current_block[0]) / 2)
    #     self._current_block_y = 0
    #
    #     if self._board.check_collision(self._current_block, (self._current_block_x, self._current_block_y)):
    #         self._game_over = True
    #
    # def drop(self):
    #     if self._game_over:
    #         return
    #
    #     if self._paused:
    #         return
    #
    #     self._current_block_y += 1
    #     if self._board.check_collision(self._current_block, (self._current_block_x, self._current_block_y)):
    #         self._board.join_matrix(self._current_block, (self._current_block_x, self._current_block_y))
    #         while True:
    #             for i, row in enumerate(self._board[:-1]):
    #                 if 0 not in row:
    #                     self._board = remove_row(self._board, i)
    #                     break
    #             else:
    #                 break
    #         self._board.update()
    #         self.new_stone()
    #
    # def rotate_stone(self):
    #     if not self._game_over and not self._paused:
    #         new_stone = rotate_counterclockwise(self._current_block)
    #         if self._current_block_x + len(new_stone[0]) >= BOARD_COLS:
    #             self._current_block_x = BOARD_COLS - len(new_stone[0])
    #         if not self._board.check_collision(new_stone, (self._current_block_x, self._current_block_y)):
    #             self._current_block = new_stone
    #
    # def update_drop(self, delta_time: float) -> None:
    #     self._drop_delta += delta_time
    #     if self._drop_delta >= self._drop_threshold:
    #         self._drop_delta %= self._drop_threshold
    #         assert self._drop_delta < self._drop_threshold
    #         self.drop()
    #
    # def move(self, delta_x: int) -> None:
    #     if self._game_over:
    #         return
    #     if self._paused:
    #         return
    #
    #     new_x = self._current_block_x + delta_x
    #     if new_x < 0:
    #         new_x = 0
    #     if new_x > BOARD_COLS - len(self._current_block[0]):
    #         new_x = BOARD_COLS - len(self._current_block[0])
    #     if not self._board.check_collision(self._current_block, (new_x, self._current_block_y)):
    #         self._current_block_x = new_x


