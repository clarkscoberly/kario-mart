import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Cart(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cart is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, name):
        super().__init__()
        self._powerups = []
        self._name = name
        
    def add_powerup(self, powerup):
        self._powerups.append(powerup)

    def get_name(self):
        return self._name

    def get_powerup(self):
        if len(self._powerups) > 0:
            return self._powerups.pop(0)
        else:
            return None

    def turn_cart(self, velocity):
        self.set_velocity(velocity)

    def get_score(self):
        return 