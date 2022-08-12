from abc import ABC, abstractmethod
from hw11.human import Human
from dataclasses import dataclass


@dataclass
class SchoolEmployee(Human, ABC):
    name: str
    surname: str
    age: int
    _sex: int
    position: str
    benefit: int
    position: str
    benefit: int

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(f'Incorrect data type of "name" parameter: {type(self.name)}. Please use "str"')
        if not isinstance(self.surname, str):
            raise TypeError(f'Incorrect data type of "surname" parameter: {type(self.surname)}. Please use "str"')
        if not isinstance(self.age, int):
            raise TypeError(f'Incorrect data type of "age" parameter: {type(self.age)}. Please use "int"')

    @abstractmethod
    def get_benefit(self):
        raise NotImplementedError('You forgot to implement this!')
