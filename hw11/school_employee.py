from abc import ABC, abstractmethod
from hw11.human import Human


class SchoolEmployee(Human, ABC):
    def __init__(self,
                 name: str,
                 surname: str,
                 age: int,
                 position: str,
                 benefit):
        #type of benefit?
        super().__init__(name, surname, age)
        self.position = position
        self.benefit = benefit

    @abstractmethod
    def get_benefit(self):
        raise NotImplementedError('You forgot to implement this!')
