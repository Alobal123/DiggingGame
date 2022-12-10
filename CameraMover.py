from pyglet.math import Vec2


class CameraMover:
    IS_MOVING = False
    SPEED = 4
    MAX_SPEED = 15
    MAX_SCROLL_HORIZONTAL = 500
    MAX_SCROLL_VERTICAL = 500

    def __init__(self, camera_sprite, game_width, game_height, window):
        self.direction = Vec2(0, 0)
        self.camera_sprite = camera_sprite
        self.game_width = game_width
        self.game_height = game_height
        self.window = window

    def get_x(self):
        return self.camera_sprite.position.x

    def get_y(self):
        return self.camera_sprite.position.y

    def start_moving(self, direction):
        self.direction = direction
        self.IS_MOVING = True

    def stop_moving(self):
        self.IS_MOVING = False
        self.SPEED = 4

    def move(self):
        dx = self.camera_sprite.position.x + self.SPEED * self.direction.x
        dy = self.camera_sprite.position.y + self.SPEED * self.direction.y

        if dx < -self.game_width / 2 - self.window.SIDE_OFFSET:
            dx = self.camera_sprite.position.x
        if dx > self.game_width / 2 - self.window.width + self.window.SIDE_OFFSET:
            dx = self.camera_sprite.position.x
        if dy < -self.game_height / 2 - self.window.BOTTOM_OFFSET:
            dy = self.camera_sprite.position.y
        if dy > self.game_height / 2 - self.window.height + self.window.TOP_OFFSET:
            dy = self.camera_sprite.position.y

        if self.IS_MOVING:
            self.camera_sprite.move_to(Vec2(dx, dy), 1)
            if self.SPEED < self.MAX_SPEED:
                self.SPEED += .7
