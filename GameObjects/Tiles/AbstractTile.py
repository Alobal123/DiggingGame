from abc import ABC

import arcade
from arcade import Sprite, SpriteList


class AbstractTile(Sprite, ABC):
    selected = False

    def __init__(self, x, y, resource, scaling):
        super().__init__(resource, scaling)
        self.center_x = x
        self.center_y = y

    def on_mouse_press(self):
        pass

    def on_mouse_drag(self):
        pass

    def get_tile_in_direction(self, x, y, tile_list: SpriteList):
        return arcade.get_sprites_at_point((self.center_x + x * self.width,
                                            self.center_y + y * self.height),
                                           tile_list)
