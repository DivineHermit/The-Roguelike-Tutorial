from typing import Set, Iterable, Any

from tcod.console import Console
from tcod.context import Context
from tcod.map import compute_fov

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        # store passed data/objects for later use
        self.entities = entities
        # reference to the EventHandler for determining actions
        self.event_handler = event_handler
        # reference to the game map
        self.game_map = game_map
        # separate reference of the player for easier access
        self.player = player
        # update the field of view
        self.update_fov()

    def handle_events(self, events: Iterable[Any]) -> None:
        """
        The event handling portion of the game loop, now as its own method.

        :param events: an Iterable of game events
        :return: None
        """
        for event in events:
            # determine the action by passing an event to the 'EventHandler'
            action = self.event_handler.dispatch(event)
            # if no valid actions exist keep looping
            if action is None:
                continue
            # perform actions
            action.perform(self, self.player)
            # update the FOV before the players next action.
            self.update_fov()

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles['transparent'],
            (self.player.x, self.player.y),
            radius=8
        )
        # If a tile is 'visible' it should be added to 'explored'.
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        """
        The display portion of the game loop, now as its own method.

        :param console:
        :param context:
        :return: None
        """
        # draw the game map on screen
        self.game_map.render(console)
        # loop through all the entities
        for entity in self.entities:
            # Only print entities that are in the FOV.
            if self.game_map.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, entity.color)
        # update the screen so we can see them
        context.present(console)
        # clear console to prevent 'trailing'
        console.clear()
