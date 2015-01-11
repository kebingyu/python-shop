# -*- coding: utf-8 -*-
"""
最大子矩阵和

一个MN的矩阵，找到此矩阵的一个子矩阵，并且这个子矩阵的元素的和是最大的，输出这个最大的值。如果所有数都是负数，就输出0。
例如：35的矩阵：

1 2 0 3 4
2 3 4 5 1
1 1 5 3 0

和最大的子矩阵是：

4 5
5 3

最后输出和的最大值17。
"""
def func1(numbers):
    max_sum = 0
    if len(numbers) > 0:
        num_row = len(numbers)
        num_col = len(numbers[0])
        for idx_row in range(num_row):
            for idx_col in range(idx_row, num_col):
                # reduce the sub-matrix into a 1d list
                reduced = []
                for idx_i in range(idx_row):
                    col_sum = 0
                    for idx_j in range(idx_col):
                        col_sum = col_sum + numbers[idx_i][idx_j]
                    reduced.append(col_sum)
                max_sum = max(max_sum, largest_sum_subset_list(reduced))
                ###
                # this part can be optimized by preprocessing the matrix
                # if use p[i][j] to store the sum of matrix elements from (0,0) to (i,j)
                # then sum of element from row i to row j, col k to col m is 
                #   sum = p[j][m] - p[j][k-1] - p[i-1][m] + p[i-1][k-1]
                # also
                #   p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + numbers[i][j]
                ###
    return max_sum

def largest_sum_subset_list(numbers):
    max_sum = 0
    if len(numbers) > 0:
        curr_sum = 0
        for _ in numbers:
            if _ + curr_sum > curr_sum:
                curr_sum = curr_sum + _
            else:
                curr_sum = _
            max_sum = max(max_sum, curr_sum)
    return max_sum

import sys
temp = sys.argv[1].split(';')
numbers = []
for row in temp:
    numbers.append([int(_) for _ in row.split(',')])
print func1(numbers)

#python largest-sum-of-subset-2.py '1,2,0,3,4;2,3,4,5,1;1,1,5,3,0'
