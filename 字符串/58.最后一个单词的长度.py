#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=' '.join(s.split())
        split_s=s.split(' ')
        if split_s[-1]=='':
            if len(split_s)==1:
                return 0
            return len(split_s[-2])
        else:
            return len(split_s[-1])
