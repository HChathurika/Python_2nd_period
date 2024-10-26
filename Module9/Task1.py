class Car:
    def __init__(self, registration_number, maximum_speed):
        self.number = registration_number
        self.max_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123" , 142)
print(f"the registration number of the car is : {car.number}")
print(f"the maximum speed of the car is : {car.max_speed}")
print(f"the current speed of the car is :  {car.current_speed}")
print(f"the travelled distance of the car is :  {car.travelled_distance}")
