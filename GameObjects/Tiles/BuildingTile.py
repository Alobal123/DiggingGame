import arcade

from GameObjects.Buildings.AbstractBuilding import AbstractBuilding
from GameObjects.Buildings.Sign import RightSign
from GameObjects.Tiles.AbstractTile import AbstractTile


class BuildingTile(AbstractTile):

    def __init__(self, x, y, scaling):
        super().__init__(x, y, ":resources:images/tiles/grassCenter_round.png", scaling)
        self.visible = False
        self.building = None

    def get_building(self) -> AbstractBuilding:
        return self.building

    def set_building(self, building: AbstractBuilding):
        self.building = building
