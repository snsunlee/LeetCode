"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""
class Solution:
    def wordBreak(self, s: str, wordDict):
        res=[]
        def dfs(s,wordDict,string_list):
            if self.check(s,wordDict):
                if len(s)==0:
                    res.append(string_list[1:])
                for i in range(1,len(s)+1):
                    if s[:i] in wordDict:
                        dfs(s[i:],wordDict,string_list+' '+s[:i])
        dfs(s,wordDict,'')
        return res

    def check(self,s,wordDict):
        if not s:
            return True
        bp=[0]
        for i in range(len(s)+1):
            for j in bp:
                if s[j:i] in wordDict:
                    bp.append(i)
                    break
        return bp[-1]==len(s)
