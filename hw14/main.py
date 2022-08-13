from coffe_machine import CoffeeMachine
from client import Client
from order import Order

coffee_machine1 = CoffeeMachine()

name = input('Please enter your name: ')
surname = input('Please enter your surname: ')

client = Client(name, surname)

while True:
    coffee_type = int(input('Please choose a kind of coffee you want to:\n'
                            '1 - Cappuccino $35 \n'
                            '2 - Latte $40\n'
                            '3 - Simple coffee $20\n'))

    topping_asker = int(input('Do you want some toppings (1 - Yes, 2 - No)? '))
    toppings_list = []

    if topping_asker == 1:
        while True:
            topping_decision = toppings_list.append(int(input('What kind of:\n'
                                                              '1 - Cinnamon $30\n'
                                                              '2 - Vanilla $25\n'
                                                              '{0}'.format("3 - Milk $15\n" if coffee_type == 3 else ""))))
            one_more_topping = int(input('One more topping (1 - Yes, 2 - No)? '))
            if one_more_topping == 2:
                break
            else:
                continue

    client_order = Order(coffee_type, toppings_list)

    money_income = int(input('Please deposit money for coffee creating: '))

    print(f'Take the rest {coffee_machine1.create_coffee(client, client_order, money_income)}')
    print(f'Your next discount is {"0" if client.discount == 1 else client.discount * 100}%')

    next_order = int(input('One more coffee (1 - Yes, 2 - No)?: '))
    if next_order == 1:
        continue
    else:
        break
