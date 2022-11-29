# -*- coding: utf-8 -*-

from typing import Dict, Tuple

from arcade import SpriteList, Texture, Sprite

from t3.objects.block import E
from t3.objects.matrix import Matrix


class Board:
    def __init__(
        self,
        cols: int,
        rows: int,
        block_width: int,
        block_height: int,
        block_margin: int,
        block_textures: Dict[int, Texture],
    ):
        assert rows > 0
        assert cols > 0

        self._cols = cols
        self._rows = rows
        self._block_width = block_width
        self._block_height = block_height
        self._block_margin = block_margin
        self._offset_x = 0
        self._offset_y = 0

        self._matrix = [[0 for _x in range(cols)] for _y in range(rows)]

        self._sprites = SpriteList()
        for y in range(rows):
            for x in range(cols):
                sprite = Sprite()
                for texture in block_textures.values():
                    sprite.append_texture(texture)
                sprite.set_texture(E)
                center = self.measure_block_center(x, y)
                sprite.center_x = center[0]
                sprite.center_y = center[1]
                self._sprites.append(sprite)

    def measure_block_center(self, col: int, row: int) -> Tuple[float, float]:
        assert self._block_width > 0
        assert self._block_height > 0
        assert self._block_margin >= 0

        bw = self._block_width
        bh = self._block_height
        m = self._block_margin

        left = (m + bw) * col + m
        top = (m + bh) * row + m

        center_x = left + (bw // 2)
        center_y = top + (bh // 2)

        return center_x, center_y

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def block_width(self) -> int:
        return self._block_width

    @property
    def block_height(self) -> int:
        return self._block_height

    @property
    def block_margin(self) -> int:
        return self._block_margin

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
    def left(self) -> int:
        return self._offset_x

    @property
    def right(self) -> int:
        return self._offset_x + self.width

    @property
    def top(self) -> int:
        return self._offset_y + self.height

    @property
    def bottom(self) -> int:
        return self._offset_y

    def as_sprite(self, col: int, row: int) -> Sprite:
        return self._sprites[self._cols * row + col]

    def set_texture(self, col: int, row: int, texture_index: int) -> None:
        self.as_sprite(col, row).set_texture(texture_index)

    def set_matrix(self, matrix: Matrix) -> None:
        self._matrix = matrix

    def update_offset(self, offset_x: int, offset_y: int) -> None:
        self._offset_x = offset_x
        self._offset_y = offset_y

        for row in range(self._rows):
            for col in range(self._cols):
                center = self.measure_block_center(col, row)
                sprite = self.as_sprite(col, row)
                sprite.center_x = offset_x + center[0]
                sprite.center_y = offset_y + center[1]

    def update_textures(self):
        for row in range(self._rows):
            for col in range(self._cols):
                self.set_texture(col, row, self._matrix[row][col])

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
        for row, line in enumerate(matrix):
            for col, val in enumerate(line):
                self._matrix[row + offset_y - 1][col + offset_x] += val

    def draw(self) -> None:
        self._sprites.draw()
