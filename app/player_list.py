from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, new_node: PlayerNode):
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        prev_node = self.tail
        prev_node.next = new_node

        self.tail = new_node
        self.tail.previous = prev_node

    def insert_at_start(self, player_node: PlayerNode):
        if not self.head:
            self.head = player_node
            self.tail = player_node
            return

        next_node = self.head
        next_node.previous = player_node

        self.head = player_node
        self.head.next = next_node



if __name__ == "__main__":
    list1 = PlayerList()
    node = PlayerNode(Player("1", "player1"))
    node2 = PlayerNode(Player("2", "player2"))
    node3 = PlayerNode(Player("3", "player3"))
    list1.insert_at_start(node)
    list1.insert_at_start(node2)
    list1.insert_at_start(node3)
    print('hithere')
    print(node3)
