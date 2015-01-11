# -*- coding: utf-8 -*-
"""
给定整型数组，其中每个元素表示木板的高度，木板的宽度都相同，求这些木板拼出的最大矩形的面积。并分析时间复杂度。如[5,4,3,2,4,5,0,7,8,4,6]中最大矩形的高度是[7,8,4,6]组成的矩形，面积为16
note:
    1. each board has to be put together continuously
    2. no board can be put on top of another
"""
def func1(numbers):#{{{
    # time O(N*logN)
    max_area = 0
    length = len(numbers)
    if length > 0:
        curr_a, max_a = maxSquare(numbers, 0, length - 1, max_area)
    return max_a

def maxSquare(numbers, fr, to, max_area):
    if fr > to:
        return (0, max_area)
    elif fr == to:
        return (numbers[fr], max_area)

    min_idx = fr
    # find smallest height
    for _ in range(fr, to + 1):
        if numbers[_] < numbers[min_idx]:
            min_idx = _

    sm_area = numbers[min_idx] * (to - fr + 1)
    lf_area, max_area = maxSquare(numbers, fr, min_idx - 1, max_area)
    rg_area, max_area = maxSquare(numbers, min_idx + 1, to, max_area)

    curr_max_area = max(sm_area, lf_area, rg_area)
    max_area = max(max_area, curr_max_area)
    return (curr_max_area, max_area)
#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)

#python largest-sum-of-subset-1.py '5,4,3,2,4,5,0,7,8,4,6'
