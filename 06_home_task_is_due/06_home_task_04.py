"""
4. В списке найти минимальный и максимальный элементы, поменять их местами.
"""


def change_max_min(lst):
    i, j = [f(range(len(lst))) for f in [min, max]]
    lst[i], lst[j] =  lst[j], lst[i]

    return lst


if __name__ == '__main__':
    assert change_max_min([1, 2, 3]) == [3, 2, 1]
    assert change_max_min([1, 1, 1]) == [1, 1, 1]
    assert change_max_min([2, 2, 1]) == [1, 2, 2]