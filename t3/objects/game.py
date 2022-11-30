# -*- coding: utf-8 -*-

from copy import deepcopy
from math import floor
from typing import Optional, Tuple

from arcade import draw_text, draw_line, draw_rectangle_outline

from t3.objects.block import (
    E,
    Matrix,
    create_block_textures,
    rotate_clockwise,
    is_active_block,
)
from t3.objects.board import Board
from t3.objects.history import History
from t3.stages.stages import create_stages
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

        self._total_delta = 0.0
        self._drop_delta = 0.0
        self._drop_threshold = 1.0

        self._stage_clear = False
        self._stage_failed = False
        self._game_over = False
        self._paused = False

        self._cursor_board: Optional[Board] = None
        self._cursor_x = 0
        self._cursor_y = 0

        self._drop_matrix: Optional[Matrix] = None
        self._drop_x = 0
        self._drop_y = 0

        self._stages = create_stages()
        self._stage = 0

        self._board.set_matrix(self._stages[0].board[::-1])
        # self._board.update_textures()

        self._history = History(
            4,
            self._stages[0].history,
            block_width,
            block_height,
            block_margin,
            4,
            self._block_textures,
        )

        self.next_block()

    def resize(self, width: float, height: float) -> None:
        half_width = width // 2
        half_height = height // 2
        x = floor(half_width - self._board.half_width)
        y = floor(half_height - self._board.half_height)
        offset_x = x if x > 0 else 0
        offset_y = y if y > 0 else 0

        self._board.update_offset(offset_x, offset_y)
        self._history.update_offset(
            self._board.right + self._theme.margin_width,
            self._board.bottom,
        )
        self.update_cursor()
        self.update_hard_drop_matrix()

    def update(self, delta_time: float) -> None:
        self._total_delta += delta_time

    def _draw_border(self) -> None:
        left = self._board.left - self._board.block_margin
        right = self._board.right + self._board.block_margin
        top = self._board.top - self._board.block_margin
        bottom = self._board.bottom + self._board.block_margin

        draw_line(
            start_x=left,
            start_y=top,
            end_x=left,
            end_y=bottom,
            color=self._theme.foreground,
            line_width=self._theme.border_width,
        )

        draw_line(
            start_x=right,
            start_y=top,
            end_x=right,
            end_y=bottom,
            color=self._theme.foreground,
            line_width=self._theme.border_width,
        )

    def _draw_right_panel(self) -> None:
        x = self._board.right + self._theme.margin_width
        top = self._board.top - self._board.block_margin

        draw_text(
            text=f"STAGE {self._stage}",
            start_x=x + (self._board.block_margin * 2),
            start_y=top,
            color=self._theme.foreground,
            font_size=self._theme.subtitle_size,
            font_name=self._theme.font_name,
            bold=True,
            anchor_x="left",
            anchor_y="top",
        )

    def draw(self):
        self._board.draw()
        self._draw_border()
        self._draw_right_panel()
        self._history.draw()

        if self._cursor_board:
            self._cursor_board.draw()

        if self._drop_matrix is not None:
            self._draw_drop_matrix()

    def _draw_drop_matrix(self) -> None:
        assert self._drop_matrix is not None

        left = self._board.left
        bottom = self._board.bottom

        for row in range(len(self._drop_matrix)):
            for col in range(len(self._drop_matrix[0])):
                value = self._drop_matrix[row][col]
                if not is_active_block(value):
                    continue

                x = self._drop_x + col
                y = self._drop_y + row
                center = self._board.measure_block_center(x, y)
                width = self._board.block_width
                height = self._board.block_height

                draw_rectangle_outline(
                    left + center[0],
                    bottom + center[1],
                    width,
                    height,
                    self._theme.accent,
                )

    def next_block(self) -> None:
        self._cursor_board = self._history.pop()

        half_cols = self._board.cols // 2
        half_cursor_block_cols = self._cursor_board.cols // 2
        self._cursor_x = half_cols - half_cursor_block_cols
        self._cursor_y = 0

        self.update_cursor()

    def update_cursor(self) -> None:
        left = self._board.left
        bottom = self._board.bottom
        block_width = self._board.block_width
        block_margin = self._board.block_margin
        offset_x = left + (block_width + block_margin) * self._cursor_x
        offset_y = bottom

        self._cursor_board.update_offset(offset_x, offset_y)

    def move(self, delta_x: int) -> None:
        if self._cursor_board is None:
            return

        board_cols = self._board.cols
        cursor_block_cols = self._cursor_board.cols
        max_x = board_cols - cursor_block_cols
        next_x = self._cursor_x + delta_x

        if next_x < 0:
            next_x = 0
        if next_x > max_x:
            next_x = max_x

        cursor_matrix = self._cursor_board.matrix
        if not self._board.check_collision(cursor_matrix, next_x, self._cursor_y):
            self._cursor_x = next_x
            self.update_cursor()
            self.update_hard_drop_matrix()

    def update_hard_drop_matrix(self) -> None:
        hard_drop_position = self.get_hard_drop_position()
        if hard_drop_position is not None:
            self._drop_matrix = deepcopy(self._cursor_board.matrix)
            self._drop_x = hard_drop_position[0]
            self._drop_y = hard_drop_position[1]
        else:
            self._drop_matrix = None
            self._drop_x = 0
            self._drop_y = 0

    def rotate(self):
        rotated_block = rotate_clockwise(self._cursor_board.matrix)
        rotated_block_width = len(rotated_block[0])

        board_cols = self._board.cols
        if self._cursor_x + rotated_block_width >= board_cols:
            next_x = board_cols - rotated_block_width
        else:
            next_x = self._cursor_x
        if not self._board.check_collision(rotated_block, next_x, self._cursor_y):
            self._cursor_board.set_matrix(rotated_block)
            self._cursor_x = next_x
            self.update_cursor()
            self.update_hard_drop_matrix()

    def get_hard_drop_position(self) -> Optional[Tuple[int, int]]:
        cursor_matrix = self._cursor_board.matrix
        x = self._cursor_x
        max_y = self._board.rows - self._cursor_board.rows
        for y in range(self._cursor_y, max_y + 1, 1):
            if self._board.check_intersection(cursor_matrix, x, y):
                if self._board.check_insertable(cursor_matrix, x, y):
                    return x, y
                else:
                    return None
        return None

    def hard_drop(self) -> None:
        if self._drop_matrix is None:
            return

        self._board.fill_matrix(self._drop_matrix, self._drop_x, self._drop_y, E)
        self._board.update_textures()

        self._drop_matrix = None
        self._drop_x = 0
        self._drop_y = 0

        if self._history.size >= 1:
            self.next_block()
            self._history.update_textures()
        else:
            self._cursor_board = None
            self._cursor_x = 0
            self._cursor_y = 0

            if self._board.is_all_inactive():
                self._stage_clear = True
            else:
                self._stage_failed = True
