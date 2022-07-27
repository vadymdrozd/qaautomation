def vacation_type(func):
    def wrapper(name, surname, vacation_start, vacation_end):
        func(name, surname, vacation_start, vacation_end)
        print(f'Hi John,\n'
              f'I need the paid vacations from {vacation_start} to {vacation_end}.\n'
              f'{name} {surname}')
    return wrapper


def sick_leave_type(func):
    def wrapper(name, surname, vacation_start, vacation_end):
        func(name, surname, vacation_start, vacation_end)
        print(f'Hi John,\n'
              f'I need the paid sick leave from {vacation_start} to {vacation_end}.\n'
              f'{name} {surname}')
    return wrapper


def day_off_type(func):
    def wrapper(name, surname, vacation_start, vacation_end):
        func(name, surname, vacation_start, vacation_end)
        print(f'Hi John,\n'
              f'I need the paid day off from {vacation_start} to {vacation_end}.\n'
              f'{name} {surname}')
    return wrapper
