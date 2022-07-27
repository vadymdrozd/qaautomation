from datetime import date
from module_hw9 import Human

vadim = Human('Vadim', 'Drozd', 'male', birthday=date(1990, 9, 5))
kateryna = Human('Kateryna', 'Belkovych', 'female', birthday=date(1995, 9, 8))


def test_age_property():
    assert vadim.age == 31
    assert kateryna.age == 26


def test_eat():
    assert vadim.eat() == f'Vadim is eating'
    assert kateryna.eat() == f'Kateryna is eating'


def test_sleep():
    assert vadim.sleep() == f'Vadim is sleeping'
    assert kateryna.sleep() == f'Kateryna is sleeping'


def test_speak():
    assert vadim.speak() == f'Vadim is speaking'
    assert kateryna.speak() == f'Kateryna is speaking'


def test_go():
    assert vadim.go() == f'Vadim is going'
    assert kateryna.go() == f'Kateryna is going'


def test_stand():
    assert vadim.stand() == f'Vadim is standing'
    assert kateryna.stand() == f'Kateryna is standing'


def test_lie():
    assert vadim.lie() == f'Vadim is lying'
    assert kateryna.lie() == f'Kateryna is lying'