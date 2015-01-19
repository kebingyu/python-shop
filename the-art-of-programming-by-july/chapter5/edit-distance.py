# -*- coding: utf-8 -*-
"""
给定一个源串和目标串，能够对源串进行如下操作：
1. 在给定位置上插入一个字符
2. 替换任意字符
3. 删除任意字符

写一个程序，返回最小操作数，使得对源串进行这些操作后等于目标串，源串和目标串的长度都小于2000。
"""
def func1(source, target):
    length_s = len(source)
    length_t = len(target)
    # use dp[i][j] to store the number of operations for source[0...i] and target[0...j]
    dp = [[0 for i in range(length_t)] for i in range(length_s)]

    # boundary: dp[i][0] = i, dp[0][j] = j
    for _ in range(length_s):
        dp[_][0] = _
    for _ in range(length_t):
        dp[0][_] = _

    # dp
    for i in range(1, length_s):
        for j in range(1, length_t):
            if source[i] == target[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(\
                        # source delete a char
                        dp[i - 1][j] + 1, \
                        # source insert a char 
                        dp[i][j - 1] + 1, \
                        # source replace a char
                        dp[i - 1][j - 1] + 1)

    return dp[length_s - 1][length_t - 1]


import sys
print func1(sys.argv[1], sys.argv[2])

#python edit-distance.py 'algorithm' 'altruistic'
