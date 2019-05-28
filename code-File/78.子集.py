#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res=[]
        def backtrack(num,tmp):
            res.append(tmp)  
            for i in range(len(num)):
                backtrack(num[i+1:],tmp+[num[i]])
        backtrack(nums,[])
        return res

