"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s: str):
        #retype: List[List[str]]
        res=[]
        if len(s)==0:
            return res
        def back(start=0,tmp=[]):
            if start>=len(s):
                res.append(tmp)
                return 
            for end in range(start+1,len(s)+1):
                if s[start:end]==s[start:end][::-1]:#该子串为回文串 继续递归
                    back(end,tmp+[s[start:end]])
        back()
        return res

print(Solution().partition("aab"))