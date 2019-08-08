#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0 or k==0:
            return []
        result = []
        window_max = max(nums[0:k])
        result.append(window_max)
        for i in range(k, len(nums)):
            if nums[i] > window_max:
                window_max = nums[i]
            elif nums[i-k] == window_max:  # 这个是要出来的
                window_max = max(nums[i-k+1:i+1])
            result.append(window_max)

        return result


