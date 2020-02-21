"""[summary]
Write a program that takes two arrays representing integers, and retums an integer representing
their product. For example, since 193707721.x -761838257287 = -147573952589676412927, if
the inputs are (1,9,3,7,0,7,7,2, 1) and (7,6,L,8,3,8,2,5,7,2,8,7), your function should return
(-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1., 2, 9, 2,7).
Returns:
    [type] -- [description]
"""


from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.

    result = []

    def get_num(list_nums):
        num = 0
        for index, number in enumerate(reversed(list_nums)):
            num += (10**index)*abs(number)

        if list_nums[0] < 0:
            num = num*-1
        return num
    int_num1 = get_num(num1)
    int_num2 = get_num(num2)
    result_number = int_num1*int_num2
    for each in str(abs(result_number)):
        result.append(int(each))
    result[0] = -1 * result[0] if result_number < 0 else result[0]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
