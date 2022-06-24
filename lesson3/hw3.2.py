# 2. Вести з консолі строку зі слів (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

print('Please enter as lot of text as you want and I count how many words in it ;)')
full_text = input()

if len(full_text) == 0:  # Empty string check
    print('Don\'t try to cheat me. I know that you haven\'t entered any word')

symbols_list = []

for symbol in full_text:
    if symbol in '.,!?:;@#$%^&*()-+_=1234567890':  # Separators and digits cleaning
        symbols_list.append(' ')
    else:
        symbols_list.append(symbol)

clear_text = "".join(symbols_list)

digits_list = []

for digit in full_text:  # Digits finding
    if digit in '1234567890 ':
        digits_list.append(digit)

clear_digits = "".join(digits_list)

words_list = len(full_text.split())

print(f'You have {len(clear_text.split())} words and {len(clear_digits.split())} digits in your text')
