#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=1
        new=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                res+=1
                new=max(res,new)
                if i!=len(nums)-2 and nums[i+1]>=nums[i+2]:
                    res=1
        return new

