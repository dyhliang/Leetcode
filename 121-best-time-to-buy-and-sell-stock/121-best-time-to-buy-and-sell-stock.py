class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        profit = 0
        for pos in range(len(prices)):
            if prices[pos] < min_price:
                min_price = prices[pos]
                    
            profit = prices[pos] - min_price
            
            if profit > max_profit:
                max_profit = profit
        
        if max_profit < 0:
            return 0
        else:
            return max_profit
                    