#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
from functools import reduce
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(reduce(self.fn,map(self.char2num,num1))*reduce(self.fn,map(self.char2num,num2)))
    def fn(self,x,y):
        return x*10+y
    def char2num(self,s):
        digits={
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
            }
        return digits[s]

