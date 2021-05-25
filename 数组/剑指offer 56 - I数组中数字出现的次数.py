#
# @lc app=leetcode.cn 剑指offer 56 lang=python3
#
# 数组中数字出现的次数
# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        for num in nums:
            ret = ret ^ num
        div = 1
        while ((div  & ret ) == 0 ):
            div <<=1
        a,b = 0 , 0
        for num in nums:
            if (div & num ) == 0:
                a = a^ num
            else:
                b = b^ num
        return [a,b]

