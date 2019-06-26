#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        right=1
        output = [1]*len(nums)
	    #左积
        for i in range(len(nums)): 
            output[i] = left
            left *= nums[i]
        #右积
        for i in range(len(nums)-1,-1,-1): 
            output[i] *= right
            right *= nums[i]
        return output



