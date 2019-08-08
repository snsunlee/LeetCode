#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res=[]
        candidates.sort()
        def backtrack(candidates,tmp_sum,tmp_list):
            if tmp_sum==target:
                res.append(tmp_list)
                return 
            for j in range(len(candidates)):
                if tmp_sum + candidates[j] >target:break
                if j>0  and candidates[j]==candidates[j-1]:continue
                backtrack(candidates[j+1:],tmp_sum+candidates[j],tmp_list+[candidates[j]]) 
        backtrack(candidates,0,[])
        return res

