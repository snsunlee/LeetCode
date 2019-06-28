#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
class Solution:
    def largestNumber(self, nums) -> str:
        from functools import cmp_to_key
        if not nums: return ""
        nums = list(map(str, nums))
        def mycmp(x,y):
            if x+y>y+x:
                return -1
            else:
                return 1
        nums.sort(key=cmp_to_key(mycmp))
        return '0' if nums[0]=='0' else "".join(nums)
print(Solution().largestNumber([10,2]))