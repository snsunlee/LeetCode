#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(list(map(lambda x:int(x),str(num))))
        return num


