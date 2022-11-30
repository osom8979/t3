# -*- coding: utf-8 -*-

from overrides import overrides
from typing import Final, Tuple

from arcade import Sound, Window, set_background_color
from arcade import run as arcade_run
from arcade import exit as arcade_exit
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIFlatButton, UIManager
from arcade.key import LEFT as ARCADE_KEY_LEFT
from arcade.key import RIGHT as ARCADE_KEY_RIGHT
from arcade.key import UP as ARCADE_KEY_UP
from arcade.key import DOWN as ARCADE_KEY_DOWN

from t3.objects.game import Game
from t3.theme.flat import FlatTheme
from t3.variables.block import BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_MARGIN
from t3.variables.board import BOARD_ROWS, BOARD_COLS
from t3.variables.fonts import GOWUN_DODUM_FONT

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 800
SCREEN_TITLE: Final[str] = "Turn The Tricks"

MUSIC_VOLUME: Final[float] = 0.3

BACKGROUND_COLOR: Final[Tuple[int, int, int, int]] = (0x0c, 0x1b, 0x23, 0xFF)


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

        self._theme = FlatTheme()
        self._game = Game(
            BOARD_COLS,
            BOARD_ROWS,
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
            BLOCK_MARGIN,
        )

        # window_width, window_height = self.get_size()
        # self._game.resize(window_width, window_height)

        # self._music = Sound(CATWALK_OGG_PATH, streaming=True)
        # self._current_player = self._music.play(MUSIC_VOLUME, loop=True)

        self._uis = self._create_ui()
        self._uis.enable()

    @staticmethod
    def _create_ui() -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="left")
        exit_button = UIFlatButton(
            text="Exit",
            width=200,
            style={"font_name": GOWUN_DODUM_FONT},
        )
        v_box.add(exit_button.with_space_around(bottom=8))

        @exit_button.event("on_click")
        def on_click_exit(event):
            arcade_exit()

        title_menu = UIAnchorWidget(
            anchor_x="left",
            anchor_y="top",
            child=v_box.with_space_around(left=16),
        )
        uis.add(title_menu)
        return uis

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def verbose(self) -> int:
        return self._verbose

    @overrides
    def on_resize(self, width: float, height: float) -> None:
        super().on_resize(width, height)
        self._uis.on_resize(width, height)
        self._game.resize(width, height)

    @overrides
    def on_update(self, delta_time: float) -> None:
        self._uis.on_update(delta_time)
        self._game.update(delta_time)

    @overrides
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self._uis.on_key_press(symbol, modifiers)

        if symbol == ARCADE_KEY_LEFT:
            self._game.move(-1)
        elif symbol == ARCADE_KEY_RIGHT:
            self._game.move(1)
        elif symbol == ARCADE_KEY_UP:
            self._game.rotate()
        elif symbol == ARCADE_KEY_DOWN:
            self._game.hard_drop()

    @overrides
    def on_draw(self) -> None:
        self.clear()
        self._uis.draw()
        self._game.draw()

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
