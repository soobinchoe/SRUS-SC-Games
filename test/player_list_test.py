import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()
        self.player_node1 = PlayerNode(Player("1", "soobin1"))
        self.player_node2 = PlayerNode(Player("2", "soobin2"))
        self.player_node3 = PlayerNode(Player("3", "soobin3"))
        self.player_node4 = PlayerNode(Player("4", "soobin4"))
        self.player_list.insert_at_end(self.player_node1)
        self.player_list.insert_at_end(self.player_node2)
        self.player_list.insert_at_end(self.player_node3)

    def test_insert_at_start(self):
        self.player_list.insert_at_start(self.player_node4)
        self.assertEqual(self.player_list.head, self.player_node4)

    def test_insert_at_end(self):
        self.player_list.insert_at_end(self.player_node4)
        self.assertEqual(self.player_list.tail, self.player_node4)

    def test_delete_at_start(self):
        self.player_list.delete_at_start()
        self.assertEqual(self.player_list.head, self.player_node2)

    def test_delete_at_end(self):
        self.player_list.delete_at_end()
        self.assertEqual(self.player_list.tail, self.player_node2)

    def test_delete_with_key(self):
        self.player_list.delete_with_key("2")
        self.assertNotEqual(self.player_node1.next, self.player_node2)
        self.assertEqual(self.player_node1.next, self.player_node3)
