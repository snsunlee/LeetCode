#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return list(map(s.find,s))==list(map(t.find,t))

