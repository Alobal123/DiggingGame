from GameObjects.Tiles.AbstractTile import AbstractTile


class InvisibleTile(AbstractTile):

    def __init__(self, x, y, scaling):
        super().__init__(x, y, ":resources:images/tiles/grassCenter.png", scaling)
        self.visible = True
