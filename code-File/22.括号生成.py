#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def dfs(b: str, left_num: int, right_num: int):
            if len(b) == n * 2:
                res.append(b)
            if left_num < n:
                dfs(b + "(", left_num + 1, right_num)
            if left_num > right_num:
                dfs(b + ")", left_num, right_num + 1)
        dfs("", 0, 0)
        return res

