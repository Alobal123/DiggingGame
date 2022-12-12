from GameObjects.Tiles.BaseTile import BaseTile
from GameObjects.Tiles.BuildingTile import BuildingTile
from GameObjects.Tiles.InvisibeTile import InvisibleTile
from GameObjects.Tiles.SolidTile import SolidTile


class Level:

    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.window = window

    def create_tiles(self, tile_width, tile_height, scaling):
        rt = []
        # Create active level tiles
        for x in range(0, self.width):
            for y in range(0, self.height):
                tile = BaseTile(tile_width * (x - ((self.width - 1) / 2)),
                                tile_height * (y - ((self.height - 1) / 2)),
                                scaling)
                rt.append(tile)

        # Create solid side borders on the right
        for x in range(0, (self.window.width // 2 + self.window.SIDE_OFFSET) // tile_width + 1):
            for y in range(0, self.height):
                tile = SolidTile(tile_width * ((self.width + 1) / 2 + x),
                                 tile_height * (y - ((self.height - 1) / 2)),
                                 scaling)

                rt.append(tile)

        # Create invisible side borders on surface on the right
        for y in range(self.height, self.height + self.window.TOP_OFFSET // tile_height + 1):
            tile = InvisibleTile(tile_width * ((self.width + 5) / 2),
                                 tile_height * (y - ((self.height - 1) / 2)),
                                 scaling)

            rt.append(tile)

        # Create solid side borders on the left
        for x in range(0, (self.window.width // 2 + self.window.SIDE_OFFSET) // tile_width + 1):
            for y in range(0, self.height):
                tile = SolidTile(tile_width * - ((self.width - 1) / 2 + x + 1),
                                 tile_height * (y - ((self.height - 1) / 2)),
                                 scaling)
                rt.append(tile)

        # Create invisible side borders on surface on the left
        for y in range(self.height, self.height + self.window.TOP_OFFSET // tile_height + 1):
            tile = InvisibleTile(tile_width * - ((self.width + 3) / 2 + 1),
                                 tile_height * (y - ((self.height - 1) / 2)),
                                 scaling)
            rt.append(tile)

        # Create solid bottom borders
        for x in range(-(self.window.width // 2 + self.window.SIDE_OFFSET) // tile_width - 1,
                       self.width + (self.window.SIDE_OFFSET + self.window.width // 2) // tile_width + 1):
            for y in range(0, self.window.BOTTOM_OFFSET // tile_height + 1):
                tile = SolidTile(tile_width * (x - ((self.width - 1) / 2)),
                                 tile_height * - ((self.height - 1) / 2 + y + 1),
                                 scaling)
                rt.append(tile)

        return rt

    def create_building_tiles(self, tile_width, tile_height, scaling):
        rt = []
        # Create top row of buildable tiles
        for x in range(-2, self.width + 2):
            y = self.height
            tile = BuildingTile(tile_width * (x - ((self.width - 1) / 2)),
                                tile_height * (y - ((self.height - 1) / 2)),
                                scaling)
            rt.append(tile)
        return rt


