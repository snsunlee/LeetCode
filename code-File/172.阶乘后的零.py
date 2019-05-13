#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>=5:
            count+=n//5
            n//=5
        return count

