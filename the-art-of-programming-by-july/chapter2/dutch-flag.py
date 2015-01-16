# -*- coding: utf-8 -*-
"""
现有n个红白蓝三种不同颜色的小球，乱序排列在一起，请通过两两交换任意两个球，使得从左至右，依次是一些红球、一些白球、一些蓝球。
"""
def func1(balls):
    length = len(balls)
    if length > 0:
        begin = 0
        curr = 0
        end = length - 1
        while curr <= end:
            if balls[curr] == 'r':
                swap(balls, curr, begin)
                curr = curr + 1
                begin = begin + 1
            elif balls[curr] == 'w':
                curr = curr + 1
            else:
                swap(balls, curr, end)
                end = end - 1
    return balls

def swap(array, first, second):
    # no exception handling
    array[first], array[second] =\
            array[second], array[first]

import sys
balls = [_ for _ in sys.argv[1].split(',')]
print func1(balls)

#python dutch-flag.py 'r,w,b,w,w,b,r,b,w,r'
