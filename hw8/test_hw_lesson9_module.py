from hw_lesson9_module import Vehicle

test_auto1 = Vehicle('Subaru', 'Impreza', 2007, 60, 240, 7)
test_auto1.tank_level = 0
test_auto1.odometer_value = 100000

test_auto2 = Vehicle('Subaru', 'Impreza', 2007, 60, 240, 7)
test_auto2.tank_level = 20
test_auto2.odometer_value = 110000


def test_refueling():
    assert test_auto1.refueling() == f'There were 60 liters refueled'
    assert test_auto2.refueling() == f'There were 40 liters refueled'


def test_get_tank_level():
    assert test_auto1.get_tank_level() == 60
    assert test_auto2.get_tank_level() == 60


def test_get_mileage():
    assert test_auto1.get_mileage() == 100000
    assert test_auto2.get_mileage() == 110000


def test_race():
    assert test_auto1.race(100) == {
                                    'Race distance': 100,
                                    'Remaining fuel': 53,
                                    'Tavel time': '31 minutes'
                                }


def test_lend_fuel():
    assert test_auto1.lend_fuel(test_auto2) == f'Дякую, бро, виручив. Ти залив мені 7.0 літрів пального'


def test_long_race():
    assert test_auto2.race(900) == {
                                    'Race distance': 757.1428571428571,
                                    'Remaining fuel': 0,
                                    'Tavel time': '236 minutes'
                                }


def test_lend_fuel_from_empty():
    assert test_auto1.lend_fuel(test_auto2) == 'Нічого страшного, якось розберуся'


def test_get_mileage_after_trips():
    assert test_auto1.get_mileage() == 100100
    assert test_auto2.get_mileage() == 110757.14285714286
