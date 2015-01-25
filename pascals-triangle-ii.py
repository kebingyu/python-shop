"""
Difficulty: Easy

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):#{{{
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        else:
            last_row = self.getRow(rowIndex - 1)
            ret = [1]
            length = len(last_row)
            for _ in range(length):
                if _ + 1 < length:
                    ret.append(last_row[_] + last_row[_ + 1])
            ret.append(1)
            return ret
#}}}
