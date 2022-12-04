from enum import Enum

import arcade
from arcade import Sprite


class WorkerState(Enum):
    MOVING = 'MOVING'
    DIGGING = 'DIGGING'


class Worker(Sprite):
    # Set up the player
    MASS = 2.0
    MAX_HORIZONTAL_SPEED = 400
    MAX_VERTICAL_SPEED = 300
    MOVE_FORCE = 4000

    def __init__(self):
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                         scale=0.4)
        self.direction = 1
        self.engine = None
        self.bounce_source = None
        self.strength = 5
        self.state = WorkerState.MOVING
        self.digging_target = None

    def start_digging(self, tile):
        self.state = WorkerState.DIGGING
        self.engine.set_friction(self, 10)
        self.digging_target = tile

    def stop_digging(self):
        self.state = WorkerState.MOVING
        self.engine.set_friction(self, 0)

    def flip_direction(self, source):
        if self.bounce_source is None or self.bounce_source.center_x != source.center_x:
            self.bounce_source = source
            self.direction *= -1

    def add_to_physics_engine(self, engine):
        self.engine = engine
        engine.add_sprite(self,
                          friction=0,
                          mass=self.MASS,
                          moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                          collision_type="worker",
                          max_horizontal_velocity=self.MAX_HORIZONTAL_SPEED,
                          max_vertical_velocity=self.MAX_VERTICAL_SPEED)

    def update(self):
        if self.state == WorkerState.MOVING:
            self.engine.apply_force(self, (self.MOVE_FORCE * self.direction, 0))
        else:
            if self.digging_target.hit(self.strength):
                self.state = WorkerState.DIGGING
                self.stop_digging()
