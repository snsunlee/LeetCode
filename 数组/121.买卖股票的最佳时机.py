#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
class Solution(object):
    def maxProfit(self, prices:List[int]) ->int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-min_price)
        return max_profit


