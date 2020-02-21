"""[summary]
Sudoku is a popular logic-based combinatorial number placement puzzle. The objective is to fill
a 9 x 9 grid with digits subject to the constraint that each column, each row, and each of the nine
3 x 3 sub-grids that compose the grid contains unique integers in [1,9]. The grid is initialized with
a partial assignment as shown in Figure 5.2(a); a complete solution is shown in Figure 5.2(b).

Check whether a 9 x9 2D array representing a partially completed Sudoku is valid. Specifically,
check that no row, column, or 3 x 3 2D subarray contains duplicates. A O-value in the 2D array
indicates that entry is blank; every other entry is in [1,9].
Returns:
    [type] -- [description]
"""


from typing import List
from collections import Counter

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    """           0  1  2  3  4  5  6  7  8

            0    [0, 0, 0, 0, 0, 0, 0, 0, 0],
            1    [0, 0, 0, 0, 0, 0, 0, 0, 0],
            2    [0, 0, 0, 0, 0, 1, 2, 0, 0],
            3    [0, 0, 0, 0, 6, 0, 4, 0, 0],
            4    [0, 0, 0, 2, 0, 0, 0, 0, 5],
            5    [7, 0, 0, 0, 0, 0, 0, 0, 0],
            6    [0, 8, 3, 0, 0, 0, 0, 0, 0],
            7    [0, 0, 0, 0, 0, 0, 3, 3, 0],
            8    [0, 0, 4, 0, 0, 0, 0, 0, 0]
    """
    def check_for_dups(input_list):
        if len([item for item, count in Counter(input_list).items() if count > 1 and item != 0]) > 0:
            return False
        else:
            return True

    # check row
    for each in partial_assignment:
        if not check_for_dups(each):
            return False

    # check column
    for each in list(zip(*partial_assignment)):
        if not check_for_dups(each):
            return False

    # check for 3 X 3
    for offset in range(0, 9, 3):
        for outer_offset in range(0, 9, 3):
            test_list = []
            for inner_offset in range(3):
                test_list.extend(
                    partial_assignment[offset:offset + 3][inner_offset][outer_offset: outer_offset+3])
            if not check_for_dups(test_list):
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
