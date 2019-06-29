#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[nums[0]]!=nums[0]:
            nums[nums[0]],nums[0]=nums[0],nums[nums[0]]
        return nums[0]

        


