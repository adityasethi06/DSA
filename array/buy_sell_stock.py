# Q)
    # you are given an array prices where prices[i] is the price of a given 
    # stock on the ith day.

    # You want to maximize your profit by choosing a single day to buy one 
    # stock and choosing a different day in the future to sell that stock.

    # Return the maximum profit you can achieve from this transaction. 
    # If you cannot achieve any profit, return 0

# A)
    # Solved using two pointers in O(n)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                max_prof = max(prices[right] - prices[left], max_prof)
            else:
                left = right
            right += 1
        return max_prof
        