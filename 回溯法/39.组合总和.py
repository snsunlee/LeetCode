#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(candidates,target,tmp_list):
            if target==0:
                res.append(tmp_list)
                return
            if target <0:
                return 
            for i in range(len(candidates)):
                if candidates[i]>target:
                    break
                backtrack(candidates[i:],target-candidates[i],tmp_list+[candidates[i]])
        backtrack(candidates,target,[])
        return res

