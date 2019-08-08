#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        def backtrack(num, tmp):
            if len(num) == len(tmp):
                res.append(tmp)
                return
            for i in range(len(num)):
                if i in visited or (i > 0 and i - 1 not in visited and num[i-1] == num[i]):
                    continue
                visited.add(i)
                backtrack(num, tmp + [num[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res

