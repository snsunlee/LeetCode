#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            left,end=0,len(nums)-1
            while left<=end:
                middle=left +(end-left)//2
                print(middle)
                if nums[middle] <target:
                    left=middle+1
                else:
                    end=middle-1
            return left

