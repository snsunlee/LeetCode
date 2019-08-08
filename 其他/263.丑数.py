#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
class Solution:
    def isUgly(self, num: int) -> bool:
        prime = [2,3,5]
        if num < 1:
            return False
        if num == 1 or num in prime:
            return True
        i=0
        while i < len(prime):
            if num % prime[i] != 0:
                i += 1
            else:
                num = num // prime[i]
                if num in prime:
                    return True
                i = 0
        return False
