from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    s, result = [], []

    while tree or s:
        if tree:
            result.append(tree.data)
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            tree = tree.right
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
