"""
换硬币问题。

想兑换100元钱，有1,2,5,10四种钱，问总共有多少兑换方法。
"""
def func2(number, dimes):#{{{
    # DP, non-recursive
    arr = [0] * (number + 1)
    arr[0] = 1

    for idx_i in range(len(dimes)):
        idx_j = dimes[idx_i]
        while idx_j <= number:
            arr[idx_j] = arr[idx_j] + arr[idx_j - dimes[idx_i]]
            idx_j = idx_j + 1

    return arr[-1]

def func3(number, dimes, m):
    # DP, recursive
    if number == 0:
        return 1
    if number < 0 or m == 0:
        return 0

    return func3(number, dimes, m - 1)\
            + func3(number - dimes[m - 1], dimes, m)
#}}}

dimes = [1,2,5,10]
print func2(number, dimes)
print func3(number, dimes, len(dimes))
