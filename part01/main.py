# Python 3 Roguelike Tutorial
# http://rogueliketutorials.com/tutorials/tcod/v2/part-1/

import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    """  """
    # console screen size
    screen_width = 80
    screen_height = 50

    # player location variables: use of int() prevents floats being returned from division

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # load image with the tileset to be used (I stored this in a 'data' folder)
    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # create an event handler
    event_handler = EventHandler()

    # create the console window, set the tileset & title
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Yet Another Roguelike Tutorial",
            vsync=True,
    ) as context:

        # create and size a 'console' to draw too &
        # tell numpy to use [x,y] instead of [y,x] by setting 'order' to 'F'
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # the game loop
        while True:
            # place an '@' on screen at the location of x & y
            root_console.print(player_x, player_y, string="@")
            # update the screen so we can actually see the '@'
            context.present(root_console)
            # clear console to prevent 'trailing'
            root_console.clear()
            # event handling: wait for some user input and loop through each 'event'
            for event in tcod.event.wait():
                # pass the event to our 'EventHandler'
                action = event_handler.dispatch(event)
                # if no valid actions exist keep looping
                if action is None:
                    continue
                # handle 'MovementAction'
                if isinstance(action, MovementAction):
                    # move the player
                    player_x += action.dx
                    player_y += action.dy
                # handle 'EscapeAction' (for now quit/could be a menu)
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
