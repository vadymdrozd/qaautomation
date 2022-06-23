# 1. Сформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

from time import sleep
from random import choice

print('Please enter any word')
word = input()
print(f'Please enter symbol number you want to get from "{word}" (Remember, you should use digits only)')
symbol_number = None

while True:
    try:
        symbol_number = int(input())
        break
    except ValueError:
        print('You should use integer number only')
        print('Please try again:')

print('Do some magic :)')

fun_phrases = ['Don\'t sleep!', 'One moment', 'Don\'t go', '...']

for sec in range(4):
    sleep(1)
    random_phrase = choice(fun_phrases)
    print(random_phrase)
    fun_phrases.remove(random_phrase)

sleep(1)
print('Aaaaaand...')

try:
    word_symbol = word[symbol_number-1]
    sleep(1)
    print(f'... your symbol is "{word_symbol}"')
except IndexError:
    sleep(1)
    print(f'You\'re cheater because you know that the {symbol_number} symbol is absent in this word:)')
