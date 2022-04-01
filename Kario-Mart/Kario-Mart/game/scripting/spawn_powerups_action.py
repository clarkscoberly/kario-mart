import datetime
import random 

from game.scripting.grow_cart_action import GrowCartAction
from game.scripting.action import Action
from game.casting.powerup import PowerUp
from game.shared.point import Point
import constants

class SpawnPowerupsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def __init__(self, audio_service, video_service):
        self._start_time = datetime.datetime.now()
        self._max_powerups = constants.NUMBER_OF_POWERUPS
        self._video_service = video_service
        self._audio_service = audio_service
        # TODO list of possible powerup actions (about) line 43
        
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        num_powerups = len(cast.get_actors("powerups"))
        if num_powerups < self._max_powerups:
            now = datetime.datetime.now()
            if ((now - self._start_time).total_seconds() > 2.0):
                # need to tell it what action to execute
  
                x = random.randint(0, constants.COLUMNS)
                y = random.randint(0, constants.ROWS)
                position = Point(x, y).scale(constants.CELL_SIZE)
                
                powerup = PowerUp()
                powerup.set_position(position)
                # TODO: change this to randomly select the powerup action to apply
                powerup.set_action(GrowCartAction(self._audio_service, self._video_service))
                cast.add_actor("powerups", powerup)

                self._start_time = now

