#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:   
        nums.sort()
        for key, value in enumerate(nums):
            if key != value:
                return key
        else:
            return key + 1



