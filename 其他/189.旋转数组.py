#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0,nums.pop())
        

