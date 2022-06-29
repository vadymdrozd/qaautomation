# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).

def float_convert(argument):
    try:
        if isinstance(argument, bool):
            raise ValueError
        float_argument = float(argument)
        return float_argument
    except (TypeError, ValueError):
        return 0.0
