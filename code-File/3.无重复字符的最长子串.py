#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        self.subString=''
        max_len=0
        index=0
        while index!=len(s):
            now_len=len(self.subString)
            if s[index] not in self.subString:
                now_len+=1
                self.subString+=s[index]
                index+=1
            else:#之前出现过这一个字母
                if now_len>max_len:
                    max_len=now_len
                repeat_index=self.subString.index(s[index])
                self.subString=self.subString[repeat_index+1:]+s[index]
                index+=1
        return max(max_len,now_len)
