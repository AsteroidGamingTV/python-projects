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

w = '~'
grid = [
    [' ',0,1,2,3,4,5,6,7,8,9],
    ['A',w,w,w,w,w,w,w,w,w,w],
    ['B',w,w,w,w,w,w,w,w,w,w],
    ['C',w,w,w,w,w,w,w,w,w,w],
    ['D',w,w,w,w,w,w,w,w,w,w],
    ['E',w,w,w,w,w,w,w,w,w,w],
    ['F',w,w,w,w,w,w,w,w,w,w],
    ['G',w,w,w,w,w,w,w,w,w,w],
    ['H',w,w,w,w,w,w,w,w,w,w],
    ['I',w,w,w,w,w,w,w,w,w,w],
    ['J',w,w,w,w,w,w,w,w,w,w],

grid[3][7] = '*'

for row in grid:
    for col in row:
        print(col)

carrier = Carrier()

start_row = input("Enter start row for Carrier:").strip().lower()
start_col = input("Enter start col for Carrier:").strip().lower()
direction = input("Enter direction for Carrier [N,S,E,W]:").strip().lower()

