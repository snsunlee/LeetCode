#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
class Solution:
    def calculate(self, s: str) -> int:
        pre_op='+'
        num=0
        Stack=[]
        for i,each in enumerate(s):
            if each.isdigit():
                num=num*10+int(each)
            if i==len(s)-1 or each in '+-/*':
                if pre_op=='+':
                    Stack.append(num)
                elif pre_op=='-':
                    Stack.append(-num)
                elif pre_op=='*':
                    Stack.append(Stack.pop()*num)
                else:
                    top=Stack.pop()
                    if top<0:
                        Stack.append(int(top/num))
                    else:
                        Stack.append(top//num)
                pre_op=each
                num=0
        return sum(Stack)

