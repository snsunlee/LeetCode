#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count=0
        a_b_hash={}
        for a in A:
            for b in B:
                a_b_hash[a+b]=a_b_hash.get(a+b,0)+1
        
        for c in C:
            for d in D:
                if -(c+d) in a_b_hash:
                    count+=a_b_hash[-(c+d)]
        return count

