# -*- coding: utf-8 -*-
"""
输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。要求时间复杂度为O(n)。
"""
def func1(numbers):#{{{
    # space O(N)
    even = []
    odd = []
    for _ in numbers:
        if _ % 2 == 0:
            even.append(_)
        else:
            odd.append(_)
    odd.extend(even)
    return odd
#}}}

def func2(numbers):#{{{
    # in place
    length = len(numbers)
    if length > 1:
        idx_i = 0
        idx_j = length - 1
        while idx_i < idx_j:
            while numbers[idx_i] % 2 == 1:
                idx_i = idx_i + 1
            while numbers[idx_j] % 2 == 0:
                idx_j = idx_j - 1
            if idx_i < idx_j:
                numbers[idx_i], numbers[idx_j] =\
                        numbers[idx_j], numbers[idx_i]
                idx_i = idx_i + 1
                idx_j = idx_j - 1
    return numbers
#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)
print func2(numbers)

#python even-odd-sort.py '2,13,29,11,0,100,5,7,22,-66'
