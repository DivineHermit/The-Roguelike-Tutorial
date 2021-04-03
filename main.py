# Python 3 Roguelike Tutorial
# http://rogueliketutorials.com/tutorials/tcod/v2/part-1/

import tcod


def main() -> None:
    """  """
    # console screen size
    screen_width = 80
    screen_height = 50

    # load image with the tileset to be used (I stored this in a 'data' folder)
    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

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
            root_console.print(x=40, y=25, string="@")
            # update the screen so we can actually see the '@'
            context.present(root_console)
            # event handling: wait for some user input and loop through each 'event'
            for event in tcod.event.wait():
                # if the console is closed
                if event.type == "QUIT":
                    # tell Python to quit
                    raise SystemExit()


if __name__ == "__main__":
    main()
