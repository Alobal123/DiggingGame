from GameObjects.AbstractBuilding import AbstractBuilding


class BaseBuilding(AbstractBuilding):

    def __init__(self, x, y):
        self.path = ":resources:images/tiles/doorClosed_mid.png"
        self.scale = 1.0
        super().__init__(x, y)
