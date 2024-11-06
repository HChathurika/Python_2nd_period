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



    class Elevator:
        def __init__(self, bottom, top):
            self.bottom_floor = bottom
            self.top_floor = top
            self.current_floor = bottom

        def go_to_floor(self, target_floor):
            if target_floor < self.bottom_floor or target_floor > self.top_floor:
                print("Invalid Floor")
                return  # Exit if the floor is invalid

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
            # Create the specified number of elevators
            self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

        def run_elevator(self, elevator_number, target_floor):



            class Elevator:
                def __init__(self, bottom, top):
                    self.bottom_floor = bottom
                    self.top_floor = top
                    self.current_floor = bottom

                def go_to_floor(self, target_floor):
                    if target_floor < self.bottom_floor or target_floor > self.top_floor:
                        print("Invalid Floor")
                        return  # Exit if the floor is invalid

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
                    # Create the specified number of elevators
                    self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

                def run_elevator(self, elevator_number, target_floor):
                    if 0 <= elevator_number < len(self.elevators):
                        print(f"\nRunning Elevator {elevator_number + 1} to floor {target_floor}:")
                        self.elevators[elevator_number].go_to_floor(target_floor)
                    else:
                        print("Invalid elevator number")
                        return

                def fire_alarm(self):
                    print("\nFire alarm triggered! Moving all elevators to the bottom floor.")
                    for i, elevator in enumerate(self.elevators):
                        print(f"\nMoving Elevator {i + 1} to the bottom floor:")
                        elevator.go_to_floor(self.bottom_floor)