"""
Write a program which takes as input an array of characters, and removes each 'b' and replaces
each 'a' by two 'd's. Specifically, along with the array, you are provided an integer-valued size. Size
denotes the number of entries of the array that the operation is to be applied to. You do not have
to worry about preserving subsequent entries. For example, if the array is (a,b,a,c, _,...) and the size
is 4, then you can return (d,d,d,d,c). You can assume there is enough space in the array to hold the
final result.

Returns:
    [type] -- [description]
"""
from pprint import pprint
import os
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    add_counter = 0

    for each in range(0, size):
        complete_index = each+add_counter
        if s[complete_index] == "a":
            s[complete_index] = "d"
            s.insert(complete_index+1, "d")
            add_counter += 1
        elif s[complete_index] == "b":
            s.pop(complete_index)
            complete_index -= 1
    return len(s)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
