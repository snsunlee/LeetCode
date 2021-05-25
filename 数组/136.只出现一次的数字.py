#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums)>1:
            if nums[0]==nums[1]:
                nums.pop(0)
                nums.pop(0)
            else:
                return nums[0]
        
        return nums[0]
    # 解法2 使用异或
    def singleNumber(self, nums: List[int]) -> int:
        a = 0 
        for num in nums:
            a = a ^ num
        return a

    # 解法3 集合数学运算
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) -sum(nums) 

