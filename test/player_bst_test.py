import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def test_insert(self):
        player = Player("1", "soobin1")
        bst = PlayerBST()
        bst.insert(player)
        self.assertEqual(player, bst.root.player)