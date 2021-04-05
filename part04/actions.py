from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    """  """

    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Perform this action with the objects needed to determine its scope.

        :param engine: is the scope this action is being performed in.
        :param entity: is the object performing the action.
        :return: None
        """
        raise NotImplementedError()


class EscapeAction(Action):
    """ Action to quit the game """

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MovementAction(Action):
    """ PLayer movement action """

    def __init__(self, dx: int, dy: int):
        # call __init__ of parent class 'Action'
        super().__init__()
        # store dx & dy as properties for later use

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        # check if movement is valid: in the game map & is walkable
        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.
        if not engine.game_map.tiles['walkable'][dest_x, dest_y]:
            return  # Destination is blocked by a tile.
        # movement is valid so move
        entity.move(self.dx, self.dy)
