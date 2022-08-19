import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

tuid1 = "1"
tname1 = "soobin1"
tuid2 = "2"
tname2 = "soobin2"
tuid3 = "3"
tname3 = "soobin3"


class TestPlayer(unittest.TestCase):
    def test_insert_at_start(self):
        player1 = Player(tuid1, tname1)
        player2 = Player(tuid2, tname2)
        player_list = PlayerList()
        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)
        player_list.insert_at_start(player_node1)
        player_list.insert_at_start(player_node2)
        self.assertEqual(player_list.head, player_node2)

    def test_insert_at_end(self):
        player1 = Player(tuid1, tname1)
        player2 = Player(tuid2, tname2)
        player_list = PlayerList()
        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)
        player_list.insert_at_end(player_node1)
        player_list.insert_at_end(player_node2)
        self.assertEqual(player_list.tail, player_node2)

    def test_delete_at_start(self):
        player_list = PlayerList()
        player_node1 = PlayerNode(Player(tuid1, tname1))
        player_node2 = PlayerNode(Player(tuid2, tname2))
        player_node3 = PlayerNode(Player(tuid3, tname3))
        player_list.insert_at_end(player_node1)
        player_list.insert_at_end(player_node2)
        player_list.insert_at_end(player_node3)
        player_list.delete_at_start()
        self.assertEqual(player_list.head, player_node2)

    def test_delete_at_end(self):
        player_list = PlayerList()
        player_node1 = PlayerNode(Player(tuid1, tname1))
        player_node2 = PlayerNode(Player(tuid2, tname2))
        player_node3 = PlayerNode(Player(tuid3, tname3))
        player_list.insert_at_end(player_node1)
        player_list.insert_at_end(player_node2)
        player_list.insert_at_end(player_node3)
        player_list.delete_at_end()
        self.assertEqual(player_list.tail, player_node2)


