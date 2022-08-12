class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self.name

    def __iter__(self):
        return (i for i in (self.name, self.uid))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return f"Player {self.name} with id: {self.uid}"


if __name__ == "__main__":
    print(Player("123", "raf"))
