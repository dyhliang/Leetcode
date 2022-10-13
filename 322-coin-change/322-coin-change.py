import sys

class Solution:
    def helper(self, coins: list[int], amount: int, countmemo: list[int]) -> int:
        if amount < 0:
            return -1
        
        if amount == 0:
            return 0
        
        if countmemo[amount] != 0:
            return countmemo[amount]
        
        inf = sys.maxsize
        min_coins = sys.maxsize
        
        for c in coins:
            c_count = self.helper(coins, amount - c, countmemo)
            
            if 0 <= c_count < min_coins:
                min_coins = c_count + 1
                
        countmemo[amount] = -1 if (min_coins == inf) else min_coins
        
        return countmemo[amount]

    
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        return self.helper(coins, amount, [0] * (amount + 1))
        