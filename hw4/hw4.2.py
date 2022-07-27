# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999, "main-service": 37.245,
# "buy.ua": 38.324, "my-store": 37.166, "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною.

items_dict = {"cilpio": 47.999,
              "a_studio": 42.999,
              "momo": 49.999,
              "main-service": 37.245,
              "buy.ua": 38.324,
              "my-store": 37.166,
              "the_partner": 38.988,
              "sto": 37.720,
              "rozetka": 38.003,
              }

lowprice_input = input('Please enter a lower price (you can use only integer or float digits with "."): ')
highprice_input = input('Please enter a higher price (you can use only integer or float digits with "."): ')

try:
    price_range = (float(lowprice_input), float(highprice_input)) if float(lowprice_input) < float(highprice_input)\
                    else (float(highprice_input), float(lowprice_input))
    shops = []
    for key, value in items_dict.items():
        if price_range[0] < value < price_range[1]:
            shops.append(key)
    if len(shops) == 0:
        print('There are no shops to suggest you items in your price range')
    else:
        print('You can buy your item in theese shops:')
        for shop in shops:
            print('--> ', shop)
except ValueError:
    print('Unfortunately you have used not only integer or float digits with "."')
