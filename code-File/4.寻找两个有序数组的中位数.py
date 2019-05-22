#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        n = len(num)
        if n % 2 == 0:
            i = int(n / 2 -1)
            j = i + 1
            return (num[i] + num[j])/2
        return float(num[int((n-1)/2)])

