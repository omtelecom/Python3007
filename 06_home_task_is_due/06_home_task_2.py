"""
2. Найти сумму положительных элементов списка.
"""


def sum_of_positives(lst):
    return sum([i for i in lst if i >=0])


if __name__ == '__main__':
    assert sum_of_positives([1, 2, -4, 0]) == 3
    assert sum_of_positives([-1, -2, -3]) == 0
    assert sum_of_positives([1, 1, 1]) == 3