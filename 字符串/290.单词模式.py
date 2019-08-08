#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词模式
#

class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        if len(pattern)!=len(string.split(' ')):
            return False
        hash_dic={}
        list_str=string.split(' ')
        return list(map(lambda x:pattern.find(x),pattern))==list(map(lambda x:list_str.index(x),list_str))

