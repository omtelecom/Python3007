"""
8. Дан список чисел. Определите, сколько в этом списке элементов,
которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""


def find_largest(lst):
    count = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
    return count


if __name__ == '__main__':
    assert find_largest([1, 2, 1, 3, 2]) == 2
    assert find_largest([1, 2, 3]) == 0
    assert find_largest([1]) == 0