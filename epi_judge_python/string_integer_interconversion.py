"""
Implement an integer to string conversion function, and a string to integer conversison function,
For example, if the input to the first function is the integer 314,it should retum the string "31.4" and
if the input to the second function is the string "314" it should return the integer 314.

Raises:
    TestFailure: [description]
    TestFailure: [description]

Returns:
    [type] -- [description]
"""


from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    return str(x)


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    return int(s)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
