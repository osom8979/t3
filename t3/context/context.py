# -*- coding: utf-8 -*-

from overrides import overrides
from typing import Final, List, Dict, Tuple
from random import choice
from math import floor

import arcade
from arcade import (
    Sprite,
    SpriteList,
    Texture,
    Window,
    draw_rectangle_filled,
    set_background_color,
)
from arcade import run as arcade_run
from arcade.window_commands import get_display_size
from arcade.key import LEFT as ARCADE_KEY_LEFT
from arcade.key import RIGHT as ARCADE_KEY_RIGHT
from arcade.key import UP as ARCADE_KEY_UP
from arcade.key import DOWN as ARCADE_KEY_DOWN

# noinspection PyUnresolvedReferences
from PIL import Image, ImageDraw

BOARD_ROWS: Final[int] = 20
BOARD_COLS: Final[int] = 10

# This sets the WIDTH and HEIGHT of each grid location
BLOCK_WIDTH: Final[int] = 22
BLOCK_HEIGHT: Final[int] = 22

BLOCK_HALF_WIDTH: Final[int] = BLOCK_WIDTH // 2
BLOCK_HALF_HEIGHT: Final[int] = BLOCK_HEIGHT // 2

# This sets the margin between each cell
# and on the edges of the screen.
BLOCK_MARGIN: Final[int] = 2

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 800
SCREEN_TITLE: Final[str] = "Turn The Tricks"

BACKGROUND_COLOR: Final[Tuple[int, int, int]] = (0x0c, 0x1b, 0x23)

GOWUN_DODUM_FONT: Final[str] = "Gowun Dodum"

E: Final[int] = 0  # EMPTY
I: Final[int] = 1  # noqa
O: Final[int] = 2  # noqa
T: Final[int] = 3
L: Final[int] = 4
J: Final[int] = 5
S: Final[int] = 6
Z: Final[int] = 7

BLOCK_NAME_TO_NUMBER: Final[Dict[str, int]] = {
    "E": E,
    "I": I,
    "O": O,
    "T": T,
    "L": L,
    "J": J,
    "S": S,
    "Z": Z,
}

BLOCK_NUMBER_TO_NAME: Final[Dict[int, str]] = {
    v: k for k, v in BLOCK_NAME_TO_NUMBER.items()
}

Matrix = List[List[int]]

BLOCK_I: Final[Matrix] = [
    [I, I, I, I],
]
BLOCK_O: Final[Matrix] = [
    [O, O],
    [O, O],
]
BLOCK_T: Final[Matrix] = [
    [T, T, T],
    [0, T, 0],
]
BLOCK_L: Final[Matrix] = [
    [0, 0, L],
    [L, L, L],
]
BLOCK_J: Final[Matrix] = [
    [J, 0, 0],
    [J, J, J],
]
BLOCK_S: Final[Matrix] = [
    [0, S, S],
    [S, S, 0],
]
BLOCK_Z: Final[Matrix] = [
    [Z, Z, 0],
    [0, Z, Z],
]

BLOCKS: Final[Dict[int, Matrix]] = {
    I: BLOCK_I,
    O: BLOCK_O,
    T: BLOCK_T,
    L: BLOCK_L,
    J: BLOCK_J,
    S: BLOCK_S,
    Z: BLOCK_Z,
}

ColorTuple = Tuple[int, int, int, int]

