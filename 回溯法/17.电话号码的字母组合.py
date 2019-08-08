#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        numStr = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        rst = ['']
        for s in digits:
            rst = [i + j for i in rst for j in numStr[s]]

        return rst
