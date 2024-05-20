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

    @staticmethod
    def tree_minimum(node: Node) -> Node:
        """
        Find the node with the minimum data in the tree.
        It should be the leftest node in the tree due to the nature of the binary search tree (BST).
        Parameter node should be the root of the subtree you want to search in.
        """
        while node.left_child is not None:
            node = node.left_child
        return node

    @staticmethod
    def tree_maximum(node: Node) -> Node:
        """
        Find the node with the maximum data in the tree.
        It should be the rightest node in the tree due to the nature of the binary search tree (BST).
        Parameter node should be the root of the subtree you want to search in.
        """
        while node.right_child is not None:
            node = node.right_child
        return node

    def tree_successor(self, node: Node) -> Node:
        """
        Find the next node of the parameter node
        """
        if node.right_child is not None:
            return self.tree_minimum(node.right_child)
        y = node.parent

        while y is not None and node is y.right_child:
            node = y
            y = node.parent
        return y

    def tree_predecessor(self, node: Node) -> Node:
        """
        Find the previous node of the parameter node
        """
        if node.left_child is not None:
            return self.tree_maximum(node.left_child)
        y = node.parent

        while y is not None and node is y.left_child:
            node = y
            y = node.parent
        return y

    def transplant(self, u: Node, v: Node):
        """Exchanges two subtrees"""
        if u.parent is None:
            self.root = v
        elif u is u.parent.left_child:
            u.parent.left_child = v
        else:
            u.parent.right_child = v
        if v is not None:
            v.parent = u.parent

    def delete(self, node: Node) -> None:
        """Delete the node from the tree"""
        if node.left_child is None:
            self.transplant(node, node.right_child)
        elif node.right_child is None:
            self.transplant(node, node.left_child)
        else:
            y = self.tree_minimum(node=node.right_child)
            if y.parent is not node:
                self.transplant(y, y.right_child)
                y.right_child = node.right_child
                y.right_child.parent = y
            self.transplant(node, y)
            y.left_child = node.left_child
            y.left_child.parent = y


if __name__ == '__main__':
    pass
