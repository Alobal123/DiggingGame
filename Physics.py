import arcade


class Physics(arcade.PymunkPhysicsEngine):
    GRAVITY = (0, -1 * 1500)
    DAMPING = 0.4

    def __init__(self):
        super().__init__(gravity=self.GRAVITY, damping=self.DAMPING)

        def tile_hit_handler(player_sprite, tile_sprite, _arbiter, _space, _data):
            if tile_sprite.selected:
                player_sprite.start_digging(tile_sprite)
            elif player_sprite.center_y - player_sprite.height / 2 <= tile_sprite.center_y:
                player_sprite.flip_direction(tile_sprite)

        self.add_collision_handler('worker', 'tile', post_handler=tile_hit_handler)
        self.add_collision_handler('worker', 'worker', begin_handler=lambda *args: False)
