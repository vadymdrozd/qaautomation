class Vehicle:
    def __init__(self,
                 producer: str,
                 model: str,
                 year: int,
                 tank_capacity: float,
                 maxspeed: int,
                 fuel_consumption: float,):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.tank_level = 0
        self.maxspeed = maxspeed
        self.fuel_consumption = fuel_consumption
        self.odometer_value = 0

    def __repr__(self):
        return f'This is the {self.producer} {self.model} created in {self.year} year.' \
               f'For now it has {self.odometer_value} kilometers of mileage'

    def refueling(self):
        refueled = self.tank_capacity - self.tank_level
        self.tank_level = self.tank_capacity
        return f'There were {refueled} liters refueled'

    def race(self, race_distance):
        tank_distance = self.tank_level / self.fuel_consumption * 100
        travel_distance = tank_distance if tank_distance < race_distance else race_distance
        travel_time = int((travel_distance / (self.maxspeed * 0.8)) * 60)
        if tank_distance > race_distance:
            self.tank_level = ((tank_distance - race_distance) * self.fuel_consumption) / 100
        else:
            self.tank_level = 0
        self.odometer_value += travel_distance
        return {
                'Race distance': travel_distance,
                'Remaining fuel': self.tank_level,
                'Tavel time': f'{travel_time} minutes',
            }

    def get_tank_level(self):
        return self.tank_level

    def get_mileage(self):
        return self.odometer_value

    def lend_fuel(self, other):
        if other.tank_level == 0:
            return 'Нічого страшного, якось розберуся'
        fuel_need = self.tank_capacity - self.tank_level
        fuel_capability = other.tank_level if other.tank_level < fuel_need else fuel_need
        self.tank_level += fuel_capability
        other.tank_level -= fuel_capability
        return f'Дякую, бро, виручив. Ти залив мені {fuel_capability} літрів пального'

    def __eq__(self, other):
        return self.odometer_value == other.odometer_value and self.year == other.year
