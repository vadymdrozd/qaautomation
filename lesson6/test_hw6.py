from hw6_1 import tickets_check

# def years_typer() testing


def test_one_year():
    assert tickets_check(1) == f'Тобі ж 1 рік! Де твої батьки?'


def test_years_with_one():
    for digit in [21, 31, 41, 51, 61]:
        assert tickets_check(digit) == f'Незважаючи на те, що вам {digit} рік, білетів все одно нема!'


def test_from_two_till_four_year():
    for digit in [2, 3, 4]:
        assert tickets_check(digit) == f'Тобі ж {digit} роки! Де твої батьки?'


def test_years_with_two_three_four():
    for digit in [23, 32, 43, 54, 62]:
        assert tickets_check(digit) == f'Незважаючи на те, що вам {digit} роки, білетів все одно нема!'


def test_retired_with_one():
    for digit in [71, 81, 91, 101, 201]:
        assert tickets_check(digit) == f'Вам {digit} рік? Покажіть пенсійне посвідчення!'


def test_repdigit_with_one_or_from_five():
    for digit in (11, 111, 1111, 55, 66, 77, 88, 99):
        assert tickets_check(digit) == f'О, вам {digit} років! Який цікавий вік!'


def test_repdigit_with_two_three_four():
    for digit in (22, 33, 44, 222):
        assert tickets_check(digit) == f'О, вам {digit} роки! Який цікавий вік!'
