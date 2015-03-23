"""
Difficulty: Medium

Given an array of integers, every element appears three times except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):#{{{
        count = [0] * 32
        result = 0;
        for i in range(32):
            # count total 0 and 1 on all 32 digits
            for j in range(len(A)):
                if (A[j] >> i) & 1:
                    count[i] += 1;
            result |= ((count[i] % 3) << i);
        # becasue Python handles negative differently
        if result & 0x80000000:
            return -(result ^ 0xFFFFFFFF ) -1
        else:
            return result
        return result;
#}}}
