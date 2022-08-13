from coffee import Coffee
from seasonings_decorators import cinnamon, vanilla, milk


@cinnamon
@vanilla
@milk
class SimpleCoffee(Coffee):
    """
    Kind of Coffee class
    Has 3 class decorators (seasonings for coffee) - cinnamon, vanilla and milk
    """
    def __init__(self):
        super().__init__()

    def make_coffee(self):
        """
        Method for simple coffee creating
        Returns: cost of coffee
        """
        return self.coffee_cost
