#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (46.16%)
# Total Accepted:    436.5K
# Total Submissions: 945.2K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #这个和之前求数组中最大的子数组和有点类似，result[i]表示在第i天卖出能获得的最大收益,
        #如果prices[i] = max(0,result[i-1] + prices[i] -prices[i-1] )
        cur_max = 0
        all_time_max = 0
        for day_index in range(1,len(prices)):
            cur_max = max(0,cur_max + (prices[day_index] - prices[day_index-1]))
            all_time_max = max(all_time_max,cur_max)

        return all_time_max

