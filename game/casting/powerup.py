import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class PowerUp(Actor):
    """
    A tasty item that carts like to eat.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Powerup."
        super().__init__()
        self.set_text("?")
        self.set_color(constants.RED)
        self._action = None

    def get_action(self):
        return self._action
    
    def set_action(self, action):
        self._action = action
        