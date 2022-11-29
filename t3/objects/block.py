# -*- coding: utf-8 -*-

from enum import Enum, unique, auto
from typing import Final, Dict

from PIL import Image, ImageDraw
from arcade import Texture

from t3.color.color_tuple import ColorTuple
from t3.objects.matrix import Matrix
from t3.theme.theme import Theme


@unique
class BlockIndex(Enum):
    e = 0
    d = auto()
    i = auto()
    o = auto()
    t = auto()
    l = auto()  # noqa
    j = auto()
    s = auto()
    z = auto()
    ic = auto()
    oc = auto()
    tc = auto()
    lc = auto()
    jc = auto()
    sc = auto()
    zc = auto()


E: Final[int] = BlockIndex.e.value  # Empty
D: Final[int] = BlockIndex.d.value  # Disable
I: Final[int] = BlockIndex.i.value  # noqa
O: Final[int] = BlockIndex.o.value  # noqa
T: Final[int] = BlockIndex.t.value
L: Final[int] = BlockIndex.l.value
J: Final[int] = BlockIndex.j.value
S: Final[int] = BlockIndex.s.value
Z: Final[int] = BlockIndex.z.value
IC: Final[int] = BlockIndex.ic.value
OC: Final[int] = BlockIndex.oc.value
TC: Final[int] = BlockIndex.tc.value
LC: Final[int] = BlockIndex.lc.value
JC: Final[int] = BlockIndex.jc.value
SC: Final[int] = BlockIndex.sc.value
ZC: Final[int] = BlockIndex.zc.value

BLOCK_NAME_TO_NUMBER: Final[Dict[str, int]] = {
    "E": E,
    "D": D,
    "I": I,
    "O": O,
    "T": T,
    "L": L,
    "J": J,
    "S": S,
    "Z": Z,
    "IC": IC,
    "OC": OC,
    "TC": TC,
    "LC": LC,
    "JC": JC,
    "SC": SC,
    "ZC": ZC,
}
BLOCK_NUMBER_TO_NAME: Final[Dict[int, str]] = {
    v: k for k, v in BLOCK_NAME_TO_NUMBER.items()
}

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

BLOCK_IC: Final[Matrix] = [
    [IC, IC, IC, IC],
]
BLOCK_OC: Final[Matrix] = [
    [OC, OC],
    [OC, OC],
]
BLOCK_TC: Final[Matrix] = [
    [TC, TC, TC],
    [0, TC, 0],
]
BLOCK_LC: Final[Matrix] = [
    [0, 0, LC],
    [LC, LC, LC],
]
BLOCK_JC: Final[Matrix] = [
    [JC, 0, 0],
    [JC, JC, JC],
]
BLOCK_SC: Final[Matrix] = [
    [0, SC, SC],
    [SC, SC, 0],
]
BLOCK_ZC: Final[Matrix] = [
    [ZC, ZC, 0],
    [0, ZC, ZC],
]

BLOCKS: Final[Dict[int, Matrix]] = {
    I: BLOCK_I,
    O: BLOCK_O,
    T: BLOCK_T,
    L: BLOCK_L,
    J: BLOCK_J,
    S: BLOCK_S,
    Z: BLOCK_Z,
    IC: BLOCK_IC,
    OC: BLOCK_OC,
    TC: BLOCK_TC,
    LC: BLOCK_LC,
    JC: BLOCK_JC,
    SC: BLOCK_SC,
    ZC: BLOCK_ZC,
}


def create_block_texture(
    name: str,
    width: int,
    height: int,
    color: ColorTuple,
) -> Texture:
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    xy = (0, 0, width, height)
    draw.rectangle(xy, color)
    return Texture(name, image=image)


def create_block_textures(width: int, height: int, theme: Theme) -> Dict[int, Texture]:
    return {
        E: create_block_texture("E", width, height, theme.empty),
        D: create_block_texture("D", width, height, theme.block_disable),
        I: create_block_texture("I", width, height, theme.block_i_normal),
        O: create_block_texture("O", width, height, theme.block_o_normal),
        T: create_block_texture("T", width, height, theme.block_t_normal),
        L: create_block_texture("L", width, height, theme.block_l_normal),
        J: create_block_texture("J", width, height, theme.block_j_normal),
        S: create_block_texture("S", width, height, theme.block_s_normal),
        Z: create_block_texture("Z", width, height, theme.block_z_normal),
        IC: create_block_texture("IC", width, height, theme.block_i_clear),
        OC: create_block_texture("OC", width, height, theme.block_o_clear),
        TC: create_block_texture("TC", width, height, theme.block_t_clear),
        LC: create_block_texture("LC", width, height, theme.block_l_clear),
        JC: create_block_texture("JC", width, height, theme.block_j_clear),
        SC: create_block_texture("SC", width, height, theme.block_s_clear),
        ZC: create_block_texture("ZC", width, height, theme.block_z_clear),
    }
