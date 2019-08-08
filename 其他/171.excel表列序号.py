#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        hash_list='* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
        res=0
        for i in range(len(s)):
            res+=hash_list.index(s[len(s)-i-1])*(26**(i))
        return res

