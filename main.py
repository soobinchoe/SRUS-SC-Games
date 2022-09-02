from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


def main():
    player1 = Player("1", "player1")
    node = PlayerNode(player1)
    player_list = PlayerList()
    player_list.insert_at_start(node)

    print(player1)
    print(node)
    print(player_list)


if __name__ == "__main__":
    main()
