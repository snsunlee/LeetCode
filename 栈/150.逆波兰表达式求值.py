#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op={'+','-','*','/'}
        for token in tokens:
            if token in op:#遇到操作符
                right=stack.pop()
                left=stack.pop()
                tmp=int(eval(str(left)+token+str(right)))
                if token=='/':
                    if left*right>0:
                        tmp=left // right
                    else:
                        tmp=-(-left//right)
                stack.append(tmp)
            else:
                stack.append(int(token))
        return stack[0]

