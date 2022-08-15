from hw11.school_employee import SchoolEmployee
from dataclasses import dataclass
from human_sex import HumanSex


@dataclass
class Director(SchoolEmployee):
    name: str
    surname: str
    age: int
    _sex: int
    position: str = 'Director'
    benefit: int = 20000

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(f'Incorrect data type of "name" parameter: {type(self.name)}. Please use "str"')
        if not isinstance(self.surname, str):
            raise TypeError(f'Incorrect data type of "surname" parameter: {type(self.surname)}. Please use "str"')
        if not isinstance(self.age, int):
            raise TypeError(f'Incorrect data type of "age" parameter: {type(self.age)}. Please use "int"')

    @property
    def sex(self):
        return HumanSex.MALE.value if self._sex == 0 else HumanSex.FEMALE.value

    def get_benefit(self):
        """
        Returns: string with director's salary information

        """
        print(f'Director gets {self.benefit} uah benefit')
