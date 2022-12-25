from typing import Optional, List

from GameObjects.Buildings.AbstractBuilding import AbstractBuilding
from GameObjects.Buildings.Sign import RightSign, LeftSign
from GameObjects.Tiles.BaseTile import BaseTile
from GameObjects.Tiles.BuildingTile import BuildingTile
from GameObjects.Tiles.SolidTile import SolidTile


class Builder:

    def __init__(self, tiles, physics):
        self.tiles = tiles
        self.physics = physics

    def click_build(self, mouse_button, tile: BuildingTile) -> Optional[AbstractBuilding]:
        building = None
        if mouse_button == 4:
            building = RightSign(tile.center_x, tile.center_y)
        if mouse_button == 1:
            building = LeftSign(tile.center_x, tile.center_y)

        return self.build(building, tile)

    def build(self, building: AbstractBuilding, tile: BuildingTile) -> Optional[AbstractBuilding]:
        if not self.can_be_build(tile):
            return None
        tile.set_building(building)
        self.switch_tile(self.get_building_foundations(tile))
        return building

    def get_building_foundations(self, tile) -> BaseTile:
        return tile.get_tile_in_direction(0, -1, self.tiles)

    def can_be_build(self, tile: BuildingTile) -> bool:
        foundation = self.get_building_foundations(tile)
        return tile.get_building() is None \
               and foundation \
               and foundation.can_be_building_foundation()

    def switch_tile(self, tile):
        if isinstance(tile, BaseTile):
            solid_tile = SolidTile(tile.center_x, tile.center_y, tile.scale)
            solid_tile.add_to_physics(self.physics)
            self.tiles.append(solid_tile)
            tile.remove_from_sprite_lists()
