from vacation_decorators import title

name_input = str(input('Please enter your name: '))
surname_input = str(input('Please enter your surname: '))

vacation_kind_input = None
while True:
    try:
        vacation_kind_input = int(input('Please choose kind of vacation you want (enter a number)? '
                                        '1 - Vacation, 2 - Sick leave, 3 - Day off: '))
        break
    except ValueError as e:
        continue

from_date_input = input('Please enter a date when you want to start your vacation: ')
to_date_input = input('Please enter a date when you want to start your vacation: ')


@title
def vacation(name, surname, vacation_start, vacation_end, vacation_kind):
    """
        This function creates a vacation request text based on the input parameters
        and decorated by @title decorator
    Args:
        name: employee's name
        surname: employee's surname
        vacation_start: the first vacation date
        vacation_end: the last vacation date
        vacation_kind: type of requested vacation

    Returns:
        string - vacation body with args inserted
    """
    vacation_types = {
        1: 'vacations',
        2: 'sick leave',
        3: 'day off',
    }
    if vacation_kind in vacation_types:
        return f'\nHi John,\n' \
               f'I need the paid {vacation_types.get(vacation_kind)} from {vacation_start} to {vacation_end}.\n' \
               f'{name} {surname}'
    return '\nI wanna get promotion :)'


print(vacation(name_input, surname_input, from_date_input, to_date_input, vacation_kind_input))
