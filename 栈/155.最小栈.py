#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack=[]

    def push(self, x: int) -> None:
        self.Stack.append(x)

    def pop(self) -> None:
        return self.Stack.pop(-1)

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return min(self.Stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

