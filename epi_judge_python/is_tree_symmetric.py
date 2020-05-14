from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def check_symmetric(left_tree, right_subtree):

        if not left_tree and not right_subtree:
            return True
        elif left_tree and right_subtree:
            return (left_tree.data == right_subtree.data)\
                and check_symmetric(left_tree.left, right_subtree.right)\
                and check_symmetric(left_tree.right, right_subtree.left)
        return False
    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
