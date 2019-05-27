#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
class Solution:
    def searchRange(self, nums, target: int):
        try:
            start_index=nums.index(target)
        except  :
            return [-1,-1]
        end_index=start_index
        for i in range(start_index+1,len(nums)):
            if nums[i]==target:
                end_index=i
            else:
                break
        return [start_index,end_index]

