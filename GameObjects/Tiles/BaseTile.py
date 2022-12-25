import arcade

from GameObjects.Tiles.AbstractTile import AbstractTile


class BaseTile(AbstractTile):
    MAX_HEALTH = 100

    def __init__(self, x, y, scaling):
        super().__init__(x, y, ":resources:images/tiles/grassCenter_round.png", scaling)
        self.health = self.MAX_HEALTH
        self.selected = False

    def unselect(self):
        self.selected = False
        self.color = (255, 255, 255)

    def select(self):
        self.selected = True
        self.color = arcade.color.GINGER

    def on_mouse_press(self):
        if self.selected:
            self.unselect()
        else:
            self.select()

    def hit(self, strength) -> bool:
        self.health -= strength
        if self.health <= 0:
            self.remove_from_sprite_lists()
            return True
        return False

    def can_be_building_foundation(self):
        return not self.selected

    def add_to_physics(self, physics):
        physics.add_sprite(self,
                           friction=0.4,
                           collision_type="tile",
                           body_type=arcade.PymunkPhysicsEngine.STATIC
                           )
