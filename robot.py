class Robot:

    def __init__(self, robot_id, row, col):
        self.robot_id = robot_id
        self.row = row
        self.col = col
        self.status = "idle"

    def move_to(self, row, col):
        self.row = row
        self.col = col
        self.status = "moving"

    def __repr__(self):
        return f"Robot({self.robot_id}) at ({self.row}, {self.col}) - {self.status}"


if __name__ == "__main__":
    r = Robot(1, 0, 0)
    print(r)              # Robot(1) at (0, 0) - idle
    r.move_to(2, 3)
    print(r)              # Robot(1) at (2, 3) - moving