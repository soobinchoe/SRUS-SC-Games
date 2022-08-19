from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.is_empty_bool = True

    def insert_at_end(self, new_node: PlayerNode):
        self.is_empty(new_node)

        prev_node = self.tail
        prev_node.next = new_node

        self.tail = new_node
        self.tail.previous = prev_node

    def insert_at_start(self, new_node: PlayerNode):
        self.is_empty(new_node)

        next_node = self.head
        next_node.previous = new_node

        self.head = new_node
        self.head.next = next_node

    def delete_at_start(self):
        if self.is_empty_bool:
            print("Nothing on the List")
            return
        prev_head = self.head
        prev_head.next.previous = None
        self.head = prev_head.next
        prev_head.next = None

    def delete_at_end(self):
        if self.is_empty_bool:
            print("Nothing on the List")
            return
        prev_tail = self.tail
        prev_tail.previous.next = None
        self.tail = prev_tail.previous
        prev_tail.previous = None

    def is_empty(self, player_node: PlayerNode):
        if not self.head:
            self.head = player_node
            self.tail = player_node
            self.is_empty_bool = False
            return


if __name__ == "__main__":
    list1 = PlayerList()
    node = PlayerNode(Player("1", "player1"))
    node2 = PlayerNode(Player("2", "player2"))
    node3 = PlayerNode(Player("3", "player3"))
    list1.insert_at_start(node)
    list1.insert_at_start(node2)
    list1.insert_at_start(node3)
    list1.delete_at_start()
    print(list1.head)
