from hw8 import tickets_check

while True:
    try:
        customer_age = int(input('Будь ласка, введіть ваш вік цілим числом: '))
        print(tickets_check(customer_age))
        break
    except ValueError as e:
        print('Вибачте, але те, що ви ввели, не є цілим числом. Будь ласка, спробуйте ще раз')
