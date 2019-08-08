#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_t=list(t)
        for i in range(len(s)):
            try:
                thing_index = list_t.index(s[i])
            except ValueError:
                return False
            list_t.pop(thing_index)
        return list_t==[]
