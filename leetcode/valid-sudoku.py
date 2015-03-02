"""
Difficulty: Easy

Determine if a Sudoku is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
    A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):#{{{
        # check row
        for _ in board:
            if self.validate(_) == False:
                return False
        # check column
        for _ in range(9):
            temp = []
            for array in board:
                temp.append(array[_])
            if self.validate(temp) == False:
                return False
        # check sub-cube
        idx = [[0,3], [3,6], [6,9]]
        for end_i in idx:
            for end_j in idx:
                temp = []
                for idx_i in range(end_i[0], end_i[1]):
                    for idx_j in range(end_j[0], end_j[1]):
                        temp.append(board[idx_i][idx_j])
                if self.validate(temp) == False:
                    return False
        return True
        
    def validate(self, array):
        temp = {}
        for _ in array:
            if _ != '.' and temp.has_key(_):
                return False
            else:
                temp[_] = 1
        return True
#}}}
