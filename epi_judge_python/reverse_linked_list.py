
"""
1->2->3->4->None
None<-1<-2<-3<-4

prev = None
---------------
next = current.next
current.next = prev
prev = current
current = next
"""


from list_node import ListNode
from test_framework import generic_test


def reverse_linked_list() -> ListNode:
    A = [1, 2, 3, 4]
    dummy_head = linked_list = ListNode(0)
    for each in A:
        linked_list.next = ListNode(each)
        linked_list = linked_list.next
    dummy_head = dummy_head.next
    # # dummy_reverse = list_head = ListNode(0, dummy_head)

    prev = None
    current = dummy_head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    dummy_head = prev

    return dummy_head


if __name__ == "__main__":
    reverse_linked_list()
