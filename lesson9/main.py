from hw_lesson9_module import Vehicle


auto = Vehicle('Subaru', 'Impreza', 2007, 60, 240, 7)
auto.tank_level = 60
auto.odometer_value = 100000

print(auto.refueling())
print(auto.race(900))

auto2 = Vehicle('Subaru', 'Impreza', 2007, 60, 240, 7)
auto2.tank_level = 60
auto2.odometer_value = 110000

print('-----')

print(auto.lend_fuel(auto2))
print(auto.get_tank_level())
print(auto2.get_tank_level())
print(auto.get_mileage())
print(auto2.get_mileage())
