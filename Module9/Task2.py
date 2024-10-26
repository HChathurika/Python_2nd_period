class Car:
    def __init__(self, registration_number, maximum_speed):
        self.number = registration_number
        self.max_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,change_speed ):
        new_speed = self.current_speed + change_speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

car = Car("ABC-123",142)

print(f"the registration number of the car is : {car.number}")
print(f"the maximum speed of the car is : {car.max_speed}")
print(f"the current speed of the car is :  {car.current_speed}")
print(f"the travelled distance of the car is :  {car.travelled_distance}")

car.accelerate(30)
print(f"Current speed is : {car.current_speed}")
car.accelerate(70)
print(f"Current speed is : {car.current_speed}")
car.accelerate(50)
print(f"Current speed is : {car.current_speed}")




