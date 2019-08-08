#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right = x
        while left <right:
            mid = int((left + right) / 2)
            if x < mid ** 2:
                right = mid
            else:
                left=mid+1
        return left-1 if left >1 else left

