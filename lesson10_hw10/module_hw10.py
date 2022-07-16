# Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
# Повернути колекцію, кожен член якої є перетвореним членом вхідної колекції.


def multiplication_on_two(collection):
    arg_list = []
    for value in collection:
        arg_list.append(value * 2)
    return arg_list


def dividing_on_two(collection):
    arg_list = []
    for value in collection:
        arg_list.append(value / 2)
    return arg_list


def pseudo_map(func, collection):
    return func(collection)
