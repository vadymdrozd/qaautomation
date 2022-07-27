#  Дана довільна строка. Напишіть код, який знайде в ній і виведе на екран кількість слів,
#  які містять дві голосні літери підряд.

from time import sleep


draft_text = input('Please enter any text and I count words with two vowels in a row in it: ')

if len(draft_text) == 0:
    print('Are you kidding me? I know that you haven\'t written any text')

clear_text = draft_text.split()

word_list = []
counter = 0

for word in range(len(clear_text)):  # cycle by words is opened
    for symbol in range(len(clear_text[word])):  # cycle by symbols in the word is opened
        try:
            if clear_text[word][symbol] in 'eyuioa' and clear_text[word][symbol+1] in 'eyuioa':  # two vowels in a row finding
                counter += 1
                if counter == 1:
                    word_list.append(clear_text[word])
                    counter = 0
                    break
        except IndexError:
            continue

print(f'Let me think...')
sleep(1)

if len(word_list) == 0 and len(draft_text) > 0:
    print('There are no words with two vowels in a row in your text')
elif len(word_list) > 0:
    print(f'There {"is" if len(word_list) == 1 else "are"} {len(word_list)} word{"s" if len(word_list) > 1 else ""} '
          f'with two vowels in a row in your text')
