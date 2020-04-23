"""
Without knowing the length of a linked list, it is not trivial to delete the kth last element in a singly
linked list.
Given a singly linked list and an integer k, write a program to remove the kth last element from the
list. Your algorithm cannot use more than a few words of storage, regardless of the length of the
list. In particular, you cannot assume that it is possible to record the length of the list.

"""


from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    head = ListNode(0, L)
    first_list = head.next

    for _ in range(k):
        first_list = first_list.next

    second_list = head

    while first_list:
        first_list, second_list = first_list.next, second_list.next

    second_list.next = second_list.next.next
    print(head.next)
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
