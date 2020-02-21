from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    # [2, 0, 1, 3]
    # [7, 2, 11, 10, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]
    # [4, 10, 14, 1, 15, 9, 16, 7, 0, 11, 12, 18, 3, 13, 5, 8, 17, 2, 6]

    offset = 0
    while offset < len(A):
        if offset == perm[offset]:
            offset += 1
        else:
            A[offset], A[perm[offset]] = A[perm[offset]], A[offset]
            temp_offset = perm[offset]
            perm[offset], perm[temp_offset] = perm[temp_offset], perm[offset]
    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
