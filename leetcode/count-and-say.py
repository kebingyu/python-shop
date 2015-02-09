"""
Difficulty: Easy

The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string.

"""
class Solution:
    # @return a string
    def countAndSay(self, n):#{{{
        if n == 1:
            return '1'
        else:
            prev = self.countAndSay(n - 1)
            ret = ''
            curr = prev[0]
            count = 1
            for _ in prev[1:]:
                if _ == curr:
                    count += 1
                else:
                    ret += str(count) + str(curr)
                    curr = _
                    count = 1
            ret += str(count) + str(curr)
            return ret
#}}}
