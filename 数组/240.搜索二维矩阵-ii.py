#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j=-1
        for row in matrix:
            while j>-len(row) and row[j]>target:
                j-=1
            if row and row[j]==target:
                return True
        return False 
        

