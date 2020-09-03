from typing import List

from test_framework import generic_test, test_utils

MAPPING = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TOV", "WXYZ")


def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    def mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonic.append("".join(partial_result))
            return
        for each in MAPPING[int(phone_number[digit])]:
            partial_result[digit] = each
            mnemonic_helper(digit+1)

    mnemonic = []
    partial_result = [0] * len(phone_number)
    mnemonic_helper(0)
    return mnemonic


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
