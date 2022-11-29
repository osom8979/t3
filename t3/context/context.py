# -*- coding: utf-8 -*-

from overrides import overrides
from typing import Final, Tuple

from arcade import (
    Window,
    set_background_color,
)
from arcade import run as arcade_run
from arcade.key import LEFT as ARCADE_KEY_LEFT
from arcade.key import RIGHT as ARCADE_KEY_RIGHT
from arcade.key import UP as ARCADE_KEY_UP
from arcade.key import DOWN as ARCADE_KEY_DOWN

# noinspection PyUnresolvedReferences
from PIL import Image, ImageDraw

from t3.objects.game import Game
from t3.variables.block import BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_MARGIN
from t3.variables.board import BOARD_ROWS, BOARD_COLS

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 800
SCREEN_TITLE: Final[str] = "Turn The Tricks"

BACKGROUND_COLOR: Final[Tuple[int, int, int, int]] = (0x0c, 0x1b, 0x23, 0xFF)

GOWUN_DODUM_FONT: Final[str] = "Gowun Dodum"


# def rotate_counterclockwise(shape):
#     return [[shape[y][x] for y in range(len(shape))]
#             for x in range(len(shape[0]) - 1, -1, -1)]
#
#
# def remove_row(board, row):
#     del board[row]
#     return [[0 for _ in range(BOARD_COLS)]] + board


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
