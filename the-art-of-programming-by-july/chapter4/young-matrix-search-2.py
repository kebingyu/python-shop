# -*- coding: utf-8 -*-
"""
给定 n×n 的实数矩阵，每行和每列都是递增的，求这 n^2 个数的中位数。

this is finding the kth biggest element in young matrix,
where k = floor(n*n/2) in this case
"""
def func1(matrix):
    row = len(matrix)
    col = 0
    if row > 0:
        col = len(matrix[0])
    if row > 0 and col > 0:
        k = (row * col) / 2
        # binary search a number x which is bigger than k elements
        # store in mid
        low = matrix[0][0]
        high = matrix[row-1][col-1]
        while low <= high:
            mid = (low + high) / 2
            order = bigger_than(matrix, row, col, mid)
            if order == k:
                break
            elif order > k:
                high = mid - 1
            else:
                low = mid + 1

        # find the largest number which is smaller than x 
        curr_r = 0
        curr_c = col - 1
        ret = mid
        while curr_r < row and curr_c >= 0:
            if matrix[curr_r][curr_c] >= mid:
                curr_c -= 1
            else:
                ret = max(matrix[curr_r][curr_c], ret)
                curr_r += 1
        return ret


def bigger_than(matrix, num_row, num_col, number):
    row = 0
    col = num_col - 1
    bigger_than = 0
    while row < num_row and col >= 0:
        if number <= matrix[row][col]:
            col -= 1
            bigger_than += num_row - row
        else:
            row += 1
    return num_row * num_col - bigger_than


matrix = []
matrix.append([1,2,8,9])
matrix.append([2,4,9,12])
matrix.append([4,7,10,13])
matrix.append([6,8,11,15])
#matrix.append([7,9,16,22])
print func1(matrix)
