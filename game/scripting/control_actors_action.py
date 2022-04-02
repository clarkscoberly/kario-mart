import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cart import Cart


class ControlActorsAction(Action):
    """
    An input action that controls the cart.
    
    The responsibility of ControlActorsAction is to get the direction and move the cart's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        direction_one = Point(0, 0)
        
        carts = cast.get_actors("carts")
        player_one = carts[0]
        player_two = carts[1]
        player_three = carts[2]
        # player_four = carts[3]
        
        # left
        if self._keyboard_service.is_key_down('a'):
            direction_one = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            direction_one = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            direction_one = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            direction_one = Point(0, constants.CELL_SIZE)
        
        # Drop bomb
        if self._keyboard_service.is_key_down('q'):
            powerup = player_one.get_powerup()
            if powerup is not None:
                powerup_action = powerup.get_action()
                script.add_action("update", powerup_action)
            
        player_one.turn_cart(direction_one)

        # ------------------------------------------------------------------------------------------
        direction_two = Point(0, 0)

        # left
        if self._keyboard_service.is_key_down('j'):
            direction_two = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            direction_two = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            direction_two = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            direction_two = Point(0, constants.CELL_SIZE)
        
        # Drop bomb
        if self._keyboard_service.is_key_down('u'):
            powerup = player_two.get_powerup()
            if powerup is not None:
                powerup_action = powerup.get_action()
                powerup_action.set_owner(player_two)
                script.add_action("update", powerup_action)

        player_two.turn_cart(direction_two)


        # ------------------------------------------------------------------------------------------


        # left
        if self._keyboard_service.is_key_down('c'):
            direction_three = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('b'):
            direction_three = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('g'):
            direction_three = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('v'):
            direction_three = Point(0, constants.CELL_SIZE)
        
        # Drop bomb
        if self._keyboard_service.is_key_down('f'):
            powerup = player_three.get_powerup()
            if powerup is not None:
                powerup_action = powerup.get_action()
                powerup_action.set_owner(player_three)
                script.add_action("update", powerup_action)

        player_three.turn_cart(direction_three)


        # ------------------------------------------------------------------------------------------

        # # left
        # if self._keyboard_service.is_key_down('i'):
        #     direction_two = Point(-constants.CELL_SIZE, 0)
        
        # # right
        # if self._keyboard_service.is_key_down('p'):
        #     direction_two = Point(constants.CELL_SIZE, 0)
        
        # # up
        # if self._keyboard_service.is_key_down('0'):
        #     direction_two = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service.is_key_down('o'):
        #     direction_two = Point(0, constants.CELL_SIZE)
        
        # # Drop bomb
        # if self._keyboard_service.is_key_down('9'):
        #     powerup = player_four.get_powerup()
        #     if powerup is not None:
        #         powerup_action = powerup.get_action()
        #         powerup_action.set_owner(player_four)
        #         script.add_action("update", powerup_action)

        # player_four.turn_cart(direction_two)