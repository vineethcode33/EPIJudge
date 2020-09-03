from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    def perm_helper(idx):
        if idx == len(A)-1:
            result.append(A.copy())
        for j in range(idx, len(A)):
            A[idx], A[j] = A[j], A[idx]
            perm_helper(idx + 1)
            A[idx], A[j] = A[j], A[idx]
        return

    result = []
    perm_helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
