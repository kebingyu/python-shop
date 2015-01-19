# -*- coding: utf-8 -*-
"""
输入三个字符串s1、s2和s3，判断第三个字符串s3是否由前两个字符串s1和s2交错而成，即不改变s1和s2中各个字符原有的相对顺序，例如当s1 = “aabcc”，s2 = “dbbca”，s3 = “aadbbcbcac”时，则输出true，但如果s3=“accabdbbca”，则输出false。
"""
def func1(s1, s2, s3):
    n = len(s1)
    m = len(s2)
    s = len(s3)

    if n + m != s:
        return False

    # dp[i][j] store if s3[0...i+j-1] is made of s1[0...i-1] and s2[0...j-1]
    dp = [[False for _ in range(n)] for _ in range(m)]
    dp[0][0] = True

    for i in range(n):
        for j in range(m):
            if dp[i][j] or\
                    (i-1 >= 0 and dp[i-1][j] == True and s1[i-1] == s3[i+j-1]) or\
                    (j-1 >= 0 and dp[i][j-1] == True and s2[j-1] == s3[i+j-1]):
                        dp[i][j] = True
            else:
                dp[i][j] = False

    return dp[n-1][m-1]


import sys
print func1(sys.argv[1], sys.argv[2], sys.argv[3])

#python mix-string.py 'aabcc' 'dbbca' 'aadbbcbcac'
#python mix-string.py 'aabcc' 'dbbca' 'accabdbbca'
