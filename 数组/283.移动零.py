#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count=0
        while i!=len(nums)-count :
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                count+=1
            else:
                i+=1

