from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack, prev, result = [tree], None, []

    while stack:
        curr = stack[-1]

        if not prev or prev.left is curr or prev.right is curr:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
            else:
                result.append(curr.data)
                stack.pop()
        elif curr.left is prev:
            if curr.right:
                stack.append(curr.right)
            else:
                result.append(curr.data)
                stack.pop()
        else:
            result.append(curr.data)
            stack.pop()
        prev = curr
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
