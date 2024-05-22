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

    def __str__(self):
        nodes = ''
        for i in self.heap_nodes:
            nodes += str(i) + '-'
        return nodes

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

    def max_heapify(self, i: int):
        """
        This function converts a heap tree to maxheap tree in subtree of i
        """
        left = self.left_child(i=i)
        right = self.right_child(i=i)
        if left < self.heap_size and self.heap_nodes[left] > self.heap_nodes[i]:
            largest = left
        else:
            largest = i
        if right < self.heap_size and self.heap_nodes[right] > self.heap_nodes[largest]:
            largest = right
        if largest != i:
            self.heap_nodes[i], self.heap_nodes[largest] = self.heap_nodes[largest], self.heap_nodes[i]
            self.max_heapify(i=largest)

    def build_max_heap(self):
        """Build a max heap of an array"""
        i = self.heap_size // 2
        while i >= 0:
            self.max_heapify(i)
            i -= 1


if __name__ == '__main__':
    pass
