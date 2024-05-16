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
    def left_child(i):
        """This method returns the index of the left child of i"""
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        """This method returns the index of the right child of i"""
        return 2 * i + 2


if __name__ == '__main__':
    pass
