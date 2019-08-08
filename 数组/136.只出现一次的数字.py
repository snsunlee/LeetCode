#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums)>1:
            if nums[0]==nums[1]:
                nums.pop(0)
                nums.pop(0)
            else:
                return nums[0]
        
        return nums[0]

