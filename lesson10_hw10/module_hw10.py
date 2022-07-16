# Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
# Повернути колекцію, кожен член якої є перетвореним членом вхідної колекції.


def multiplication_on_two(argument):
    return [arg * 2 for arg in argument]


def dividing_on_two(argument):
    return [arg / 2 for arg in argument]


def pseudo_map(func, collection):
    return func(collection)
