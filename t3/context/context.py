# -*- coding: utf-8 -*-

from overrides import overrides
from typing import Final, Tuple

from PIL import Image

from arcade import Sound, Window, Texture, set_background_color
from arcade import run as arcade_run
from arcade import exit as arcade_exit
from arcade.gui import (
    UIAnchorWidget,
    UIBoxLayout,
    UIFlatButton,
    UIManager,
    UIMessageBox,
    UILabel,
    UITextureButton,
)
from arcade.key import R as ARCADE_KEY_R
from arcade.key import LEFT as ARCADE_KEY_LEFT
from arcade.key import RIGHT as ARCADE_KEY_RIGHT
from arcade.key import UP as ARCADE_KEY_UP
from arcade.key import DOWN as ARCADE_KEY_DOWN
from arcade.key import SPACE as ARCADE_KEY_SPACE

from t3.assets.path import (
    EXIT_RUN_NORMAL_PATH,
    EXIT_RUN_HOVERED_PATH,
    EXIT_RUN_PRESSED_PATH,
)
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

        self._show_exit_alert = False
        self._exit_alert = self._exit_alert_ui()
        self._main_buttons = self._create_ui()
        self._main_buttons.enable()

    def _exit_alert_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="center")
        title = UILabel(
            text="Quit the game?",
            font_name=GOWUN_DODUM_FONT,
            font_size=self._theme.title_size,
            text_color=self._theme.foreground,
            bold=True,
        )
        v_box.add(title)

        ok_button = UIFlatButton(
            text="Ok",
            width=200,
            style={"font_name": GOWUN_DODUM_FONT},
        )
        v_box.add(ok_button.with_space_around(top=24, bottom=8))

        @ok_button.event("on_click")
        def on_click_ok(event):
            self.close()

        cancel_button = UIFlatButton(
            text="Cancel",
            width=200,
            style={"font_name": GOWUN_DODUM_FONT},
        )
        v_box.add(cancel_button)

        @cancel_button.event("on_click")
        def on_click_exit(event):
            self.hide_exit_alert_dialog()

        anchor = UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(anchor)
        return uis

    def _create_ui(self) -> UIManager:
        uis = UIManager()
        v_box = UIBoxLayout(x=0, y=0, vertical=True, align="left")
        exit_run_normal = Texture("ExitRunNormal", Image.open(EXIT_RUN_NORMAL_PATH))
        exit_run_hovered = Texture("ExitRunHovered", Image.open(EXIT_RUN_HOVERED_PATH))
        exit_run_pressed = Texture("ExitRunPressed", Image.open(EXIT_RUN_PRESSED_PATH))
        exit_button = UITextureButton(
            texture=exit_run_normal,
            texture_hovered=exit_run_hovered,
            texture_pressed=exit_run_pressed,
        )
        v_box.add(exit_button.with_space_around(bottom=8))

        @exit_button.event("on_click")
        def on_click_exit(event):
            self.show_exit_alert_dialog()

        title_menu = UIAnchorWidget(
            anchor_x="left",
            anchor_y="top",
            child=v_box.with_space_around(left=8, top=8),
        )
        uis.add(title_menu)
        return uis

    def show_exit_alert_dialog(self) -> None:
        self._show_exit_alert = True
        self._main_buttons.disable()
        self._exit_alert.enable()

    def hide_exit_alert_dialog(self) -> None:
        self._show_exit_alert = False
        self._main_buttons.enable()
        self._exit_alert.disable()

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def verbose(self) -> int:
        return self._verbose

    @overrides
    def on_resize(self, width: float, height: float) -> None:
        super().on_resize(width, height)
        self._main_buttons.on_resize(width, height)
        self._game.resize(width, height)

    @overrides
    def on_update(self, delta_time: float) -> None:
        self._main_buttons.on_update(delta_time)
        self._game.update(delta_time)

    @overrides
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self._main_buttons.on_key_press(symbol, modifiers)

        if symbol == ARCADE_KEY_R:
            self._game.reset()
        if symbol == ARCADE_KEY_LEFT:
            self._game.move(-1)
        elif symbol == ARCADE_KEY_RIGHT:
            self._game.move(1)
        elif symbol == ARCADE_KEY_DOWN or symbol == ARCADE_KEY_SPACE:
            self._game.hard_drop()
        elif symbol == ARCADE_KEY_UP:
            self._game.rotate()

    @overrides
    def on_draw(self) -> None:
        self.clear()
        if self._show_exit_alert:
            self._exit_alert.draw()
        else:
            self._main_buttons.draw()
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
