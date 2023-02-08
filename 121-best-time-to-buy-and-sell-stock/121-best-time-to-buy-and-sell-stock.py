class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff <= 0:
                left = right
                right += 1
            else:
                profit = max(diff, profit)
                right += 1
                
        return profit
            
            