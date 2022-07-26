from lesson11_hw11.school_employee import SchoolEmployee


class Director(SchoolEmployee):
    def __init__(self, name: str,
                 surname: str,
                 age: int,
                 position: str = 'Director',
                 benefit: int = 20000):
        super().__init__(name, surname, age, position, benefit)

    def get_benefit(self):
        """
        Returns: string with director's salary information

        """
        print(f'Director gets {self.benefit} uah benefit')