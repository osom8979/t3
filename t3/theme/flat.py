# -*- coding: utf-8 -*-

from t3.theme.theme import Theme
from t3.color.palette.flat_ui import (
    TURQUOISE,
    EMERALD,
    PETER_RIVER,
    AMETHYST,
    WET_ASPHALT,
    GREEN_SEA,
    NEPHRITIS,
    BELIZE_HOLE,
    WISTERIA,
    MIDNIGHT_BLUE,
    SUN_FLOWER,
    CARROT,
    ALIZARIN,
    CLOUDS,
    CONCRETE,
    ORANGE,
    PUMPKIN,
    POMEGRANATE,
    SILVER,
    ASBESTOS,
)


class FlatTheme(Theme):
    background = MIDNIGHT_BLUE
    foreground = CLOUDS

    empty = WET_ASPHALT
    block_disable = ASBESTOS

    block_i_normal = TURQUOISE
    block_o_normal = EMERALD
    block_t_normal = PETER_RIVER
    block_l_normal = AMETHYST
    block_j_normal = SUN_FLOWER
    block_s_normal = CARROT
    block_z_normal = ALIZARIN

    block_i_clear = GREEN_SEA
    block_o_clear = NEPHRITIS
    block_t_clear = BELIZE_HOLE
    block_l_clear = WISTERIA
    block_j_clear = ORANGE
    block_s_clear = PUMPKIN
    block_z_clear = POMEGRANATE

    reserve1 = CONCRETE
    reserve2 = SILVER