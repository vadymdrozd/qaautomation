# Задача 1: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії
# (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

print('first + second =', first + second)
print('first - second =', first - second)
print('first * second =', first * second)
print('first / second =', first / second)

# Задача 2: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

compare = first > second
print('first > second is', compare)
compare = first < second
print('first < second is', compare)
compare = first == second
print('first == second is', compare)
compare = first != second
print('first != second is', compare)

# Задача 3: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". Виведіть на екран.

str1 = "Hello "
str2 = "world"

str_concat = str1 + str2

print(str_concat)
