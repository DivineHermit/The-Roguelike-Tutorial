from typing import Set, Iterable, Any

from tcod.console import Console
from tcod.context import Context

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        # store passed data/objects for later use
        self.entities = entities
        # reference to the EventHandler for determining actions
        self.event_handler = event_handler
        # separate reference of the player for easier access
        self.player = player

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
            # handle 'MovementAction'
            if isinstance(action, MovementAction):
                # move the player
                self.player.move(dx=action.dx, dy=action.dy)
            # handle 'EscapeAction' (for now quit/could be a menu)
            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        """
        The display portion of the game loop, now as its own method.

        :param console:
        :param context:
        :return: None
        """
        # loop through all the entities
        for entity in self.entities:
            # and place them on the console
            console.print(entity.x, entity.y, entity.char, entity.color)
        # update the screen so we can see them
        context.present(console)
        # clear console to prevent 'trailing'
        console.clear()
