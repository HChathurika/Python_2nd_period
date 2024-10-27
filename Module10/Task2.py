class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid Floor")
            return

        while target_floor > self.current_floor:
            self.floor_up()

        while target_floor < self.current_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")
        else:
            print("You are at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")
        else:
            print("You are at the bottom floor")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):

        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning Elevator {elevator_number + 1} to floor {target_floor}:")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number")



if __name__ == "__main__":

    building = Building(1, 10, 3)


    building.run_elevator(0, 5)  # Run elevator 1 to floor 5
    building.run_elevator(1, 8)  # Run elevator 2 to floor 8
    building.run_elevator(2, 3)  # Run elevator 3 to floor 3


    print("\nReturning Elevator 1 to the bottom floor:")
    building.run_elevator(0, 1)
