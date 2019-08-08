#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ###先转置矩阵 后每一行逆序
        n=len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]

