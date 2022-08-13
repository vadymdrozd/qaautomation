from coffee import Coffee
from seasonings_decorators import cinnamon, vanilla


@cinnamon
@vanilla
class Cappuccino(Coffee):
    """
    Kind of Coffee class
    Has 2 class decorators (seasonings for cappuccino) - cinnamon and vanilla
    """
    def __init__(self):
        super().__init__()
        self.cappuccino_milk_cost = 15

    def make_coffee(self):
        """
        Method for cappuccino creating
        Returns: total cost of coffee with cappuccino milk
        """
        return self.coffee_cost + self.cappuccino_milk_cost
