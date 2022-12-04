import arcade
from pyglet.math import Vec2

from CameraMover import CameraMover
from GameObjects.BaseBuilding import BaseBuilding
from GameObjects.BaseTile import BaseTile
from GameObjects.InvisibeTile import InvisibleTile
from GameObjects.SolidTile import SolidTile
from Physics import Physics


class GameView(arcade.View):
    """ Main application class. """

    SPRITE_SCALING = 0.5
    SCREEN_TITLE = "Title"

    # How fast the camera pans to the player. 1.0 is instant.
    CAMERA_SPEED = 0.1

    def __init__(self, window, level):
        """
        Initializer
        """
        super().__init__(window)
        self.level = level

        # Sprite lists
        self.sprite_lists = [arcade.SpriteList(use_spatial_hash=spatial_hashing) for spatial_hashing in
                             (False, False, True)]
        self.tile_list, self.building_list, self.worker_list = self.sprite_lists
        self.physics_engine = None

        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)

        tile = BaseTile(self.SPRITE_SCALING)
        self.tile_width = tile.width
        self.tile_height = tile.height
        self.game_width = self.level.width * (self.tile_width + 1)
        self.game_height = self.level.height * (self.tile_height + 1)

        self.camera_mover = CameraMover(self.camera_sprites,
                                        self.game_width,
                                        self.game_height,
                                        self.window)

        # Variables for controling mouse dragging behaviour
        self.last_dragged_over = None
        self.drag_counter = 0

        # Move camera to base position
        self.camera_sprites.move_to(Vec2(-self.window.width / 2,
                                         self.get_ground_height() - self.window.height / 2))

    def setup_tiles(self, width, height):

        # Create active level tiles
        for x in range(0, self.level.width):
            for y in range(0, self.level.height):
                tile = BaseTile(self.SPRITE_SCALING)
                tile.center_x = width * (x - ((self.level.width - 1) / 2))
                tile.center_y = height * (y - ((self.level.height - 1) / 2))
                self.tile_list.append(tile)

        # Create solid side borders on the right
        for x in range(0, self.window.SIDE_OFFSET // width + 1):
            for y in range(0, self.level.height):
                tile = SolidTile(self.SPRITE_SCALING)
                tile.center_x = width * ((self.level.width + 1) / 2 + x)
                tile.center_y = height * (y - ((self.level.height - 1) / 2))
                self.tile_list.append(tile)

        # Create invisible side borders on surface on the right
        for y in range(self.level.height, self.level.height + self.window.TOP_OFFSET // height + 1):
            tile = InvisibleTile(self.SPRITE_SCALING)
            tile.center_x = width * ((self.level.width + 5) / 2)
            tile.center_y = height * (y - ((self.level.height - 1) / 2))
            self.tile_list.append(tile)

        # Create solid side borders on the left
        for x in range(0, self.window.SIDE_OFFSET // width + 1):
            for y in range(0, self.level.height):
                tile = SolidTile(self.SPRITE_SCALING)
                tile.center_x = width * - ((self.level.width - 1) / 2 + x + 1)
                tile.center_y = height * (y - ((self.level.height - 1) / 2))
                self.tile_list.append(tile)

        # Create invisible side borders on surface on the left
        for y in range(self.level.height, self.level.height + self.window.TOP_OFFSET // height + 1):
            tile = InvisibleTile(self.SPRITE_SCALING)
            tile.center_x = width * - ((self.level.width + 3) / 2 + 1)
            tile.center_y = height * (y - ((self.level.height - 1) / 2))
            self.tile_list.append(tile)

        # Create solid bottom borders
        for x in range(-self.window.SIDE_OFFSET // width + 1, self.level.width + self.window.SIDE_OFFSET // width + 1):
            for y in range(0, self.window.BOTTOM_OFFSET // height + 1):
                tile = SolidTile(self.SPRITE_SCALING)
                tile.center_x = width * (x - ((self.level.width - 1) / 2))
                tile.center_y = height * - ((self.level.height - 1) / 2 + y + 1)
                self.tile_list.append(tile)

    def get_ground_height(self):
        return round(self.tile_height + 1) * (self.level.height / 2 + 1)

    def setup_buildings(self):

        base = BaseBuilding(0, self.get_ground_height(), self.physics_engine, self.worker_list)
        self.building_list.append(base)

        self.physics_engine.add_sprite_list(self.building_list,
                                            collision_type='building',
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)
        self.physics_engine = Physics()

        width = round(self.tile_width + 1)
        height = round(self.tile_height + 1)

        self.setup_tiles(width, height)
        self.setup_buildings()

        self.physics_engine.add_sprite_list(self.tile_list,
                                            friction=0.4,
                                            collision_type="tile",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw sky
        arcade.draw_lrtb_rectangle_filled(-self.game_width,
                                          self.game_width,
                                          self.game_height // 2 + self.window.TOP_OFFSET,
                                          self.game_height // 2 + 1,
                                          arcade.color.AIR_SUPERIORITY_BLUE)

        # Draw all the sprites.
        for sprite_list in self.sprite_lists:
            sprite_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """
        for worker in self.worker_list:
            worker.update()
        for building in self.building_list:
            building.update()

        self.physics_engine.step()
        self.camera_mover.move()

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        MARGIN_SIZE = 70
        direction = Vec2(0, 0)

        if x < MARGIN_SIZE:
            direction.x = -1
        if x > self.window.width - MARGIN_SIZE:
            direction.x = 1
        if y < MARGIN_SIZE:
            direction.y = -1
        if y > self.window.height - MARGIN_SIZE:
            direction.y = 1

        if direction == Vec2(0, 0):
            self.camera_mover.stop_moving()
        else:
            self.camera_mover.start_moving(direction)

    def get_mouse_coordinates(self, x, y):
        return x + self.camera_mover.get_x(), y + self.camera_mover.get_y()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        tiles = arcade.get_sprites_at_point(self.get_mouse_coordinates(x, y), self.tile_list)
        for tile in tiles:
            tile.on_mouse_press()
            self.last_dragged_over = tile

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, _buttons: int, _modifiers: int):
        if self.drag_counter == 0:
            self.drag_counter = 8
            tiles = arcade.get_sprites_at_point(self.get_mouse_coordinates(x, y), self.tile_list)
            for tile in tiles:
                if tile != self.last_dragged_over:
                    tile.on_mouse_press()
                    self.last_dragged_over = tile
        else:
            self.drag_counter -= 1

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.last_dragged_over = None
