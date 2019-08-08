#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: 
            return False
        first_val,second_val=float('inf'),float('inf')
        for i in range(len(nums)):
            if nums[i]<=first_val:
                first_val=nums[i]
            elif nums[i]<=second_val:
                second_val=nums[i]
            else:
                return True #找到比第二个值还大的数 满足
        return False
