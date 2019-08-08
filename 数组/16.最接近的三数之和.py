#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

class Solution:
    def threeSumClosest(self, nums, target):
        result = nums[0]+nums[1]+nums[2]
        dis = abs(result-target)
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = abs(nums[i]+nums[j]+nums[k]-target)
                if temp<dis:
                    dis = temp
                    result = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k]<target:
                    j += 1
                elif nums[i]+nums[j]+nums[k]>target:
                    k -= 1
                else:
                    return nums[i]+nums[j]+nums[k]
        return result 

