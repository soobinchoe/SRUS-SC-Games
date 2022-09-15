from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    """
        PlayerList class used to represent Player's List

        Attributes
        ----------
        head : PlayerNode
            the head node of the list
        tail : PlayerNode
            the tail node of the list
        """

    def __init__(self):
        """ This method initialize player list class attributes """
        self.head = None
        self.tail = None

    def insert_at_end(self, new_node: PlayerNode):
        """ This method insert player at the end of the list """
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        prev_node = self.tail
        prev_node.next = new_node

        self.tail = new_node
        self.tail.previous = prev_node

    def insert_at_start(self, new_node: PlayerNode):
        """ This method insert player at the start of the list """
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        next_node = self.head
        next_node.previous = new_node

        self.head = new_node
        self.head.next = next_node

    def delete_at_start(self):
        """ This method delete player from the start of the list """
        if self.is_empty():
            return
        prev_head = self.head
        prev_head.next.previous = None
        self.head = prev_head.next
        prev_head.next = None

    def delete_at_end(self):
        """ This method delete player from the end of the list """
        if self.is_empty():
            return
        prev_tail = self.tail
        prev_tail.previous.next = None
        self.tail = prev_tail.previous
        prev_tail.previous = None

    def delete_with_key(self, key):
        """ This method delete player using provided key """
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
        """ This method display player list by order, forward as default """
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
        """ This method check if the list is empty"""
        if not self.head:
            return True
        return False

    def sort_descending(self):
        """ This method make player list as array list then call sorting method"""
        if self.head == self.tail:
            return

        player_node = self.head
        player_array = []
        while player_node:
            player_array.append(player_node)
            player_node = player_node.next

        self.player_sort(player_array, 0, len(player_array) - 1)
        return player_array

    def player_sort(self, player_array, left, right):
        """ This method sort player array list recursively by quick sort"""
        if left < right:
            pivot = self.partition(player_array, left, right)
            self.player_sort(player_array, left, pivot-1)
            self.player_sort(player_array, pivot+1, right)

    def partition(self, player_array, left, right):
        """ This method swap player order by player score """
        pivot = player_array[right]
        i = (left-1)
        for j in range(left, right):
            if player_array[j].player > pivot.player:
                i += 1
                temp = player_array[i]
                player_array[i] = player_array[j]
                player_array[j] = temp

        temp = player_array[i + 1]
        player_array[i + 1] = player_array[right]
        player_array[right] = temp
        return i + 1
