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
        while True:
            bst_order = input('Enter a value to insert node to binary search tree or \'end\' to exit: ')
            if bst_order == 'end':
                break
            elif bst_order.isnumeric():
                binary_search_tree.insert_node(data=int(bst_order))
            else:
                print('This value is not allowed! Please try again.')
        return binary_search_tree


def create_heap():
    """A function to create max heap"""
    data = list()
    while True:
        number = input('Please enter a number or \'end\': ')
        if number == 'end':
            break
        elif number.isnumeric():
            data.append(int(number))
        else:
            print('This value is not allowed! Please try again.')
    new_heap = MaxHeap(heap_nodes=np.array(data))
    new_heap.build_max_heap()
    return new_heap


if __name__ == '__main__':
    # Default value of bst is None until the user create a bst
    bst = None
    try:
        while True:
            print(MENU)
            order = int(input('Please enter your order: '))
            if order == 1:
                max_heap = create_heap()
                print(max_heap)
            if order == 2:
                bst = create_binary_search_tree()
                while True:
                    how_to_show = input('1. Inorder tree walk\n2. Do not show\n: ')
                    if how_to_show == '1':
                        print('Inorder Tree Walk: ', end='')
                        bst.inorder_tree_walk(bst.root)
                        break
                    elif how_to_show == '2':
                        break
                    else:
                        print('This value is not allowed! Please try again.')
            if order == 3:
                if bst is None:
                    print('You should first create a binary search tree to add them to max heap!')
                else:
                    while True:
                        count = input('How many nodes you wish to add to max heap? ')
                        if not count.isnumeric():
                            print('This value is not allowed! Please try again.')
                        elif int(count) <= 0:
                            print('You should enter a number higher than zero!')
                        else:
                            heap = bst.add_to_max_heap(count=int(count))
                            print(heap)
                            break
            if order == 4:
                if bst is None:
                    print('You should first create a binary search tree to see its maximum!')
                else:
                    print(bst.tree_maximum(node=bst.root))
            if order == 5:
                if bst is None:
                    print('You should first create a binary search tree to see its minimum!')
                else:
                    print(bst.tree_minimum(node=bst.root))
            if order == 6:
                if bst is None:
                    print('You should first create a binary search tree to walk into it!')
                else:
                    print('Inorder Tree Walk: ', end='')
                    bst.inorder_tree_walk(node=bst.root)
            if order == 0:
                break
    except ValueError as error:
        print('ValueError:', error)
    except AttributeError as error:
        print('AttributeError:', error)
