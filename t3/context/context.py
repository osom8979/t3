# -*- coding: utf-8 -*-


class Context:
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
        self.fullscreen = fullscreen
        self.resizable = resizable
        self.fps = fps
        self.antialiasing = antialiasing
        self.vsync = vsync
        self.center_window = center_window
        self.debug = debug
        self.verbose = verbose

    def run(self) -> int:
        return 0


def run_context(
    fullscreen=False,
    resizable=False,
    fps=60,
    antialiasing=False,
    vsync=False,
    center_window=False,
    debug=False,
    verbose=0,
) -> int:
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
    return context.run()
