"""
Difficulty: Medium

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):#{{{
        # first find all 'O' on edges, then any inside 'O'
        # connects to 'O' is not to be flipped
        
        # get total column and row
        row = len(board)
        if row == 0:
            return
        col = len(board[0])
        if col == 0:
            return
            
        position = []
        # store position of "O" on left and right edge
        for i in range(row):
            if board[i][0] == 'O':
                board[i][0] = 'N' # means not closed
                position.append((i, 0))
            if board[i][col - 1] == 'O':
                board[i][col - 1] = 'N'
                position.append((i, col - 1))
        # store position of "0" on top and bottom edge
        for i in range(1, col - 1):
            if board[0][i] == 'O':
                board[0][i] = 'N'
                position.append((0, i))
            if board[row - 1][i] == 'O':
                board[row - 1][i] = 'N'
                position.append((row - 1, i))
                
        # traverse the whole board
        while len(position) > 0:
            i, j = position.pop()
            if i - 1 >= 0 and board[i - 1][j] == 'O':
                board[i - 1][j] = 'N'
                position.append((i - 1, j))
            if i + 1 < row and board[i + 1][j] == 'O':
                board[i + 1][j] = 'N'
                position.append((i + 1, j))
            if j - 1 >= 0 and board[i][j - 1] == 'O':
                board[i][j - 1] = 'N'
                position.append((i, j - 1))
            if j + 1 < col and board[i][j + 1] == 'O':
                board[i][j + 1] = 'N'
                position.append((i, j + 1))
                
        # ready to flip
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
#}}}
