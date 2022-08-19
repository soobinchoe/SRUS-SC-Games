import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

tuid1 = "123"
tname1 = "soobin"
tuid2 = "1234"
tname2 = "soobin2"


class TestPlayer(unittest.TestCase):
    def test_player_node_insert_at_start(self):
        player1 = Player(tuid1, tname1)
        player2 = Player(tuid2, tname2)
        player_list = PlayerList()
        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)
        player_list.insert_at_start(player_node1)
        player_list.insert_at_start(player_node2)
        self.assertEqual(player_list.head, player_node2)

    def test_player_node_insert_at_end(self):
        player1 = Player(tuid1, tname1)
        player2 = Player(tuid2, tname2)
        player_list = PlayerList()
        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)
        player_list.insert_at_end(player_node1)
        player_list.insert_at_end(player_node2)
        self.assertEqual(player_list.tail, player_node2)
