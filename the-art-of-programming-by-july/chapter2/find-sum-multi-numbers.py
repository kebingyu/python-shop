# -*- coding: utf-8 -*-
"""
输入两个整数n和sum，从数列1，2，3.......n 中随意取几个数，使其和等于sum，要求将其中所有的可能组合列出来。
"""
def func1(n, expected_sum, pool):#{{{
    if n <= 0 or expected_sum <= 0:
        return

    if n == expected_sum:
        string = ''
        for _ in pool:
            string = string + str(_) + ' + '
        print string + str(n)

    pool.append(n)
    func1(n - 1, expected_sum - n, pool)
    pool.pop()
    func1(n - 1, expected_sum, pool)
#}}}

import sys
n = int(sys.argv[1])
expected_sum = int(sys.argv[2])
func1(n, expected_sum, [])
