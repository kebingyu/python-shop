# -*- coding: utf-8 -*-
"""
有个长度为2n的数组{a1,a2,a3,...,an,b1,b2,b3,...,bn}，希望排序后{a1,b1,a2,b2,....,an,bn}，请考虑有无时间复杂度o(n)，空间复杂度0(1)的解法。
"""
def func1(numbers):
    # O(N) O(N)
    length = len(numbers)
    ret = ''
    if length > 0:
        a = []
        b = []
        for _ in range(0, length / 2):
            a.append(numbers[_])
        for _ in range(length / 2, length):
            b.append(numbers[_])
        for _ in range(len(a)):
            ret = ret + ',' + a[_] + ',' + b[_]
    return ret

def func2(numbers):
    # O(N^2) O(1)
    length = len(numbers)
    if length > 0:
        n = length / 2
        temp = 1
        for _ in range(n, length):
            # find the target position
            target_idx = _ - n + temp
            temp = temp + 1
            # swap to the target position
            curr_idx = _
            while curr_idx != target_idx:
                numbers[curr_idx], numbers[curr_idx - 1] =\
                        numbers[curr_idx - 1], numbers[curr_idx]
                curr_idx = curr_idx - 1
    return numbers


import sys
numbers = [_ for _ in sys.argv[1].split(',')]
print func1(numbers)
print func2(numbers)

#python 2n-list-sorting.py 'a1,a2,a3,a4,b1,b2,b3,b4'
