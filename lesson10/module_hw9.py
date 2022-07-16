from datetime import date


class Human:
    population = 0

    @classmethod
    def population_increase(cls):
        cls.population += 1

    def __init__(self,
                 name: str,
                 surname: str,
                 sex: str,
                 birthday=date.today()):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.__birthday = birthday
        self.__class__.population_increase()

    @property
    def age(self):
        return (date.today() - self.__birthday).days // 365

    def eat(self):
        return f'{self.name} is eating'

    def sleep(self):
        return f'{self.name} is sleeping'

    def speak(self):
        return f'{self.name} is speaking'

    def go(self):
        return f'{self.name} is going'

    def stand(self):
        return f'{self.name} is standing'

    def lie(self):
        return f'{self.name} is lying'