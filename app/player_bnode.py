class PlayerBNode:
    """
        Represent Player Binary search tree Node

        Attributes
        ----------
        player : Player
            Player class
        left :
            left child of Node
        previous :
            right child of Node
    """
    def __init__(self, player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, value):
        self._left = value

    @right.setter
    def right(self, value):
        self._right = value
