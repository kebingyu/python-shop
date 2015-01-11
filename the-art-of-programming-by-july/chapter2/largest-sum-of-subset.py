# -*- coding: utf-8 -*-
"""
输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。 求所有子数组的和的最大值，要求时间复杂度为O(n)。

例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2， 因此输出为该子数组的和18。
"""
def func1(numbers):#{{{
    length = len(numbers)
    if length == 0:
        return 0

    curr_sum = 0
    max_sum = float('-inf')
    for _ in numbers:
        if curr_sum + _ > _:
            curr_sum = curr_sum + _
        else:
            curr_sum = _
        max_sum = max(max_sum, curr_sum)
    return max_sum
#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)

#python largest-sum-of-subset.py '1,-2,3,10,-4,7,2,-5'

"""
如果是要你求子数组的最大乘积列?
"""
def func2(numbers):#{{{
    length = len(numbers)
    if length == 0:
        return 0

    neg_sum = 0
    for _ in range(length):
        if numbers[_] < 0:
            neg_sum = neg_sum + 1

    if neg_sum % 2 == 0:
        return numbers
    else:
        first_neg_idx = None
        last_neg_idx = None
        for _ in range(length):
            if numbers[_] < 0 and first_neg_idx == None:
                first_neg_idx = _
                break
        for _ in range(length - 1, -1, -1):
            if numbers[_] < 0 and last_neg_idx == None:
                last_neg_idx = _
                break

        exclude_first_neg = 1
        exclude_last_neg = 1
        for _ in numbers[first_neg_idx + 1:]:
            exclude_first_neg = exclude_first_neg * _
        for _ in numbers[:last_neg_idx]:
            exclude_last_neg = exclude_last_neg * _

        if exclude_first_neg > exclude_last_neg:
            return numbers[first_neg_idx+1:]
        else:
            return numbers[:last_neg_idx]
#}}}

print func2(numbers)
