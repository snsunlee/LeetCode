#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num = nums[0]
        sum_num = nums[0]
        for num in nums[1:]:
            # 当前元素大于连续子数组和加上元素本身并且最大值比元素还小时，
            # 抛弃前面的连续子数组，重新开始计算连续数组和
            if num > (sum_num + num):
                sum_num = num
                if num>max_num:
                    max_num = num
            # 加上当前元素后，数组和比最大值还大，则连续该元素
            elif sum_num + num > max_num:
                max_num = sum_num + num
                sum_num += num
            else:
                sum_num += num
        return max_num

