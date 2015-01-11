# -*- coding: utf-8 -*-
"""
Find the maximum sum of a compact subsequence of array elements after performing a single swap operation.
"""
def func1(numbers):#{{{
    answer = help_func(numbers)
    numbers.reverse()
    answer = max(answer, help_func(numbers))
    return answer

def help_func(numbers):
    length = len(numbers)
    f = [0] * length
    f[0] = numbers[0]
    now = numbers[0]
    for _ in range(1, length):
        now = max(now, numbers[_])
        f[_] = max(numbers[_] + f[_ - 1], now)

    g = [0] * length
    g[length - 1] = numbers[length - 1]
    answer = numbers[length - 1]
    for _ in range(length - 2, -1, -1):
        g[_] = max(g[_ + 1], 0) + numbers[_]
        answer = max(answer, g[_])

    for _ in range(1, length):
        answer = max(answer, g[_] - numbers[_] + f[_ - 1])

    return answer#}}}

import sys
numbers = [int(_) for _ in sys.argv[1].split(',')]
print func1(numbers)

#python largest-sum-of-subset-3.py '3,2,-6,3,1'

"""
发现可以dp，dp也是很巧妙的。
设f[i]表示以i结尾的一段连续的最大子数组外加单独一个元素的最大和。这里需要多说几句，这个定义非常重要。首先：
（1） 以i结尾的连续一段可以为空，但如果非空的话，一定要以i结尾 （废话）
（2） 单独存在的一个点不能为空，并且这个点不能在（1）之内 （同一个元素不能加两次嘛）
定义这个的目的是，如果我们有了这个值，那个单独的元素就是我们换入最终结果的元素。

那么f的递推式是 f[i] = max(f[i - 1] + A[i], max{A[0..i]}}
前者对应以i结尾的连续一段非空的情况，这个和传统最大子段和很像……
后面那个其实是如果连续一段为空，按照f的定义，我们只能取一个点，那么这个点显然要取A[0..i]最大的。如此，我们定义好了f。
再定义一个g,这个g是和传统最大子段和定义是一样的，g[i]表示以i开头的最大子段和。这个不多说g[i] = max(g[i + 1] , 0) + A[i],
那么我们倒着循环i的时候（i = n - 2..0)顺便能求出每个g的值，并且也能求出不交换的普通的最大子段和。也就是max{g[0..n-1]}。
那么对于交换的情况，我们考虑A[i]和某个元素j < i做了交换，那么其实结果是g[i] - a[i] + f[i - 1] , 也就是说f[i - 1]里面包含了a[i]要换入的元素。所以我们再循环一次取max就行了。
可是这种交换值对应了i和j < i的交换。 所以我们还需要把A中的元素翻转，再计算一次。
"""
