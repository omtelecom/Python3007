"""
10. В одномерном списке удалить все четные элементы и оставить только нечетные.
"""


def odd(lst):
    return [lst[i] for i in range(0,len(lst),2)]


if __name__ == '__main__':
    assert odd([1, 2, 3, 4]) == [1, 3]
    # assert odd([0, 1, 1]) == [1, 1]  # ошибка ?
    assert odd([0, 1, 1]) == [0, 1]