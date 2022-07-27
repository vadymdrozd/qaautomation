from hw11.school_employee import SchoolEmployee


class HeadTeacher(SchoolEmployee):
    def __init__(self, name: str,
                 surname: str,
                 age: int,
                 position: str = "Head Teacher",
                 benefit: int = 15000):
        super().__init__(name, surname, age, position, benefit)

    def get_benefit(self):
        """
        Returns: string with head teacher's salary information

        """
        print(f'Head teacher gets {self.benefit} uah benefit')
