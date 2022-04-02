import constants


from game.casting.cast import Cast
from game.casting.powerup import PowerUp
from game.casting.score import Score
from game.casting.cart import Cart
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.spawn_powerups_action import SpawnPowerupsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()

    player_one = Cart('Grant')
    player_one.set_position(Point(10, 10).scale(constants.CELL_SIZE))
    player_one.set_color(constants.BLUE)
    player_one.set_text("O")

    player_two = Cart('Dallin')
    player_two.set_position(Point(30, 10).scale(constants.CELL_SIZE))
    player_two.set_color(constants.GREEN)
    player_two.set_text("O")
    
    cast.add_actor("carts", player_one)
    cast.add_actor("carts", player_two)
    # cast.add_actor("carts", player_three)
    # cast.add_actor("carts", player_four)

    score_1 = Score()
    score_1.set_position(Point(constants.MAX_X, constants.MAX_Y))
    score_1.set_color(constants.BLUE)
    score_1.set_text("Score: ")
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    audio_service = AudioService()
    audio_service.initialize()
    audio_service.load_sounds("assets")

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", SpawnPowerupsAction(audio_service, video_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()