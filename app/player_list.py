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

    def insert_at_start(self, new_node: PlayerNode):
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        next_node = self.head
        next_node.previous = new_node

        self.head = new_node
        self.head.next = next_node

    def delete_at_start(self):
        if self.is_empty():
            print("Nothing")
            return
        prev_head = self.head
        prev_head.next.previous = None
        self.head = prev_head.next
        prev_head.next = None

    def delete_at_end(self):
        if self.is_empty():
            print("Nothing on the List")
            return
        prev_tail = self.tail
        prev_tail.previous.next = None
        self.tail = prev_tail.previous
        prev_tail.previous = None

    def delete_with_key(self, key):
        if self.is_empty():
            print("Nothing on the List")
            return
        player_node = self.head
        while player_node.next:
            if player_node.player.uid == key:
                prev_node = player_node.previous
                next_node = player_node.next
                player_node.next.previous = prev_node
                player_node.previous.next = next_node
                return
            player_node = player_node.next

    def display(self, forward=True):
        if self.is_empty():
            print("Nothing on the List")
            return
        if forward:
            player_node = self.head
            while player_node:
                print(player_node)
                player_node = player_node.next
        elif not forward:
            player_node = self.tail
            while player_node:
                print(player_node)
                player_node = player_node.previous

    def is_empty(self):
        if not self.head:
            return True
        return False


if __name__ == "__main__":
    list1 = PlayerList()
    node = PlayerNode(Player("1", "player1"))
    node2 = PlayerNode(Player("2", "player2"))
    node3 = PlayerNode(Player("3", "player3"))
    list1.insert_at_end(node)
    list1.insert_at_end(node2)
    list1.insert_at_end(node3)
    list1.delete_at_start()

    # list1.is_empty()

    # list1.display(False)
