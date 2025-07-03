"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_price = 0
        max_profit = 0
        for p in prices:
            min_price = min(min_price, prices[p])
            max_profit = max(max_profit, p - min_price)
        return max_profit