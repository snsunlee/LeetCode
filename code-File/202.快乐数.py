#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
class Solution:
    def isHappy(self, n: int) -> bool:
        num_set=set()
        while n!=1:
            n=sum(list(map(lambda x:int(x)**2,list(str(n)))))
            if n in num_set:
                return False
            else:
                num_set.add(n)
        return True
        

