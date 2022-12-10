from typing import Optional

from GameObjects.Buildings.AbstractBuilding import AbstractBuilding
from GameObjects.Buildings.Sign import RightSign, LeftSign
from GameObjects.Tiles.BuildingTile import BuildingTile


class Builder:

    def build(self, mouse_button, tile: BuildingTile) -> Optional[AbstractBuilding]:

        if tile.get_building():
            return None

        building = None
        if mouse_button == 4:
            building = RightSign(tile.center_x, tile.center_y)
        if mouse_button == 1:
            building = LeftSign(tile.center_x, tile.center_y)

        tile.set_building(building)
        return building
