# -*- coding: utf-8 -*-
"""
3-sum问题

给定一个整数数组，判断能否从中找出3个数a、b、c，使得他们的和为0，如果能，请找出所有满足和为0个3个数对。
"""
def func1(numbers):#{{{
    # O(N^2) time, O(1) space
    length = len(numbers)
    if length > 0:
        numbers.sort()
        for _ in range(length):
            curr_sum = -numbers[_]
            idx_i = 0
            idx_j = length - 1
            while idx_i < idx_j:
                if idx_i == _:
                    idx_i = idx_i + 1
                elif idx_j == _:
                    idx_j = idx_j - 1
                else:
                    if numbers[idx_i] + numbers[idx_j] > curr_sum:
                        idx_j = idx_j - 1
                    elif numbers[idx_i] + numbers[idx_j] < curr_sum: 
                        idx_i = idx_i + 1
                    else:
                        print numbers[idx_i], numbers[idx_j], -curr_sum
                        idx_i = idx_i + 1
                        idx_j = idx_j - 1
    return#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)

#python find-sum-two-numbers-2.py '1,2,4,5,11,15,12,-6,-12'
