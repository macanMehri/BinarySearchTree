import numpy as np


class MaxHeap:
    """
    A class for max heap objects
    Max heap is a data structure which is a complete binary tree
    Parents are always greater than the children
    Uses arrays to store data
    """
    def __init__(self, heap_nodes: np.array):
        self.heap_nodes = heap_nodes
        self.heap_size = len(heap_nodes)

    @staticmethod
    def left_child(i: int) -> int:
        """
        This method returns the index of the left child of i.
        i: Is given index of a node in max heap tree.
        return: Index of left child.
        """
        return 2 * i + 1

    @staticmethod
    def right_child(i: int) -> int:
        """
        This method returns the index of the right child of i.
        i: Is given index of a node in max heap tree.
        return: Index of right child.
        """
        return 2 * i + 2

    @staticmethod
    def parent(i: int) -> int:
        """
        This method returns the index of the parent of i.
        i: Is given index of a node in max heap tree.
        return: Index of parent.
        """
        # Because our array indexes are starting with 0 we need to add a unit to it
        # Then after division subtract one unit from it
        i += 1
        i //= 2
        return i - 1


if __name__ == '__main__':
    pass
