#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Stack=[]
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.Stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.Stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.Stack[-1]
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.Stack)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

