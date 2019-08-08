#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
'''
比如[1,3,5,2,6,1,3] 
profit=（3-1)+(5-3)+(6-2)+(3-1)=3-1+5-3+(6-2)+(3-1)=(5-1)+(6-2)+(3-1) 
实际直接求解是profit = (5-1)+(6-2)+(3-1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit

