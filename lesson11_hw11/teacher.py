from lesson11_hw11.school_employee import SchoolEmployee


class Teacher(SchoolEmployee):
    def __init__(self, name: str,
                 surname: str,
                 age: int,
                 position: str = 'Teacher',
                 benefit: int = 6000):
        super().__init__(name, surname, age, position, benefit)

    def get_benefit(self):
        """
        Returns: string with teacher's salary information

        """
        print(f'Teacher gets {self.benefit} uah benefit')