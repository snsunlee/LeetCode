#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sorted_list=[]
        for i in range(len(matrix)):
            sorted_list.extend(matrix[i])
        sorted_list.sort()
        return sorted_list[k-1]

