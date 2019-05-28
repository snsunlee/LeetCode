#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        def backtrack(num,tmp):
            if not num:
                res.append(tmp)
            for i in range(len(num)):
                backtrack(num[:i]+num[i+1:],tmp+[num[i]])
        backtrack(nums,[])
        return res

