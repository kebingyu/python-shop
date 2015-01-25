"""
Difficulty: Easy

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]

"""
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):#{{{
        ret = []
        if numRows > 0:
            self.table = {}
            for _ in range(1, numRows + 1):
                ret.append(self.getNthRow(_))
        return ret
        
    def getNthRow(self, n):
        if self.table.has_key(n):
            ret = self.table[n]
        else:
            if n <= 0:
                ret = []
            elif n == 1:
                ret = [1]
            else:
                last_row = self.getNthRow(n - 1)
                ret = [1]
                length = len(last_row)
                for _ in range(length):
                    if _ + 1 < length:
                        ret.append(last_row[_] + last_row[_ + 1])
                ret.append(1)
            self.table[n] = ret
        return ret
        #}}}
