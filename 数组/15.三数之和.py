#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if temp>0:
                    k = k-1
                elif temp<0:
                    j = j+1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    ###以下代码用来优化 时间复杂度 去重重复的项目
                    while j<k and nums[j]==nums[j+1]:
                        j = j+1
                    while j<k and nums[k]==nums[k-1]:
                        k = k-1     
                    j = j+1
                    k = k-1
        return result



