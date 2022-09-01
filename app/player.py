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

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

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


if __name__ == "__main__":
    player = Player("123", "soobin")
    player.add_password("hello1234")
    # player.verify_password("hello1234")
    print(str(player.verify_password("hello1234")))
