class Ship():
    size = None
    def _init_(self):
        self.location

class Carrier(Ship):
    size = 5

class Battleship(Ship):
    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 3

class PatrolBoat(Ship):
    size = 2

#---------------------------------------------------------------------------------------------------------

print("Welcome to Battleship! ")

grid = [[' ~' * 10] *10]

for row in grid:
    for col in row:
        print(col)

carrier = Carrier()

start_row = input("Enter start row for Carrier:").strip().lower()
start_col = input("Enter start col for Carrier:").strip().lower()
direction = input("Enter direction for Carrier [N,S,E,W]:").strip().lower()

