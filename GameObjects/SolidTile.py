import arcade

from GameObjects.AbstractTile import AbstractTile


class SolidTile(AbstractTile):

    def __init__(self, scaling):
        super().__init__(":resources:images/tiles/grassCenter_round.png", scaling)
        self.color = arcade.color.GRAY
