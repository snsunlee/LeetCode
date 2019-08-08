#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=list(range(1,n+1))
        res=''
        k=k-1
        while n>0:
            i=k//math.factorial(n-1)
            k=k%math.factorial(n-1)
            res+=str(nums[i])
            nums.pop(i)
            n-=1
        return res

