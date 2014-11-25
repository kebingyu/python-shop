"""
implementation of 2D grid

"""
class Grid(object):
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
        return not (curr[0] < 0 \
                or curr[0] > self.getHeight() - 1 \
                or curr[1] < 0 \
                or curr[1] > self.getWidth() - 1)

    """
    Setter and Getter
    """
    def getData(self, curr):
        if self.isInGrid(curr):
            return self.board[curr[0]][curr[1]]
        else:
            return None

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
    """
    def getNeighbor(self, curr):
        neighbor = []
        if self.isInGrid(curr):
            if self.isInGrid((curr[0] - 1, curr[1])):
                neighbor.append((curr[0] - 1, curr[1]))
            if self.isInGrid((curr[0], curr[1] + 1)):
                neighbor.append((curr[0], curr[1] + 1))
            if self.isInGrid((curr[0] + 1, curr[1])):
                neighbor.append((curr[0] + 1, curr[1]))
            if self.isInGrid((curr[0], curr[1] - 1)):
                neighbor.append((curr[0], curr[1] - 1))
        return neighbor
