# -*- coding: utf-8 -*-
"""
在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

例如下面的二维数组就是每行、每列都递增排序。如果在这个数组中查找数字6，则返回true；如果查找数字5，由于数组不含有该数字，则返回false。

1 2  8  9
2 4  9 12
4 7 10 13
6 8 11 15

"""
def func1(matrix, n):#{{{
    # time O(m+n)
    row = len(matrix)
    if row > 0:
        col = len(matrix[0])
    else:
        col = 0
    if row > 0 and col > 0:
        idx_r = 0
        idx_c = col - 1
        while idx_r < row and idx_c >= 0:
            if n < matrix[idx_r][idx_c]:
                idx_c = idx_c - 1
            elif n > matrix[idx_r][idx_c]:
                idx_r = idx_r + 1
            else:
                return True
    return False
#}}}

def func2(matrix, n):#{{{
    # time O((m*n)^log4(3))
    row = len(matrix)
    col = 0
    if row > 0:
        col = len(matrix[0])
    if row > 0 and col > 0:
        return search(matrix, n, (0, row - 1), (0, col - 1))
    return False

def search(matrix, n, t_r, t_c):
    if t_c[1] == t_c[0] and t_r[1] == t_r[0]:
        if n == matrix[t_r[0]][t_c[0]]:
            return True
        else:
            return False
    else:
        i = t_r[0]
        j = t_r[1]
        s = t_c[0]
        t = t_c[1]
        if n == matrix[(i+j)/2][(s+t)/2]:
            return True
        elif n < matrix[(i+j)/2][(s+t)/2]:
            return search(matrix, n, (i, (i+j)/2), (s, (s+t)/2))
        else:
            upper_right = search(matrix, n, (i, (i+j)/2), ((s+t)/2 + 1, t))
            lower_left = search(matrix, n, ((i+j)/2 + 1, j), (s, (s+t)/2))
            lower_right = search(matrix, n, ((i+j)/2 + 1, j), ((s+t)/2 + 1, t))
            return upper_right == True or\
                    lower_left == True or\
                    lower_right == True
#}}}

import sys
matrix = []
matrix.append([1,2,8,9])
matrix.append([2,4,9,12])
matrix.append([4,7,10,13])
matrix.append([6,8,11,15])
n = int(sys.argv[1])
print func1(matrix, n)
print func2(matrix, n)

#python young-matrix-search.py 6
