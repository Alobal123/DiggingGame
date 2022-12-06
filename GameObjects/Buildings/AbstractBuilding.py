from abc import ABC

import arcade


class AbstractBuilding(arcade.Sprite, ABC):
    cost = 0
    path = ''
    scale = 1.0

    def __init__(self, x, y):
        super().__init__(self.path, self.scale)
        self.center_x = x
        self.center_y = y + self.height/2
