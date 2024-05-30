from typing import Any

import numpy as np

from max_heap import MaxHeap


class Node:
    """A class for BST tree nodes"""
    def __init__(self, data: Any, left_child=None, right_child=None, parent=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def __str__(self) -> str:
        return f'({self.data})'

    def __gt__(self, other):
        """Compare two nodes check if first one is greater than second one or not"""
        if self.data > other.data:
            return True
        return False

    def __lt__(self, other):
        """Compare two nodes check if first one is lower than second one or not"""
        if self.data < other.data:
            return True
        return False

    def __eq__(self, other):
        """Compare two nodes check if first one is as equal as the second one or not"""
        if self.data == other.data:
            return True
        return False


class BinarySearchTree:
    """
    A class for binary search tree or BST.
    BST is a data structure which is not a complete binary tree.
    The right child is greater than the parent and the parent is greater than the left child.
    Uses linked lists to store data.
    Use this data structure for searching or sorting.
    """
    def __init__(self, root: Node):
        self.root = root

    def __str__(self):
        pass

    def __add__(self, other):
        """
        When you add two binary search trees this would happen.
        First the new tree is the first one then each level we add the root of the other tree.
        Then we delete the others root until the other tree is finished
        """
        first_tree = self
        second_tree = other

        while second_tree.root is not None:
            first_tree.insert_node(second_tree.root.data)
            second_tree.delete(second_tree.root)
        return first_tree

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
        elif u == u.parent.left_child:
            u.parent.left_child = v
        else:
            u.parent.right_child = v
        if v is not None:
            v.parent = u.parent

    def delete(self, node: Node) -> None:
        """Delete the node from the tree"""
        if node is None:
            return
        if node.left_child is None:
            self.transplant(node, node.right_child)
        elif node.right_child is None:
            self.transplant(node, node.left_child)
        else:
            y = self.tree_minimum(node=node.right_child)
            if y.parent != node:
                self.transplant(y, y.right_child)
                y.right_child = node.right_child
                y.right_child.parent = y
            self.transplant(node, y)
            y.left_child = node.left_child
            y.left_child.parent = y

    def reset_bst(self) -> None:
        """
        This function reset the binary search tree by reset the root
        Make roots left and right child none
        """
        self.root.left_child = None
        self.root.right_child = None

    def add_to_max_heap(self, count: int):
        """Take top count the highest numbers of bst and store them to max-heap"""
        if count <= 0:
            return
        maximum = self.tree_maximum(self.root)
        list_of_top_count = list()
        list_of_top_count.append(maximum)
        count -= 1
        node = maximum
        while count > 0:
            next_node = self.tree_predecessor(node=node)
            list_of_top_count.append(next_node)
            node = next_node
            count -= 1

        array_of_top_count = np.array(list_of_top_count)

        heap = MaxHeap(array_of_top_count)
        heap.build_max_heap()
        return heap


if __name__ == '__main__':
    pass
