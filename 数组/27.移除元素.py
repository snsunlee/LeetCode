#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)
        for i in range(j-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)    
        return len(nums)

####双指针解法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        while index!=len(nums):
            if nums[index]==val:
                nums.pop(index)
            else:
                index+=1
