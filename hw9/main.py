from datetime import date
from module_hw9 import Human


vadim = Human('Vadim', 'Drozd', 'male', birthday=date(1990, 9, 5))
print(vadim.age)
print(Human.population)
print(vadim.stand())
print(vadim.eat())
print(vadim.sleep())
print(vadim.go())
print(vadim.lie())
print(vadim.speak())
