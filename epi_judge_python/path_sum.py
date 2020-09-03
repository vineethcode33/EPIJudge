from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if not tree:
        return False

    if not tree.left and not tree.right:
        return remaining_weight == tree.data

    isLeft = has_path_sum(tree.left, remaining_weight - tree.data)
    isRight = has_path_sum(tree.right, remaining_weight-tree.data)
    return isLeft or isRight


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
