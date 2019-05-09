#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=='':
            return True
        new_s=''
        for char in s:
            if char.isalpha() or char.isdigit():
                new_s+=char.lower()
        if new_s==new_s[::-1]:
            return True
        return False
