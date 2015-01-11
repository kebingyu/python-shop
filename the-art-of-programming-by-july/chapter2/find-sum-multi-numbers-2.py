# -*- coding: utf-8 -*-
"""
有n个数，输出期中所有和为s的k个数的组合。

举个例子，假定n=6，这6个数为：1 2 1 3 0 1，如果要求输出和为3的全部组合的话，

1 2
1 2 0
0 3
1 1 1
1 1 1 0
而题目加了个限制条件，若令k=2，则只要求输出：[{1,2}, {0,3}] 即可。
"""
def func1(numbers, idx, expected_sum, pool):#{{{
    if idx >= len(numbers) or expected_sum <= 0:
        return

    if numbers[idx] == expected_sum:
        string = ''
        for _ in pool:
            string = string + str(_) + ' + '
        print string + str(numbers[idx])

    pool.append(numbers[idx])
    func1(numbers, idx+1, expected_sum - numbers[idx], pool)
    pool.pop()
    func1(numbers, idx+1, expected_sum, pool)
#}}}

func1([1,2,1,3,0,1], 0, 3, [])
