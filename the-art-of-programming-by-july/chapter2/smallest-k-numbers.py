# -*- coding: utf-8 -*-
"""
输入n个整数，输出其中最小的k个。
"""
####{{{
# 1. Push the first k numbers into a max heap. Assume they are the smallest k numbers.
# 2. Loop through the rest n-k numbers. For each number, compare with the root of the max heap. 
#    If the number is smaller, swap with the root and maintain the heap.
# 3. complexity: O(k + (n - k) * logk) = O(k*logk)
####}}}

"""
输入是两个整数数组，他们任意两个数的和又可以组成一个数组，求这个和中前k个数怎么做？
"""
####{{{
# find the smallest k numbers of A[i] + B[j]
####}}}

"""
有两个序列A和B,A=(a1,a2,...,ak),B=(b1,b2,...,bk)，A和B都按升序排列。对于1<=i,j<=k，求k个最小的（ai+bj）
"""
####{{{
# 1. Push a node into a min heap. The node carries the following datas:
#    n.value = A[0] + B[0]
#    n.idxa  = 0
#    n.idxb  = 0
# 2. Pop the root. Push node of A[i+1] + B[j] and A[i] + B[j+1] into heap, where root.idxa = i, root.idxb = j
# 3. Pop k times.
# 4. complexity O(k*logk)
####}}}
