"""
Difficulty: Medium

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note:
    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
        (-1, 0, 1)
        (-1, -1, 2)

"""
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, numbers):#{{{
        result = []
        length = len(numbers)
        if length > 0:
            numbers.sort()
            for _ in range(length):
                curr_sum = -numbers[_]
                idx_i = 0
                idx_j = length - 1
                while idx_i < idx_j:
                    if idx_i == _:
                        idx_i = idx_i + 1
                    elif idx_j == _:
                        idx_j = idx_j - 1
                    else:
                        if numbers[idx_i] + numbers[idx_j] > curr_sum:
                            idx_j = idx_j - 1
                        elif numbers[idx_i] + numbers[idx_j] < curr_sum: 
                            idx_i = idx_i + 1
                        else:
                            if _ <= idx_i:
                                temp = (numbers[_], numbers[idx_i], numbers[idx_j])
                            elif _ >= idx_j:
                                temp = (numbers[idx_i], numbers[idx_j], numbers[_])
                            else:
                                temp = (numbers[idx_i], numbers[_], numbers[idx_j])
                            result.append(temp)
                            idx_i = idx_i + 1
                            idx_j = idx_j - 1
                # end of while
            # end of for
        # end of if
        result = set(result)
        result2 = []
        for _ in result:
            result2.append(list(_))
        return result2
#}}}
