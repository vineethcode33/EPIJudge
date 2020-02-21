from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.

    all_primes = []
    is_prime = [False, False] + [True] * (n-1)

    for each in range(2, n+1):
        if is_prime[each]:
            all_primes.append(each)
            for every_multiple in range(each, n+1, each):
                is_prime[every_multiple] = False
    return all_primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
