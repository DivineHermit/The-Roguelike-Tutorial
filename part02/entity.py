from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        # store passed data for later use, starting with x & y coordinates
        self.x = x
        self.y = y
        # followed by the character to display e.g. '@' for the player
        self.char = char
        # finally a tuple with the RGB color values in it
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # move the entity by given amount
        self.x += dx
        self.y += dy
