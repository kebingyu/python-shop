"""
Exiting a 2D maze
"""
from grid import Grid
from stack import Stack

def getGridOne():
    board = Grid(5, 6)
    board.addRow(0, '111111')
    board.addRow(1, '111001')
    board.addRow(2, '1000e1')
    board.addRow(3, '100m11')
    board.addRow(4, '111111')
    return board

def getGridTwo():
    board = Grid(11, 11)
    board.addRow(0, '11111111111')
    board.addRow(1, '10000010001')
    board.addRow(2, '10100010101')
    board.addRow(3, 'e0100000101')
    board.addRow(4, '10111110101')
    board.addRow(5, '10101000101')
    board.addRow(6, '10001010001')
    board.addRow(7, '11111010001')
    board.addRow(8, '101m1010001')
    board.addRow(9, '10000010001')
    board.addRow(10, '11111111111')
    return board

# Initial grid
#board = getGridOne()
board = getGridTwo()
print board

# Exit maze
path = Stack() # save path for backtracking
curr = (3, 3) # initial cell where the mouse is
while board.getData(curr) != 'e':
    board.markVisited(curr)

    for _ in board.getUnvisitedNeighbor(curr):
        path.push(_)

    if path.isEmpty():
        print 'path empty'
    else:
        curr = path.top()
# Done
print board
