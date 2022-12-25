import arcade

from GameObjects.Buildings.Sign import Sign
from GameObjects.Worker import Worker


class Physics(arcade.PymunkPhysicsEngine):
    GRAVITY = (0, -1 * 1500)
    DAMPING = 0.4

    def __init__(self):
        super().__init__(gravity=self.GRAVITY, damping=self.DAMPING)

        def tile_hit_handler(worker_sprite, tile_sprite, _arbiter, _space, _data):
            if tile_sprite.selected:
                worker_sprite.start_digging(tile_sprite)
            elif worker_sprite.center_y - worker_sprite.height / 2 <= tile_sprite.center_y:
                worker_sprite.flip_direction(tile_sprite)

        def sign_hit_handler(worker_sprite: Worker, sign_sprite: Sign, _arbiter, _space, _data):
            if worker_sprite.center_y - worker_sprite.height//2 > sign_sprite.center_y:
                return False
            if sign_sprite.direction != worker_sprite.direction:
                worker_sprite.flip_direction(sign_sprite)
                return True
            return False

        self.add_collision_handler('worker', 'tile', post_handler=tile_hit_handler)
        self.add_collision_handler('worker', 'worker', begin_handler=lambda *args: False)
        self.add_collision_handler('worker', 'building', begin_handler=lambda *args: False)
        self.add_collision_handler('worker', 'sign', begin_handler=sign_hit_handler)
        self.add_collision_handler('sign', 'tile', begin_handler=lambda *args: False)
        self.add_collision_handler('building', 'tile', begin_handler=lambda *args: False)
