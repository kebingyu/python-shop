"""
Eight queens problem: print all the possible solutions

my very inefficient implementation without using left/right diagonals

'1': available cell
'0': occupied cell
'Q': queen cell

"""

from grid import Grid

class QueenGrid(Grid):
    DIAGONAL_OFFSET = {
        'upper-left'  : (-1, -1),
        'upper-right' : (-1, 1),
        'lower-left'  : (1, -1),
        'lower-right' : (1, 1)
    }
    def __init__(self, row, col):
        super(QueenGrid, self).__init__(row, col)
        for _ in range(row):
            self.addRow(_, '1' * col)
        self.queens = []

    """
    Return all diagonal cells of the current position in a list
    """
    def getDiagonalCells(self, curr):
        cells = []
        for _ in self.DIAGONAL_OFFSET.values():
            cell = (curr[0] + _[0], curr[1] + _[1])
            while self.isInGrid(cell):
                cells.append(cell)
                cell = (cell[0] + _[0], cell[1] + _[1])
        return cells

    def markOccupied(self):
        # repaint
        for _ in range(self.getHeight()):
            self.addRow(_, '1' * self.getWidth())
        for curr in self.queens:
            # mark self
            self.setData(curr, 'Q')
            # mark diagonal
            for _ in self.getDiagonalCells(curr):
                self.setData(_, '0')
            # mark column
            for _ in range(0, curr[0]):
                self.setData((_, curr[1]), '0')
            for _ in range(curr[0] + 1, self.getHeight()):
                self.setData((_, curr[1]), '0')

    def placeQueen(self, curr):
        self.queens.append(curr)
        self.markOccupied()

    def removeQueen(self):
        self.queens.pop()
        self.markOccupied()

    """
    Return all available cells on the given row in a list
    """
    def getAvailableCells(self, row):
        cells = []
        for _ in range(self.getWidth()):
            cell = (row, _)
            if self.getData(cell) == '1':
                cells.append(cell)
        return cells

def putQueen(board, row):
    for _ in board.getAvailableCells(row):
        board.placeQueen(_)
        if row < board.getHeight() - 1:
            putQueen(board, row + 1)
        else:
            print board
        board.removeQueen()

n = 5
board = QueenGrid(n, n)
putQueen(board, 0)
