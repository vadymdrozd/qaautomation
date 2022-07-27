from hw5_1 import arg_type
from hw5_2 import float_convert
from hw5_3 import multi_func

# hw5_1 tests


def test_int_arg_type():
    assert arg_type(3) == int


def test_float_arg_type():
    assert arg_type(3.1) == float


def test_bool_arg_type():
    assert arg_type(True) == bool


def test_str_arg_type():
    assert arg_type('str') == str


def test_list_arg_type():
    assert arg_type([1, 2, 2, 3]) == list


def test_tuple_arg_type():
    assert arg_type((1, 2, 2, 3)) == tuple


def test_set_arg_type():
    assert arg_type({1, 2, 2, 3}) == set


def test_dict_arg_type():
    assert arg_type({1: 2, 2: 3}) == dict


# hw5_2 tests


def test_positive_float_convert():
    for arg in (1, 1.0, '1.0', True):
        assert float_convert(arg) == 1.0


def test_negative_float_convert():
    for arg in ('asdf', {1: 3}, (1, 2), [2, 3, 4], {1, 2, 3}, None, False):
        assert float_convert(arg) == 0.0


# hw5_3 tests


def test_int_multi_func():
    assert multi_func(5, 1) == 4


def test_float_multi_func():
    assert multi_func(5.0, 1.0) == 4


def test_str_multi_func():
    assert multi_func('5.0 ', '1.0') == '5.0 1.0'


def test_dict_multi_func():
    assert multi_func('5.0', 1.0) == {'5.0': 1.0}


def test_other_multi_func():
    assert multi_func(None, True) == (None, True)
