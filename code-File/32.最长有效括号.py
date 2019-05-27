#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        return self.findLengthOfLCIS(res.sort())
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=1
        new=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                res+=1
                new=max(res,new)
                if i!=len(nums)-2 and nums[i+1]>=nums[i+2]:
                    res=1
        return new

