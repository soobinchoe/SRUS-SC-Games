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
        else:
            current_node.player.name = key

    def search(self, key):
        """ Check if no root or root is key, otherwise call search method """
        if not self.root or self.root.player.name == key:
            return key

        return self._search(key, self.root)

    def _search(self, key, current_node):
        """ Search through BST using key """
        if key == current_node.player.name:
            return True
        elif key < current_node.player.name and current_node.left:
            return self._search(key, current_node.left)
        elif key > current_node.player.name and current_node.right:
            return self._search(key, current_node.right)
        return False

    def sort_bst(self, root, nodes):
        """ Make array list of bst """
        if not root:
            return

        self.sort_bst(root.left, nodes)
        nodes.append(root)
        self.sort_bst(root.right, nodes)

    def balance_tree(self):
        """ Call sort method and balance method """
        nodes = []
        self.sort_bst(self.root, nodes)

        return self._balance_tree(nodes)

    def _balance_tree(self, nodes):
        """ Make balanced BST """
        if not nodes:
            return None

        mid = len(nodes) // 2
        node = PlayerBNode(nodes[mid])

        node.left = self._balance_tree(nodes[:mid])
        node.right = self._balance_tree(nodes[mid+1:])
        return node

    def pre_order(self, node):
        """ Print balanced Binary Search Tree in Order """
        if not node:
            return
        print(node.player.player.name)
        self.pre_order(node.left)
        self.pre_order(node.right)
