import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("1", "b")
        self.player2 = Player("2", "a")
        self.player3 = Player("2", "c")
        self.bst = PlayerBST()
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)

    def test_insert(self):

        self.assertEqual(self.player1, self.bst.root.player)
        self.assertEqual(self.player2, self.bst.root.left.player)
        self.assertEqual(self.player3, self.bst.root.right.player)

    def test_search(self):
        self.assertTrue(self.bst.search("a"))
        self.assertFalse(self.bst.search("d"))
