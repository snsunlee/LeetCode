#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
class Solution:
    def generate(self, numRows: int):
        if numRows<3:
            if numRows==1:
                return [[1]]
            elif numRows==2:
                return [[1],[1,1]]
            else:
                return []
        first=[1,1]
        res=[[1],[1,1]]
        for _ in range(numRows-2):
            added=first[1:]+[0]
            second=[1]+list(map(lambda x,y:x+y,first,added))
            res.append(second)
            first=second
        return res

