#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=list(map(str,digits))
        digits_int=int(''.join(digits))
        digits_plus_1=str(digits_int+1)
        return list((map(int,digits_plus_1)))

