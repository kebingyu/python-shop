"""
implementation of 2D grid

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
class Grid:
    def __init__(self, row, col):
        self.board = [[] * col] * row 
        self.height = row
        self.width = col

    def __str__(self):
        for row in range(self.getHeight()):
            print ''.join(_ for _ in self.board[row])
        return ''

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    """
    Check if the given position is valid
    """
    def isInGrid(self, curr):
        return curr[0] >= 0 \
                and curr[0] <= self.getHeight() - 1 \
                and curr[1] >= 0 \
                and curr[1] <= self.getWidth() - 1

    """
    Return the data of given position
    """
    def getData(self, curr):
        if self.isInGrid(curr):
            return self.board[curr[0]][curr[1]]

    def setData(self, curr, data):
        if self.isInGrid(curr):
            self.board[curr[0]][curr[1]] = data

    """
    row index starts with zero
    data is a string
    """
    def addRow(self, row, data):
        height = self.getHeight()
        width = self.getWidth()
        if row >= 0 and row <= height - 1 and len(data) == width:
            self.board[row] = [_ for _ in data]

    """
    Return neighbor cells in a list
    curr is a tuple of current position
    Note: due to the grid set up, curr will never be at the edge of the grid
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

