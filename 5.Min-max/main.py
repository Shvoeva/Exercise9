def min(*args, key=None):
    min_val = None
    if len(args) == 1:
        iterable = args[0]
    else:
        iterable = args

    for val in iterable:
        if min_val is None or (key(val) if key else val) < (key(min_val) if key else min_val):
            min_val = val

    return min_val


def max(*args, key=None):
    max_val = None
    if len(args) == 1:
        iterable = args[0]
    else:
        iterable = args

    for val in iterable:
        if max_val is None or (key(val) if key else val) > (key(max_val) if key else max_val):
            max_val = val

    return max_val

if __name__ == '__main__':
    assert max(3, 2) == 3
    assert min(3, 2) == 2
    assert max([1, 2, 0, 3, 4]) == 4
    assert min("hello") == "e"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6
    assert min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]

