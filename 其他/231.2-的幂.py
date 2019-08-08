#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            return bin(n).count('1') == 1

