"""
Write a program that takes two lists, assumed to be sorted, and returns their merge.
The only field your program can change in a node is its next field.

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'data', 'next']

Returns:
    [type] -- [description]
"""

from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    temp_list_head = temp_list_tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            temp_list_tail.next, L1 = L1, L1.next
        else:
            temp_list_tail.next, L2 = L2, L2.next
        temp_list_tail = temp_list_tail.next
    temp_list_tail.next = L1 or L2
    return temp_list_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
