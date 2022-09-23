from app.player_node import PlayerNode


class PlayerList:
    """
        Represent Player's List

        Attributes
        ----------
        head : PlayerNode
            the head node of the list
        tail : PlayerNode
            the tail node of the list
        """

    def __init__(self):
        """ Initialize head and tail node to None """
        self.head = None
        self.tail = None
        # consider playerlist in init (easy to test)

    def insert_at_end(self, new_node: PlayerNode):
        """ Insert player at the end of the list """
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        prev_node = self.tail
        prev_node.next = new_node

        self.tail = new_node
        self.tail.previous = prev_node

    def insert_at_start(self, new_node: PlayerNode):
        """ Insert player at the start of the list """
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        next_node = self.head
        next_node.previous = new_node

        self.head = new_node
        self.head.next = next_node

    def delete_at_start(self):
        """ Delete player from the start of the list """
        if self.is_empty():
            return
        prev_head = self.head
        prev_head.next.previous = None
        self.head = prev_head.next
        prev_head.next = None

    def delete_at_end(self):
        """ Delete player from the end of the list """
        if self.is_empty():
            return
        prev_tail = self.tail
        prev_tail.previous.next = None
        self.tail = prev_tail.previous
        prev_tail.previous = None

    def delete_with_key(self, key):
        """ Delete player using provided key """
        if self.is_empty():
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
        """ Display player list by order, forward as default """
        if self.is_empty():
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
        """ Check if the list is empty"""
        if not self.head:
            return True
        return False


