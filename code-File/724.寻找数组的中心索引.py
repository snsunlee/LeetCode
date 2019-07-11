#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_all=0
        l_sum=[]#左侧数之和
        for num in nums:
            sum_all+=num
            l_sum.append(sum_all-num)
        for i in range(len(nums)):
            r_sum=sum_all-nums[i]-l_sum[i]
            if l_sum[i]==r_sum:
                return i
        return -1

