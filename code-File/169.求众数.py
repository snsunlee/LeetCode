#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        self.hash={}
        for item in nums:
            if item not in self.hash:
                self.hash[item]=1
            else:
                self.hash[item]+=1
        max_value=0
        returned_=0
        for item in self.hash.items():
            if item[1]>max_value:
                max_value=item[1]
                returned_=item[0]
        return returned_
