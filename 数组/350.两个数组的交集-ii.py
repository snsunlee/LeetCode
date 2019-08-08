#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
#两种写法竟相差50% 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=set(nums1)&set(nums2)
        res=[]
        for item in intersection:
            res.extend([item]*min(nums1.count(item),nums2.count(item)))
        return res
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     from collections import Counter
    #     nums1, nums2, ans = Counter(nums1), Counter(nums2), []
    #     for key in nums1.keys():
    #         try:
    #             ans += [key]*min(nums1[key], nums2[key])
    #         except KeyError:
    #             continue
    #     return ans
