from argon2 import PasswordHasher

""" This module provide Hash function for hashing password"""
from argon2.exceptions import VerifyMismatchError
""" This module verify password """


class Player:
    """
    Player class userd to represent Player

    Attributes
    ----------
    uid : str
        the id of user
    name : str
        the name of user
    password : str
        the password for user
    """
    def __init__(self, uid: str, name: str):
        """ This method initialize player class attributes """
        self._uid = uid
        self._name = name
        self._password = None
        self._score = 0

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def __iter__(self):
        """ This method iterate player"""
        return (i for i in (self.name, self.uid))

    def __str__(self):
        """ This method shows class attribute with defined format """
        return f"Player name : {self.name} & id: {self.uid}"

    def add_password(self, password: str):
        """ This method add password to player class using hashing """
        ph = PasswordHasher()
        self._password = ph.hash(password)

    def verify_password(self, password: str):
        """ This method verify password to player class using hashing """
        ph = PasswordHasher()
        try:
            return ph.verify(self._password, password)
        except VerifyMismatchError:
            return False

    @score.setter
    def score(self, value):
        """ This method set score value to player """
        if value > 0:
            self._score = value

    def __eq__(self, other):
        """ This method is to compare if other player's score is equal to current player """
        return self._score == other.score

    def __ge__(self, other):
        """ This method is to compare if other player's score is greater than or equal to current player """
        return self._score >= other.score

    def __le__(self, other):
        """ This method is to compare if other player's score is less than or equal to current player """
        return self._score <= other.score

    def __lt__(self, other):
        """ This method is to compare if other player's score is less than current player """
        return self._score < other.score

    def __gt__(self, other):
        """ This method is to compare if other player's score is greater than current player """
        return self._score > other.score


if __name__ == "__main__":
    player = Player("123", "soobin")
    player.add_password("hello1234")
    # player.verify_password("hello1234")
    print(str(player.verify_password("hello1234")))
