from vacation_decorators import vacation_type, sick_leave_type, day_off_type


vacation_types = {
    1: vacation_type,
    2: sick_leave_type,
    3: day_off_type,
}

name_input = str(input('Please enter your name: '))
surname_input = str(input('Please enter your surname: '))
vacation_kind_input = int(input('Please choose kind of vacation you want (enter a number)? '
                          '1 - Vacation, 2 - Sick leave, 3 - Day off: '))
from_date = input('Please enter a date when you want to start your vacation in format DD-MM-YYYY: ')
to_date = input('Please enter a date when you want to start your vacation in format DD-MM-YYYY: ')


@vacation_types.get(vacation_kind_input)
def vacation(name, surname, vacation_start, vacation_end):
    print('\nCEO Red Bull Inc.\nMr. John Bigbull\n')


print(vacation(name_input, surname_input, from_date, to_date))