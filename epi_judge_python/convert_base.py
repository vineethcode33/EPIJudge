"""
Write a program that performs base conversion. The input is a string, an integer b1, and another
integer b2. The string represents an integer in base br. The output should be the string representing
the integer in base 02. Assume 2 < bt,b2 < 16. Use " N' to represent L0, "B" for 1.L,.. ., and "F" fot
15. (For example, if the string is "61.5", h is 7 and bz is 13, then the result should be "1A7", since
6x72 +1x7 + 5 = 1x 132 +70xL3+7.)

Returns:
    [type] -- [description]
"""


from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    return ''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
