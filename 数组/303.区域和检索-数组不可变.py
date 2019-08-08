#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
    def sumRange(self, i: int, j: int) -> int:
        if j==len(self.nums)-1:
            return sum(self.nums[i:])
        else:
            return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

