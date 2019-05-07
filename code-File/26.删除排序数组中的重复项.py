#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        index=1
        while index!=len(nums):
            if nums[index] in nums[:index]:
                nums.pop(index)
            else:
                index+=1
        return len(nums)


