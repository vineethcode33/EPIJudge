from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    OPERATORS = {
        "+": lambda y, x: x+y,
        "-": lambda y, x: x-y,
        "*": lambda y, x: x*y,
        "/": lambda y, x: int(x/y)
    }

    for each in expression.split(","):

        if each in OPERATORS:
            stack.append(OPERATORS[each](stack.pop(), stack.pop()))
        else:
            stack.append(int(each))
    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
