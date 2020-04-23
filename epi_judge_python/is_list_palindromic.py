"""
Write a program that tests whether a singly linked list is palindromic.

# Notes -> Implementaion thoughts
---------------------------------
1. Two list instances
    one straight another one reversed
    iterate and return False if not equal

"""

from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.

    def reverse_linked_list(dummy_head):
        prev = None
        current = dummy_head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        dummy_head = prev
        return dummy_head

    while L is not None:
        slow, fast = L

        while fast is not None and slow is not None:
            slow, fast = slow.next, fast.next.next

        first_half, second_half = L, reverse_linked_list(slow)

        while second_half and first_half:
            if second_half.data != first_half.data:
                return False
            second_half, first_half = second_half.next, first_half.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
