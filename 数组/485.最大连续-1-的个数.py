#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start=0
        max_length=0
        while start<len(nums):
            if nums[start]==1:
                end=start
                while end<len(nums):
                    if nums[end]==1:
                        end+=1
                    else:
                        if max_length<end-start:
                            max_length=end-start
                        break
                if end==len(nums):
                    if max_length<end-start:
                        max_length=end-start
                start=end+1
            else:
                start+=1
        return max_length

