from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.head = None

    def insert(self, player_node: PlayerNode):
        if self.is_empty:
            self.head = player_node
            return
        next_node = self.head
        while next_node.next:
            next_node = next_node.next
        next_node.next = player_node

    def is_empty(self):
        return bool(self.head)
