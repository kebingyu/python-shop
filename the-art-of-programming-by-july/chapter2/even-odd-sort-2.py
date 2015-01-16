# -*- coding: utf-8 -*-
"""
一个未排序整数数组，有正负数，重新排列使负数排在正数前面，并且要求不改变原来的正负数之间相对顺序
比如： input: 1,7,-5,9,-12,15 ans: -5,-12,1,7,9,15 要求时间复杂度O(n),空间O(1)。
"""
def func1(numbers):#{{{
    # time O(N^2)
    length = len(numbers)
    if length > 1:
        idx_n = 0
        while idx_n < length:
            # find the first available negative
            while idx_n < length and numbers[idx_n] > 0:
                idx_n = idx_n + 1
            # reach the end and we are done
            if idx_n >= length:
                break
            temp_n = idx_n
            # last positive on the left of idx_n
            if idx_n == 0:
                idx_p = 0
            else:
                idx_p = idx_n - 1
            temp_p = idx_p
            # swap
            while idx_p >=0 and numbers[idx_p] > 0:
                numbers[idx_p], numbers[idx_n] =\
                        numbers[idx_n], numbers[idx_p]
                idx_n = idx_n - 1
                idx_p = idx_p - 1
            # move pointers
            idx_n = temp_n + 1
            idx_p = temp_p + 1
    return numbers
#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)

#python even-odd-sort-2.py '1,7,-5,9,-12,15'
