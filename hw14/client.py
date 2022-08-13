from discount import Discount


class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.balance = 0

    @property
    def discount(self):
        """
        Clients property which counts client's discount base on Enum class Discount
        Returns: client's discount
        """
        if self.balance < 50:
            return 0
        if 50 < self.balance < 100:
            return Discount.UP_TO_100.value
        if 100 < self.balance < 250:
            return Discount.UP_TO_250.value
        if 250 < self.balance < 300:
            return Discount.UP_TO_300
        if 300 < self.balance:
            return Discount.MORE_THAN_300

    def balance_increase(self, increment: int):
        """
        Method for clients balance increasing
        Args:
            increment: int object
        """
        self.balance += increment
