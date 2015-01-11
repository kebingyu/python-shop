# -*- coding: utf-8 -*-
"""
输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字。

要求时间复杂度是O(N)。如果有多对数字的和等于输入的数字，输出任意一对即可。

例如输入数组1、2、4、7、11、15和数字15。由于4+11=15，因此输出4和11。
"""
def func1(numbers):#{{{
    # O(N) space and time
    length = len(numbers)
    if length > 0:
        pool = {}
        for _ in numbers:
            pool[_] = True
        for _ in numbers:
            if pool.has_key(15 - _):
                print _, 15 - _
                break
    return
#}}}

def func2(numbers):#{{{
    # O(N) time, O(1) space if numbers is already sorted
    # O(N*logN) time, O(1) space if numbers is not sorted
    length = len(numbers)
    if length > 0:
        idx_i = 0
        idx_j = length - 1
        while idx_i < idx_j:
            if numbers[idx_i] + numbers[idx_j] > 15:
                idx_j = idx_j - 1
            elif numbers[idx_i] + numbers[idx_j] < 15: 
                idx_i = idx_i + 1
            else:
                print numbers[idx_i], numbers[idx_j]
                break
    return
#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)
print func2(numbers)

#python find-sum-two-numbers.py '1,2,4,7,11,15'
