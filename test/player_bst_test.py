import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def test_insert(self):
        player1 = Player("1", "b")
        player2 = Player("2", "a")
        player3 = Player("2", "c")
        bst = PlayerBST()
        bst.insert(player1)
        bst.insert(player2)
        bst.insert(player3)
        self.assertEqual(player1, bst.root.player)
        self.assertEqual(player2, bst.root.left.player)
        self.assertEqual(player3, bst.root.right.player)
