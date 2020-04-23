"""
Write a program which takes a singly linked list L and two integers "s" and "f" as
arguments, and reverses the order of the nodes from the "sth" node to "fth" node,
inclusive. The numbering begins at 1., i.e., the head node is the first node. Do not allocate additional nodes.

Returns:
    [type] -- [description]
"""

from typing import Optional
from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    list_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return list_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
