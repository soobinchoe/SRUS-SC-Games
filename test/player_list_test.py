import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

tuid = "123"
tname = "soobin"


class TestPlayer(unittest.TestCase):
    def testPlayerNodeHeadIsNotEmpty(self):
        player = Player(tuid, tname)
        player_list = PlayerList()
        player_node = PlayerNode(player)
        player_list.insert(player_node)
        self.assertEqual(player_list.head, player_node)