PAPER_PIXELS_PALETTE: List[ColorTuple] = [
    (0xee, 0xe1, 0xc4, 0xff),  # 0 - Background
    (0xe6, 0xd9, 0xbd, 0xff),
    (0xdb, 0xcf, 0xb1, 0xff),
    (0xd6, 0xc7, 0xa3, 0xff),
    (0xc3, 0xb7, 0x97, 0xff),
    (0xad, 0xa3, 0x87, 0xff),  # 5 - I
    (0xcc, 0x99, 0x70, 0xff),  # 6 - O
    (0xa9, 0x7e, 0x5c, 0xff),
    (0x93, 0x7b, 0x6a, 0xff),  # 8 - T
    (0xa0, 0xa0, 0xa0, 0xff),  # 9
    (0x83, 0x83, 0x83, 0xff),  # 10 - Text
    (0x9e, 0xb5, 0xc0, 0xff),  # 11
    (0x83, 0x9c, 0xa9, 0xff),
    (0x6d, 0x83, 0x8e, 0xff),  # 13 - L
    (0xc8, 0x7e, 0x7e, 0xff),  # 14
    (0xa0, 0x5e, 0x5e, 0xff),  # 15 - J
    (0xb0, 0x89, 0xab, 0xff),  # 16
    (0x8e, 0x6d, 0x89, 0xff),  # 17 - S
    (0xb9, 0xab, 0x73, 0xff),  # 18
    (0x97, 0x8c, 0x63, 0xff),
    (0x87, 0xa9, 0x85, 0xff),  # 20
    (0x6f, 0x8b, 0x6e, 0xff),  # 21 - Z
]

COLORS: Final[Dict[int, ColorTuple]] = {
    E: PAPER_PIXELS_PALETTE[0],
    I: PAPER_PIXELS_PALETTE[5],
    O: PAPER_PIXELS_PALETTE[6],
    T: PAPER_PIXELS_PALETTE[8],
    L: PAPER_PIXELS_PALETTE[13],
    J: PAPER_PIXELS_PALETTE[15],
    S: PAPER_PIXELS_PALETTE[17],
    Z: PAPER_PIXELS_PALETTE[21],
}


