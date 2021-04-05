from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    """
    EventHandler subclasses tcod's EventDispatch class
    allowing us to send events to methods based on
    the type of event.
    """

    def ev_quit(self, event: "tcod.event.Quit") -> Optional[Action]:
        """ Handle quit events like clicking a windows 'X' button. """
        raise SystemExit

    def ev_keydown(self, event: "tcod.event.KeyDown") -> Optional[Action]:
        """
        Receive key press events and return an 'Action' or None
        if no valid key was pressed

        :param event: a key press
        :return: and 'Action' or None
        """
        #  action will default to None or be assigned an 'Action'
        action: Optional[Action] = None
        # key holds which key was pressed (doesn't include modifiers like shift or alt
        key = event.sym
        # create a 'MovementAction' with the desired direction
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
        # if the 'escape' key is pressed return an 'EscapeAction'
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # no valid key was pressed (returns None)
        return action
