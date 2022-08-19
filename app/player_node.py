from app.player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._previous = None

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"node : {self}"
