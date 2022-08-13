from cappuccino import Cappuccino
from latte import Latte
from simple_coffee import SimpleCoffee
from client import Client
from order import Order
from exceptions import LowMoneyException


class CoffeeMachine:
    """
    Coffee machine class. Contains coffee types. Has method for creating coffee with toppings
    """
    def __init__(self):
        self.coffee_type = {
            1: Cappuccino(),
            2: Latte(),
            3: SimpleCoffee(),
        }

    def create_coffee(self, client: Client, order: Order, money_income: int):
        """
        Method for creating coffee with toppings. If no toppings in an order, makes just coffee
        Args:
            client: client object for: 1. find out client discount; 2. increase client balance after coffee creating
            order: order object for find out ordered: 1. coffee type; 2. toppings
            money_income: client money income attribute
        Returns: money rest if money income mote than order total money, else raises LowMoneyException
        """
        coffee = self.coffee_type.get(order.coffee_type)
        order_total = coffee.make_coffee()
        for topping in order.toppings_list:
            if topping == 1:
                order_total += coffee.add_cinnamon()
            if topping == 2:
                order_total += coffee.add_vanilla()
            if topping == 3 and order.coffee_type == 3:
                order_total += coffee.add_milk()
        if order_total > money_income:
            raise LowMoneyException('Your deposit is low')
        order_discount = order_total * client.discount
        order_total = order_total - order_discount
        client.balance_increase(order_total - order_discount)
        return money_income - order_total
