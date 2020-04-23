# write your psudo code here
from typing import List

OPEN_PARAMS = ["{", "[", "("]
CLOSE_PARAMS = ["}", "]", ")"]
PARAMS_DICT = {"{": "}", "[": "]", "(": ")"}


def peek_stack(stack):
    return stack[-1]


def is_well_formed(s: str) -> bool:
    stack = []
    for each_char in list(s):
        if each_char in CLOSE_PARAMS:
            if len(stack) > 0:
                prev_param = peek_stack(stack)
                if PARAMS_DICT[prev_param] == each_char:
                    stack.pop()
                else:
                    return False
            else:
                return False
        else:
            stack.append(each_char)

    return True if len(stack) == 0 else False


print(is_well_formed("()"))
