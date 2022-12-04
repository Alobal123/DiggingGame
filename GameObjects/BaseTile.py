import arcade

from GameObjects.AbstractTile import AbstractTile


class BaseTile(AbstractTile):
    MAX_HEALTH = 100

    def __init__(self, scaling):
        super().__init__(":resources:images/tiles/grassCenter_round.png", scaling)
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
