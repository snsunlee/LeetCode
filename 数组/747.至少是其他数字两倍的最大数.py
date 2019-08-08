#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num=max(nums)
        for i in range(len(nums)):
            if max_num==nums[i]:
                nums[i]==max_num
            else:
                if 2*nums[i]>max_num:
                    nums[i]='None'
        if 'None' in nums:
            return -1
        return nums.index(max_num)


