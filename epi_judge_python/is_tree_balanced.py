from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import namedtuple


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    isBalanced_height = namedtuple("isBalanced_height", ("balanced", "height"))

    def check_balanced(tree):
        if not tree:
            return isBalanced_height(True, -1)

        left_status = check_balanced(tree.left)
        if not left_status.balanced:
            return isBalanced_height(False, 0)

        right_status = check_balanced(tree.right)
        if not right_status.balanced:
            return isBalanced_height(False, 0)

        isBalanced = abs(left_status.height - right_status.height) <= 1
        height = max(left_status.height, right_status.height) + 1
        return isBalanced_height(isBalanced, height)

    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
