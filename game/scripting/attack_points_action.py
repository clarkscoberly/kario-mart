from game.scripting.action import Action
from game.casting.score import Score
import constants
import datetime


class AttackPointsAction(Action):
    """
    An update action that decreases other player's points.
    
    The responsibility of AttackPointsAction is to decrease the points of all carts except the cart
    that hits a powerup with this action.
    """

    def __init__(self, audio_service, video_service):
        super().__init__()
        self._audio_service = audio_service
        self._video_service = video_service
        self._start_time = datetime.datetime.now()
        self._executed = False

    def execute(self, cast, script):
        """Executes the attack points action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        cart = self.get_owner()
        name = cart.get_name()
        opponents = cast.get_actors("scores")
        for opponent in opponents:
            opponent.add_points(-100)


        # Flashes the background color to the cart which used a powerup
        if self._executed == False:
            self._start_time = datetime.datetime.now()
            self._video_service.change_background(cart.get_color())
            self._audio_service.play_sound("assets\\explosion.wav")
            # TODO have actor color swapped to something different to have it still be visible
            
            # TODO: always change this for the specific kind of powerup action
            # -------------------------------------------------------------------------------------
            print(f"{name} decreased everyone's points by -100")
            # -------------------------------------------------------------------------------------
            
            self._executed = True

        # Returns the color to it's original color
        now = datetime.datetime.now()
        if ((now - self._start_time).total_seconds() > 1.0):
            self._video_service.change_background(constants.BLACK)
            script.remove_action("update", self)
            # TODO have actor color swap back to original color


