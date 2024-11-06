class Car:
    def __init__(self, registration_number, max_speed):
        self.number = registration_number
        self.maximum_speed = max_speed
        self.kilometers_driven = 0

    def drive(self, hours):
        distance = self.maximum_speed * hours
        self.kilometers_driven += distance

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.drive(3)
gasoline_car.drive(3)


print(f"Electric Car ({electric_car.number}) - Kilometers Driven: {electric_car.kilometers_driven} km")
print(f"Gasoline Car ({gasoline_car.number}) - Kilometers Driven: {gasoline_car.kilometers_driven} km")