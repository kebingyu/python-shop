# -*- coding: utf-8 -*-
"""
一个台阶总共有n 级，如果一次可以跳1 级，也可以跳2 级。

求总共有多少总跳法，并分析算法的时间复杂度。
"""
def func1(number):#{{{
    # this is another way of calculating Fibonacci numbers
    # The problem can be splitted into two possibilities:
    # 1. jump 1 step, the rest of ways equals f(n-1)
    # 2. jump 2 step, the rest of ways equals f(n-2)
    # So f(n) = f(n-1) + f(n-2), plus special case when n = 1 or 2
    pass
#}}}

import sys
number = int(sys.argv[1])
print func1(number)

#python fibonacci.py '10'
