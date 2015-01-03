# -*- coding: utf-8 -*-
"""
13、最长重复子串

一个长度为10000的字符串，写一个算法，找出最长的重复子串，如abczzacbca,结果是bc。

提示：此题是后缀树/数组的典型应用，即是求后缀数组的height[]的最大值。
"""

# 1. build a suffix tree of the given string S and reversed given string S': O(N)
# 2. preprocess suffix tree so that the lookup of LCA (lowest common ancestor) is O(1): O(N)
# 3. for i in range(N), get LCA( S(i), S'(N-i+1) ) and LCA( S(i+1), S'(N-i+1) ): O(N)
# 4. find the largest LCA, times 2 and we are done
