from GameObjects.Tiles.AbstractTile import AbstractTile


class InvisibleTile(AbstractTile):

    def __init__(self, scaling):
        super().__init__(":resources:images/tiles/grassCenter.png", scaling)
        self.visible = False
