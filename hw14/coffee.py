from abc import ABC, abstractmethod


class Coffee(ABC):
    """
    Abstract class for coffee types
    """
    def __init__(self):
        self.coffee_cost = 20

    @abstractmethod
    def make_coffee(self):
        """
        Abstract method for coffee making
        """
        pass
