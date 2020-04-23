"""
7.3
---
Write a program that takes the head of a singly linked list and retuns null if
there does not exist a cycle, and the node at the start of the cycle, if a cycle
is present, (You do not know the length of the list in advance.)

"""

import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:

    # cycle => head.data == tail.next.data and tail.next != None and
    # tail.net.next.data == head.next.data
    # how to find tail?

    def get_cycle_length(cycle_node):
        start = cycle_node
        cycle_lenght = 0
        while True:
            cycle_lenght += 1
            start = start.next
            if start is cycle_node:
                return cycle_lenght

    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_length = get_cycle_length(slow)
            start_pointer = head
            for _ in range(cycle_length):
                start_pointer = start_pointer.next

            node_finder = head

            while node_finder is not start_pointer:
                node_finder = node_finder.next
                start_pointer = start_pointer.next
            return node_finder
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
