"""
Найти номер и значение первого положительного элемента списка.
"""


def find_first_positive(lst):
    for i, j in enumerate(lst):
        if j > 0:
            return i, j


if __name__ == '__main__':
    # some tests
    assert find_first_positive([-1, 2, 5]) == (1, 2)
    assert find_first_positive([1, 2, 5]) == (0, 1)
    assert find_first_positive([-1, -2, 5]) == (2, 5)
    assert find_first_positive([-1, -2, -5]) is None
