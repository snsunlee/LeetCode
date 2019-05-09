#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
