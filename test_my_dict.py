"""
The tests are the comparison between behaviour of python dict and MyDict.

In each test, result is asserted with sorted() because MyDict doesn't
keep the insertion order.
"""

from my_dict import MyDict


def _initialize_dicts():
    my_dict, python_dict = MyDict(5), {}
    keys_values = [
        ('key1', 1),
        ('key2', 2),
        ('key3', 3),
        ('key3', 4),  # same key as previous
        ('key4', 5),
        ('key5', 6),
        ('key5', 7),  # same key as previous
        ('key6', 8),  # more values than space in MyDict, collision guarantee
    ]
    for key, value in keys_values:
        my_dict[key], python_dict[key] = value, value

    return my_dict, python_dict


def test_keys_method():
    my_dict, python_dict = _initialize_dicts()
    assert sorted(my_dict.keys()) == sorted(python_dict.keys())


def test_values_method():
    my_dict, python_dict = _initialize_dicts()
    assert sorted(my_dict.values()) == sorted(python_dict.values())


def test_items_method():
    my_dict, python_dict = _initialize_dicts()
    assert sorted(my_dict.items()) == sorted(python_dict.items())


def test_eq_method():
    my_dict1, my_dict2 = MyDict(5), MyDict(10)
    keys_values = [
        ('key1', 1),
        ('key2', 2),
        ('key3', 3),
    ]
    for key, value in keys_values:
        my_dict1[key] = value
        my_dict2[key] = value

    assert my_dict1 == my_dict2


def test_ne_method():
    my_dict1, my_dict2 = MyDict(5), MyDict(5)
    my_dict2[1], my_dict2[1] = False, True
    assert my_dict1 != my_dict2
