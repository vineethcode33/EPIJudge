""" 5.12 Sample offline data
This problem is motivated by the need for a company to select a random subset of its customers to
roll out a new feature to. For example, a social networking company may want to see the effect of
a new UI on page visit duration without taking the chance of alienating all its users if the rollout is
unsuccessful.
Implement an algorithm that takes as input an array of distinct elements and a size, and returns
a subset of the given size of the array elements. All subsets should be equally likely. Retum the
result in input array itself.
Hint: How would you construct a random subset of size k + 1 given a random subset of size k?

Returns:
    [type] -- [description]
"""

import functools
from typing import List
import random
from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_sampling(k: int, A: List[int]) -> None:
    # TODO - you fill in here.
    # print(A)
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    # print(A)
    # print("======================")
    return A


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
