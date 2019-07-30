#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    ####利用记忆化存储来减少重复计算
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        first,second,third=1,2,0
        for i in range(n-2):
            third=first+second
            first=second
            second=third
        return second
    ####思路一致
     def climbStairs1(self, n: int) -> int:
        cash=[1,1]
        if n==0 or n==1:
            return 1
        i=2
        while i<n:
            cash.append(cash[i-1] + cash[i-2])
            i+=1
        cash.append(cash[i-1] + cash[i-2])
        return cash[i]

