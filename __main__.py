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

    player_one = Cart('Player 1')
    player_one.set_position(Point(5, 5).scale(constants.CELL_SIZE))
    player_one.set_color(constants.BLUE)
    player_one.set_text("O")

    player_two = Cart('Player 2')
    player_two.set_position(Point(35, 5).scale(constants.CELL_SIZE))
    player_two.set_color(constants.GREEN)
    player_two.set_text("O")
    
    # player_three = Cart('Michelle')
    # player_three.set_position(Point(5, 15).scale(constants.CELL_SIZE))
    # player_three.set_color(constants.YELLOW)
    # player_three.set_text("O")

    # player_four = Cart('Clark')
    # player_four.set_position(Point(35, 15).scale(constants.CELL_SIZE))
    # player_four.set_color(constants.WHITE)
    # player_four.set_text("O")

    cast.add_actor("carts", player_one)
    cast.add_actor("carts", player_two)
    # cast.add_actor("carts", player_three)
    # cast.add_actor("carts", player_four)

    
    #TODO: add font-size
    score_1 = Score()
    score_1.set_position(Point(constants.MAX_X, constants.MAX_Y))
    score_1.set_color(constants.BLUE)
    score_1.set_font_size(constants.FONT_SIZE)
    score_1.set_text("")

    score_2 = Score()
    score_2.set_position(Point(constants.MAX_X, constants.MAX_Y))
    score_2.set_color(constants.GREEN)
    score_2.set_font_size(constants.FONT_SIZE)
    score_2.set_text("")
    
    # score_3 = Score("Player 3")
    # score_3.set_position(Point(constants.MAX_X, constants.MAX_Y))
    # score_3.set_color(constants.GREEN)
    # score_3.set_text("")

    #add scores to cast
    cast.add_actor("scores", score_1)
    cast.add_actor("scores", score_2)
    # cast.add_actor("scores", score_3)

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