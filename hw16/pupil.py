from hw11.school_employee import SchoolEmployee
from random import randint
from dataclasses import dataclass, field
from human_sex import HumanSex


@dataclass
class Pupil(SchoolEmployee):
    name: str
    surname: str
    age: int
    _sex: int
    position: str = 'Pupil'
    benefit: int = int
    benefits_list: list = field(default_factory=list)

    @property
    def sex(self):
        return HumanSex.MALE.value if self._sex == 0 else HumanSex.FEMALE.value

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(f'Incorrect data type of "name" parameter: {type(self.name)}. Please use "str"')
        if not isinstance(self.surname, str):
            raise TypeError(f'Incorrect data type of "surname" parameter: {type(self.surname)}. Please use "str"')
        if not isinstance(self.age, int):
            raise TypeError(f'Incorrect data type of "age" parameter: {type(self.age)}. Please use "int"')

    def get_benefit(self):
        """
        Adds to pupil's list self.benefits_list random int from 60 to 95 like a points for study
        Returns: Nothing
        """
        self.benefit = randint(60, 95)
        self.benefits_list.append(self.benefit)
        print(f'{self.name} {self.surname} gets {self.benefit} points')

    def get_average_points(self):
        """
        Returns: integer - pupil's average points from list self.benefits_list
        """
        return sum(self.benefits_list) / len(self.benefits_list)
