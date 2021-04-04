# Python 3 Roguelike Tutorial
# http://rogueliketutorials.com/tutorials/tcod/v2/part-1/

import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    """  """
    # console screen size
    screen_width = 80
    screen_height = 50

    # map size
    map_width = 80
    map_height = 45

    # dungeon room data
    room_size_max = 10
    room_size_min = 6
    max_rooms = 30

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

    # create an instance of the GameMap
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_size_min=room_size_min,
        room_size_max=room_size_max,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

    # create game engine for event handling and rendering
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

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
            # handle game display
            engine.render(console=root_console, context=context)
            # get game events
            events = tcod.event.wait()
            # handle events and determine actions
            engine.handle_events(events)


if __name__ == "__main__":
    main()
