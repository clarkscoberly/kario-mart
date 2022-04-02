import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.powerup import PowerUp

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cart collides
    with the powerup, or the cart collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        
    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_powerup_collision(cast)
            self._handle_game_over(cast)

    def _handle_powerup_collision(self, cast):
        """Updates the score nd moves the powerup if the cart collides with the powerup.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        powerups = cast.get_actors("powerups")
        carts = cast.get_actors("carts")
        
        for cart in carts:
            for powerup in powerups:
                if cart.get_position().equals(powerup.get_position()):
                    print("\n\n\n", cart, "\n\n\n")
                    powerup.get_action().set_owner(cart)
                    cart.add_powerup(powerup)
                    cast.remove_actor("powerups", powerup)
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cart and powerup white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cart = cast.get_first_actor("carts")
            segments = cart.get_segments()
            powerup = cast.get_first_actor("powerups")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            powerup.set_color(constants.WHITE)