def rotate_counterclockwise(shape):
    return [[shape[y][x] for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]


def remove_row(board, row):
    del board[row]
    return [[0 for _ in range(BOARD_COLS)]] + board


def create_block_textures(block_width: int, block_height: int) -> List[Texture]:
    result = list()
    for color in COLORS.values():
        image = Image.new("RGBA", (block_width, block_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        xy = (0, 0, block_width, block_height)
        draw.rectangle(xy, color)
        result.append(Texture(str(color), image=image))
    return result


def calc_block_center(
    x: int,
    y: int,
    block_width: int,
    block_height: int,
    margin=0,
) -> Tuple[float, float]:
    block_half_width = block_width // 2
    block_half_height = block_height // 2
    left = (margin + block_width) * x + margin
    top = (margin + block_height) * y + margin
    center_x = left + block_half_width
    center_y = top + block_half_height
    return center_x, center_y


def create_sprites(
    board_cols: int,
    board_rows: int,
    block_width: int,
    block_height: int,
    block_margin: int,
    textures: List[Texture],
) -> SpriteList:
    result = SpriteList()
    for y in range(board_rows):
        for x in range(board_cols):
            sprite = Sprite()
            for texture in textures:
                sprite.append_texture(texture)
            sprite.set_texture(0)
            center = calc_block_center(x, y, block_width, block_height, block_margin)
            sprite.center_x = center[0]
            sprite.center_y = center[1]
            result.append(sprite)
    return result


class Board:
    def __init__(
        self,
        cols: int,
        rows: int,
        block_width: int,
        block_height: int,
        block_margin: int,
    ):
        self._cols = cols
        self._rows = rows
        self._block_width = block_width
        self._block_height = block_height
        self._block_margin = block_margin

        self._matrix = [[0 for _x in range(cols)] for _y in range(rows)]
        self._block_textures = create_block_textures(block_width, block_height)
        self._sprites = create_sprites(
            cols,
            rows,
            block_width,
            block_height,
            block_margin,
            self._block_textures,
        )

    @property
    def matrix(self) -> Matrix:
        return self._matrix

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def width(self) -> int:
        margin = self._block_margin
        width = self._block_width
        cols = self._cols
        return (margin + width) * cols + margin

    @property
    def height(self) -> int:
        margin = self._block_margin
        height = self._block_height
        rows = self._rows
        return (margin + height) * rows + margin

    @property
    def half_width(self) -> int:
        return self.width // 2

    @property
    def half_height(self) -> int:
        return self.height // 2

    @property
    def sprites(self) -> SpriteList:
        return self._sprites

    def update_offset(self, offset_x: int, offset_y: int) -> None:
        for y in range(self._rows):
            for x in range(self._cols):
                center = calc_block_center(
                    x, y, self._block_width, self._block_height, self._block_margin
                )
                sprite = self._sprites[self._cols * y + x]
                sprite.center_x = offset_x + center[0]
                sprite.center_y = offset_y + center[1]

    def update(self):
        for y in range(self._rows):
            for x in range(self._cols):
                v = self._matrix[y][x]
                i = y * self._cols + x
                self._sprites[i].set_texture(v)

    def draw(self) -> None:
        self._sprites.draw()

    def check_collision(self, shape, offset) -> bool:
        off_x, off_y = offset
        for cy, row in enumerate(shape):
            for cx, cell in enumerate(row):
                if cell is E:
                    continue
                if self._matrix[cy + off_y][cx + off_x] is not E:
                    return True
        return False

    def join_matrix(self, matrix: Matrix, matrix_2_offset):
        offset_x, offset_y = matrix_2_offset
        for y, line in enumerate(matrix):
            for x, val in enumerate(line):
                self._matrix[y + offset_y - 1][x + offset_x] += val


class Game:
    def __init__(
        self,
        board_cols=BOARD_COLS,
        board_rows=BOARD_ROWS,
        block_width=BLOCK_WIDTH,
        block_height=BLOCK_HEIGHT,
        block_margin=BLOCK_MARGIN,
    ):
        self._board = Board(
            board_cols,
            board_rows,
            block_width,
            block_height,
            block_margin,
        )
        self._board.update()

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


class Context(Window):
    def __init__(
        self,
        fullscreen=False,
        resizable=False,
        fps=60,
        antialiasing=False,
        vsync=False,
        center_window=False,
        debug=False,
        verbose=0,
    ):
        self._update_rate = 1.0 / fps
        self._debug = debug
        self._verbose = verbose

        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title=SCREEN_TITLE,
            fullscreen=fullscreen,
            resizable=resizable,
            update_rate=self._update_rate,
            antialiasing=antialiasing,
            vsync=vsync,
            center_window=center_window,
        )

        set_background_color(BACKGROUND_COLOR)

        self._game = Game(
            BOARD_COLS,
            BOARD_ROWS,
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
            BLOCK_MARGIN,
        )

        # window_width, window_height = self.get_size()
        # self._game.resize(window_width, window_height)

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def verbose(self) -> int:
        return self._verbose

    @overrides
    def on_resize(self, width: float, height: float) -> None:
        super().on_resize(width, height)
        self._game.resize(width, height)

    @overrides
    def on_update(self, delta_time: float) -> None:
        self._game.update(delta_time)

    @overrides
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == ARCADE_KEY_LEFT:
            self.move(-1)
        elif symbol == ARCADE_KEY_RIGHT:
            self.move(1)
        elif symbol == ARCADE_KEY_UP:
            self.rotate_stone()
        elif symbol == ARCADE_KEY_DOWN:
            self.drop()

    @overrides
    def on_draw(self) -> None:
        self.clear()
        self._game.draw()

        # draw_text(
        #     text=str(floor(self._total_delta)),
        #     start_x=0,
        #     start_y=0,
        #     color=arcade.color.RED,
        #     font_name=GOWUN_DODUM_FONT,
        # )

    def run(self) -> None:
        arcade_run()


def run_context(
    fullscreen=False,
    resizable=False,
    fps=60,
    antialiasing=False,
    vsync=False,
    center_window=False,
    debug=False,
    verbose=0,
) -> None:
    context = Context(
        fullscreen=fullscreen,
        resizable=resizable,
        fps=fps,
        antialiasing=antialiasing,
        vsync=vsync,
        center_window=center_window,
        debug=debug,
        verbose=verbose,
    )
    context.run()
