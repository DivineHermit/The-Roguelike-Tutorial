class Action:
    """  """
    pass


class EscapeAction(Action):
    """  """
    pass


class MovementAction(Action):
    """ PLayer movement action """

    def __init__(self, dx: int, dy: int):
        # call __init__ of parent class 'Action'
        super().__init__()
        # store dx & dy as properties for later use

        self.dx = dx
        self.dy = dy
