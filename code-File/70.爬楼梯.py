#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        first,second,third=1,2,0
        for i in range(n-2):
            third=first+second
            first=second
            second=third
        return second

