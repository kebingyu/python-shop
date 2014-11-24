"""
Exiting a 2D maze

'1': wall cell
'0': walkable cell
'e': exit cell
'm': mouse, the starting point
'.': visited cell

111111
111001
1000e1
100m11
111111
"""

from grid import Grid

class MazeGrid(Grid):
    """
    Return neighbor cells in a list
    curr is a tuple of current position
    Note: due to the maze grid set up, curr will never be at the edge of the grid
    """
    def getNeighbor(self, curr):
        neighbor = []
        if self.isInGrid(curr):
            neighbor.append((curr[0] - 1, curr[1]))
            neighbor.append((curr[0], curr[1] + 1))
            neighbor.append((curr[0] + 1, curr[1]))
            neighbor.append((curr[0], curr[1] - 1))
        return neighbor

    """
    Return unvisited neighbor cells in a list
    Visited cell is replaced by '.'
    """
    def getUnvisitedNeighbor(self, curr):
        neighbor = []
        for _ in self.getNeighbor(curr):
            data = self.getData(_)
            if data != '.' and data != '1':
                neighbor.append(_)
        return neighbor

    def markVisited(self, curr):
        self.setData(curr, '.')

def getGridOne():
    board = MazeGrid(5, 6)
    board.addRow(0, '111111')
    board.addRow(1, '111001')
    board.addRow(2, '1000e1')
    board.addRow(3, '100m11')
    board.addRow(4, '111111')
    return board

def getGridTwo():
    board = MazeGrid(11, 11)
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
board = getGridOne()
#board = getGridTwo()
print board

from stack import Stack
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
