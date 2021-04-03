# Python 3 Roguelike Tutorial
# http://rogueliketutorials.com/tutorials/tcod/v2/part-1/

import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


def main() -> None:
    """  """
    # console screen size
    screen_width = 80
    screen_height = 50

    # load image with the tileset to be used (I stored this in a 'data' folder)
    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # create an event handler
    event_handler = EventHandler()

    # create entities: player & npc
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', (255, 255, 0))
    entities = {npc, player}

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
            # display the player '@' on screen using its data
            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            # update the screen so we can actually see the player
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
                    player.move(dx=action.dx, dy=action.dy)
                # handle 'EscapeAction' (for now quit/could be a menu)
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
