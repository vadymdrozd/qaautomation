from vacation_decorators import title
import time

name_input = ''

while len(name_input.strip()) == 0:
    name_input = (input('Please enter your name: ')).strip()
    if len(name_input) == 0:
        print('Please enter your real name')
        continue  # starts while again if a user enters just spaces in the name_input

surname_input = ''

while len(surname_input) == 0:
    surname_input = (input('Please enter your surname: ')).strip()
    if len(surname_input) == 0:
        print('Please enter your real name')
        continue  # starts while again if a user enters just spaces in the surname_input

vacation_kind_input = None

while True:
    try:
        vacation_kind_input = int(input('Please choose kind of vacation you want (enter a number)? '
                                        '1 - Vacation, 2 - Sick leave, 3 - Day off: '))
        break  # brakes if a user enters int
    except ValueError as e:
        continue  # starts while again if a user enters not int value

from_date_input = None
valid_from_date = None

while True:
    try:
        from_date_input = input('Please enter a date when you want to start your vacation in format DD.MM.YYYY: ')
        valid_from_date = time.strptime(from_date_input, '%d.%m.%Y')  # checks correct date format
        break  # brakes if a user enters start date in correct format (e.g. 05.09.1990)
    except ValueError as e:
        print('There is a mistake with start date format. Please try to enter it in format DD.MM.YYYY')
        continue  # starts while again if a user enters an incorrect format date

to_date_input = None

while True:
    try:
        to_date_input = input('Please enter a date when you want to end your vacation in format DD.MM.YYYY: ')
        valid_to_date = time.strptime(to_date_input, '%d.%m.%Y')  # checks a correct date format
        try:
            if valid_to_date < valid_from_date:  # checks if a user enters a date earlier than start date
                raise ValueError
        except ValueError as e:
            print('End date mustn\'t be earlier than start')
            continue  # starts while again if a user enters a date earlier than start date
        break  # brakes if a user enters date in a correct format (e.g. 05.09.1990) and it's later than start date
    except ValueError as e:
        print('There is a mistake with end date format. Please try to enter it in format DD.MM.YYYY')
        continue  # starts while again if a user enters an incorrect format date


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
