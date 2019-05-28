#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        nums.sort()
        def backtrack(nums,tmp):
            res.append(tmp)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:continue
                backtrack(nums[i+1:],tmp+[nums[i]])
        backtrack(nums,[])
        return res

