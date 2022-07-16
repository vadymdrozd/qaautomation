from module_hw10 import pseudo_map
from module_hw10 import dividing_on_two
from module_hw10 import multiplication_on_two


test_collection = [2, 4, 6, 8, 10]


def test_dividing_on_two():
    assert dividing_on_two(4) == 2


def test_multiplication_on_two():
    assert multiplication_on_two(2) == 4


def test_pseudo_map_dividing():
    assert pseudo_map(dividing_on_two, test_collection) == [1, 2, 3, 4, 5]


def test_pseudo_map_multiplication():
    assert pseudo_map(multiplication_on_two, test_collection) == [4, 8, 12, 16, 20]
