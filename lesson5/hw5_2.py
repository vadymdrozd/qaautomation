# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).

def float_convert(argument):
    try:
        return float(argument)
    except:
        return 0.0
