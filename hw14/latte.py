from coffee import Coffee
from seasonings_decorators import cinnamon, vanilla


@cinnamon
@vanilla
class Latte(Coffee):
    """
    Kind of Coffee class
    Has 2 class decorators (seasonings for latte) - cinnamon and vanilla
    """
    def __init__(self):
        super().__init__()
        self.latte_milk_cost = 20

    def make_coffee(self):
        """
        Method for latte creating
        Returns: total cost of coffee with latte milk
        """
        return self.coffee_cost + self.latte_milk_cost
