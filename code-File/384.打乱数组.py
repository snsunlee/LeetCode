#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
class Solution:

    def __init__(self, nums: List[int]):
        self._nums=nums
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        new_list=self._nums[:]
        for i in range(len(new_list),1,-1):
            t=random.randint(0,i-1)
            tmp = new_list[t]
            new_list[t] = new_list[i-1]
            new_list[i-1] = tmp
        return new_list


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

