"""
Difficulty: Easy

Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):#{{{
        v1 = [int(_) for _ in version1.split('.')]
        v2 = [int(_) for _ in version2.split('.')]
        len_v1 = len(v1)
        len_v2 = len(v2)
        idx_v1 = 0
        idx_v2 = 0
        while idx_v1 < len_v1 and idx_v2 < len_v2:
            if v1[idx_v1] > v2[idx_v2]:
                return 1
            elif v1[idx_v1] < v2[idx_v2]:
                return -1
            else:
                idx_v1 += 1
                idx_v2 += 1
        sum_v1 = 0
        sum_v2 = 0
        while idx_v1 < len_v1:
            sum_v1 += v1[idx_v1]
            idx_v1 += 1
        while idx_v2 < len_v2:
            sum_v2 += v2[idx_v2]
            idx_v2 += 1
        if sum_v1 > 0:
            return 1
        elif sum_v2 > 0:
            return -1
        else:
            return 0
#}}}
