from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        """ Initialize root node to None """
        self.root = None

    def insert(self, player: Player):
        """ Set root & Call _insert method """
        if not self.root:
            self.root = PlayerBNode(player)
            return

        self._insert(player, self.root)

    def _insert(self, player, current_node: PlayerBNode):
        """ Insert player to BST recursively by comparing key """
        key = player.name
        if key < current_node.player.name:
            if not current_node.left:
                current_node.left = PlayerBNode(player)
            else:
                self._insert(player, current_node.left)
        elif key > current_node.player.name:
            if not current_node.right:
                current_node.right = PlayerBNode(player)
            else:
                self._insert(player, current_node.right)
