"""
Difficulty: Medium

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:
    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.
    
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

"""
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):#{{{
        length = len(num)
        result = []
        if length > 0:
            num.sort()
            i = 0
            while i < length:
                curr_num = num[i]
                start = i
                while i + 1 < length and num[i + 1] == curr_num:
                    i += 1
                end = i
                temp_num = num[:start]
                temp_num.extend(num[end + 1:])
                temp_target = target - curr_num
                temp_result = self.threeSum(temp_num, temp_target)
                for _ in temp_result:
                    _.append(curr_num)
                    _.sort()
                    result.append(_)
                i += 1
        return result
        
    def threeSum(self, num, target):
        length = len(num)
        result = []
        if length > 0:
            for _ in range(length):
                i = 0
                j = length - 1
                while i < j:
                    if i == _:
                        i += 1
                    elif j == _:
                        j -= 1
                    else:
                        if num[_] + num[i] + num[j] > target:
                            j -= 1
                        elif num[_] + num[i] + num[j] < target:
                            i += 1
                        else:
                            if _ <= i:
                                temp = (num[_], num[i], num[j])
                            elif _ >= j:
                                temp = (num[i], num[j], num[_])
                            else:
                                temp = (num[i], num[_], num[j])
                            result.append(temp)
                            i += 1
                            j -= 1
        result = set(result)
        result2 = []
        for _ in result:
            result2.append(list(_))
        return result2
#}}}
