# Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
# Повернути колекцію, кожен член якої є перетвореним членом вхідної колекції.


def multiplication_on_two(argument):
    return argument * 2


def dividing_on_two(argument):
    return argument / 2


def pseudo_map(func, collection):
    return [func(arg) for arg in collection]