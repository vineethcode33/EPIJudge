from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.

    if not L:
        return L

    even_head, odd_head = ListNode(0), ListNode(0)
    even_odd_list, even_odd = [even_head, odd_head], 0
    while L:
        even_odd_list[even_odd].next = L
        L = L.next
        even_odd_list[even_odd] = even_odd_list[even_odd].next
        even_odd ^= 1
    even_odd_list[1].next = None
    even_odd_list[0].next = odd_head.next
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
