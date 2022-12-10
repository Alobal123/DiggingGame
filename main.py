import arcade

from GameView import GameView
from Level import Level

DEFAULT_SCREEN_WIDTH = 1100
DEFAULT_SCREEN_HEIGHT = 600

SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"


class MyGame(arcade.Window):
    """ Main application class. """

    BOTTOM_OFFSET = 200
    SIDE_OFFSET = 200

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True, fullscreen=True)
        self.TOP_OFFSET = self.height - 300


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    level = Level(16, 17)
    start_view = GameView(window, level)
    start_view.setup()
    window.show_view(start_view)

    arcade.run()


if __name__ == "__main__":
    main()
