# Hапишіть програму "Касир в кінотеатрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!)
# - вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
#
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"
#
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг або тайпхінтінг.
# Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.
#
# P.S. Для цієї і для всіх наступних домашок пишіть в функціях докстрінги або хінтінг

def years_typer(age: int) -> str:
    """
    Receives an int age parameter and determines which text add to him
    Args:
        age: an int parameter from tickets_check function
    Returns:
        an age and determined additional text to age
    """
    str_age = str(age)
    if 4 < age < 21 or len(str_age) > 2 and str_age[-2:] in '11 12 13 14':
        return f'{age} років'
    if age % 10 == 1:
        return f'{age} рік'
    if str_age[-1] in '234':
        return f'{age} роки'
    if age > 24:
        return f'{age} років'


def interesting_age(age: int) -> str:
    """
    Determines if a user age has is a repdigit (e.g. 11, 22, 111)
    Args:
        age: an int parameter from the input
    Returns:
        an 'f'-string with text and the repdigit, if it contains in the age, with text
        determined according to the years_typer function output
    """
    str_age = str(age)
    if 1 < len(str_age) == str_age.count(str_age[0]):
        return f'О, вам {years_typer(age)}! Який цікавий вік!'


def tickets_check(age: int) -> str:
    """
    Receives an int age parameter, defines a user's age and makes tickets check
    Args:
        age: an int parameter from input
    Returns:
        an 'f'-string with tickets check and the user's age with text determined
        according to the years_typer function output
    """
    if age < 1:
        return 'Вибач, але так не може бути'
    elif 1 <= age < 7:
        return f'Тобі ж {years_typer(age)}! Де твої батьки?'
    elif 7 <= age < 16:
        return f'Тобі лише {years_typer(age)}, а цей фільм для дорослих!'
    elif age >= 65:
        return f'Вам {years_typer(age)}? Покажіть пенсійне посвідчення!'
    else:
        return f'Незважаючи на те, що вам {years_typer(age)}, білетів все одно нема!'


while True:
    try:
        customer_age = int(input('Будь ласка, введіть ваш вік цілим числом: '))
        print(tickets_check(customer_age))
        print(interesting_age(customer_age))
        break
    except ValueError as e:
        print('Вибачте, але те, що ви ввели, не є цілим числом. Будь ласка, спробуйте ще раз')