# -*- coding: utf-8 -*-
"""
给定一个有序的数组，查找某个数是否在数组中，请编程实现。
"""
def func1(numbers, n):
    length = len(numbers)
    if length > 0:
        middle = length / 2
        if n < numbers[middle]:
            return func1(numbers[:middle], n)
        elif n > numbers[middle]:
            return func1(numbers[middle + 1:], n)
        else:
            return True
    return False


def func2(numbers, n):
    length = len(numbers)
    if length > 0:
        fr = 0
        to = length - 1
        while fr < to:
            middle = (fr + to) / 2
            if n > numbers[middle]:
                fr = middle + 1
            elif n < numbers[middle]:
                to = middle - 1
            else:
                return True
    return False


import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers, int(sys.argv[2]))
print func2(numbers, int(sys.argv[2]))

#python binary_search.py '1,2,3,4,5,6,7' 7
