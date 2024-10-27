class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

def go_to_floor(self, target_floor):
    if target_floor < self.bottom_floor or target_floor > self.top_floor:
        print("Invalid Floor ")
        return
    # up or down

    # call floor_up or floor_down
    while target_floor>self.current_floor:
            self.floor_up()

    while target_floor<self.current_floor:
            self.floor_down()


def floor_up(self):
    if self.current_floor<self.top_floor:
        self.current_floor += 1
        print(f"current floor : {self.current_floor}")
    else:
        print(f"You are at the top floor")

def floor_down(self):
    if self.current_floor>self.bottom_floor:
        self.current_floor -= 1
        print(f"current floor : {self.current_floor}")
    else:
        print(f"You are at the bottom floor")

    if __name__ == "__main__":
        elevator = Elevator(1, 10)
        print("Moving to the 5th floor:")
        elevator.go_to_floor(5)


        print("\nMoving back to the bottom floor:")
        elevator.go_to_floor(1)

