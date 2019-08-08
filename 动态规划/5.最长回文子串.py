#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        for length in range(len(s),0,-1):
            for i in range(0,len(s)-length+1):
                now_s=s[i:i+length]
                if now_s==now_s[::-1]:
                    return now_s
