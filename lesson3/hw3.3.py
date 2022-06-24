# 3. Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2.1', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

digits_list = []

for item in lst1:
    try:
        if type(item) is int:  # Checking if item is integer
            digits_list.append(item)
        elif item.isdigit():  # Checking if item is digit but present as str
            digits_list.append(item)
        elif float(item):  # Checking if item is float but present as str
            digits_list.append(item)
    except (ValueError, AttributeError):
        continue

if len(digits_list) == 0:
    print('There are no digits in this list')
elif 0 < len(digits_list) < 2:
    print(f'This list contains 1 digit - here is {digits_list}')
else:
    print(f'There are {len(digits_list)} digits in your list. Here are {digits_list}')