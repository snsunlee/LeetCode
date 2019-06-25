#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val,min_val,res=nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                max_val,min_val=min_val,max_val
            max_val=max(max_val*nums[i],nums[i])
            min_val=min(min_val*nums[i],nums[i])
            res=max(max_val,res)
        return res

