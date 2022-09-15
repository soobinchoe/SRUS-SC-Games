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
        self.player4 = Player("4", "soobin4")
        self.player5 = Player("5", "soobin5")
        self.player6 = Player("6", "soobin6")
        self.player_list.insert_at_end(PlayerNode(self.player1))
        self.player_list.insert_at_end(PlayerNode(self.player2))
        self.player_list.insert_at_end(PlayerNode(self.player3))
        self.player_list.insert_at_end(PlayerNode(self.player4))
        self.player_list.insert_at_end(PlayerNode(self.player5))
        self.player_list.insert_at_end(PlayerNode(self.player6))
        self.player1.score = 10
        self.player2.score = 30
        self.player3.score = 20
        self.player4.score = 70
        self.player5.score = 10
        self.player6.score = 50

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


