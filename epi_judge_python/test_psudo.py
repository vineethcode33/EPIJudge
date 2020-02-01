# write your psudo code here
from typing import List


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    # A - [1, 2, 9]

    carry_over = 0
    first = True
    last = False
    return_array = []

    for each in range(1, len(A)+1):

        last = True if each == len(A) else False

        if first:
            carry_over = 1 if A[each*-1]+1 > 9 else 0
            insert_element = 0 if carry_over == 1 else A[each*-1]+1
            return_array.insert(0, insert_element)
            first = False

        else:
            temp_carry_over = 1 if A[each*-1] + carry_over > 9 else 0
            insert_element = 0 if A[each*-1] + \
                carry_over > 9 else A[each*-1]+carry_over
            return_array.insert(0, insert_element)

            carry_over = temp_carry_over

        if last and carry_over == 1:
            return_array.insert(0, 1)
    return return_array


print(plus_one([9, 9, 9]))
