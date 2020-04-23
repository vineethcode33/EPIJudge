"""
Write a Program that takes two cycle-free singly linked lists, and determines if
there exists a node that is common to both lists.

"""

import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # TODO - you fill in here.

    def get_length(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    lenght_node_zero = get_length(l0)
    lenght_node_one = get_length(l1)

    if lenght_node_zero > lenght_node_one:
        l0, l1 = l1, l0

    for _ in range(abs(lenght_node_one-lenght_node_zero)):
        l1 = l1.next

    while l1 and l0 and l1 is not l0:
        l1, l0 = l1.next, l0.next

    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
