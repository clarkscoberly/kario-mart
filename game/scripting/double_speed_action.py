# import constants
from game.scripting.action import Action
from game.casting.score import Score
from game.shared.point import Point
import constants
import datetime


class DoubleSpeedAction(Action):
    """
    An update action that increases a player's speed.
    
    The responsibility of DoubleSpeedAction is to increase the speed of the cart
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


        now = datetime.datetime.now()
        x = cart.get_x()
        y = cart.get_y()
        velocity = Point(x * constants.MODIFIER, y * constants.MODIFIER).scale(constants.CELL_SIZE) 
        if ((now - self._start_time).total_seconds() > 2.0):
            cart.set_velocity(velocity)
            script.remove_action("update", self) #might not need this. experiment with taking it out


        


        # Flashes the background color to the cart which used a powerup
        if self._executed == False:
            self._start_time = datetime.datetime.now()
            self._video_service.change_background(cart.get_color())
            self._audio_service.play_sound("assets\\explosion.wav")
            # TODO have actor color swapped to something different to have it still be visible
            
            # TODO: always change this for the specific kind of powerup action
            # -------------------------------------------------------------------------------------
            print(f"increased the speed of {name}'s cart!")
            # -------------------------------------------------------------------------------------
            
            self._executed = True

        # Returns the color to it's original color
        now = datetime.datetime.now()
        if ((now - self._start_time).total_seconds() > 1.0):
            self._video_service.change_background(constants.BLACK)
            script.remove_action("update", self)
            # TODO have actor color swap back to original color



    # def _increase_velocity(self):
    #         x = velocity.get_x*constants.MODIFIER
    #         y = velocity.get_y*constants.MODIFIER
    #         velocity = Point(x,y).scale(constants.CELL_SIZE) 
