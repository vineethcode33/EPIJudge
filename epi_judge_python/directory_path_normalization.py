from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    OPERATORS = [".", ".."]
    stack = []
    for each in path.split("/"):
        if each in OPERATORS:
            if each == "..":
                if len(stack) > 0 and stack[-1] not in OPERATORS:
                    stack.pop()
                else:
                    stack.append(each)
        elif len(each) > 0:
            stack.append(each)

    short_path = "/".join(stack)

    if path[0] == "/":
        short_path = "/"+short_path

    return short_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
