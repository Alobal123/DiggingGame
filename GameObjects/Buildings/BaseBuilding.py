from arcade import SpriteList

from GameObjects.Buildings.AbstractBuilding import AbstractBuilding
from GameObjects.Worker import Worker
from Physics import Physics


class BaseBuilding(AbstractBuilding):
    SPAWN_RATE = 500

    def __init__(self, x, y, physics_engine: Physics, worker_list: SpriteList):
        self.path = ":resources:images/tiles/doorClosed_mid.png"
        self.scale = 0.5

        self.spawn_rate = 0

        self.physics_engine = physics_engine
        self.worker_list = worker_list
        super().__init__(x, y)

    def spawn_worker(self):
        worker = Worker()
        worker.center_x = self.center_x
        worker.center_y = self.center_y
        worker.add_to_physics_engine(self.physics_engine)
        self.worker_list.append(worker)

    def update(self):
        if self.spawn_rate == 0:
            self.spawn_worker()
            self.spawn_rate = self.SPAWN_RATE
        else:
            self.spawn_rate -= 1
