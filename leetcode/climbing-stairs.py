"""
Difficulty: Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):#{{{
        table = {}
        return self.helper(n, table)
        
    def helper(self, n, table):
        if n <= 0:
            return 0
        elif n == 1:
            table[1] = 1
            return 1
        elif n == 2:
            table[2] = 2
            return 2
        else:
            if not table.has_key(n):
                table[n] = self.helper(n - 1, table) + self.helper(n - 2, table)
            return table[n] 
        #}}}
