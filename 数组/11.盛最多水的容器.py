#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
class Solution:
    def maxArea(self, height) -> int:
        left,right=0,len(height)-1
        maxVal=0
        while left<right:
            maxVal=max(maxVal,min(height[left],height[right])*(right-left) )
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxVal

