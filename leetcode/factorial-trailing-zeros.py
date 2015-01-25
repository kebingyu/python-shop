"""
Difficulty: Easy

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Examples:
Input: n = 5
Output: 1 
Factorial of 5 is 20 which has one trailing 0.

Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has 4 trailing zeroes.

Input: n = 100
Output: 24

"""
class Solution:
    # @return an integer
    def trailingZeroes(self, n):#{{{
        total = 0
        curr_power = 1
        while n >= 5 ** curr_power:
            total += n / (5 ** curr_power)
            curr_power += 1
        return total
#}}}
