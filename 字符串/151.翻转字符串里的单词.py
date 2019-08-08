#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
class Solution:
    def reverseWords(self, s: str) -> str:
        list_reverse=s.split()
        return ' '.join(list_reverse[::-1])


