from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Player:
    def __init__(self, uid: str, name: str):
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
        return (i for i in (self.name, self.uid))

    def __str__(self):
        return f"Player name : {self.name} & id: {self.uid}"

    def add_password(self, password: str):
        ph = PasswordHasher()
        self._password = ph.hash(password)

    def verify_password(self, password: str):
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
