class Warehouse:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for _ in range(height):
            self.grid.append([])
            for _ in range(width):
                self.grid[-1].append(0)

    def add_shelf(self, row, col):
        self.grid[row][col] = 1

    def is_blocked(self, row, col):
        if self.grid[row][col] == 1:
            return True
        return False

    def is_in_bounds(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return True
        return False


if __name__ == "__main__":
    w = Warehouse(5, 5)
    w.add_shelf(1, 1)
    print(w.is_blocked(1, 1))       # True
    print(w.is_blocked(0, 0))       # False
    print(w.is_in_bounds(2, 2))     # True
    print(w.is_in_bounds(2, 99))    # False
    print(w.is_in_bounds(-1, 0))    # False