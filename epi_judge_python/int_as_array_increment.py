from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    # A - [1, 2, 9]

    carry_over = 0
    first = True
    for each in reversed(A):
        each = each+carry_over
        if first:
            if int(each+1) == 10:
                carry_over = 1

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
