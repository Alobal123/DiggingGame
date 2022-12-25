from abc import ABC

import arcade


class AbstractBuilding(arcade.Sprite, ABC):
    cost = 0
    path = ''
    scale = 1.0

    def __init__(self, x, y):
        super().__init__(self.path, self.scale)
        self.center_x = x
        self.center_y = y

    def add_to_physics(self, physics):
        physics.add_sprite(self,
                           collision_type='building',
                           body_type=arcade.PymunkPhysicsEngine.STATIC)
