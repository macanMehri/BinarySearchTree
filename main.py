from binary_search_tree import BinarySearchTree, Node
from max_heap import MaxHeap
from constants import MENU
import numpy as np


def create_binary_search_tree():
    """A function to create a binary search tree"""
    try:
        root_data = int(input('Please enter value of the root: '))
    except ValueError as err:
        print(err)
    else:
        binary_search_tree = BinarySearchTree(root=Node(data=root_data, left_child=None, right_child=None))


def create_heap():
    """A function to create max heap"""
    data = list()
    while True:
        number = input('Please enter a number or end: ')
        if number == 'end':
            break
        elif number.isnumeric():
            data.append(int(number))
        else:
            print('This value is not allowed! Please try again later.')
    heap = MaxHeap(heap_nodes=np.array(data))
    heap.build_max_heap()
    return heap


if __name__ == '__main__':
    try:
        while True:
            print(MENU)
            order = int(input('Please enter your order: '))
            if order == 1:
                max_heap = create_heap()
                print(max_heap)
            if order == 2:
                create_binary_search_tree()
            if order == 0:
                break
    except ValueError as error:
        print('ValueError:', error)
    except AttributeError as error:
        print('AttributeError:', error)
