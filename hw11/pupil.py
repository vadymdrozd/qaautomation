from hw11.school_employee import SchoolEmployee
from random import randint


class Pupil(SchoolEmployee):
    def __init__(self, name: str,
                 surname: str,
                 age: int,
                 position: str = 'Pupil',
                 benefit: int = int):
        super().__init__(name, surname, age, position, benefit)
        self.benefits_list = []

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