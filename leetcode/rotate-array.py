"""
Difficulty: Easy

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

"""
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate1(self, nums, k):#{{{
        length = len(nums)
        if length > 1:
            k = k % length
            if k == 0:
                return nums
            for i in range(k):
                temp = nums[0]
                for j in range(1, length):
                    next = ( j + 1) % length
                    nums[j] = temp
                    temp = nums[next]
                        
        return nums
#}}}
