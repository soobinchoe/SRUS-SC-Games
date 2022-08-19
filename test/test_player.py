import unittest

from app.player import Player

tuid = "123"
tname = "soobin"


class TestPlayer(unittest.TestCase):
    def testPlayerString(self):
        player = Player(tuid, tname)
        self.assertIn(tuid, str(player))
        self.assertIn(tname, str(player))
