import arcade

from GameObjects.Tiles.AbstractTile import AbstractTile


class SolidTile(AbstractTile):

    def __init__(self, x, y, scaling):
        super().__init__(x, y, ":resources:images/tiles/grassCenter_round.png", scaling)
        self.color = arcade.color.GRAY

    def can_be_building_foundation(self):
        return True
