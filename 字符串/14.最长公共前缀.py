#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.68%)
# Total Accepted:    72.4K
# Total Submissions: 220K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or '' in strs:
            return ''
        strs.sort(key=lambda x:len(x))##min_len sort
        subString=strs[0][0]
        res=all(subString== item[0] for item in strs[1:])
        if not res:
            return ''
        for i in range(len(strs[0])):
            subString=strs[0][:i+1]
            len_subString=len(subString)
            res=all([subString in everString[:len_subString] for everString in strs[1:]])
            if not res:
                return subString[:-1]
        return subString

