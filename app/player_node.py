from app.player import Player


class PlayerNode:
    """
            PlayerList class userd to represent Player's List

            Attributes
            ----------
            player : Player
                Player class
            next :
                pointer of next node
            previous :
                pointer of previous node
            """
    def __init__(self, player: Player):
        """ This method initialize player node class attributes """
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @next.setter
    def next(self, value):
        self._next = value

    @previous.setter
    def previous(self, value):
        self._previous = value

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"{self._player}"

    def __lt__(self, other):
        return self.player.score < other.player.score
