"""
6. Дан список чисел. Выведите все элементы списка,
которые больше предыдущего элемента.
"""


def get_largest(lst):
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]


if __name__ == '__main__':
    assert get_largest([1, 2, 3, 4]) == [2, 3, 4]
    assert get_largest([2, 3, 100, 4]) == [3, 100]
    assert get_largest([-10, -2, 0, 4]) == [-2, 0, 4]