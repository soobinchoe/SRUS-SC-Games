from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Player:
    """
    Represent Player

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
        """ initialize id and name with arguments received, password as None, score to 0 """
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
        """ Iterate player"""
        return (i for i in (self.name, self.uid))

    def __str__(self):
        """ Shows class attribute with defined format """
        return f"Player name : {self.name} & id: {self.uid}"

    def add_password(self, password: str):
        """ Add password to player class using hashing """
        ph = PasswordHasher()
        self._password = ph.hash(password)

    def verify_password(self, password: str):
        """ Verify password to player class using hashing """
        ph = PasswordHasher()
        try:
            return ph.verify(self._password, password)
        except VerifyMismatchError:
            return False

    @score.setter
    def score(self, value):
        """ Set score value to player """
        if value > 0:
            self._score = value

    def __eq__(self, other):
        """ Compare if other player's score is equal to current player """
        return self._score == other.score

    def __ge__(self, other):
        """ Compare if other player's score is greater than or equal to current player """
        return self._score >= other.score

    def __le__(self, other):
        """ Compare if other player's score is less than or equal to current player """
        return self._score <= other.score

    def __lt__(self, other):
        """ Compare if other player's score is less than current player """
        return self._score < other.score

    def __gt__(self, other):
        """ Compare if other player's score is greater than current player """
        return self._score > other.score

    @staticmethod
    def transfer_array(player_list):
        """ Make player list as array list """
        if player_list.head == player_list.tail:
            return

        player_node = player_list.head
        player_array = []
        while player_node:
            player_array.append(player_node)
            player_node = player_node.next

        return player_array

    @staticmethod
    def sort_descending(player_list):
        """ Call transfer array list method then call sorting method"""
        try:
            player_array = Player.transfer_array(player_list)
        except AttributeError:
            player_array = player_list

        Player.player_sort(player_array, 0, len(player_array) - 1)
        return player_array

    @staticmethod
    def player_sort(player_array, left, right):
        """ Sort player array list recursively by quick sort"""
        if left < right:
            pivot = Player.partition(player_array, left, right)
            Player.player_sort(player_array, left, pivot - 1)
            Player.player_sort(player_array, pivot + 1, right)

    @staticmethod
    def partition(player_array, left, right):
        """ Swap player order by player score """
        pivot = player_array[right]
        i = (left - 1)
        for j in range(left, right):
            if player_array[j].player > pivot.player:
                i += 1
                temp = player_array[i]
                player_array[i] = player_array[j]
                player_array[j] = temp

        temp = player_array[i + 1]
        player_array[i + 1] = player_array[right]
        player_array[right] = temp
        return i + 1


if __name__ == "__main__":
    player = Player("123", "soobin")
    player.add_password("hello1234")
    # player.verify_password("hello1234")
    print(str(player.verify_password("hello1234")))
