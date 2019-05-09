#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
class Solution(object):
    def maxProfit(self, prices:List[int]) ->int:
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit


