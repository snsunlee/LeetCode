#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前K个高频元素
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        res=sorted(hash_map.items(),key=lambda x:x[1],reverse=True)
        res_return=[]
        for i in range(k):
            res_return.append(res[i][0])
        return res_return

