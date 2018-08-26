"""
12. Дан список значений. Превратить список в словарь
поочередно превращая елменты в ключи и значения.
[1, 2, 3, 4, 5, 6] -> {1: 2, 3: 4, 5: 6}

"""


def list_to_dict(lst):
    return {lst[i - 1]:lst[i] for i in range(1,len(lst),2)}


if __name__ == '__main__':
    assert list_to_dict([1, 2, 3, 4, 5]) == {1: 2, 3: 4}
    assert list_to_dict(['k', 'v', 'k2', 'v2']) == {'k': 'v', 'k2': 'v2'}