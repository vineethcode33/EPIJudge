from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import namedtuple


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    BalancedWithHeight = namedtuple(
        "BalancedWithHeight", ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedWithHeight(True, -1)

        left_status = check_balanced(tree.left)

        if not left_status.balanced:
            return BalancedWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedWithHeight(False, 0)

        height = max(left_status.height, right_result.height)+1
        is_balanced = abs(left_status.height - right_result.height) <= 1
        return BalancedWithHeight(is_balanced, height)
    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
