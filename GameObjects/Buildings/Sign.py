from abc import ABC

import arcade

from GameObjects.Buildings.AbstractBuilding import AbstractBuilding


class Sign(AbstractBuilding, ABC):
    scale = 0.6
    direction = 0

    def __init__(self, x, y):
        super().__init__(x, y)

    def add_to_physics(self, physics):
        physics.add_sprite(self,
                           collision_type="sign",
                           body_type=arcade.PymunkPhysicsEngine.STATIC)


class RightSign(Sign):
    def __init__(self, x, y):
        self.path = ":resources:images/tiles/signRight.png"
        self.direction = 1
        super().__init__(x, y)


class LeftSign(Sign):
    def __init__(self, x, y):
        self.path = ":resources:images/tiles/signLeft.png"
        self.direction = -1
        super().__init__(x, y)
