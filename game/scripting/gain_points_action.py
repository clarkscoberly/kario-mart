from game.scripting.action import Action
from game.casting.score import Score
import constants
import datetime


class GainPointsAction(Action):
    """
    An update action that increases a player's points.
    
    The responsibility of GainPointsAction is to increase the points of the cart
    that hits a powerup with this action.
    """

    def __init__(self, audio_service, video_service):
        super().__init__()
        self._audio_service = audio_service
        self._video_service = video_service
        self._start_time = datetime.datetime.now()
        self._executed = False

    def execute(self, cast, script):
        """Executes the gain points action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cart = self.get_owner()
        name = cart.get_name()
        opponents = cast.get_actors("scores")
        for opponent in opponents:
            opponent.add_points(45)
       
       
       
        # scores = cast.get_actors("scores")
        # for score in scores:
        #     if name == "Player 1":
        #         player_score = cast.get_actor("scores", score)
        #         points_1 = player_score.add_points(50)
        #         print('\n\n This is working: Otherwise something has gone horribly horribly awry. \n\n')
        #         return points_1
        #     if name == "Player 2":
        #         player_score = cast.get_actor("scores", score)
        #         points_2 = player_score.add_points(50)
        #         return points_2


        # Flashes the background color to the cart which used a powerup
        if self._executed == False:
            self._start_time = datetime.datetime.now()
            self._video_service.change_background(cart.get_color())
            self._audio_service.play_sound("assets\\mk64_mario_a11.wav")
            # TODO have actor color swapped to something different to have it still be visible
            
            # TODO: always change this for the specific kind of powerup action
            # -------------------------------------------------------------------------------------
            # print(f"increased the {points_1} points of {name}'s cart!")
            # -------------------------------------------------------------------------------------
            
            self._executed = True

        # Returns the color to it's original color
        now = datetime.datetime.now()
        if ((now - self._start_time).total_seconds() > 1.0):
            self._video_service.change_background(constants.BLACK)
            script.remove_action("update", self)
            # TODO have actor color swap back to original color


