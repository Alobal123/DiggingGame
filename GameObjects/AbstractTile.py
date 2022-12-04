from abc import ABC, abstractmethod

from arcade import Sprite


class AbstractTile(Sprite, ABC):

    selected = False
    def on_mouse_press(self):
        pass

    def on_mouse_drag(self):
        pass

