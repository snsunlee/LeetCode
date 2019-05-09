#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<2:
            if rowIndex==0:
                return [1]
            elif rowIndex==1:
                return [1,1]
            else:
                return []
        first=[1,1]
        for _ in range(rowIndex-1):
            added=first[1:]+[0]
            second=[1]+list(map(lambda x,y:x+y,first,added))
            first=second
        return second

