from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def check_symmetric(left_node, right_node):
        if not left_node and not right_node:
            return True
        elif left_node and right_node:
            return ((left_node.data == right_node.data) and check_symmetric(left_node.right, right_node.left) and check_symmetric(left_node.left, right_node.right))
        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
