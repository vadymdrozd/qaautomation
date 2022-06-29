# Напишіть функцію, що приймає два аргументи. Функція повинна:
# a. якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
# b. якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# c. якщо перший - строка, а другий - ні - повернути dict де ключ це перший аргумент, а значення - другий
# d. у будь-якому іншому випадку повернути кортеж з цих аргументів

def multi_func(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 - arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    elif isinstance(arg1, str) and type(arg2) is not str:
        return {arg1: arg2}
    else:
        return arg1, arg2
