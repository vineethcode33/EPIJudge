"""5.18

Returns:
    [type] -- [description]
"""

from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:

    def clock_wise_elements(offset):
        if offset == len(square_matrix) - offset - 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset: -1 - offset])

        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset: -1 - offset])
        spiral_ordering.extend(
            square_matrix[-1 - offset][-1 - offset:offset: -1])

        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering: List[int] = []

    for offset in range((len(square_matrix)+1) // 2):
        clock_wise_elements(offset)

    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
