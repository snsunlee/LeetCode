#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start,end=0,0
        min_lenght=len(nums)+1
        sum_all=0
        while start < len(nums):
            if sum_all<s and end<len(nums):
                sum_all+=nums[end]
                end+=1
            else:
                sum_all-=nums[start]
                start+=1
            if sum_all>=s:
                min_lenght=min(min_lenght,end-start)
        if min_lenght==len(nums)+1:
            return 0
        return min_lenght
