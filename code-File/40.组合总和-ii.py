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
        n=len(candidates)
        def backtrack(i,tmp_sum,tmp_list):
            if tmp_sum==target:
                res.append(tmp_list)
                return
            for j in range(i,n):
                if tmp_sum + candidates[j] >target:break
                if j>i  and candidates[j]==candidates[j-1]:continue
                backtrack(j+1,tmp_sum+candidates[j],tmp_list+[candidates[j]])
        backtrack(0,0,[])
        return res

