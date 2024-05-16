from typing import Any


class Node:
    """A class for BST tree nodes"""
    def __init__(self, data: Any, left_child, right_child, parent):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def __str__(self) -> str:
        return f'({self.data})'


class BinarySearchTree:
    """
    A class for binary search tree or BST.
    BST is a data structure which is not a complete binary tree.
    The right child is greater than the parent and the parent is greater than the left child.
    Uses linked lists to store data.
    Use this data structure for searching or sorting.
    """
    def __init__(self, root_data: Any):
        self.root = Node(
            data=root_data,
            left_child=None,
            right_child=None,
            parent=None,
        )

    def insert_node(self, data: Any) -> None:
        """Insert new node to the tree in the right place"""
        z = Node(
            data=data,
            left_child=None,
            right_child=None,
            parent=None,
        )
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left_child
            else:
                x = x.right_child
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left_child = z
        else:
            y.right_child = z

    def inorder_tree_walk(self, node: Node) -> None:
        """
        Inorder tree walk is a tree walk with this order:
        Left child - Root - Right child
        Due to the nature of the binary search tree (BST) with this tree walk the output is in order
        """
        if node is not None:
            self.inorder_tree_walk(node=node.left_child)
            print(node)
            self.inorder_tree_walk(node=node.right_child)


if __name__ == '__main__':
    pass
