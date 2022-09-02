import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class TestComparisonPlayer(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()
        self.player1 = Player("1", "soobin1")
        self.player2 = Player("2", "soobin2")
        self.player3 = Player("3", "soobin3")
        self.player_list.insert_at_end(PlayerNode(self.player1))
        self.player_list.insert_at_end(PlayerNode(self.player2))
        self.player_list.insert_at_end(PlayerNode(self.player3))
        self.player1.score = 10
        self.player2.score = 20
        self.player3.score = 10

    def test_score_eq(self):
        self.assertTrue(self.player1 == self.player3)

    def test_score_ge(self):
        self.assertTrue(self.player1 >= self.player3)

    def test_score_le(self):
        self.assertTrue(self.player1 <= self.player2)

    def test_score_lt(self):
        self.assertTrue(self.player1 < self.player2)

    def test_score_gt(self):
        self.assertTrue(self.player2 > self.player1)

    def test_sort_descending(self):
        self.player_list.sort_descending()

