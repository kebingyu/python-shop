# -*- coding: utf-8 -*-
"""
给一个浮点数序列，取最大乘积连续子串的值，例如 -2.5，4，0，3，0.5，8，-1，则取出的最大乘积连续子串为3，0.5，8。
也就是说，上述数组中，3 0.5 8这3个数的乘积3*0.5*8=12是最大的，而且是连续的。
"""
def func1(numbers, curr_idx):#{{{
    # time O(3*N)
    if curr_idx < len(numbers) - 1:
        # get the max substring of sub array
        maxSub_fr, maxSub_to = func1(numbers, curr_idx + 1)
        # current element
        product_self = numbers[curr_idx]
        # max substring of sub array
        product_sub  = getProduct(numbers, maxSub_fr, maxSub_to)
        # from the current element to the end of max substring of sub array
        product_sub_and_self = getProduct(numbers, curr_idx, maxSub_to)
        product_max = max(product_self, product_sub, product_sub_and_self)
        if product_max == product_self:
            return (curr_idx, curr_idx + 1)
        elif product_max == product_sub:
            return (maxSub_fr, maxSub_to)
        else:
            return (curr_idx, maxSub_to)
    else:
        # reach last element
        return (curr_idx, curr_idx + 1)

def getProduct(array, fr, to):
    # no boundary checking
    ret = 1.0
    for _ in range(fr, to):
        ret = ret * array[_]
    return ret
#}}}

import sys
numbers = [float(_) for _ in sys.argv[1].split(',')]
fr, to = func1(numbers, 0)
print numbers[fr:to]

#python largest-product-substring.py '-2.5,4,0,3,0.5,8,-1'
