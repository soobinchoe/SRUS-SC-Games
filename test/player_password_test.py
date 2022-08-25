import unittest

from app.player import Player

tuid = "123"
tname = "soobin"
tpassword = "test1234"


class TestPassword(unittest.TestCase):
    def test_add_password(self):
        player = Player(tuid, tname)
        player.add_password(tpassword)
        self.assertTrue(tpassword, player.add_password(tpassword))

    def test_verify_password(self):
        player = Player(tuid, tname)
        player.add_password(tpassword)
        self.assertTrue(player.verify_password(tpassword))
